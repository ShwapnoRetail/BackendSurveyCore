from .modules import *


# Create your views here.


@api_view(['POST'])
def create_department(request):
    try:
        payload = request.data
        serializer = DepartmentSerializer(data=payload)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'code': status.HTTP_201_CREATED,
                'message': "Department created successfully",
                'data': serializer.data
            })

        else:
            return Response({
                serializer.errors
            })

    except Exception as e:
        return Response({
            'code': status.HTTP_400_BAD_REQUEST,
            'message': str(e)
        })


@api_view(['PUT'])
def update_department(request, id):
    try:
        dept_obj = Department.objects.get(id=id)
        serializer = DepartmentSerializer(dept_obj, data=request.data, partial=True)

        if not serializer.is_valid():
            return Response({
                'status': status.HTTP_400_BAD_REQUEST,
                'payload': serializer.errors,
                'message': 'Validation Failed'
            })

        serializer.save()
        return Response({
            'status': status.HTTP_200_OK,
            'payload': serializer.data,
            'message': 'Department updated successfully'
        })

    except Department.DoesNotExist:
        return Response({
            'code': status.HTTP_404_NOT_FOUND,
            'message': 'Department not found'
        })

    except Exception as e:
        return Response({
            'code': status.HTTP_400_BAD_REQUEST,
            'message': str(e)
        })


@api_view(['GET'])
def get_departments(request):
    try:
        dept_list = Department.objects.all()
        print(dept_list)
        serializer = DepartmentSerializer(dept_list, many=True)
        return Response({
            'message': 'Department retrieved successfully',
            'code': status.HTTP_200_OK,
            'data': serializer.data

        })

    except Exception as e:
        return Response({
            'code': status.HTTP_400_BAD_REQUEST,
            'message': str(e)
        })


@api_view(['DELETE'])
def delete_department(request, id):
    try:
        dept_obj = Department.objects.get(id=id)
        dept_obj.delete()
        return Response({
            'code': status.HTTP_200_OK,
            'message': 'Department deleted successfully'

        })
    except Department.DoesNotExist:
        return Response({
            'code': status.HTTP_404_NOT_FOUND,
            'message': 'Department not found'
        })

    except Exception as e:
        return Response({
            'code': status.HTTP_400_BAD_REQUEST,
            'message': str(e)

        })


@api_view(['GET'])
def get_department_id(request, id):
    try:
        dept_obj = Department.objects.get(id=id)
        serializer = DepartmentSerializer(dept_obj)
        return Response({
            'code': status.HTTP_200_OK,
            'data': serializer.data,
            'message': 'Department retrieved successfully'
        })

    except Exception as e:
        return Response({
            'code': status.HTTP_400_BAD_REQUEST,
            'message': str(e)
        })


@api_view(['POST'])
def create_survey_type(request):
    try:
        payload = request.data
        survey_serailizer = SurveyTypeSerializer(data=payload)
        if survey_serailizer.is_valid():
            survey_serailizer.save()
            return Response({
                'code': status.HTTP_201_CREATED,
                'message': "Survey created successfully",
                'data': survey_serailizer.data
            })
        else:
            return Response({
                'code': status.HTTP_400_BAD_REQUEST,
                'message': survey_serailizer.errors
            })


    except Exception as e:
        return Response({
            'code': status.HTTP_400_BAD_REQUEST,
            'message': str(e)
        })


@api_view(['GET'])
def get_survey_type_id(request, id):
    try:
        survey_type = SurveyType.objects.get(id=id)
        serializer = SurveyTypeSerializer(survey_type)
        return Response({
            'code': status.HTTP_200_OK,
            'data': serializer.data,
            'message': 'Survey type retrieved successfully'
        })


    except Exception as e:
        return Response({
            'code': status.HTTP_400_BAD_REQUEST,
            'message': str(e)
        })


@api_view(['PUT'])
def update_survey_type(request, id):
    try:
        surveyObj = SurveyType.objects.get(id=id)
        serializer = SurveyTypeSerializer(surveyObj, data=request.data, partial=True)
        if not serializer.is_valid():
            return Response({
                'status': status.HTTP_400_BAD_REQUEST,
                'payload': serializer.errors,
                'message': 'Validation Failed'
            })

        serializer.save()
        return Response({
            'status': status.HTTP_200_OK,
            'payload': serializer.data,
            'message': 'Survey type updated successfully'
        })

    except Exception as e:
        return Response({
            'code': status.HTTP_400_BAD_REQUEST,
            'message': str(e)
        })


