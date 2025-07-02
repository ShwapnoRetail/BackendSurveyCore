from rest_framework import serializers
# from .models import Survey, SurveyTarget, Question, Choice, Department, SurveyType
import requests
from .models import *


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'




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
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')

    def create(self, validated_data):
        questions_data = validated_data.pop('questions', [])
        targets_data = validated_data.pop('targets', [])

        survey = Survey.objects.create(**validated_data)

        # Create questions and choices
        for question_data in questions_data:
            choices_data = question_data.pop('choices', [])
            question = Question.objects.create(survey=survey, **question_data)

            for choice_data in choices_data:
                Choice.objects.create(question=question, **choice_data)

        # Create targets
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

        # Handle questions update (delete existing and create new)
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

# class SurveyResponseSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = SurveyResponse
#         fields = ['id', 'survey', 'user_id', 'submitted_at', 'location_lat', 'location_lon']
#

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ['id', 'response', 'question', 'answer_text', 'selected_choice',
                 'image', 'marks_obtained', 'is_admin_submission', 'submitted_by']
        extra_kwargs = {
            'image': {'required': False, 'allow_null': True},
            'selected_choice': {'required': False, 'allow_null': True},
        }

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if instance.selected_choice:
            representation['selected_choice'] = instance.selected_choice.id
        return representation




# class SurveyResponseDetailSerializer(serializers.ModelSerializer):
#     answers = AnswerSerializer(many=True, read_only=True)
#
#     class Meta:
#         model = SurveyResponse
#         fields = ['id', 'survey', 'user_id', 'submitted_at',
#                   'location_lat', 'location_lon', 'answers']




class SurveyTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SurveyType
        fields = '__all__'






class QuestionResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionResponse
        fields = ['question', 'answer_text', 'selected_choice_ids', 'score_awarded']

class SurveyResponseCreateSerializer(serializers.ModelSerializer):
    question_responses = QuestionResponseSerializer(many=True)

    class Meta:
        model = SurveyResponse
        fields = ['survey', 'user_id', 'location_lat', 'location_lon', 'question_responses']

    def create(self, validated_data):
        question_responses_data = validated_data.pop('question_responses')
        survey_response = SurveyResponse.objects.create(**validated_data)

        total_score = 0

        for q_data in question_responses_data:
            question = q_data['question']
            answer_text = q_data.get('answer_text')
            selected_choice_ids = q_data.get('selected_choice_ids', [])

            score = 0
            if question.has_marks:
                # For choice-based or yes/no
                correct_choice_ids = set(
                    question.choices.filter(is_correct=True).values_list('id', flat=True)
                )
                submitted_ids = set(selected_choice_ids or [])

                if correct_choice_ids == submitted_ids:
                    score = question.marks or 0

            q_resp = QuestionResponse.objects.create(
                survey_response=survey_response,
                question=question,
                answer_text=answer_text,
                selected_choice_ids=selected_choice_ids,
                score_awarded=score
            )
            total_score += score

        survey_response.total_score = total_score
        survey_response.save()

        return survey_response

class SurveyResponseDetailSerializer(serializers.ModelSerializer):
    question_responses = QuestionResponseSerializer(many=True, read_only=True)

    class Meta:
        model = SurveyResponse
        fields = '__all__'
