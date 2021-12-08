from django.urls import path
from . import views

app_name = "community"
urlpatterns = [
    path('reviews/', views.review_list),
    path('review/<int:review_pk>/', views.review_detail),
    path('movie/<int:movie_pk>/review/', views.review_create),
    path('movie/<int:movie_pk>/review/<int:review_pk>/', views.review_update_or_delete),
    # path('movie/review/<int:review_pk>', views.review_update_or_delete),

    path('review/<int:review_pk>/comment/', views.comment_create),
    path('review/comment/<int:comment_pk>/', views.comment_update_or_delete),

    path('review/<int:review_pk>/like/', views.review_like),

]