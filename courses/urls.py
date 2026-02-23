from django.urls import path
from .views import CategoryListCreateAPIView, CourseListCreateAPIView, ModuleListCreateAPIView, LessonListCreateAPIView, HomeworkListCreateAPIView

urlpatterns = [
    path('category/', CategoryListCreateAPIView.as_view()),
    path('category/<int:pk>/', CategoryListCreateAPIView.as_view()),

    path('course/', CourseListCreateAPIView.as_view()),
    path('course/<int:pk>/', CourseListCreateAPIView.as_view()),

    path('module/', ModuleListCreateAPIView.as_view()),
    path('module/<int:pk>/', ModuleListCreateAPIView.as_view()),

    path('lesson/', LessonListCreateAPIView.as_view()),
    path('lesson/<int:pk>/', LessonListCreateAPIView.as_view()),

    path('homework/', HomeworkListCreateAPIView.as_view()),
    path('homework/<int:pk>/', HomeworkListCreateAPIView.as_view()),
]