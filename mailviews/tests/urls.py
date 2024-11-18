from django.urls import re_path

from mailviews.previews import autodiscover, site

autodiscover()

app_name = "mailviews"

urlpatterns = [re_path(route=r"", view=site.urls)]
