from django.urls import path
from account import views

app_name = "account"

urlpatterns = [
    path("kyc-form/", views.kyc_registration_view, name="kyc-form")
]
