from django.db.models import F
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.utils import timezone
from django.views import generic

from .models import Question, Choice

class IndexView(generic.ListView):
    template_name = "polls/index.html"
    # context_object_name = "latest_question_list"
    model = Question

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by("-pub_date")[:5]

    def get(self, request):
        return render(request, self.template_name, context={"object_list": self.get_queryset()})

    def post(self, request):
        if (len(request.POST["question-text"]) > 200):
            return render(request
                        , self.template_name
                        , {"error_message": "Question is too long."})
        if request.user.is_authenticated:
            owner = request.user.username
            Question.objects.create(question_text=request.POST["question-text"], pub_date=timezone.now(), owner=owner)
        else:
            Question.objects.create(question_text=request.POST["question-text"], pub_date=timezone.now())
            
        return HttpResponseRedirect(reverse("polls:index"))

class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/details.html"

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        list = Question.objects.filter(pub_date__lte=timezone.now())
        return list

class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        list = Question.objects.filter(pub_date__lte=timezone.now())
        return list

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(
            request,
            "polls/details.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes = F("votes") + 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))