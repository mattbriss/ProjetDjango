from unicodedata import name
from django.urls import path
from.import views

urlpatterns = [
    
    path('',views.index, name='index'),
    path('machines/', views.machine_list_view, name='machines'),
    #path('commutateurs/'), views.machine_list_view, name='commutateurs'),
    #path('terminal/<pk>'),view.machine_detail_view, name='machine-detail'),
    path('add-machine', views.machine_add_form name='add-machine'),
]   