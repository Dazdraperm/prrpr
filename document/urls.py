from django.urls import path, include, re_path
from .views import statements, index, category, info, UpdateProfile, document

urlpatterns = [
    path('', index, name='index'),
    path('statements', statements, name='statements'),
    path('category', category, name='category'),
    path('info', info, name='info'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('profile/<int:pk>/', UpdateProfile.as_view(), name='profile'),
    path('document', document, name='document')
]

