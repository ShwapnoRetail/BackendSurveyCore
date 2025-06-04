from django.contrib import admin
from .models import (
    Department, SurveyType, Survey, Question, Choice,
    SurveyTarget, SurveyResponse, Answer
)


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description_snippet')
    search_fields = ('name', 'description')
    list_per_page = 20

    def description_snippet(self, obj):
        return obj.description[:50] if obj.description else '-'

    description_snippet.short_description = "Description"


@admin.register(SurveyType)
class SurveyTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description_snippet')
    search_fields = ('name', 'description')
    list_per_page = 20

    def description_snippet(self, obj):
        return obj.description[:50] if obj.description else '-'

    description_snippet.short_description = "Description"


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 1
    fields = ('text', 'is_correct')
    list_per_page = 20


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'text_snippet', 'type', 'has_marks', 'marks', 'is_required', 'survey_title')
    list_filter = ('type', 'has_marks', 'is_required', 'survey__title')
    search_fields = ('text', 'survey__title')
    inlines = [ChoiceInline]
    list_editable = ('is_required',)
    list_per_page = 20

    def text_snippet(self, obj):
        return obj.text[:50]

    text_snippet.short_description = "Question"

    def survey_title(self, obj):
        return obj.survey.title

    survey_title.short_description = "Survey"


class QuestionInline(admin.TabularInline):
    model = Question
    extra = 0
    fields = ('text', 'type', 'has_marks', 'marks', 'is_required')
    show_change_link = True


class SurveyTargetInline(admin.TabularInline):
    model = SurveyTarget
    extra = 1
    fields = ('target_type', 'user_id', 'department', 'site_id', 'role_name')
    list_per_page = 20


@admin.register(Survey)
class SurveyAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'title', 'description_snippet', 'department_name',
        'survey_type_name', 'site_id', 'is_location_based',
        'is_image_required', 'is_active', 'created_at', 'updated_at',
        'created_by_user_id'
    )
    list_filter = (
        'is_active', 'is_location_based', 'is_image_required',
        'department', 'survey_type', 'created_at'
    )
    search_fields = ('title', 'description', 'site_id')
    inlines = [QuestionInline, SurveyTargetInline]
    readonly_fields = ('created_at', 'updated_at')
    list_editable = ('is_active',)
    list_per_page = 20
    fieldsets = (
        (None, {
            'fields': ('title', 'description', 'site_id', 'department', 'survey_type')
        }),
        ('Features', {
            'fields': ('is_location_based', 'is_image_required', 'is_active')
        }),
        ('Metadata', {
            'fields': ('created_by_user_id', 'created_at', 'updated_at')
        }),
    )

    def description_snippet(self, obj):
        return obj.description[:50] if obj.description else '-'

    description_snippet.short_description = "Description"

    def department_name(self, obj):
        return obj.department.name if obj.department else '-'

    department_name.short_description = "Department"

    def survey_type_name(self, obj):
        return obj.survey_type.name if obj.survey_type else '-'

    survey_type_name.short_description = "Survey Type"


@admin.register(SurveyTarget)
class SurveyTargetAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'survey_title', 'target_type', 'user_id',
        'role_name', 'department_name', 'site_id'
    )
    list_filter = (
        'target_type', 'role_name', 'department', 'survey'
    )
    search_fields = (
        'survey__title', 'role_name', 'user_id', 'site_id'
    )
    list_select_related = ('survey', 'department')
    list_per_page = 20

    def survey_title(self, obj):
        return obj.survey.title

    survey_title.short_description = "Survey"

    def department_name(self, obj):
        return obj.department.name if obj.department else '-'

    department_name.short_description = "Department"


class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 0
    readonly_fields = (
        'question', 'answer_text', 'selected_choice',
        'image_preview', 'marks_obtained'
    )
    fields = (
        'question', 'answer_text', 'selected_choice',
        'image_preview', 'marks_obtained'
    )

    def image_preview(self, obj):
        if obj.image:
            return f'<img src="{obj.image.url}" width="100" />'
        return '-'

    image_preview.allow_tags = True
    image_preview.short_description = "Image"


@admin.register(SurveyResponse)
class SurveyResponseAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'survey_title', 'user_id', 'submitted_at',
        'has_location'
    )
    list_filter = ('survey', 'submitted_at')
    search_fields = ('survey__title', 'user_id')
    readonly_fields = ('submitted_at',)
    inlines = [AnswerInline]
    list_per_page = 20

    def survey_title(self, obj):
        return obj.survey.title

    survey_title.short_description = "Survey"

    def has_location(self, obj):
        return bool(obj.location_lat and obj.location_lon)

    has_location.boolean = True
    has_location.short_description = "Has Location"


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'question_text', 'response_id', 'survey_title',
        'answer_snippet', 'selected_choice', 'has_image',
        'marks_obtained'
    )
    list_filter = (
        'question__type', 'question__survey', 'response__survey'
    )
    search_fields = (
        'answer_text', 'question__text', 'response__user_id'
    )
    readonly_fields = ('image_preview',)
    list_select_related = ('question', 'response', 'selected_choice')
    list_per_page = 20

    def question_text(self, obj):
        return obj.question.text[:50]

    question_text.short_description = "Question"

    def response_id(self, obj):
        return obj.response.id

    response_id.short_description = "Response ID"

    def survey_title(self, obj):
        return obj.response.survey.title

    survey_title.short_description = "Survey"

    def answer_snippet(self, obj):
        return obj.answer_text[:50] if obj.answer_text else '-'

    answer_snippet.short_description = "Answer"

    def has_image(self, obj):
        return bool(obj.image)

    has_image.boolean = True
    has_image.short_description = "Has Image"

    def image_preview(self, obj):
        if obj.image:
            return f'<img src="{obj.image.url}" width="100" />'
        return '-'

    image_preview.allow_tags = True
    image_preview.short_description = "Image Preview"
