from django import forms
from .models import ToursBook
from .models import Comment

class DateInput(forms.DateInput):
      input_type = 'date'

class ToursBookForm(forms.ModelForm):

    class Meta:
        model= ToursBook
        fields = ['name','Email','Nationality','phone_number' , 'adults','children','From' ,'To']

        widgets = {
            'From': DateInput(),
            'To': DateInput(),

         }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'content')
