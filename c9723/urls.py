"""c9723 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from council import views

from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('profile_list', views.ProfileList.as_view(), name='profile_list'),
    path('profile_list_13774', views.ProfileList13774.as_view(), name='profile_list_13774'),
    path('profile_list_15167', views.ProfileList15167.as_view(), name='profile_list_15167'),
    path('profile_list_15311', views.ProfileList15311.as_view(), name='profile_list_15311'),
    path('profile_list_16314', views.ProfileList16314.as_view(), name='profile_list_16314'),
    path('', views.faith, name='faith'),
    path('faiths/', views.faiths, name='faiths'),

    path('officers_term/', views.OfficersTerm.as_view(), name='officers_term'),
    
    path('CommunityRespondent/', views.CommunityRespondent, name='CommunityRespondent'),
    path('CommunityDisasterPreparation/', views.CommunityDisasterPreparation, name='CommunityDisasterPreparation'),
    path('CommunityResources/', views.CommunityResources, name='CommunityResources'),
    path('CommunityIndividualResponse/', views.CommunityIndividualResponse, name='CommunityIndividualResponse'),
    path('community/', views.community, name='community'),
    path('life/', views.life, name='life'),
    path('family/', views.family, name='family'),

    path('form/', views.form, name='form'),
    path('OfficersGuide/', views.OfficersGuide, name='OfficersGuide'),
    path('LeadershipResource/', views.LeadershipResource, name='LeadershipResource'),
    path('LeadershipRecruitment/', views.LeadershipRecruitment, name='LeadershipRecruitment'),
    path('LeadershipProgramming/', views.LeadershipProgramming, name='LeadershipProgramming'),

    path('council/<int:pk>', views.ProfileDetail.as_view(), name='profile_detail'),
    path('council_13774/<int:pk>', views.ProfileDetail13774.as_view(), name='profile_detail_13774'),
    path('council_15167/<int:pk>', views.ProfileDetail15167.as_view(), name='profile_detail_15167'),
    path('council_15311/<int:pk>', views.ProfileDetail15311.as_view(), name='profile_detail_15311'),
    path('council_16314/<int:pk>', views.ProfileDetail16314.as_view(), name='profile_detail_16314'),

    path('create', views.ProfileCreate.as_view(), name='profile_create'),
    
    path('update/<int:pk>', views.ProfileUpdate.as_view(), name='profile_update'),
    path('update_13774/<int:pk>', views.ProfileUpdate13774.as_view(), name='profile_update_13774'),
    path('update_15167/<int:pk>', views.ProfileUpdate15167.as_view(), name='profile_update_15167'),
    path('update_15311/<int:pk>', views.ProfileUpdate15311.as_view(), name='profile_update_15311'),
    path('update_16314/<int:pk>', views.ProfileUpdate16314.as_view(), name='profile_update_16314'),

    path('delete/<int:pk>', views.ProfileDelete.as_view(), name='profile_delete'),
    path('register/', views.register, name='register'),

    url(r'^password/$', auth_views.PasswordChangeView.as_view(template_name='council/password_change.html'), name='password_change'),
    url(r'^password/done/$', auth_views.PasswordChangeDoneView.as_view(template_name='council/password_change_done.html'), name='password_change_done'),


    path('login/', auth_views.LoginView.as_view(template_name='council/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='council/logout.html'), name='logout'),
    path('password-reset/',
         auth_views.PasswordResetView.as_view(
             template_name='council/password_reset.html'
         ),
         name='password_reset'),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='council/password_reset_done.html'
         ),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='council/password_reset_confirm.html'
         ),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='council/password_reset_complete.html'
         ),
         name='password_reset_complete'),   
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)