from django.db import models


class SponsorChoices(models.TextChoices):
    new = "Yangi"
    moderation = "Moderatsiyada"
    approved = "Tasdiqlangan"
    canceled = "Bekor qilingan"


class Sponsor(models.Model):
    full_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)
    amount = models.IntegerField(default=0)
    used_amount = models.IntegerField(default=0)
    status = models.CharField(
        max_length=15, choices=SponsorChoices.choices, default=SponsorChoices.new
    )

    sponsor_app = models.OneToOneField('SponsorApplication', on_delete=models.CASCADE, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.full_name

    def update_full_name(self):
        self.full_name = self.sponsor_app.full_name

    def update_phone(self):
        self.phone = self.sponsor_app.phone

    def update_amount(self):
        self.amount = self.sponsor_app.amount

    def update_status(self):
        self.status = SponsorChoices.moderation

    def get_person_type(self):
        person_type = self.sponsor_app.type
        return person_type

    def get_company_name(self):
        company_name = self.sponsor_app.company_name
        return company_name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)


class SponsorApplicationChoices(models.TextChoices):
    physical = "Jismoniy"
    legal = "Yuridik"


class SponsorApplication(models.Model):
    full_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)
    amount = models.IntegerField(default=0)
    type = models.CharField(
        max_length=15,
        choices=SponsorApplicationChoices.choices,
        default=SponsorApplicationChoices.physical,
    )

    company_name = models.CharField(max_length=255, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.full_name

    # def get_status(self):
    #     status = self.sponsor.status
    #     return status
    #
    # def get_used_amount(self):
    #     used_amount = self.sponsor.used_amount
    #     return used_amount
    #
    # def save(self, *args, **kwargs):
    #     if self.pk == self.sponsor.pk:
    #         super().save(*args, **kwargs)
    #     else:
    #         return {"error": "Not found sponsor!"}
