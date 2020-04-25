from django.urls import path
from .views import statements, index, category, info

urlpatterns = [
    path('', index, name='index'),
    path('statements', statements, name='statements'),
    path('category', category, name='category'),
    path('info', info, name='info'),
]