@api_view(['DELETE'])
def delete_survey_type_id(request, id):
    try:
        surveyObj = SurveyType.objects.get(id=id)
        surveyObj.delete()
        return Response({
            'code': status.HTTP_200_OK,
            'message': 'Survey type deleted successfully'

        })

    except SurveyType.DoesNotExist:
        return Response({
            'code': status.HTTP_404_NOT_FOUND,
            'message': 'Survey type not found'
        })

    except Exception as e:
        return Response({
            'code': status.HTTP_400_BAD_REQUEST,
            'message': str(e)
        })


@api_view(['GET'])
def get_survey_list(request):
    try:
        survey_type = SurveyType.objects.all()

        serializer = SurveyTypeSerializer(survey_type, many=True)
        return Response({
            'code': status.HTTP_200_OK,
            'data': serializer.data,
            'message': 'Survey list retrieved successfully'
        })

    except Exception as e:
        return Response({
            'code': status.HTTP_400_BAD_REQUEST,
            'message': str(e)
        })


@api_view(['POST'])
def create_survey(request):
    try:
        payload = request.data
        # Add created_by_user_id from request (assuming it's in the JWT or session)
        # In a real implementation from the authenticated user
        payload['created_by_user_id'] = request.user.id if request.user.is_authenticated else 1

        serializer = SurveySerializer(data=payload)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'code': status.HTTP_201_CREATED,
                'message': "Survey created successfully",
                'data': serializer.data
            })
        else:
            return Response({
                'code': status.HTTP_400_BAD_REQUEST,
                'message': serializer.errors
            })

    except Exception as e:
        return Response({
            'code': status.HTTP_400_BAD_REQUEST,
            'message': str(e)
        })


@api_view(['GET'])
def get_survey_list(request):
    try:
        surveys = Survey.objects.all()
        serializer = SurveySerializer(surveys, many=True)
        return Response({
            'message': 'Survey list retrieved successfully',
            'code': status.HTTP_200_OK,
            'data': serializer.data

        })
    except Exception as e:
        return Response({
            'code': status.HTTP_400_BAD_REQUEST,
            'message': str(e)
        })


@api_view(['GET'])
def get_survey_detail(request, id):
    try:
        survey = Survey.objects.get(id=id)
        serializer = SurveySerializer(survey)

        # Get site details from central system
        site_details = None
        try:
            response = requests.get(f'https://api.shwapno.app/users/api/sites/{survey.site_id}/')
            if response.status_code == 200:
                site_details = response.json().get('data')
        except:
            pass

        response_data = serializer.data
        response_data['site_details'] = site_details

        return Response({
            'message': 'Survey retrieved successfully',
            'code': status.HTTP_200_OK,
            'data': response_data,

        })
    except Survey.DoesNotExist:
        return Response({
            'code': status.HTTP_404_NOT_FOUND,
            'message': 'Survey not found'
        })
    except Exception as e:
        return Response({
            'code': status.HTTP_400_BAD_REQUEST,
            'message': str(e)
        })


@api_view(['PUT'])
def update_survey(request, id):
    try:
        survey = Survey.objects.get(id=id)
        serializer = SurveySerializer(survey, data=request.data, partial=True)

        if not serializer.is_valid():
            return Response({
                'code': status.HTTP_400_BAD_REQUEST,
                'message': serializer.errors
            })

        serializer.save()
        return Response({
            'message': 'Survey updated successfully',
            'code': status.HTTP_200_OK,
            'data': serializer.data,

        })
    except Survey.DoesNotExist:
        return Response({
            'code': status.HTTP_404_NOT_FOUND,
            'message': 'Survey not found'
        })
    except Exception as e:
        return Response({
            'code': status.HTTP_400_BAD_REQUEST,
            'message': str(e)
        })


@api_view(['DELETE'])
def delete_survey(request, id):
    try:
        survey = Survey.objects.get(id=id)
        survey.delete()
        return Response({
            'code': status.HTTP_200_OK,
            'message': 'Survey deleted successfully'
        })
    except Survey.DoesNotExist:
        return Response({
            'code': status.HTTP_404_NOT_FOUND,
            'message': 'Survey not found'
        })
    except Exception as e:
        return Response({
            'code': status.HTTP_400_BAD_REQUEST,
            'message': str(e)
        })


