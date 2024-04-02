"""
URL configuration for jackson project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.conf.urls.i18n import i18n_patterns
from django.urls import path, re_path, reverse, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps import Sitemap
from django.contrib.sitemaps.views import sitemap
from django.contrib import sitemaps
from django.contrib.sitemaps import GenericSitemap
from django.utils.translation import gettext_lazy as _
from django.views.i18n import JavaScriptCatalog

from index.views import home_view, test_view, promotions_view, library_index, library_article, logout_view, about_view
from index.models import Article


class HighPrioSitemap(sitemaps.Sitemap):
    priority = 0.9
    changefreq = "daily"
    i18n = True

    def items(self):
        return ["home", "promotions"]

    def location(self, item):
        return reverse(item)

class LowPrioSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = "daily"
    i18n = True

    def items(self):
        return ["library", "about"]

    def location(self, item):
        return reverse(item)
    
class ArticleSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.5
    i18n = True

    def items(self):
        return Article.objects.all()
    
    def lastmod(self, obj):
        return obj.date_updated



sitemaps = {
    "main": HighPrioSitemap,
    "additional": LowPrioSitemap,
    "articles": ArticleSitemap



}



urlpatterns = [
    path("i18n/", include("django.conf.urls.i18n")),
    path('admin/', admin.site.urls),
    path(
        "sitemap.xml",
        sitemap,
        {"sitemaps": sitemaps},
        name="django.contrib.sitemaps.views.sitemap",
    ),
    path('ckeditor/', include('ckeditor_uploader.urls')),
]

urlpatterns += i18n_patterns(
    path('', home_view, name='home'),
    path(_('promotions/'), promotions_view, name='promotions'),
    re_path(r'^test/?$', test_view, name='test'),
    path(_('library/'), library_index, name='library'),
    # re_path(r'^article/(?P<article_id>[0-9]+)/?$', library_article, name="article"),
    path('article/<slug:slug>', library_article, name="article"),
    re_path(r'^logout/?$', logout_view, name="logout"),
    path(_('about/'), about_view, name="about"),
    path("jsi18n/", JavaScriptCatalog.as_view(), name="javascript-catalog"),
)


if settings.DEBUG:
     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)