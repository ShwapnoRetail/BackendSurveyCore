from rest_framework import serializers
from .models import Survey, SurveyTarget, Question, Choice, Department, SurveyType
import requests


class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ['id', 'text', 'is_correct']


class QuestionSerializer(serializers.ModelSerializer):
    choices = ChoiceSerializer(many=True, required=False)

    class Meta:
        model = Question
        fields = ['id', 'text', 'type', 'has_marks', 'marks', 'is_required', 'choices']


class SurveyTargetSerializer(serializers.ModelSerializer):
    class Meta:
        model = SurveyTarget
        fields = ['target_type', 'user_id', 'department', 'site_id', 'role_name']


class SurveySerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True, required=False)
    targets = SurveyTargetSerializer(many=True, required=False)

    class Meta:
        model = Survey
        fields = ['id', 'title', 'description', 'site_id', 'department', 'survey_type',
                  'is_location_based', 'is_image_required', 'is_active', 'created_at',
                  'updated_at', 'created_by_user_id', 'questions', 'targets']

    def validate_site_id(self, value):
        # Verify site exists in central system
        response = requests.get('https://api.shwapno.app/users/api/sites/')
        if response.status_code == 200:
            sites = response.json().get('data', [])
            if not any(site['id'] == value for site in sites):
                raise serializers.ValidationError("Site does not exist in central system")
        return value

    def create(self, validated_data):
        questions_data = validated_data.pop('questions', [])
        targets_data = validated_data.pop('targets', [])

        survey = Survey.objects.create(**validated_data)

        for question_data in questions_data:
            choices_data = question_data.pop('choices', [])
            question = Question.objects.create(survey=survey, **question_data)

            for choice_data in choices_data:
                Choice.objects.create(question=question, **choice_data)

        for target_data in targets_data:
            SurveyTarget.objects.create(survey=survey, **target_data)

        return survey

    def update(self, instance, validated_data):
        questions_data = validated_data.pop('questions', [])
        targets_data = validated_data.pop('targets', [])

        # Update survey fields
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        # Handle questions update (this is a simplified approach)
        # In production, you'd want more sophisticated handling of updates
        instance.questions.all().delete()
        for question_data in questions_data:
            choices_data = question_data.pop('choices', [])
            question = Question.objects.create(survey=instance, **question_data)

            for choice_data in choices_data:
                Choice.objects.create(question=question, **choice_data)

        # Handle targets update
        instance.targets.all().delete()
        for target_data in targets_data:
            SurveyTarget.objects.create(survey=instance, **target_data)

        return instance