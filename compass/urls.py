from django.urls import path
from . import views

urlpatterns = [
    path('compass/', views.compass_view, name='compass'),
    path('instructions/<int:instruction_id>/',
         views.instruction_detail_view, name='instruction_detail'),
]
