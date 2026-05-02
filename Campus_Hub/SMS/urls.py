from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('insert/', views.insert_record, name='insert'),
    path('search/',views.search_record,name='search'),
    path('update/',views.update_record,name='update'),
    path('delete/',views.delete_record,name='delete'),

]