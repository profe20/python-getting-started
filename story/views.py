from django.shortcuts import render,get_object_or_404
from .models import  Category,Story
from .filters import storyFilter
from django.db.models import Q
# Create your views here.
def story_list(request,category_slug=None):
    category = None
    categories = Category.objects.all()
    story = Story.objects.all()
    myfilter = storyFilter(request.GET,queryset=story)
    story = myfilter.qs

    if category_slug:
        category = get_object_or_404(Category,slug=category_slug)
        story = story.filter(category=category)

    query=request.GET.get('q')
    if query:
         story = Story.objects.filter(
          Q(name__icontains=query)|
          Q(category__name__icontains=query)

        )

    return render(request, 'story_list.html', {'categories':categories,
                                              'category':category,
                                              'story':story,
                                              'myfilter': myfilter,
                                              })

def story_detail(request,id):
    story=get_object_or_404(Story,id=id)
    return render(request,'story_detail.html',{'story':story})
