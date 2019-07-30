from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.base import TemplateView
from news.forms import NewsForm
from news.models import News, Comment
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods


# def home(request):
#     print(request)
#     template_name = "index.html"
#     context = {'content':'this is my home page'}
#     return render(request, template_name, context)

def category(request):
    print(request)
    template_name = "category.html"
    context = {'content':'this is my home page'}
    return render(request, template_name, context)

def elements(request):
    print(request)
    template_name = "elements.html"
    context = {'content':'this is my home page'}
    return render(request, template_name, context)

def contact(request):
    print(request)
    template_name = "contact.html"
    context = {'content':'this is my home page'}
    return render(request, template_name, context)

def singlepost(request):
    print(request)
    template_name = "singlepost.html"
    context = {'content':'this is my home page'}
    return render(request, template_name, context)

class NewsCreateView(LoginRequiredMixin,CreateView):
    login_url = '/accounts/login/'
    template_name   =  "news/create.html"
    form_class      =   NewsForm
    queryset        =   News.objects.all()
    success_url     =   "/"  

    def form_valid(self, form):
        news        =   form.save(commit=False)
        news.author =   self.request.user
        news.save()
        return super(NewsCreateView,self).form_valid(form)
        
    def form_invalid(self, form):
        print(form.errors)
        pass

# class NewsList(ListView):
#     model = News
#     context_object_name = 'news_list'
#     template_name='index.html'
#     ordering        =   ['-created_at']

class NewsTemplateView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(NewsTemplateView, self).get_context_data(**kwargs)
        context["news_list"] = News.objects.all().order_by('-created_at')[:10]
        context["top_news_list"] = News.objects.all().order_by('-view_count')[:10]
        return context
    



class NewsDetailView(DetailView):
    model = News
    template_name='news/details_news.html'
    context_object_name = 'news'

    def get_context_data(self, **kwargs): #For Count visited Page
        context = super().get_context_data(**kwargs)
        context['comments'] = Comment.objects.filter(news=self.object)
        self.object.view_count   = self.object.view_count + 1
        self.object.save()
        return context
    

class NewsDetailEdit(LoginRequiredMixin, UpdateView):
    model                = News
    template_name        =  "news/update_news.html"
    success_url          =  reverse_lazy('index')
    fields               =  ("title","story","cover_image")


    def get_queryset(self):
        return News.objects.filter(author=self.request.user)


# class NewsDetailDelete(DeleteView):
#     model       = News
#     template_name="news/delete_news.html"
#     success_url = reverse_lazy('index')

class NewsDetailDelete(LoginRequiredMixin, DeleteView):
    model       = News
    success_url = reverse_lazy('index')

    def get(self, *args, **kwargs):
        return  self.post(self, *args, **kwargs)
    
    def get_queryset(self):
        return News.objects.filter(author=self.request.user)




@login_required(login_url='accounts/login')
@require_http_methods(['POST'])
def comments(request, *args, **kwargs):
    print("I AM INSIDE VIEW",args, kwargs)
    template_name   =   "news/comment.html"
    comment =  request.POST
    feedback        =   comment.get("feedback")
    news            =   get_object_or_404(News, pk=kwargs.get("news_id"))
    comment         =   Comment(feedback=feedback, commentor=request.user,news=news)
    comment.save()
    comments        = Comment.objects.filter(news=news)
    return render(request, template_name, {"comments": comments})