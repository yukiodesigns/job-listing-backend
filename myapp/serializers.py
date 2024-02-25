from rest_framework import serializers
from .models import CustomUser, Company, Job, Application

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email', 'role')

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ('id', 'name', 'location', 'description')

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = ('id', 'company', 'title', 'description', 'qualifications', 'requirements', 'specifications', 'working_times', 'history')

class ApplicationSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = Application
        fields = ('id', 'job', 'user', 'applicant_name', 'applicant_email', 'cover_letter', 'application_date')
