from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from contact.models import Contact
from django.http import Http404
from django.core.paginator import Paginator

def create(request):
    if request.method == 'POST':
        print("-"*20)
        print(request.method)
        print(request.POST.get('first_name'))
        print("-"*20)
    
    
    context = {

    }

    return render(
        request,
        'contact/create.html',
        context
    )