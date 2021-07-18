from django.conf.urls import url 
from django.urls import  path
from . import views


urlpatterns = [
    path('',views.index, name='index'),
    path('search/',views.search_result,name='search_result'),
    path('project/<project_id>',views.project,name = 'project'),
    path('profile/',views.profile, name='profile'),
    path('register/',views.register, name='register'),
    path('update/',views.update, name='update'),
    path('upload_project/',views.upload_project,name='upload_project'),
    path('rate/<project_id>/',views.rate,name='rate')
]