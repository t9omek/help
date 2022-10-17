from django.urls import path
from filmyweb.views import all_issues, nowy_film, edytuj_film, usun_film

urlpatterns = [
    path('all/', all_issues, name="all_issues"),
    path('nowy/', nowy_film, name="nowy_film"),
    path('edytuj/<int:id>/', edytuj_film, name="edytuj_film"),
    path('usun/<int:id>/', usun_film, name="usun_film"),
]
