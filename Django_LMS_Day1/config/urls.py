"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from http.client import responses

from django.contrib import admin
from django.http import HttpResponse, Http404
from django.urls import path
from django.shortcuts import render
game_list = [
    {'title': '로스트아크', 'type': 'RPG'},
    {'title': '던전앤파이터', 'type': 'RPG'},
    {'title': '서든어택', 'type': 'FPS'},
    {'title': '카스온라인', 'type': 'FPS'}
]

def index(request):
    return HttpResponse("<h1>Hello</h1>")


def blog_list(request):

    # book_text = ''
    # for i in range(0,10):
    #     book_text += f'book{i}<br>'
    return render(request, "books.html", {'range': range(0,10)})



def book(request, num):
    return render(request, "book.html", {'num':num})

def language(request, lang):
    return HttpResponse(f"<h1>{lang}언어 페이지입니다.</h1>")

def games(request):
    # game_titles = [
    #     f'<a href="/game/{index}/">{game["title"]}</a>'
    #     for index, game in enumerate(game_list)
    # ]

    # game_titles = []
    # for game in game_list:
    #   game_title.append(game['title'])

    # responses_text = '<br>'.join(game_titles)
    # # for index, title in enumerate(game_titles):
    # #     responses_text += f'<a href="/game/{index}/">{title}</a><br>'
    # return HttpResponse(responses_text)
    return render(request, "games.html", {'game_list': game_list})

def game_detail(request, index):
    if index > len(game_list) - 1:
        raise Http404

    game = game_list[index]

    #context = {'game_list' : game_list, 'index':index}
    return render(request, "game.html", {'game': game})

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('blog/', blog_list),
    path('blog/<int:num>/', book),
    path('blog/<str:lang>/', language),
    path('game/', games),
    path('game/<int:index>/', game_detail),
]
