from django.db import models
from sponsor.models import Sponsor


class StudyChoices(models.TextChoices):
    bakalavr = "Bakalavr"
    magistr = "Magistr"


class University(models.Model):
    title = models.CharField(max_length=255, unique=True)


# Create your models here.
class Student(models.Model):
    full_name = models.CharField(max_length=256)
    phone = models.CharField(max_length=15)

    university = models.ForeignKey(University, on_delete=models.CASCADE)
    study_type = models.CharField(max_length=15, choices=StudyChoices.choices)

    required_amount = models.IntegerField(default=0)
    payed_amount = models.IntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class StudentSponsor(models.Model):
    sponsor = models.ForeignKey(Sponsor, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    amount = models.IntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class SponsorTransactions(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    sponsor = models.ForeignKey(Sponsor, on_delete=models.CASCADE)
    amount = models.IntegerField(default=0)
    is_success = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
