from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseBadRequest
from .models import ThemeModel
import traceback
from io import StringIO
from contextlib import redirect_stdout

from django.db.models import Q


def homepage(request, pk=None):
    themes = ThemeModel.objects.all().order_by('id')
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


def execute_code(code):
    try:
        output_buffer = StringIO()
        with redirect_stdout(output_buffer):
            exec(code)
        output = output_buffer.getvalue()
    except Exception as e:
        output = f"Error: {str(e)}\n{traceback.format_exc()}"
    return output


def index(request):
    if request.method == "GET":
        code_string = request.GET.get("value", "")
        code_string = (
            code_string.replace("\\n", "\n").replace("\\t", "\t").replace("plus", "+").replace("comment","#")
        )
        output = execute_code(code_string)
        return render(request, "compiler.html", {"code": code_string, "output": output})


def runcode(request):
    if request.method == "POST":
        codeareadata = request.POST.get("codearea", "")
        output = execute_code(codeareadata)
        return render(
            request, "compiler.html", {"code": codeareadata, "output": output}
        )
    else:
        return HttpResponseBadRequest("Method not allowed")
