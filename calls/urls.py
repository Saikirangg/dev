from django.urls import path
from calls import views

urlpatterns = [
    path('call_tags/', views.snippet_list),
    path('call_tags/<int:pk>', views.snippet_detail),
    path('call_status/', views.call_status_snippet_list),
    path('call_status/<int:pk>', views.call_status_snippet_detail),
]