# Question CRUD APIs
@api_view(['POST'])
def create_question(request):
    try:
        survey_id = request.data.get('survey')
        if not survey_id:
            return Response({
                'code': status.HTTP_400_BAD_REQUEST,
                'message': "Survey ID is required"
            })

        try:
            survey = Survey.objects.get(id=survey_id)
        except Survey.DoesNotExist:
            return Response({
                'code': status.HTTP_400_BAD_REQUEST,
                'message': "Survey does not exist"
            })

        question_data = request.data.copy()
        question = Question.objects.create(
            survey=survey,
            text=question_data.get('text'),
            type=question_data.get('type'),
            has_marks=question_data.get('has_marks', False),
            marks=question_data.get('marks'),
            is_required=question_data.get('is_required', True)
        )

        # Handle choices if provided
        if question_data.get('choices'):
            for choice_data in question_data['choices']:
                Choice.objects.create(
                    question=question,
                    text=choice_data.get('text'),
                    is_correct=choice_data.get('is_correct', False)
                )

        serializer = QuestionSerializer(question)
        return Response({
            'code': status.HTTP_201_CREATED,
            'message': "Question created successfully",
            'data': serializer.data
        })

    except Exception as e:
        return Response({
            'code': status.HTTP_400_BAD_REQUEST,
            'message': str(e)
        })


@api_view(['GET'])
def get_question(request, id):
    try:
        question = Question.objects.get(id=id)
        serializer = QuestionSerializer(question)
        return Response({
            'code': status.HTTP_200_OK,
            'data': serializer.data,
            'message': 'Question retrieved successfully'
        })
    except Question.DoesNotExist:
        return Response({
            'code': status.HTTP_404_NOT_FOUND,
            'message': 'Question not found'
        })
    except Exception as e:
        return Response({
            'code': status.HTTP_400_BAD_REQUEST,
            'message': str(e)
        })


@api_view(['PUT'])
def update_question(request, id):
    try:
        question = Question.objects.get(id=id)
        serializer = QuestionSerializer(question, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'message': 'Question updated successfully',
                'code': status.HTTP_200_OK,
                'data': serializer.data,

            })
        return Response({
            'code': status.HTTP_400_BAD_REQUEST,
            'message': serializer.errors
        })
    except Question.DoesNotExist:
        return Response({
            'code': status.HTTP_404_NOT_FOUND,
            'message': 'Question not found'
        })
    except Exception as e:
        return Response({
            'code': status.HTTP_400_BAD_REQUEST,
            'message': str(e)
        })


@api_view(['DELETE'])
def delete_question(request, id):
    try:
        question = Question.objects.get(id=id)
        question.delete()
        return Response({
            'message': 'Question deleted successfully',
            'code': status.HTTP_200_OK,

        })
    except Question.DoesNotExist:
        return Response({
            'code': status.HTTP_404_NOT_FOUND,
            'message': 'Question not found'
        })
    except Exception as e:
        return Response({
            'code': status.HTTP_400_BAD_REQUEST,
            'message': str(e)
        })


@api_view(['GET'])
def get_questions_by_survey(request, id):
    try:
        survey = Survey.objects.get(id=id)
        questions = Question.objects.filter(survey=survey).prefetch_related('choices')

        # Custom serialization
        data = []
        for q in questions:
            question_data = {
                'id': q.id,
                'text': q.text,
                'type': q.type,
                'has_marks': q.has_marks,
                'marks': q.marks,
                'is_required': q.is_required,
                'choices': [{'id': c.id, 'text': c.text} for c in q.choices.all()]
            }
            data.append(question_data)

        return Response({
            'message': 'Questions Retrieved Successfully by Survey ID',
            'code': status.HTTP_200_OK,
            'survey_id': id,
            'survey_title': survey.title,
            'questions': data
        })

    except Survey.DoesNotExist:
        return Response({
            'code': status.HTTP_404_NOT_FOUND,
            'message': f'Survey not found'
        })


# Choice CRUD APIs
@api_view(['POST'])
def create_choice(request):
    try:
        serializer = ChoiceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'code': status.HTTP_201_CREATED,
                'message': "Choice created successfully",
                'data': serializer.data
            })
        return Response({
            'code': status.HTTP_400_BAD_REQUEST,
            'message': serializer.errors
        })
    except Exception as e:
        return Response({
            'code': status.HTTP_400_BAD_REQUEST,
            'message': str(e)
        })


@api_view(['GET'])
def get_choice(request, id):
    try:
        choice = Choice.objects.get(id=id)
        serializer = ChoiceSerializer(choice)
        return Response({
            'code': status.HTTP_200_OK,
            'data': serializer.data,
            'message': 'Choice retrieved successfully'
        })
    except Choice.DoesNotExist:
        return Response({
            'code': status.HTTP_404_NOT_FOUND,
            'message': 'Choice not found'
        })
    except Exception as e:
        return Response({
            'code': status.HTTP_400_BAD_REQUEST,
            'message': str(e)
        })


