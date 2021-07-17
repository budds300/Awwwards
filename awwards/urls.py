from django.conf.urls import url 
from django.urls import  path
from . import views


urlpatterns = [
    path('',views.index, name='index'),
    path('search/',views.search_result,name='search_result'),
    path('project/<project_id>',views.project,name = 'project'),
    path('profile/',views.profile, name='profile')
]