
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


@api_view(['POST'])
def create_choice(request):
    try:
        question_id = request.data.get('question') or request.data.get('question_id')
        if not question_id:
            return Response({'code': 400, 'message': 'Question ID is required'})

        try:
            question = Question.objects.get(id=question_id)
            if question.type != 'choice':
                return Response({
                    'code': 400,
                    'message': f'Cannot add choices to {question.type} type questions. Only "choice" type questions accept custom choices.'
                })

            choice = Choice.objects.create(
                question=question,
                text=request.data.get('text'),
                is_correct=request.data.get('is_correct', False)
            )
            return Response({
                'code': 201,
                'message': 'Choice created successfully',
                'data': ChoiceSerializer(choice).data
            })

        except Question.DoesNotExist:
            return Response({
                'code': 404,
                'message': f'Question with ID {question_id} not found. Please provide a valid question ID of type "choice".'
            })

    except Exception as e:
        return Response({
            'code': 400,
            'message': str(e)
        })


@api_view(['GET'])
def get_choice(request, id):
    try:
        choice = Choice.objects.get(id=id)
        serializer = ChoiceSerializer(choice)
        return Response({
            'message': 'Choice retrieved successfully',
            'code': status.HTTP_200_OK,
            'data': serializer.data,

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
                'message': 'Choice updated successfully',
                'code': status.HTTP_200_OK,
                'data': serializer.data,

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
        survey_id = request.data.get('survey')
        if not survey_id:
            return Response({
                'code': 400,
                'message': 'survey field is required'
            }, status=400)

        try:
            survey = Survey.objects.get(id=survey_id)
        except Survey.DoesNotExist:
            return Response({
                'code': 404,
                'message': 'Survey not found'
            }, status=404)

        target = SurveyTarget.objects.create(
            survey=survey,
            target_type=request.data.get('target_type'),
            role_name=request.data.get('role_name'),
            department_id=request.data.get('department'),
            user_id=request.data.get('user_id'),
            site_id=request.data.get('site_id')
        )

        serializer = SurveyTargetSerializer(target)
        return Response({
            'message': 'Target created successfully',
            'code': 201,
            'data': serializer.data
        }, status=201)

    except Exception as e:
        return Response({
            'code': 400,
            'message': str(e)
        }, status=400)


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
                'message': 'Survey target updated successfully',
                'code': status.HTTP_200_OK,
                'data': serializer.data,

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
# @api_view(['POST'])
# def create_answer(request):
#     try:
#         serializer = AnswerSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({
#                 'code': status.HTTP_201_CREATED,
#                 'message': "Answer created successfully",
#                 'data': serializer.data
#             })
#         return Response({
#             'code': status.HTTP_400_BAD_REQUEST,
#             'message': serializer.errors
#         })
#     except Exception as e:
#         return Response({
#             'code': status.HTTP_400_BAD_REQUEST,
#             'message': str(e)
#         })
#
#
# @api_view(['GET'])
# def get_answer(request, id):
#     try:
#         answer = Answer.objects.get(id=id)
#         serializer = AnswerSerializer(answer)
#         return Response({
#             'code': status.HTTP_200_OK,
#             'data': serializer.data,
#             'message': 'Answer retrieved successfully'
#         })
#     except Answer.DoesNotExist:
#         return Response({
#             'code': status.HTTP_404_NOT_FOUND,
#             'message': 'Answer not found'
#         })
#     except Exception as e:
#         return Response({
#             'code': status.HTTP_400_BAD_REQUEST,
#             'message': str(e)
#         })
#
#
# @api_view(['PUT'])
# def update_answer(request, id):
#     try:
#         answer = Answer.objects.get(id=id)
#         serializer = AnswerSerializer(answer, data=request.data, partial=True)
#         if serializer.is_valid():
#             # Handle image upload separately if needed
#             serializer.save()
#             return Response({
#                 'message': 'Answer updated successfully',
#                 'code': status.HTTP_200_OK,
#                 'data': serializer.data,
#
#             })
#         return Response({
#             'code': status.HTTP_400_BAD_REQUEST,
#             'message': serializer.errors
#         })
#     except Answer.DoesNotExist:
#         return Response({
#             'code': status.HTTP_404_NOT_FOUND,
#             'message': 'Answer not found'
#         })
#     except Exception as e:
#         return Response({
#             'code': status.HTTP_400_BAD_REQUEST,
#             'message': str(e)
#         })
#
#
# @api_view(['DELETE'])
# def delete_answer(request, id):
#     try:
#         answer = Answer.objects.get(id=id)
#         answer.delete()
#         return Response({
#             'message': 'Answer deleted successfully',
#             'code': status.HTTP_200_OK,
#
#         })
#     except Answer.DoesNotExist:
#         return Response({
#             'code': status.HTTP_404_NOT_FOUND,
#             'message': 'Answer not found'
#         })
#     except Exception as e:
#         return Response({
#             'code': status.HTTP_400_BAD_REQUEST,
#             'message': str(e)
#         })




def get_user_from_request(request):
    auth_header = request.headers.get('Authorization')
    if not auth_header or not auth_header.startswith('Bearer '):
        raise AuthenticationFailed('Authorization header missing or invalid')

    token = auth_header.split(' ')[1]
    return validate_shwapno_jwt(token)




@api_view(['POST'])
@authentication_classes([ShwapnoJWTAuthentication])
@permission_classes([IsJWTAuthenticated])
def create_answer(request):
    def validate_answer(question, data, files):
        """Validate answer data against question type"""
        if question.type == 'yesno':
            if 'answer_text' not in data or data['answer_text'] not in ['Yes', 'No']:
                return 'Yes/No questions require answer_text of "Yes" or "No"'

        elif question.type == 'choice':
            if 'selected_choice' not in data:
                return 'Choice questions require selected_choice'
            if not question.choices.filter(id=data['selected_choice']).exists():
                return 'Invalid choice selected'

        elif question.type == 'image':
            if 'image' not in files:
                return 'Image questions require an image upload'

        elif question.type == 'location':
            if not all(k in data for k in ['location_lat', 'location_lon']):
                return 'Location questions require both latitude and longitude'

        elif question.type == 'text':
            if 'answer_text' not in data or not data['answer_text'].strip():
                return 'Text questions require answer_text'

        return None

    try:
        # Get authenticated user from JWT
        user_data = request.user
        user_id = user_data['user_id']
        is_admin = user_data.get('is_admin', False)

        # Validate required fields
        required_fields = ['response', 'question']
        if not all(field in request.data for field in required_fields):
            return Response({
                'code': status.HTTP_400_BAD_REQUEST,
                'message': f'Required fields: {", ".join(required_fields)}'
            }, status=status.HTTP_400_BAD_REQUEST)

        response_id = request.data['response']
        question_id = request.data['question']

        # Get survey response
        try:
            response = SurveyResponse.objects.get(id=response_id)
            # Verify the response belongs to the user (unless admin)
            if not is_admin and response.user_id != user_id:
                return Response({
                    'code': status.HTTP_403_FORBIDDEN,
                    'message': 'You can only answer your own surveys'
                }, status=status.HTTP_403_FORBIDDEN)
        except SurveyResponse.DoesNotExist:
            return Response({
                'code': status.HTTP_404_NOT_FOUND,
                'message': 'Survey response not found'
            }, status=status.HTTP_404_NOT_FOUND)

        # Validate question exists and belongs to the survey
        try:
            question = Question.objects.get(id=question_id)
            if question.survey_id != response.survey_id:
                return Response({
                    'code': status.HTTP_400_BAD_REQUEST,
                    'message': 'Question does not belong to this survey'
                }, status=status.HTTP_400_BAD_REQUEST)
        except Question.DoesNotExist:
            return Response({
                'code': status.HTTP_404_NOT_FOUND,
                'message': 'Question not found'
            }, status=status.HTTP_404_NOT_FOUND)

        # Validate answer format
        error = validate_answer(question, request.data, request.FILES)
        if error:
            return Response({
                'code': status.HTTP_400_BAD_REQUEST,
                'message': error
            }, status=status.HTTP_400_BAD_REQUEST)

        # Prepare answer data
        answer_data = {
            'response': response,
            'question': question,
            'answer_text': request.data.get('answer_text'),
            'is_admin_submission': is_admin,
            'submitted_by': {
                'user_id': user_id,
                'username': user_data.get('username', ''),
                'email': user_data.get('email', ''),
                'is_admin': is_admin
            }
        }

        # Create or update answer
        answer, created = Answer.objects.update_or_create(
            response=response,
            question=question,
            defaults=answer_data
        )

        serializer = AnswerSerializer(answer)
        return Response({
            'code': status.HTTP_201_CREATED,
            'message': 'Answer submitted successfully',
            'data': serializer.data,
            'created': created
        }, status=status.HTTP_201_CREATED)

    except Exception as e:
        import traceback
        logger.error(f"Error submitting answer: {str(e)}\n{traceback.format_exc()}")
        return Response({
            'code': status.HTTP_500_INTERNAL_SERVER_ERROR,
            'message': str(e)
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



# Similar updates for other CRUD operations
@api_view(['GET', 'PUT', 'DELETE'])
def answer_operations(request, id):
    try:
        # Authentication
        try:
            auth_data = get_user_from_request(request)
            user_id = auth_data['user_id']
            is_admin = auth_data['is_admin']
        except AuthenticationFailed as e:
            return Response({
                'code': status.HTTP_401_UNAUTHORIZED,
                'message': str(e)
            })

        answer = Answer.objects.get(id=id)
        response = answer.response

        # Permission check
        if not is_admin and response.user_id != user_id:
            return Response({
                'code': status.HTTP_403_FORBIDDEN,
                'message': 'You can only access your own answers'
            })

        if request.method == 'GET':
            serializer = AnswerSerializer(answer)
            return Response({
                'code': status.HTTP_200_OK,
                'data': serializer.data,
                'message': 'Answer retrieved successfully',
                'user_info': {
                    'user_id': user_id,
                    'username': auth_data['username'],
                    'email': auth_data['email']
                }
            })

        elif request.method == 'PUT':
            serializer = AnswerSerializer(answer, data=request.data, partial=True)
            if serializer.is_valid():
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

        elif request.method == 'DELETE':
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
