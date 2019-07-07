from django.shortcuts import render

def home(request):
    print(request)
    template_name = "index.html"
    context = {'content':'this is my home page'}
    return render(request, template_name, context)

def catagory(request):
    print(request)
    template_name = "catagory.html"
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
