#python base.py runserver 8080
import os
import sys

from django.conf import settings

#DEBUG = os.environ.get('DEBUG', 'on') == 'on'
DEBUG = True

SECRET_KEY = os.environ.get('SECRET_KEY', os.urandom(32))

#ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', 'localhost').split(',')
ALLOWED_HOSTS = ['127.0.0.1']

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

from django.conf.urls import url
from django.core.wsgi import get_wsgi_application
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.views.generic.base import TemplateView
from django.views.generic import ListView

#class index(TemplateView):
class index(ListView):
	template_name = 'base.html'
	paginate_by = 5
	queryset = range(50)
	
	#def get_context_data(self, **kwargs):
	#	context = super(index, self).get_context_data(**kwargs)
	#	context['content'] = range(50)
#		return context


urlpatterns = (
    url(r'^$', index.as_view(), name='index'),
)


application = get_wsgi_application()


if __name__ == "__main__":
    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
