from django.db import models


class SponsorStatusChoices(models.TextChoices):
    new = "Yangi"
    moderation = "Moderatsiyada"
    approved = "Tasdiqlangan"
    not_approved = "Tasdiqlanmagan"
    canceled = "Bekor qilingan"


class SponsorPersonChoices(models.TextChoices):
    physical = "Jismoniy"
    legal = "Yuridik"


class Sponsor(models.Model):
    full_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)
    amount = models.IntegerField(default=0)
    used_amount = models.IntegerField(default=0)
    status = models.CharField(
        max_length=15, choices=SponsorStatusChoices.choices, default=SponsorStatusChoices.not_approved
    )
    person_type = models.CharField(
        max_length=15,
        choices=SponsorPersonChoices.choices,
        default=SponsorPersonChoices.physical,
    )

    company_name = models.CharField(max_length=255, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.full_name

    def update_status(self):
        self.status = SponsorStatusChoices.approved

    def save(self, *args, **kwargs):
        super(Sponsor, self).save(*args, **kwargs)
