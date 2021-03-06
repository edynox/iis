from django.shortcuts import render, redirect
from ..models import Watch, Message
from .forms import WatchForm
from django.contrib.auth.decorators import login_required, user_passes_test
from ..security import manager_check
from django.contrib import messages


@login_required
def watchList(request):
    context = {}

    watches = Watch.objects.all().order_by('-active', '-id')

    context['watches'] = watches
    return render(request, 'app/watch/list.html', context)


@login_required
def detail(request):
    context = {}
    watchID = request.GET.get('id_watch')
    watch = Watch.objects.get(pk=watchID)
    messages = Message.objects.filter(from_watch=watch.id)
    context['watch'] = watch
    context['messages_all'] = messages
    return render(request, 'app/watch/detail.html', context)

@login_required
@user_passes_test(manager_check)
def create(request):
    context = {}
    form = WatchForm()

    if request.method == 'POST':
        form = WatchForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Watch created")
            return redirect('watch_list')

        messages.error(request, "Watch wasn't crated")

    context['form'] = form
    return render(request, 'app/watch/create.html', context)


@login_required
@user_passes_test(manager_check)
def end(request):

    watchid = request.GET.get('id_watch')
    try:
        watch = Watch.objects.get(pk=watchid)
        watch.active = False
        watch.save()
    except:
        pass
    return redirect('watch_list')
