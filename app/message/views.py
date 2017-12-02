from django.shortcuts import render, redirect
from .forms import MessageForm
from ..models import Watch, Hunter
from django.contrib.auth.decorators import login_required, user_passes_test
from ..security import privileged_check

@login_required
@user_passes_test(privileged_check)
def messageList(request):
    cont = {}
    hunter = Hunter.objects.get(pk=request.user.id)
    active_watch = Watch.objects.filter(hunters=hunter, active=True)
    if active_watch:
        cont['onwatch'] = True
    else:
        cont['onwatch'] = False
    return render(request, 'app/message/list.html', cont)

@login_required
@user_passes_test(privileged_check)
def detail(request):
    return render(request, 'app/message/list.html')

@login_required
def create(request):
    if request.method != 'POST':
        return redirect('index')

    form = MessageForm(request.POST)
    if not form.is_valid():
        return redirect('index')

    message = form.save(commit=False)

    activeWatch = None
    watch = Watch.objects.filter(hunters=request.user.id, active=True).first()
    # find out if hunter is active watch
    if watch:
        activeWatch = watch

    if not activeWatch:
        return redirect('index')

    message.from_watch = activeWatch
    message.save()

    return redirect('index')
