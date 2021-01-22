from django.urls import path
from .views import homePage, test, addJob, addTask, getExperts, getStatusList, deleteJob, deleteTask, indexPage, updateJob, updateTask

urlpatterns = [
    path('home', homePage),
    path('test', test),
    path('addJob', addJob),
    path('addTask', addTask),
    path('getExperts', getExperts),
    path('getStatusList', getStatusList),
    path('deleteTask/<str:id>', deleteTask),
    path('deleteJob/<str:id>', deleteJob),
    path('updateJob/<str:id>', updateJob),
    path('updateTask/<str:id>', updateTask),
    path('', indexPage)
]