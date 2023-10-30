from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import UniversityAPIView, StudentListCreateAPIView, StudentDetailAPIView, \
    SponsorTransactionsListCreateAPIView

router = DefaultRouter()
router.register('', UniversityAPIView)

urlpatterns = [
    path('student/', StudentListCreateAPIView.as_view(), name='student'),
    path('student/<int:pk>/', StudentDetailAPIView.as_view(), name='student-detail'),
    path('student/sponsor-trans/', SponsorTransactionsListCreateAPIView.as_view(), name='sponsor-trans'),

    path('university/', include(router.urls)),
]