@api_view(['PUT'])
def update_choice(request, id):
    try:
        choice = Choice.objects.get(id=id)
        serializer = ChoiceSerializer(choice, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'code': status.HTTP_200_OK,
                'data': serializer.data,
                'message': 'Choice updated successfully'
            })
        return Response({
            'code': status.HTTP_400_BAD_REQUEST,
            'message': serializer.errors
        })
    except Choice.DoesNotExist:
        return Response({
            'code': status.HTTP_404_NOT_FOUND,
            'message': 'Choice not found'
        })
    except Exception as e:
        return Response({
            'code': status.HTTP_400_BAD_REQUEST,
            'message': str(e)
        })


@api_view(['DELETE'])
def delete_choice(request, id):
    try:
        choice = Choice.objects.get(id=id)
        choice.delete()
        return Response({
            'code': status.HTTP_200_OK,
            'message': 'Choice deleted successfully'
        })
    except Choice.DoesNotExist:
        return Response({
            'code': status.HTTP_404_NOT_FOUND,
            'message': 'Choice not found'
        })
    except Exception as e:
        return Response({
            'code': status.HTTP_400_BAD_REQUEST,
            'message': str(e)
        })


# Survey Target CRUD APIs
@api_view(['POST'])
def create_survey_target(request):
    try:
        serializer = SurveyTargetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'code': status.HTTP_201_CREATED,
                'message': "Survey target created successfully",
                'data': serializer.data
            })
        return Response({
            'code': status.HTTP_400_BAD_REQUEST,
            'message': serializer.errors
        })
    except Exception as e:
        return Response({
            'code': status.HTTP_400_BAD_REQUEST,
            'message': str(e)
        })


@api_view(['GET'])
def get_survey_target(request, id):
    try:
        target = SurveyTarget.objects.get(id=id)
        serializer = SurveyTargetSerializer(target)
        return Response({
            'code': status.HTTP_200_OK,
            'data': serializer.data,
            'message': 'Survey target retrieved successfully'
        })
    except SurveyTarget.DoesNotExist:
        return Response({
            'code': status.HTTP_404_NOT_FOUND,
            'message': 'Survey target not found'
        })
    except Exception as e:
        return Response({
            'code': status.HTTP_400_BAD_REQUEST,
            'message': str(e)
        })


@api_view(['PUT'])
def update_survey_target(request, id):
    try:
        target = SurveyTarget.objects.get(id=id)
        serializer = SurveyTargetSerializer(target, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'code': status.HTTP_200_OK,
                'data': serializer.data,
                'message': 'Survey target updated successfully'
            })
        return Response({
            'code': status.HTTP_400_BAD_REQUEST,
            'message': serializer.errors
        })
    except SurveyTarget.DoesNotExist:
        return Response({
            'code': status.HTTP_404_NOT_FOUND,
            'message': 'Survey target not found'
        })
    except Exception as e:
        return Response({
            'code': status.HTTP_400_BAD_REQUEST,
            'message': str(e)
        })


@api_view(['DELETE'])
def delete_survey_target(request, id):
    try:
        target = SurveyTarget.objects.get(id=id)
        target.delete()
        return Response({
            'code': status.HTTP_200_OK,
            'message': 'Survey target deleted successfully'
        })
    except SurveyTarget.DoesNotExist:
        return Response({
            'code': status.HTTP_404_NOT_FOUND,
            'message': 'Survey target not found'
        })
    except Exception as e:
        return Response({
            'code': status.HTTP_400_BAD_REQUEST,
            'message': str(e)
        })


# Survey Response CRUD APIs
@api_view(['POST'])
def create_survey_response(request):
    try:
        serializer = SurveyResponseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'code': status.HTTP_201_CREATED,
                'message': "Survey response created successfully",
                'data': serializer.data
            })
        return Response({
            'code': status.HTTP_400_BAD_REQUEST,
            'message': serializer.errors
        })
    except Exception as e:
        return Response({
            'code': status.HTTP_400_BAD_REQUEST,
            'message': str(e)
        })


