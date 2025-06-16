from django.urls import path
from .views import *

urlpatterns = [
    # Department URLs
    path('api/departments/', get_departments),
    path('api/departments/create/', create_department),
    path('api/departments/<int:id>/', get_department_id),
    path('api/departments/update/<int:id>/', update_department),
    path('api/departments/delete/<int:id>/', delete_department),

    # Survey Type URLs
    path('api/survey-types/', get_survey_list),
    path('api/survey-types/create/', create_survey_type),
    path('api/survey-types/<int:id>/', get_survey_type_id),
    path('api/survey-types/update/<int:id>/', update_survey_type),
    path('api/survey-types/delete/<int:id>/', delete_survey_type_id),

    # Survey URLs
    path('api/surveys/', get_survey_list),
    path('api/surveys/create/', create_survey),
    path('api/surveys/<int:id>/', get_survey_detail),
    path('api/surveys/update/<int:id>/', update_survey),
    path('api/surveys/delete/<int:id>/', delete_survey),
    path('api/surveys/<int:id>/questions/', get_questions_by_survey),

    # Question URLs
    path('api/questions/create/', create_question),
    path('api/questions/<int:id>/', get_question),
    path('api/questions/update/<int:id>/', update_question),
    path('api/questions/delete/<int:id>/', delete_question),
    path('api/get-questions-survey/<int:id>/', get_questions_by_survey),

    # Choice URLs
    path('api/choices/create/', create_choice),
    path('api/choices/<int:id>/', get_choice),
    path('api/choices/update/<int:id>/', update_choice),
    path('api/choices/delete/<int:id>/', delete_choice),

    # Survey Response URLs
    path('api/survey-responses/create/', create_survey_response),
    path('api/survey-responses/<int:id>/', get_survey_response),
    path('api/survey-responses/update/<int:id>/', update_survey_response),
    path('api/survey-responses/delete/<int:id>/', delete_survey_response),
    path('api/survey-responses/survey/<int:survey_id>/', get_responses_for_survey),

    # Answer URLs
    path('api/answers/create/', create_answer),
    path('api/answers/<int:id>/', answer_operations),
    path('api/answers/update/<int:id>/', answer_operations),
    path('api/answers/delete/<int:id>/', answer_operations),

    # Survey Target URLs
    path('api/targets/create/', create_survey_target),
    path('api/targets/<int:id>/', get_survey_target),
    path('api/targets/update/<int:id>/', update_survey_target),
    path('api/targets/delete/<int:id>/', delete_survey_target),
]



