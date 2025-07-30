from django import forms


class PersonalInformation(forms.Form):
    GENDERS = (
        ('m', 'Male'),
        ('f', 'Female')
    )
    gender = forms.ChoiceField(choices=GENDERS)
    full_name = forms.CharField()   # 5 <= fullname's length <= 60
    height = forms.IntegerField()   # 70 <= height <= 250
    age = forms.IntegerField()      # 14 <= age <= 99

    def clean_full_name(self):
        name = self.cleaned_data['full_name']
        if name.istitle() and 5 <= len(name) <= 60:
            return name
        raise forms.ValidationError("full_name is not valid")
    
    def clean_height(self):
        if 70 <= self.cleaned_data['height'] <= 250:
            return self.cleaned_data['height']
        raise forms.ValidationError("height is not valid")
    
    def clean_age(self):
        if 14 <= self.cleaned_data['age'] <= 99:
            return self.cleaned_data['age']
        raise forms.ValidationError("age is not valid")