from django.urls import path
from . import views

app_name = "movies"
urlpatterns = [
    path('movie/', views.movie_list),
    path('movie/<int:movie_pk>/', views.movie_detail),
    path('movie/<int:movie_pk>/like/', views.movie_like),

    path('movie/recommand/', views.movie_recommand),
    path('movie/recommandBykeyword/', views.movie_recommand_by_keyword),
]