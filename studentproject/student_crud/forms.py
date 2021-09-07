from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import StudentAcademics, StudentInfo


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class StudentRecordForm(forms.ModelForm):

    class Meta:
        model = StudentInfo
        fields = '__all__'


class Academics(forms.ModelForm):

    class Meta:
        model = StudentAcademics
        fields = '__all__'
        exclude = ['roll_no_id',]

    def __init__(self, roll_no=None, *args, **kwargs):

        super(Academics, self).__init__(*args, **kwargs)
        #self.fields['roll_no_id'] = forms.ModelChoiceField(queryset=StudentInfo.objects.filter(studentacademics=roll_no))



