from django.db import models
from users.models import User
from courses.models import Course, Lesson, Homework

# Create your models here.

class StudentCourse(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    start_date = models.DateTimeField(blank=True, null=True)
    finish_date = models.DateTimeField(blank=True, null=True)
    is_blocked = models.BooleanField(default=False)
    is_paid = models.BooleanField(default=False)
    video_link = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user} | {self.course}"
    

class StudentLessonProgress(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    student_course = models.ForeignKey(Course, on_delete=models.CASCADE)
    is_opened = models.DateTimeField(default=False)
    opened_at = models.DateTimeField(blank=True, null=True)
    is_complated = models.DateTimeField(default=False)
    complated_at = models.DateTimeField(blank=True, null=True)
    is_homework_done = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.lesson} | {self.student_course} | {self.is_homework_done}"
    


class StudentLessonFeedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    is_deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    star = models.PositiveIntegerField(default=5)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user} | {self.lesson} | {self.star}"
    


class HomeworkSubmission(models.Model):
    homework = models.ForeignKey(Homework, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)
    file = models.FileField(blank=True, null=True)
    ball = models.IntegerField(default=0)
    is_checked = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.homework} | {self.user}"
    

    
