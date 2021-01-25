from django.urls import path
from .views import configs, task

urlpatterns = [
#    path('config/', configs),
   path('task/', task),
   path('config/', configs)

]
