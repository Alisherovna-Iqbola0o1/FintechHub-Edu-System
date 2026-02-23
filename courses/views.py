from rest_framework.generics import ListCreateAPIView
from .models import Category, Course, Module, Lesson, Homework
from .serializers import CategorySerializer, CourseSerializer, ModuleSerializer, LessonSerializer, HomeworkSerializer
# Create your views here.

class CategoryListCreateAPIView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CourseListCreateAPIView(ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class ModuleListCreateAPIView(ListCreateAPIView):
    queryset = Module.objects.all()
    serializer_class = ModuleSerializer

class LessonListCreateAPIView(ListCreateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer

class HomeworkListCreateAPIView(ListCreateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = HomeworkSerializer
