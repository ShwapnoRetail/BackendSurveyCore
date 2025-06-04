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
        dept_obj=Department.objects.get(id=id)
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