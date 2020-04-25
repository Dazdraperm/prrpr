from django.urls import path
from .views import statements, index, category, info, get_name

urlpatterns = [
    path('', index, name='index'),
    path('statements', statements, name='statements'),
    path('category', category, name='category'),
    path('info', info, name='info'),
    path('get_name', get_name, name='get_name'),
]
