from django.shortcuts import render
from django.shortcuts import render
from django.contrib.auth.models import User
from django import forms

# Create your views here.
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404 ,redirect
from django.views.generic.edit import FormMixin
from django.utils.translation import gettext as _
from django.conf.urls import url

from django.views.generic import  ListView ,DetailView
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib.auth.decorators import permission_required
from django.utils.decorators import method_decorator
from .models import Tours,Comment,ToursBook,Important_links,featureTours
from.forms import ToursBookForm
from contact .models import Contact,Info
from .filters import ToursFilter
# Create your views here.




def Tourslist(request):
    Tours_list = Tours.objects.all()
    Tours_list = Tours.objects.all()
    Infoo = Info.objects.all()[:1]
    ## filters
    myfilter = ToursFilter(request.GET,queryset=Tours_list)
    Tours_list = myfilter.qs


    #paginator = Paginator(Tours_list, 3) # Show 25 contacts per page.
    #page_number = request.GET.get('page')
    #page_obj = paginator.get_page(page_number)


    context = {'Tours_list' :Tours_list , 'myfilter' : myfilter,'Infoo' : Infoo}
 # template name
    return render(request,'Tourslist.html',context)


#filer


class ToursDetail(FormMixin,DetailView):
     model=Tours
     template_name = 'Tours_detail.html'
     form_class =ToursBookForm


    ##books

     def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['relatede'] = Important_links.objects.all()
        context['Infoo'] = Info.objects.all()
        context["related"] = Tours.objects.filter(category=self.get_object().category)[:3]
        # ^^^ bad duplication.
        return context

     #def get_context_data(self, **kwargs):
         #context = super().get_context_data(**kwargs)
         #context['relatede'] = Important_links.objects.all()
         #return context

        #return context



     #@method_decorator(login_required(login_url='/accounts/login/'))
     def post(self, request, *args, **kwargs):
      form = self.get_form()

      if form.is_valid():
        myform = form.save(commit=False)
        myform.Tours=self.get_object()
        #myform.user = request.user
        myform.save()
        return redirect('Post:thank_you')



        ##books
