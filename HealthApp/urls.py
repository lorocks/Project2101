from django.urls import path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("patient_dashboard", views.patient_dashboard_view, name="patient_dashboard"),
    path("doctor_dashboard", views.doctor_dashboard_view, name="doctor_dashboard"),
    path("http_api/", views.http_api, name="http_api"),
    path("redirect_add", views.redirect_adddata_view, name="redirect_add"),
    path("add_weekly", views.add_weekly_view, name="add_weekly"),
    path("add_daily", views.add_daily_view, name="add_daily"),
    path("redirect_notify", views.redirect_notify, name="redirect_notify"),
    path("doctor_email", views.doctor_email, name="doctor_email"),
    path("start", views.index, name="start"),
    path("imagetest", views.image_view, name="image_view"),
    path("send_data_api/", views.send_data_api, name="send_data_api"),
    path("alert_api/", views.alert_api, name="alert_api"),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)