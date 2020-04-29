from django.urls import path, include
from .views import statements, index, category, info, profile, UpdateCharacterView

urlpatterns = [
    path('', index, name='index'),
    path('statements', statements, name='statements'),
    path('category', category, name='category'),
    path('info', info, name='info'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('profile', profile, name='profile'),
    path('profile?', UpdateCharacterView, name='profile?')
]

