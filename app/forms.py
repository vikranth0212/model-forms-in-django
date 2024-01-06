from app.models import *
from app.views import *
from django import forms

class TopicForm(forms.ModelForm):
    class Meta():
        model=Topic
        fields='__all__'

class WebpageForm(forms.ModelForm):
    class Meta():
        model=Webpage
        fields='__all__'

class AccessRecordForm(forms.ModelForm):
    class Meta():
        model=Accessrecord
        fields='__all__'        