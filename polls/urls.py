from django.urls import path

from . import views

app_name = "polls"
urlpatterns = [
    path("", views.index, name="index"),
    # ex: /polls/5/
    path("<int:question_id>/", views.question_details, name="batatafrita"),
    # ex: /polls/5/results/
    path("<int:question_id>/results/", views.poll_results, name="results"),
    # ex: /polls/5/vote/
    path("<int:question_id>/vote/", views.vote, name="vote"),
    
]