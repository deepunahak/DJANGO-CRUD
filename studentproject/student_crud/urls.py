"""student_crud URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [

    path('', views.student_list, name='welcome'),
    path('register/', views.registerPage, name='register'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),

    path('home/', views.home, name='home'),

    path('create_student/', views.student_form, name='create_student'),
    path('create_student/<str:pk>/', views.student_form, name='create_student'),
    # path('update_student/<str:pk>/', views.updateStudent, name='update_student'),
    # path('delete_student/<str:pk>/', views.deleteStudent, name='delete_student'),

    path('reset_password/', auth_views.PasswordResetView.as_view(template_name='accounts/password_reset.html'), name='reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name='accounts/password_reset_sent.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='accounts/password_reset_form.html'), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_done.html'), name='password_reset_complete'),

]

'''
1 - Submit email form                             //  PasswordResetView.as_view()
2 - Email sent success message                    //  PasswordResetDoneView.as_view()
3 - Link to password Reset form in email          //  PasswordResetConfirmView.as_view()
4 - Password Successfully changed message         //  PasswordResetCompleteView.as_view()
'''
