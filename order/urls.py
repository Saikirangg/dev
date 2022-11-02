from django.urls import path
from order import views

urlpatterns = [
    path('details', views.snippet_list),
    path('details/<int:pk>', views.snippet_detail),
    path('tickets', views.tickets_list),
    path('pincodes', views.delivery_pincode),
    path('pincodes/<int:id>', views.delivery_pincode),
    path('tickets/<int:id>', views.ticket),

]
