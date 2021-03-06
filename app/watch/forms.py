from django.forms import ModelForm
from ..models import Watch, Hunter, Hunt
from django.db.models import Q


class WatchForm(ModelForm):
    class Meta:
        model = Watch
        fields = ['location', 'hunters', 'active']

    def __init__(self, *args, **kwargs):
        super(ModelForm, self).__init__(*args, **kwargs)
        watches = Watch.objects.filter(active=True)
        hunts = Hunt.objects.filter(finished=False)
        hunters = Hunter.objects.filter(~Q(watch__in=watches) &
                                        ~Q(hunt__in=hunts) &
                                        Q(role=0) &
                                        Q(killedIn=None))
        self.fields['hunters'].queryset = hunters
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

        self.fields['active'].widget.attrs['class'] = 'flat'
