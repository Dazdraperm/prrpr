from django.urls import path, include
from .views import statements, index, category, info, document, admin, login, schedule, auto_fill, \
    UpdatePassport, UpdateProfile


urlpatterns = [
    path('', index, name='index'),
    path('statements', statements, name='statements'),
    path('category', category, name='category'),
    path('info/<int:pk>/', info, name='info'),
    path('auto_fill', auto_fill, name='auto_fill'),
    path('schedule', schedule, name='schedule'),
    path('accounts/', include('django.contrib.auth.urls')),
    # path('profile', profile, name='profile'),
    path('profile/<int:pk>/', UpdateProfile.as_view(), name='profile'),
    path('passport/<int:pk>/', UpdatePassport.as_view(), name='passport'),
    # path('CourseGroup/<int:pk>/', UpdateCourse.as_view(), name='CourseGroup'),
    path('document', document, name='document'),
    path('admin1', admin, name='admin1'),
    path('login', login, name='login'),
]
