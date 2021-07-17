from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect,Http404
from .models import Project,Profile,Rating,User
from django.contrib.auth.decorators import login_required
from django.contrib import  messages
from cloudinary.forms import cl_init_js_callbacks
from django.core.exceptions import ObjectDoesNotExist
from .forms import UserRegistrationForm,RatingForm,ProfileUpdateForm,ProjectUploadForm,UserUpdateForm

# Create your views here.
def index(request):
    project = Project.objects.all()
    users = User.objects.all()
    return render(request,'index.html',{'projects':project[::-1],'users':users})

def search_result(request):
    if 'query' in request.GET and request.GET['query']:
        search_item=request.GET.get('query')
        search_query=Project.search_project(search_item)
        messages= f'{search_query}'
        context = {'message':message, 'projects':search_query}
        
        return render(request,'search.html',context)
        
    else:
        messages="You haven't searched for any item"
        
        return render(request,'search.html',{'message':message})

def project(request,project_id):
    try:
        project = Project.objects.get(id=project_id)
    except ObjectDoesNotExist:
        raise Http404()
    
    return render(request,'project.html',{"project":project})
@login_required
def profile(request):
    projects = request.user.profile.projects.all()
    return render(request,'registration/profile.html',{'projects':projects[::-1]})    