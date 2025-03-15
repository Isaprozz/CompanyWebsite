from django.contrib.sitemaps import Sitemap
from django.urls import reverse

class StaticViewSitemap(Sitemap):
    """Sitemap for static pages like Home, About, Services, and Contact."""
    priority = 0.8
    changefreq = "monthly"

    def items(self):
        return ['home', 'about', 'services', 'contact']  # Match names in urls.py

    def location(self, item):
        return reverse(item)  # Get the correct URL for each page
