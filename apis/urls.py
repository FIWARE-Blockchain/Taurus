from django.urls import path
from .views import version, configs, task, configByID

urlpatterns = [
   path('version/', version),
   path('task/', task),   
   path('config/', configs),
   path('config/<int:id>', configByID)
]
