from django.urls import path,include
from . import views


urlpatterns = [
    path('hello/', views.say_hello),
    path('', views.ApiOverview, name='home'),
    path('user/create/', views.UserCreate.as_view(), name='add-user'),
    path('allusers/', views.view_users, name='view_users'),
    path('user/<str:pk>/update/', views.UserUpdate.as_view(), name='update_users'),
    path('user/<str:pk>/delete/', views.delete_user, name='delete_user'),
    path('electricity/create/', views.ElectricityCreate.as_view(), name='add-electricity'),
    path('allelectricities/', views.view_electricity_consumption, name='view_electricity'),
    path('electricity/<str:pk>/update/', views.ElectrictyUpdate.as_view(), name='update_electricity'), 
    path('electricity/<str:pk>/delete/', views.ElectricityDelete.as_view(), name='delete_electricity'),
    path('water/create/', views.WaterCreate.as_view(), name='add-water'),
    path('allwater/', views.view_water_consumption, name='view_water'),
    path('water/<str:pk>/update/', views.WaterUpdate.as_view(), name='update_water'), 
    path('water/<str:pk>/delete/', views.WaterDelete.as_view(), name='delete_water'),
    path('heating/create/', views.HeatingCreate.as_view(), name='add-heating'),
    path('allheatings/', views.view_heating_consumption, name='view_heating'),
    path('heating/<str:pk>/update/', views.HeatingUpdate.as_view(), name='update_heating'), 
    path('heating/<str:pk>/delete/', views.HeatingDelete.as_view(), name='delete_heating'),
    path('league/create/', views.HeatingCreate.as_view(), name='add-league'),
    path('allleague/', views.view_league, name='view_league'),
    path('league/<str:pk>/update/', views.HeatingUpdate.as_view(), name='update_league'), 
    path('league/<str:pk>/delete/', views.HeatingDelete.as_view(), name='delete_league'),
    path('quiz/create/', views.QuizCreate.as_view(), name='add-quiz'),
    path('allquizes/', views.view_quiz, name='view_quiz'),
    path('quiz/<str:pk>/update/', views.QuizUpdate.as_view(), name='update_quiz'), 
    path('quiz/<str:pk>/delete/', views.QuizDelete.as_view(), name='delete_quiz'),
    path('quizquestion/create/', views.QuizQuestionCreate.as_view(), name='add-quizquestion'),
    path('allquizquestions/', views.view_quiz_question, name='view_quizquestion'),
    path('quizquestion/<str:pk>/update/', views.QuizQuestionUpdate.as_view(), name='update_quizquestion'), 
    path('quizquestion/<str:pk>/delete/', views.QuizQuestionDelete.as_view(), name='delete_quizquestion'),
    path('quizanswer/create/', views.QuizAnswerCreate.as_view(), name='add-quiz'),
    path('allquizanswers/', views.view_quiz_answer, name='view_quiz'),
    path('quizanswer/<str:pk>/update/', views.QuizAnswerUpdate.as_view(), name='update_quiz'), 
    path('quizanswer/<str:pk>/delete/', views.QuizAnswerDelete.as_view(), name='delete_quiz'),
    path('take/create/', views.TakeCreate.as_view(), name='add-quiz'),
    path('alltakes/', views.view_take, name='view_quiz'),
    path('take/<str:pk>/update/', views.TakeUpdate.as_view(), name='update_quiz'), 
    path('take/<str:pk>/delete/', views.TakeDelete.as_view(), name='delete_quiz'),
    path('takeanswer/create/', views.TakeAnswerCreate.as_view(), name='add-quiz'),
    path('alltakesanswers/', views.view_take_answer, name='view_quiz'),
    path('takeanswer/<str:pk>/update/', views.TakeAnswerUpdate.as_view(), name='update_quiz'), 
    path('takeanswer/<str:pk>/delete/', views.TakeAnswerDelete.as_view(), name='delete_quiz'),   
]