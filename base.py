#!py
#coding=utf-8
import os
import sys

from django.conf import settings


# SETTINGS
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
print(BASE_DIR)
#DEBUG = os.environ.get('DEBUG', 'on') == 'on'
DEBUG = True

SECRET_KEY = os.environ.get('SECRET_KEY', os.urandom(32))

#ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', 'localhost').split(',')
ALLOWED_HOSTS = ['127.0.0.1', 'xiaowanzi.com', 'www.xiaowanzi.com']

settings.configure(
    DEBUG=DEBUG,
    SECRET_KEY=SECRET_KEY,
    ALLOWED_HOSTS=ALLOWED_HOSTS,
    ROOT_URLCONF=__name__,
    MIDDLEWARE_CLASSES=(
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ),
        TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.dirname(__file__),
        ],
        },
        ],
)


# VC
import markdown
import celery
from django.conf.urls import url
from django.core.wsgi import get_wsgi_application
from django.http import HttpResponse

# from django.views.generic.base import TemplateView
# from django.views.generic import ListView
# VIEWS
# class index(ListView):
#       template_name = 'base.html'
#       paginate_by = 5
#       queryset = range(50)
# 
#       #def get_context_data(self, **kwargs):
#       #       context = super(index, self).get_context_data(**kwargs)
#       #       context['content'] = range(50)
#       #       return context

class webhook(ListView):
    pass


# URLS
urlpatterns = (
    url(r'^webhook$', webhook.as_view(), name='webhook'),
)


application = get_wsgi_application()


if __name__ == "__main__":
    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
