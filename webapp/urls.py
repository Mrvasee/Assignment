from django.urls import path
from . import views
urlpatterns=[

path('Home',views.Home,name='Home'),
path('Home/Weather', views.weather_Info, name='weather'),
path('Form_Submission/', views.form_submission, name='form_submission'),
path('intern-Login',views.Intern_Login,name='intern-login'),
path('view-details/', views.view_details, name='view-details'),
path('Home/About',views.About,name='About')
]