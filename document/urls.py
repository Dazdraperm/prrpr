from django.urls import path, include
from .views import statements, index, category, info, document, admin, login, schedule, auto_fill, \
    UpdatePassport, UpdateProfile

from .views import statements, index, category, info, UpdateProfile, document, admin, login, schedule, info_6, consent, \
    survey_questionnaire, statement_of_command, additional_bank, contract, how, conditions, position, material_aid

urlpatterns = [
    path('', index, name='index'),
    path('statements', statements, name='statements'),
    path('schedule', schedule, name='schedule'),
    path('consent', consent, name='consent'),
    path('survey_questionnaire', survey_questionnaire, name='survey_questionnaire'),
    path('statement_of_command', statement_of_command, name='statement_of_command'),
    path('additional_bank', additional_bank, name='additional_bank'),
    path('contract', contract, name='contract'),
    path('material_aid', material_aid, name='material_aid'),
    path('how', how, name='how'),
    path('position', position, name='position'),
    path('conditions', conditions, name='conditions'),
    path('category', category, name='category'),
    path('info/<int:pk>/', info, name='info'),
    path('info_6', info_6, name='info_6'),
    path('auto_fill', auto_fill, name='auto_fill'),
    path('schedule', schedule, name='schedule'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('profile/<int:pk>/', UpdateProfile.as_view(), name='profile'),
    path('passport/<int:pk>/', UpdatePassport.as_view(), name='passport'),
    # path('CourseGroup/<int:pk>/', UpdateCourse.as_view(), name='CourseGroup'),
    path('document', document, name='document'),
    path('admin1', admin, name='admin1'),
    path('login', login, name='login'),
]
