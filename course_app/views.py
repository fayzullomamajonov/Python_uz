from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseBadRequest
from .models import ThemeModel
import traceback
from io import StringIO
from contextlib import redirect_stdout

from django.db.models import Q


def homepage(request, pk=None):
    themes = ThemeModel.objects.all()
    default_theme = ThemeModel.objects.order_by('id').first()
    search_query = request.GET.get('search')

    if search_query:
        themes = themes.filter(Q(theme_name__icontains=search_query))

    if pk is not None:
        theme = get_object_or_404(ThemeModel, pk=pk)
    else:
        theme = None

    if theme is not None:
        context = {
            "themes": themes,
            "theme": theme,
            # 'search_theme': search_theme,
        }
    else:
        if default_theme is not None:
            context = {
                "themes": themes,
                "default_theme": default_theme,
            }
        else:
            context = {
                "message": "Kurs mavjud emas 😕",
            }

    return render(request, "home.html", context=context)
