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
        search_term =request.GET.get('query')
        search_projects=Project.search_project(search_term)
        messages= f'{search_projects}'
        context = {'message':messages, 'projects':search_projects}
        
        return render(request,'search.html',context)
        
    else:
        messages="You haven't searched for any item"
        
        return render(request,'search.html',{'message':messages})

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

def register(request):
   form = UserRegistrationForm()
   if request.method == 'POST':
       form=UserRegistrationForm(request.POST)
       if form.is_valid():
           form.save()
           username= form.cleaned_data['username']
           messages.success(request, f'You have successfully created a new account of username {username}')
           
           return redirect('login')
   return render(request,'registration/registration.html',{'form':form})
@login_required
def upload_project(request):
    users=User.objects.exclude(id = request.user.id) 
    form=ProjectUploadForm()
    if request.method == 'POST':
        form= ProjectUploadForm(request.POST,request.FILES)
        if form.is_valid():
            project=form.save(commit=False)
            project.prof_ref=request.user.profile
            project.save()
            messages.success(request,f'Successfully uploaded your Project!')
            
            context={'form':form,'users':user}

    return render(request,'upload_project.html',context)

@login_required
def update(request):
    if request.method == 'POST':
     u_form = UserUpdateForm(request.POST,instance=request.user) 
     p_form = ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
     if u_form.is_valid() and p_form.is_valid():
         u_form.save()
         p_form.save()
         messages.success(request,f'Successfully updated your account')
         
         return redirect('profile')
              
    else:
        u_form=UserUpdateForm(instance=request.user)
        p_form=ProfileUpdateForm(instance=request.user.profile)
    context={'u_form':u_form, 'p_form':p_form}
    
    return render(request,'registration/update.html',context)
            
def rate(request,project_id):
       project = Profile.objects.get(id=project_id)  
       user=request.user
       
       if request.method == 'POST':
           form = PostForm(request.POST)
           if form.is_valid():
                 rate=form.save(commit=False)  
                 rate.user = user
                 rate.project = project
                 rate.save()
           return render(request,'project.html',locals())
       else:
           form = RatingForm()
       return render(request,'rate.html',locals())
            