@api_view(['GET'])
def get_survey_response(request, id):
    try:
        response = SurveyResponse.objects.get(id=id)
        serializer = SurveyResponseDetailSerializer(response)
        return Response({
            'code': status.HTTP_200_OK,
            'data': serializer.data,
            'message': 'Survey response retrieved successfully'
        })
    except SurveyResponse.DoesNotExist:
        return Response({
            'code': status.HTTP_404_NOT_FOUND,
            'message': 'Survey response not found'
        })
    except Exception as e:
        return Response({
            'code': status.HTTP_400_BAD_REQUEST,
            'message': str(e)
        })


@api_view(['GET'])
def get_responses_for_survey(request, survey_id):
    try:
        responses = SurveyResponse.objects.filter(survey_id=survey_id)
        serializer = SurveyResponseDetailSerializer(responses, many=True)
        return Response({
            'code': status.HTTP_200_OK,
            'data': serializer.data,
            'message': 'Survey responses retrieved successfully'
        })
    except Exception as e:
        return Response({
            'code': status.HTTP_400_BAD_REQUEST,
            'message': str(e)
        })


@api_view(['PUT'])
def update_survey_response(request, id):
    try:
        response = SurveyResponse.objects.get(id=id)
        serializer = SurveyResponseSerializer(response, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'code': status.HTTP_200_OK,
                'data': serializer.data,
                'message': 'Survey response updated successfully'
            })
        return Response({
            'code': status.HTTP_400_BAD_REQUEST,
            'message': serializer.errors
        })
    except SurveyResponse.DoesNotExist:
        return Response({
            'code': status.HTTP_404_NOT_FOUND,
            'message': 'Survey response not found'
        })
    except Exception as e:
        return Response({
            'code': status.HTTP_400_BAD_REQUEST,
            'message': str(e)
        })


@api_view(['DELETE'])
def delete_survey_response(request, id):
    try:
        response = SurveyResponse.objects.get(id=id)
        response.delete()
        return Response({
            'code': status.HTTP_200_OK,
            'message': 'Survey response deleted successfully'
        })
    except SurveyResponse.DoesNotExist:
        return Response({
            'code': status.HTTP_404_NOT_FOUND,
            'message': 'Survey response not found'
        })
    except Exception as e:
        return Response({
            'code': status.HTTP_400_BAD_REQUEST,
            'message': str(e)
        })


# Answer CRUD APIs
@api_view(['POST'])
def create_answer(request):
    try:
        serializer = AnswerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'code': status.HTTP_201_CREATED,
                'message': "Answer created successfully",
                'data': serializer.data
            })
        return Response({
            'code': status.HTTP_400_BAD_REQUEST,
            'message': serializer.errors
        })
    except Exception as e:
        return Response({
            'code': status.HTTP_400_BAD_REQUEST,
            'message': str(e)
        })


@api_view(['GET'])
def get_answer(request, id):
    try:
        answer = Answer.objects.get(id=id)
        serializer = AnswerSerializer(answer)
        return Response({
            'code': status.HTTP_200_OK,
            'data': serializer.data,
            'message': 'Answer retrieved successfully'
        })
    except Answer.DoesNotExist:
        return Response({
            'code': status.HTTP_404_NOT_FOUND,
            'message': 'Answer not found'
        })
    except Exception as e:
        return Response({
            'code': status.HTTP_400_BAD_REQUEST,
            'message': str(e)
        })


@api_view(['PUT'])
def update_answer(request, id):
    try:
        answer = Answer.objects.get(id=id)
        serializer = AnswerSerializer(answer, data=request.data, partial=True)
        if serializer.is_valid():
            # Handle image upload separately if needed
            serializer.save()
            return Response({
                'code': status.HTTP_200_OK,
                'data': serializer.data,
                'message': 'Answer updated successfully'
            })
        return Response({
            'code': status.HTTP_400_BAD_REQUEST,
            'message': serializer.errors
        })
    except Answer.DoesNotExist:
        return Response({
            'code': status.HTTP_404_NOT_FOUND,
            'message': 'Answer not found'
        })
    except Exception as e:
        return Response({
            'code': status.HTTP_400_BAD_REQUEST,
            'message': str(e)
        })


@api_view(['DELETE'])
def delete_answer(request, id):
    try:
        answer = Answer.objects.get(id=id)
        answer.delete()
        return Response({
            'code': status.HTTP_200_OK,
            'message': 'Answer deleted successfully'
        })
    except Answer.DoesNotExist:
        return Response({
            'code': status.HTTP_404_NOT_FOUND,
            'message': 'Answer not found'
        })
    except Exception as e:
        return Response({
            'code': status.HTTP_400_BAD_REQUEST,
            'message': str(e)
        })
