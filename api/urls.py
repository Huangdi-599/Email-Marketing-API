from django.urls import path
from . import views

urlpatterns = [
    
    
    path('signup', views.UserSignup.as_view()),

    
    path('lists', views.CreateLists.as_view()),
    path('lists/<int:pk>/update', views.UpdateLists.as_view()),
    path('lists/<int:pk>/delete',views.DeleteLists.as_view()),
    
    
   
]