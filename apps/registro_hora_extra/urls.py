from django.urls import path
from . import views

app_name = 'horas_extras'

urlpatterns = [
    path('', views.HorasExtrasList.as_view(), name='horas_extras-lista'),
]