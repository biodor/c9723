'''
from django.urls import path
from . import views

urlpatterns = [
    # [...]
    path('', views.ProfileList.as_view(), name='profile_list'),
    path('council/<int:pk>', views.ProfileDetail.as_view(), name='profile_detail'),
    path('create', views.ProfileCreate.as_view(), name='profile_create'),
    path('update/<int:pk>', views.ProfileUpdate.as_view(), name='profile_update'),
    path('delete/<int:pk>', views.ProfileDelete.as_view(), name='profile_delete'),
]
'''