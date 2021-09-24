from django import forms

from common.models import Comment
from pets.models import Pet


class CommentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for (_, field) in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    pet_id = forms.IntegerField(widget=forms.HiddenInput())

    class Meta:
        model = Comment
        fields = ('comment', )

    def save(self, commit=True):
        pet_id = self.cleaned_data['pet_id']
        pet = Pet.objects.get(pk=pet_id)
        comment = Comment(
            comment=self.cleaned_data['comment'],
            pet=pet,
        )

        if commit:
            comment.save()

        return comment
