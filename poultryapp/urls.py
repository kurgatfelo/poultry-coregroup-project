from django.urls import path,re_path
from . import views
from django.conf import settings



urlpatterns =[
    path('',views.homepage,name='homepage'),
    path('profile/',views.profile,name='profile'),
    path('disease/',views.disease,name='disease'),
    path('search/',views.search_results,name='search'),
    path('uprofile/',views.update_profile,name='uprofile'),
    path('upload/',views.upload_disease,name='upload'),
    path('comments/',views.comments,name='comments')
    







]