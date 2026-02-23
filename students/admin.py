from django.contrib import admin
from .models import StudentCourse, StudentLessonProgress, StudentLessonFeedback, HomeworkSubmission
# Register your models here.

admin.site.register(StudentCourse)
admin.site.register(StudentLessonProgress)
admin.site.register(StudentLessonFeedback)
admin.site.register(HomeworkSubmission)

