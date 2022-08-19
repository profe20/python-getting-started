from django.shortcuts import render
from django.shortcuts import render, get_object_or_404 ,redirect
from django.views.generic.edit import FormMixin

from django.views.generic import  ListView

from .models import about
from .models import gallery
from .models import Privacy
from Post  .models import Post
from contact .models import Contact,Info

# Create your views here.


class aboutList(ListView):
    model=about

    def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      context['Infoo'] = Info.objects.all()
    # ^^^ bad duplication.
      return context


def gallery_List(request):
    gallery_List = gallery.objects.all()

    page_number = request.GET.get('page')

    context = {'gallery_List' :gallery_List }

    return render(request ,  'gallery_List.html',context)

def Privacy_List(request):
    Privacy_List = Privacy.objects.all()
    page_number = request.GET.get('page')

    context = {'Privacy_List' :Privacy_List }

    return render(request ,  'Privacy_List.html',context)
