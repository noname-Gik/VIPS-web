from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# Основная страница
@login_required
def home(request):
    return render(request, 'webmain/body_content.html', {})
