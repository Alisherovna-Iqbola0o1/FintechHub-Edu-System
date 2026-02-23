from django.db import models
from users.models import User
from students.models import Course
# Create your models here.

class PaymentType(models.TextChoices):
    CART = "Cart", "Karta"
    CASH = "Cash", "Naqd Pul"
    CLICK = "Click", "Click Orqali"
    PAYME = "Payme", "Payme Orqali"
    COIN = "Coin", "Tagada"

class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    student_course = models.ForeignKey(Course, on_delete=models.SET_NULL, blank=True, null=True)
    payment_type = models.CharField(
        max_length=50, 
        choices=PaymentType,
        default=PaymentType.CASH
    )