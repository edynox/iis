from ..models import Mammoth, Message, Hunt, Hunter
from django.shortcuts import render, redirect
from .forms import MammothForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages



@login_required
def profile(request):
    cont = {}
    tmp = request.GET.get('id_mammoth')
    mammoth = Mammoth.objects.get(pk=tmp)
    location = False
    try:
        tmp_loc = Message.objects.filter(mammoths=mammoth.id).latest('id')
        location = tmp_loc.from_watch.location
    except:
        pass
    try:
        tmp_loc = Hunt.objects.filter(target=mammoth.id).latest('id')
        location = tmp_loc.pit.location
    except:
        pass

    if not location:
        location = 'Unknown'
    mammoth.location = location
    try:
        hunt = Hunt.objects.filter(target=mammoth.id, finished=False).latest('id')
    except:
        hunt = False
    if hunt:
        mammoth.hunted_w = 'Yes'
    else:
        mammoth.hunted_w = 'No'
    if not mammoth.killedIn and mammoth.health > 0:
        mammoth.status = 'Alive'
    else:
        mammoth.status = 'Dead'

    cont['hunts'] = Hunt.objects.filter(target=mammoth.id).order_by('finished', '-id')
    for hunt in cont['hunts']:
        try:
            if hunt.target.killedIn.id == hunt.id:
                hunt.successful = 'Yes'
        except:
            hunt.successful = 'No'

    cont['last_messages'] = Message.objects.filter(mammoths=mammoth.id).order_by('-id')
    for message in cont['last_messages']:
        message.location = message.from_watch.location

    cont['form'] = MammothForm(instance=mammoth)
    if not request.user.isOfficer():
        for field in cont['form'].fields.values():
            field.widget.attrs['readonly'] = True
    if mammoth.killedIn:
        cont['form'].fields['health'].widget.attrs['readonly'] = True
    if request.method == 'POST':
        cont['form'] = MammothForm(request.POST, instance=mammoth)
        if cont['form'].is_valid():
            mammoth = cont['form'].save()
            messages.success(request, "Mammoth updated")
        else:
            messages.error(request, "Mammoth update failed")


    cont['mammoth'] = mammoth
    return render(request, 'app/mammoth/profile.html', cont)


@login_required
def mammothList(request):
    cont = {}

    cont['mammoths'] = Mammoth.objects.all()
    cont['mammoths'] = cont['mammoths'].extra(select={'living':"health > '0'"})
    cont['mammoths'] = cont['mammoths'].extra(order_by=['-living', '-hunt', '-id'])
    for mammoth in cont['mammoths']:
        try:
            tmp_loc = Message.objects.filter(mammoths=mammoth.id).latest('id')
            location = tmp_loc.from_watch.location
        except:
            location = 'Unknown'
        mammoth.location = location

        try:
            hunt = Hunt.objects.filter(target=mammoth.id, finished=False).latest('id')
            mammoth.hunted = True
            mammoth.hunt_id = hunt.id
            mammoth.hunted_w = 'Yes'
        except:
            mammoth.hunted_w = 'No'

        if not mammoth.killedIn and mammoth.health > 0:
            mammoth.status = 'Alive'
        else:
            mammoth.status = 'Dead'

    return render(request, 'app/mammoth/list.html', cont)


@login_required
def create(request, returnToDash=False):
    cont = {}
    cont['form'] = MammothForm()
    if request.method == 'POST':
        cont['form'] = MammothForm(request.POST)
        if cont['form'].is_valid():
            cont['form'].save()
            messages.success(request, "Mammoth created")
        else:
            messages.error(request, "Mammoth creation failed")

    if returnToDash:
        return redirect('index')
    return render(request, 'app/mammoth/create.html', cont)


@login_required
def createInDash(request):
    return create(request, returnToDash=True)
