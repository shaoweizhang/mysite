from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.http import Http404
from polls.models import Poll,Choice
from django.core.urlresolvers import reverse

# Create your views here.
def index(request):
    latest_poll_list = Poll.objects.order_by('-pub_date')[:5]
    context = {'latest_poll_list': latest_poll_list}
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    try:
        poll = Poll.objects.get(pk=question_id)
    except Poll.DoesNotExist:
        raise Http404

    return render(request, 'polls/detail.html', {'poll': poll})

def results(request, question_id):
    poll = get_object_or_404(Poll, pk=question_id)
    return render(request, 'polls/results.html', {'poll': poll})

def vote(request, question_id):
    p = get_object_or_404(Poll, pk=question_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'poll': p,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))
