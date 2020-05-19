from django.contrib.auth import login
from django.urls import path, include
from .views import statements, index, category, info, UpdateProfile, document, admin, UpdatePassport

urlpatterns = [
    path('', index, name='index'),
    path('statements', statements, name='statements'),
    path('category', category, name='category'),
    path('info', info, name='info'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('profile/<int:pk>/', UpdateProfile.as_view(), name='profile'),
    path('passport/<int:pk>/', UpdatePassport.as_view(), name='passport'),
    path('document', document, name='document'),
    path('admin1', admin, name='admin1'),
    path('login', login, name='login')
]
