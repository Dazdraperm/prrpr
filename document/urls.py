from django.urls import path, include
from .views import statements, index, category, info, UpdateProfile, document, admin, login, schedule, auto_fill

urlpatterns = [
    path('', index, name='index'),
    path('statements', statements, name='statements'),
    path('category', category, name='category'),
    path('info', info, name='info'),
    path('auto_fill', auto_fill, name='info'),
    path('schedule', schedule, name='schedule'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('profile/<int:pk>/', UpdateProfile.as_view(), name='profile'),
    path('document', document, name='document'),
    path('admin1', admin, name='admin1'),
    path('login', login, name='login')
]
