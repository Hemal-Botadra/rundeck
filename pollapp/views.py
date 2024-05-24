from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import CreatePollForm
from .models import Poll
# Create your views here.
def homepage(request):
    polls = Poll.objects.all()
    context = {
        'polls': polls
    }

    return render(request,'homepage.html',context)

def make(request):
    form = CreatePollForm()
    if request.method == 'POST':
        form = CreatePollForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    context = {
        'form': form
    }
    return render(request,'make.html',context)

def vote(request, poll_id):
    poll = Poll.objects.get(pk=poll_id)
    print(poll)
    if request.method == 'POST':

        selected_option = request.POST['poll']
        print(selected_option)
        if selected_option == 'option1':
            poll.option_one_count += 1
        elif selected_option == 'option2':
            poll.option_two_count += 1
        elif selected_option == 'option3':
            poll.option_three_count += 1
        else:
            return HttpResponse(400, 'Invalid form')

        poll.save()

        return redirect('result', poll.id)

    context = {
        'poll': poll
    }
    return render(request, 'vote.html', context)

def result(request,poll_id):
    poll = Poll.objects.get(pk=poll_id)
    context = {
        'poll': poll
    }

    return render(request,'result.html',context)


