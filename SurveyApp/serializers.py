from rest_framework import serializers
from.models import *



class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'




class SurveyTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SurveyType
        fields = '__all__'



