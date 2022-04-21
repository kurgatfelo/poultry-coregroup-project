from django.urls import path
from . import views


urlpatterns=[
    # re_path('^$',views.welcome,name = 'welcome'),
    path('',views.homepage,name = 'homepage'),
    path('search/', views.search_results, name='search_results'),
]