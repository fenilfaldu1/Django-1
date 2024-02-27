from rest_framework import serializers
from .models import Student, Standard

class StudentModelSerializer(serializers.ModelSerializer):
    # standard_name = serializers.SerializerMethodField()
    class Meta:
        model = Student
        fields = '__all__'

    # def get_standard_name(self, obj):
    #     return obj.standard_name.standard_name if obj.standard_name is not None else None

class StandardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Standard
        fields = '__all__'
