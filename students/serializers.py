from rest_framework import serializers
from .models import (
    StudentCourse,
    StudentLessonProgress,
    StudentLessonFeedback,
    HomeworkSubmission
)

class StudentCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentCourse
        fields = '__all__'


class StudentLessonProgressSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentLessonProgress
        fields = '__all__'


class StudentLessonFeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentLessonFeedback
        fields = '__all__'


class HomeworkSubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeworkSubmission
        fields = '__all__'