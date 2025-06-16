from django.urls import path
from .views import *

urlpatterns = [
    # Department URLs
    path('api/create-department', create_department),
    path('api/update-department/<id>/', update_department),
    path('api/get-all-department/', get_departments),
    path('api/delete-department/<id>/', delete_department),
    path('api/get-dept/<id>/', get_department_id),

    # Survey Type URLs
    path('api/create-survey-type/', create_survey_type),
    path('api/get-survey-type/<id>/', get_survey_type_id),
    path('api/update-survey-type/<id>/', update_survey_type),
    path('api/delete-survey-type/<id>/', delete_survey_type_id),
    path('api/get-survey-list/', get_survey_list),

    # Survey URLs
    path('api/create-survey/', create_survey),
    path('api/get-survey-list/', get_survey_list),
    path('api/get-survey/<int:id>/', get_survey_detail),
    path('api/update-survey/<int:id>/', update_survey),
    path('api/delete-survey/<int:id>/', delete_survey),

    # Question URLs
    path('api/questions/create/', create_question),
    path('api/questions/<int:id>/', get_question),
    path('api/questions/update/<int:id>/', update_question),
    path('api/questions/delete/<int:id>/', delete_question),
    path('api/get-questions-survey/<int:id>/', get_questions_by_survey),

    # Answer URLs
    path('api/answers/create/', create_answer),
    path('api/answers/<int:id>/', get_answer),
    path('api/answers/update/<int:id>/', update_answer),
    path('api/answers/delete/<int:id>/', delete_answer),

    # Choice URLs
    path('api/choices/create/', create_choice),
    path('api/choices/<int:id>/', get_choice),
    path('api/choices/update/<int:id>/', update_choice),
    path('api/choices/delete/<int:id>/', delete_choice),

    # Survey Target URLs
    path('api/survey-targets/create/', create_survey_target),
    path('api/survey-targets/<int:id>/', get_survey_target),
    path('api/survey-targets/update/<int:id>/', update_survey_target),
    path('api/survey-targets/delete/<int:id>/', delete_survey_target),

    # Survey Response URLs
    path('api/survey-responses/create/', create_survey_response),
    path('api/survey-responses/<int:id>/', get_survey_response),
    path('api/survey-responses/update/<int:id>/', update_survey_response),
    path('api/survey-responses/delete/<int:id>/', delete_survey_response),
    path('api/survey-responses/survey/<int:survey_id>/', get_responses_for_survey),

]
