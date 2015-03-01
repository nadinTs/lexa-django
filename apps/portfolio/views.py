from django.shortcuts import render
from django.http import HttpResponse
from portfolio.models import Category, Project
from django.template import RequestContext, loader


def index(request):
    categories = Category.objects.all()
    data = {
        'categories': categories,
    }
    return render(request, 'portfolio/index.html', data)


def project_details(request, category_nick, project_nick):
    return HttpResponse("You are looking at project %s." % project_nick)


def category_index(request, category_nick):
    return HttpResponse("You are looking at projects in category %s." % category_nick)

