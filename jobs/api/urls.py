from django.urls import path
from jobs.api import views

urlpatterns = [
    path('jobs/', views.ListView.as_view(), name= 'list'),
    path('jobs/<int:pk>/', views.DetailViews.as_views(), name ='detail'),

]