from django.shortcuts import render
from django.http import Http404
from portfolio.models import Category, Project


def index(request):
    data = {
        'categories':  Category.objects.all(),
    }
    return render(request, 'portfolio/index.html', data)


def project_details(request, category_nick, project_nick):
    try:
        project = Project.objects.get(nick=project_nick)
    except Project.DoesNotExist:
        raise Http404("Project %s doesn't exist" % project_nick)
    data = {
        'categories': Category.objects.all(),
        'project': project,
        'category_nick': category_nick
    }
    return render(request, 'portfolio/project_details.html', data)


def category_index(request, category_nick):
    try:
        category = Category.objects.get(nick=category_nick)
    except Category.DoesNotExist:
        raise Http404("Category %s doesn't exist" % category_nick)
    data = {
        'categories': Category.objects.all(),
        'category': category,
        'category_nick': category_nick
    }
    return render(request, 'portfolio/category_index.html', data)

def base(request):
    return render(request, 'portfolio/base.html')

