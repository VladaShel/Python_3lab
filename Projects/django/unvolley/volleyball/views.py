from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import redirect
from django.template.loader import render_to_string
from django.shortcuts import render
from django.views.decorators.cache import never_cache
from django.http import FileResponse

menu = [{'title': "Войти", 'url_name': 'login'},
        {'title': "Рейтинг", 'url_name': 'top_t'},
        {'title': "Турниры", 'url_name': 'competitions'},
        {'title': "О сайте", 'url_name': 'about'}
        ]


data_db = [
    {'id': 1, 'title': 'Женская сборная', 'content':
        'Состав женской сборной', 'is_published': True},
    {'id': 2, 'title': 'Мужская сборная', 'content':
        'Состав мужской сборной', 'is_published': True},
    {'id': 3, 'title': 'Преподавательский состав', 'content':
        'Состав из числа преподавателей', 'is_published': False},
]


cats_db = [
    {'id': 1, 'name': 'Тренера'},
    {'id': 2, 'name': 'Игроки'},
]


def index(request):
    data = {
        'title': 'Главная страница',
        'menu': menu,
        'posts': data_db,
        'cat_selected': 0,
    }

    return render(request, 'volleyball/index.html', context=data)


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Старница не найдена</h1>')


def about(request):
    return render(request, 'volleyball/about.html', {'title': 'О сайте', 'menu': menu})


def show_team(request, team_id):
    return HttpResponse(f"Отображение состава с id = {team_id}")


def login(request):
    return HttpResponse("Авторизация")


def top_t(request):
    return HttpResponse("Рейтинг")


def competitions(request):
    return HttpResponse("Турниры")


def show_category(request, cat_id):
    data = {
        'title': 'Отображение по рубрикам',
        'menu': menu,
        'posts': data_db,
        'cat_selected': cat_id,
    }
    return render(request, 'volleyball/index.html', context=data)


def serve_nstu_icon(request):
    # Код для обслуживания файла nstu.ico
    # Например, если файл расположен по указанному пути
    from django.conf import settings
    import os
    icon_path = os.path.join(settings.STATIC_ROOT, 'volleyball/images/nstu.ico')
    return FileResponse(open(icon_path, 'rb'), content_type='image/x-icon')