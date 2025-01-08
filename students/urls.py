from django.urls import path
from . import views

app_name = 'students'
urlpatterns = [
    path('list/', views.student_list, name='list'),
    path('create/', views.student_create, name='create'),
    path('update/<int:year>/<int:month>/<int:day>/<slug:slug>/', views.student_update, name='update'),
    path('delete/<int:year>/<int:month>/<int:day>/<slug:slug>/', views.student_delete, name='delete'),
    path('detail/<int:year>/<int:month>/<int:day>/<slug:slug>/', views.student_detail, name='detail'),
]