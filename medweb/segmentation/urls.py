from django.urls import path, include
from .views import *
urlpatterns = [
    path('segmentation/', SegmentationAPIView.as_view()),
    path('correction/', CorrectionAPIView.as_view())
]