from ..models import Mammoth, Message, Hunt, Hunter
from django.shortcuts import render, redirect
from .forms import MammothForm

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
    if not mammoth.killedIn:
        mammoth.status = 'Alive'
    else:
        mammoth.status = 'Dead'

    cont['hunts'] = Hunt.objects.filter(target=mammoth.id)
    for hunt in cont['hunts']:
        hunt.location = hunt.pit.location

    cont['messages'] = Message.objects.filter(mammoths=mammoth.id)
    for message in cont['messages']:
        message.location = message.from_watch.location

    try:
        cont['us'] = Hunter.objects.get(pk=request.user.id).role
    except:
        cont['us'] = 2
    cont['form'] = MammothForm(instance=mammoth)
    if cont['us'] != 2:
        for field in cont['form'].fields.values():
            field.widget.attrs['readonly'] = True
    if request.method == 'POST':
        cont['form'] = MammothForm(request.POST, instance=mammoth)
        if cont['form'].is_valid():
            mammoth = cont['form'].save()

    cont['mammoth'] = mammoth
    return render(request, 'app/mammoth/profile.html', cont)

def mammothList(request):
    cont = {}

    cont['mammoths'] = Mammoth.objects.all()

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

        if not mammoth.killedIn:
            mammoth.status = 'Alive'
        else:
            mammoth.status = 'Dead'

    return render(request, 'app/mammoth/list.html', cont)

def create(request, returnToDash=False):
    cont = {}
    cont['form'] = MammothForm()
    if request.method == 'POST':
        cont['form'] = MammothForm(request.POST)
        if cont['form'].is_valid():
            cont['form'].save()
    if returnToDash:
        return redirect('index')
    return render(request, 'app/mammoth/create.html', cont)

def createInDash(request):
    return create(request, returnToDash=True)
