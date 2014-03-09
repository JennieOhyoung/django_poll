# from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
# from django.template import RequestContext, loader
from polls.models import Poll, Choice
from django.core.urlresolvers import reverse
# from django.http import Http404



# Each view is responsible for doing one of two things: returning an HttpResponse object containing the content for the requested page, or raising an exception such as Http404. 

# def index(request):
#     return HttpResponse("Hello, world. You're at the poll index.")

# def index(request):
#     latest_poll_list = Poll.objects.order_by('pub_date')[:5]
#     #latest_poll_list = Poll.objects.order_by('pub_date')[:5] in reverse order
#     template = loader.get_template('polls/index.html')
#     # output = ', '.join([p.question for p in latest_poll_list])
#     context = RequestContext(request, {
#         'latest_poll_list': latest_poll_list,  
#         })
#     return HttpResponse(template.render(context))

# The render() function takes the request object as its first argument, a template name as its second argument and a dictionary as its optional third argument. It returns an HttpResponse object of the given template rendered with the given context.

def index(request):
    latest_poll_list = Poll.objects.all().order_by('pub_date')[:5]
    context = {'latest_poll_list': latest_poll_list}
    return render(request, 'polls/index.html', context)

# def detail(request, poll_id):
#     return HttpResponse("You're looking at poll %s." % poll_id)

# def detail(request, poll_id):
#     try:
#         poll = Poll.objects.get(pk=poll_id)
#     except Poll.DoesNotExist:
#         raise Http404
#     return render(request, 'polls/detail.html', {'poll': poll})

def detail(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    return render(request, 'polls/detail.html', {'poll': poll})

# def results(request, poll_id):
#     return HttpResponse("You're looking at the results of poll %s." % poll_id)

def results(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    return render(request, 'polls/results.html', {'poll': poll})

# def vote(request, poll_id):
#     return HttpResponse("You're voting on poll %s." % poll_id)

def vote(request, poll_id):
    p = get_object_or_404(Poll, pk=poll_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the poll voting form.
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




















