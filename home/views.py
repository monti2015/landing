from django.shortcuts import render
from django.utils.translation import gettext as _

# Create your views here.

def index(request):

  # from django.utils import translation
  # user_language = 'th'
  # translation.activate(user_language)
  # request.session[translation.LANGUAGE_SESSION_KEY] = user_language
  # if translation.LANGUAGE_SESSION_KEY in request.session:
  #   del request.session[translation.LANGUAGE_SESSION_KEY]

  context = {
    'hello' : _('Hello')
  }

  return render(request, 'index.html', context)