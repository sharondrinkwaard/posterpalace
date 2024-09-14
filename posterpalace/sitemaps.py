from django.contrib.sitemaps import Sitemap
from posters.models import Poster, Category
from django.urls import reverse

class PosterSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.7

    def items(self):
        # Return all active posters (Django expects a method named `items`)
        return Poster.objects.all()
    
class StaticViewSitemap(Sitemap):
    priority = 0.5
    changefreq = 'yearly'

    def items(self):
        return ['index', 'service', 'posters']  # Add other static pages here

    def location(self, item):
        return reverse(item)