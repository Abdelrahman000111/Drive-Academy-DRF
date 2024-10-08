from django.contrib import admin
from django.urls import path , include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('accounts/',include('accounts.urls',namespace='accounts')),
    path('admin/', admin.site.urls),
    path('' , views.home , name = 'home'),
    path('courses/',include('course.urls',namespace='course')),
    path('about/',include('about.urls',namespace='about')),
    path('trainers/',include('trainers.urls',namespace='trainers')),
    path('pages/',include('pages.urls',namespace='pages')),
    path('contact/',include('contact.urls',namespace='contact')),
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)