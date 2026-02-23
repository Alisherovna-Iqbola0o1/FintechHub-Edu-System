from rest_framework.generics import ListCreateAPIView
from .models import StudentCourse, StudentLessonProgress, StudentLessonFeedback, HomeworkSubmission
from .serializers import StudentCourseSerializer, StudentLessonProgressSerializer, StudentLessonFeedbackSerializer, HomeworkSubmissionSerializer
# Create your views here.

class StudentCourseListCreateAPIView(ListCreateAPIView):
    queryset = StudentCourse.objects.all()
    serializer_class = StudentCourseSerializer

class StudentLessonProgressListCreateAPIView(ListCreateAPIView):
    queryset = StudentLessonProgress.objects.all()
    serializer_class = StudentLessonProgressSerializer

class StudentLessonFeedbackListCreateAPIView(ListCreateAPIView):
    queryset = StudentLessonFeedback.objects.all()
    serializer_class = StudentLessonFeedbackSerializer

class HomeworkSubmissionListCreateAPIView(ListCreateAPIView):
    queryset = HomeworkSubmission.objects.all()
    serializer_class = HomeworkSubmissionSerializer