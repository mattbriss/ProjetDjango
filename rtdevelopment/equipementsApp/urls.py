from django.urls import urlpatterns, path
from.import views

urlpatterns = [
    
    path('',views.index, name='index'),
]