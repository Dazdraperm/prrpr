from django.urls import path, include
from django.conf.urls import url
from .views import my_login, my_logout, auto_fill, UpdatePassport, statements, index, category, info, UpdateProfile, \
    document, admin, schedule, consent, survey_questionnaire, statement_of_command, additional_bank, contract, how, \
    conditions, position, material_aid, online_wallet, social_nutrition, UpdateCourse, register

urlpatterns = [
    path('register/', register, name='registration'),
    path('', index, name='index'),
    path('statements', statements, name='statements'),
    path('schedule', schedule, name='schedule'),
    path('consent', consent, name='consent'),
    path('survey_questionnaire', survey_questionnaire, name='survey_questionnaire'),
    path('statement_of_command', statement_of_command, name='statement_of_command'),
    path('additional_bank', additional_bank, name='additional_bank'),
    path('contract', contract, name='contract'),
    path('online_wallet', online_wallet, name='online_wallet'),
    path('material_aid', material_aid, name='material_aid'),
    path('how', how, name='how'),
    path('social_nutrition', social_nutrition, name='social_nutrition'),
    path('position', position, name='position'),
    path('conditions', conditions, name='conditions'),
    path('category', category, name='category'),
    path('info/<int:pk>/', info, name='info'),
    path('info/<int:pk>/auto_fill', auto_fill, name='auto_fill'),
    path('schedule', schedule, name='schedule'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('profile/<int:pk>/', UpdateProfile.as_view(), name='profile'),
    path('passport/<int:pk>/', UpdatePassport.as_view(), name='passport'),
    path('CourseGroup/<int:pk>/', UpdateCourse.as_view(), name='course_group'),
    path('info/<int:pk>/document', document, name='document'),
    path('admin1', admin, name='admin1'),
    path('login', my_login, name='my_login'),
    path('logout', my_logout, name='my_logout'),
]
