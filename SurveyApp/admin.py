from django.contrib import admin
from .models import (
    Department, SurveyType, Survey, Question, Choice,
    SurveyTarget, SurveyResponse, Answer
)


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


@admin.register(SurveyType)
class SurveyTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 1


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'text_snippet', 'type', 'has_marks', 'marks', 'survey_title')
    list_filter = ('type', 'has_marks', 'survey__title')
    search_fields = ('text', 'survey__title')
    inlines = [ChoiceInline]

    def text_snippet(self, obj):
        return obj.text[:50]
    text_snippet.short_description = "Question"

    def survey_title(self, obj):
        return obj.survey.title


class QuestionInline(admin.TabularInline):
    model = Question
    extra = 0


@admin.register(Survey)
class SurveyAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'department_name', 'survey_type_name', 'site_id', 'is_location_based', 'is_image_required', 'is_active', 'created_at')
    list_filter = ('is_active', 'is_location_based', 'is_image_required', 'department__name', 'survey_type__name')
    search_fields = ('title', 'description')
    inlines = [QuestionInline]
    readonly_fields = ('created_at',)

    def department_name(self, obj):
        return obj.department.name if obj.department else '-'

    def survey_type_name(self, obj):
        return obj.survey_type.name if obj.survey_type else '-'


@admin.register(SurveyTarget)
class SurveyTargetAdmin(admin.ModelAdmin):
    list_display = ('id', 'survey_title', 'target_type', 'user_id', 'role_name', 'department_name', 'site_id')
    list_filter = ('target_type', 'role_name', 'department__name')
    search_fields = ('survey__title', 'role_name')

    def survey_title(self, obj):
        return obj.survey.title

    def department_name(self, obj):
        return obj.department.name if obj.department else '-'


class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 0
    readonly_fields = ('question', 'answer_text', 'selected_choice', 'image', 'location_lat', 'location_lon')


@admin.register(SurveyResponse)
class SurveyResponseAdmin(admin.ModelAdmin):
    list_display = ('id', 'survey_title', 'user_id', 'submitted_at')
    list_filter = ('survey__title',)
    search_fields = ('survey__title', 'user_id')
    readonly_fields = ('submitted_at',)
    inlines = [AnswerInline]

    def survey_title(self, obj):
        return obj.survey.title


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ('id', 'question_text', 'response_id', 'answer_text', 'selected_choice', 'has_image', 'has_location')
    list_filter = ('question__type',)
    search_fields = ('answer_text', 'question__text')

    def question_text(self, obj):
        return obj.question.text[:50]

    def response_id(self, obj):
        return obj.response.id

    def has_image(self, obj):
        return bool(obj.image)
    has_image.boolean = True

    def has_location(self, obj):
        return bool(obj.location_lat and obj.location_lon)
    has_location.boolean = True
