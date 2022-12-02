from django.urls import re_path
from locus import views

urlpatterns = [
    re_path(r'^file_upload/$', views.FileUploadView.as_view()),
    re_path(r'^list/$', views.PatientListAPIView.as_view())
]