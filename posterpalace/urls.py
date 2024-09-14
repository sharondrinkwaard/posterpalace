from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from posterpalace.sitemaps import PosterSitemap, StaticViewSitemap

sitemaps = {
    'posters': PosterSitemap,
    'static': StaticViewSitemap,
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('homepage.urls')),
    path('posters/', include('posters.urls')),
    path('cart/', include('cart.urls')),
    path('profiles/', include('profiles.urls')),
    path('checkout/', include('checkout.urls')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
