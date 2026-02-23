from django.urls import path
from .views import StudentCourseListCreateAPIView, StudentLessonProgressListCreateAPIView,StudentLessonFeedbackListCreateAPIView, HomeworkSubmissionListCreateAPIView

urlpatterns = [
    path('student-course/', StudentCourseListCreateAPIView.as_view()),
    path('student-course/<int:pk>/', StudentCourseListCreateAPIView.as_view()),

    path('student-lesson-progress/', StudentLessonProgressListCreateAPIView.as_view()),
    path('student-lesson-progress/<int:pk>/', StudentLessonProgressListCreateAPIView.as_view()),

    path('student-lesson-feedback/', StudentLessonFeedbackListCreateAPIView.as_view()),
    path('student-lesson-feedback/<int:pk>/', StudentLessonFeedbackListCreateAPIView.as_view()),

    path('homework-submission/', HomeworkSubmissionListCreateAPIView.as_view()),
    path('homework-submission/<int:pk>/', HomeworkSubmissionListCreateAPIView.as_view()),
]