"""django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView as TV
from wagtail import urls as wagtail_urls
from wagtail.admin import urls as wagtailadmin_urls
from wagtail.contrib.sitemaps.views import sitemap
from wagtail.documents import urls as wagtaildocs_urls

from contact.views import ContactMessageView as contact_views

from . import views as base_views

urlpatterns = [
    path("sitemap.xml", sitemap),
    path("", base_views.index, name="index"),
    path("admin/", admin.site.urls),
    path("admin-blog/", include(wagtailadmin_urls)),
    path("documents/", include(wagtaildocs_urls)),
    path("blog/", include(wagtail_urls)),
    path("contact/", contact_views.as_view(), name="contact"),
    path("contact/thanks", TV.as_view(template_name="contact/thanks.html")),
    path("cookies", TV.as_view(template_name="cookies.html")),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += [path('silk/', include('silk.urls', namespace='silk'))]
