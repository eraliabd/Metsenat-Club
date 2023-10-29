from django.contrib import admin

from .models import University, Student, StudentSponsor, SponsorTransactions

admin.site.register(University)
admin.site.register(Student)
admin.site.register(StudentSponsor)
admin.site.register(SponsorTransactions)
