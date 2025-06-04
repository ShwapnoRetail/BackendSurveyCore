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
            'code': status.HTTP_200_OK,
            'data': serializer.data,
            'message': 'Department retrieved successfully'
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
        surveyObj=SurveyType.objects.get(id=id)
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
        survey_type=SurveyType.objects.all()

        serializer=SurveyTypeSerializer(survey_type, many=True)
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
        # In a real implementation, you'd get this from the authenticated user
        payload['created_by_user_id'] = request.user.id if request.user.is_authenticated else 1  # Default for testing

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
            'code': status.HTTP_200_OK,
            'data': serializer.data,
            'message': 'Survey list retrieved successfully'
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
            'code': status.HTTP_200_OK,
            'data': response_data,
            'message': 'Survey retrieved successfully'
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
            'code': status.HTTP_200_OK,
            'data': serializer.data,
            'message': 'Survey updated successfully'
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