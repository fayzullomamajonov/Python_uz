from django.urls import path
from .views import homepage, runcode, index


urlpatterns = [
    path("", homepage, name="homepage"),
    path("home/<int:pk>/", homepage, name="homepage_with_pk"),
    path("index", index, name="index"),
    path("runcode/", runcode, name="runcode"),
]
