from django.shortcuts import render
from django.utils.translation import gettext as _

# Create your views here.

def index(request):
  context = {
    'hello' : _('Hello')
  }
  return render(request, 'index.html', context)