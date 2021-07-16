from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect,Http404
from .models import models
from django.contrib.auth.decorators import login_required
from django.contrib import  messages
from cloudinary.forms import cl_init_js_callbacks
from django.core.exceptions import ObjectDoesNotExist


# Create your views here.
def index(request):
    return render(request,'index.html')