from django.db import models
from sponsor.models import Sponsor


class StudyChoices(models.TextChoices):
    bakalavr = "Bakalavr"
    magistr = "Magistr"


class University(models.Model):
    title = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "University"
        verbose_name_plural = "Universities"


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

    def __str__(self):
        return self.full_name

    def update_payed_amount(self):
        self.payed_amount = self.sponsors.filter('amount').count()

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)


class StudentSponsor(models.Model):
    sponsor = models.ForeignKey(Sponsor, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='sponsors')
    amount = models.IntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.student} - {self.sponsor}"


class SponsorTransactions(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    sponsor = models.ForeignKey(Sponsor, on_delete=models.CASCADE)
    amount = models.IntegerField(default=0)
    is_success = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.student} - {self.sponsor}"

    def trans_amount(self):
        if self.sponsor.amount >= self.amount:
            sponsor_amount = self.sponsor.amount - self.amount

            self.sponsor.amount = sponsor_amount
            self.sponsor.used_amount += self.amount

            self.student.payed_amount += self.amount
            self.is_success = True
        else:
            return {"error": "There are insufficient funds in your account"}

    def save(self, *args, **kwargs):
        super(SponsorTransactions, self).save(*args, **kwargs)

