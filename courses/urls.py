from django.urls import path
from . import views

app_name = 'courses'
urlpatterns = [
    path('list/', views.course_list, name='list'),
    path('create/', views.course_create, name='create'),
    path('delete/<int:year>/<int:month>/<int:day>/<slug:slug>/', views.course_delete, name='delete'),
    path('detail/<int:year>/<int:month>/<int:day>/<slug:slug>/', views.course_detail, name='detail'),
]