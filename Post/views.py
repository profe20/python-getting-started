from django.shortcuts import render, get_object_or_404 ,redirect
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404 ,redirect
from django.views.generic.edit import FormMixin

from django.views.generic import  ListView ,DetailView

# Create your views here.
from django import forms
from .models import Post
from .forms  import PostForm
from contact .models import Contact,Info
from Tours .models import Tours,Destinations,featureTours
from django.conf.urls import url
from django.core.paginator import Paginator
from story .models import Category,Story

def index(request,category_slug=None):


    Propertyrft = Post.objects.all()[:3]
    Infoo = Info.objects.all()[:1]
    Tourss = Tours.objects.all()[:3]
    Toursss = Tours.objects.all()[:6]
    featured_post = featureTours.objects.featured_post()
    featureTourss = featureTours.objects.all()[:2]
    Toursssss =Tours.objects.all().order_by('Destinations', '-id').values()[:1]
    Tourssssss =Tours.objects.all().order_by('category', '-id').values()[:1]

    category = None
    categories = Category.objects.all()
    story = Story.objects.all()
    
    if category_slug:
        category = get_object_or_404(Category,slug=category_slug)
        story = story.filter(category=category)






    return render(request ,  'index.html',{

       'Propertyrft' : Propertyrft,
       'Infoo' : Infoo,
        'Tourss' : Tourss,
        'Toursss' : Toursss,
        'Toursssss' : Toursssss,
        'Tourssssss' : Tourssssss,
        'featureTourss' : featureTourss,
        'featured_post' : featured_post,
         'categories':categories,
          'category':category,
          'story':story,

    })






def all_posts(request):
    all_posts = Post.objects.all()
    Infoo = Info.objects.all()[:1]


    paginator = Paginator(all_posts, 5) # Show 25 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'all_posts' :page_obj,'Infoo' :Infoo  }

    return render(request ,  'all_posts.html',context)



def post(request,  id):
    #post= Post.objects.get(id=id)
    post = get_object_or_404( Post , id=id)
    Infoo = Info.objects.all()[:1]


    context = {
         'post' : post ,
          'Infoo' : Infoo ,
    }
    return render(request , 'datail.html',context)


def create_post(request):
    if request.method== 'POST':

        form = PostForm(request.POST , request.FILES)
        if form.is_valid():
           new_form = form.save(commit=False)
           new_form.user = request.user
           new_form.save()
           return redirect('/')


    else:
         form = PostForm()

    context = {
        'form' : form ,
         }
    return render(request,'create.html',context)

def edit_post(request,  id):
    post = get_object_or_404( Post ,  id=id)
    if request.method== 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.user = request.user
            new_form.save()
            return redirect('/')


    else:
         form = PostForm(instance=post)

    context = {
        'form' : form ,
  }
    return render(request,'edit.html',context)


def thank_you(request):
    Infoo = Info.objects.all()
    context = {'Infoo' :Infoo }


    return render(request ,  'thank_you.html',context)
