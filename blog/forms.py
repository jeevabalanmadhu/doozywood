from pyexpat import model
from django import forms 

from .models import Post
from django.forms import DateTimeInput




class ChoicesForm(forms.Form):
    POST_CHOICES = (
    (0,'---'),    
    (1,'Show'),
    (2,'Talent'),
    (3,'Event/Festival'),
    (4,'Rent'),
    (5,'Contact'),

    
    )
    post_select = forms.ChoiceField(choices=POST_CHOICES)


class ShowForm(forms.ModelForm):
    class Meta:
        model = Post
        widgets = {
                
                'description': forms.Textarea(attrs={
                    'cols': 20, 
                    'rows': 3
                }),
        }
        fields = ['name', 'show', 'video_link','img', 'show_language','genre','description','tags']
      
    
    def __init__(self, *args, **kwargs):
        super(ShowForm, self).__init__(*args, **kwargs)
        self.fields['name'].label = "Movie Name"
        self.fields['show_language'].label = "Language"
        self.fields['img'].label ="Poster"
        self.fields['tags'].label = "#Tags"

class TalentForm(forms.ModelForm):
    class Meta:
        model=Post
        widgets = {
                
                'description': forms.Textarea(attrs={
                    'cols': 20, 
                    'rows': 3
                }),
        }
        fields=['name','talent','language','location','img','description','tags']
    def __init__(self, *args, **kwargs):
        super(TalentForm, self).__init__(*args, **kwargs)
        self.fields['img'].label ="Photo"
        self.fields['tags'].label = "#Tags"
        

class EventForm(forms.ModelForm):
    class Meta:
        model = Post
        widgets = {
                'From': DateTimeInput(attrs={
                   
                'type': "datetime-local",
                
                
                }),
                'to': DateTimeInput(attrs={
                   
                'type': "datetime-local",
                
                
                }),
                'description': forms.Textarea(attrs={
                    'cols': 20, 
                    'rows': 3
                }),
        }
        fields = ['name','From','to','img','location','description','tags']        

    def __init__(self, *args, **kwargs):
        super(EventForm, self).__init__(*args, **kwargs)
        self.fields['name'].label = "Event Name"
        self.fields['img'].label = "Poster"
        self.fields['tags'].label = "#Tags"



class RentalForm(forms.ModelForm):
    class Meta:
        model = Post
        widgets = {
                
                'description': forms.Textarea(attrs={
                    'cols': 20, 
                    'rows': 3
                }),
        }
        fields = ['name', 'img', 'rent_option', 'currency','price_per_day','location','description','tags']
      
    
    def __init__(self, *args, **kwargs):
        super(RentalForm, self).__init__(*args, **kwargs)
        self.fields['name'].label = "Rent Name"
        self.fields['price_per_day'].label ="Price per day"
        self.fields['img'].label ="Image"
        self.fields['tags'].label = "#Tags"

class ContactForm(forms.ModelForm):
    class Meta:
        model = Post
        widgets = {
                
                'description': forms.Textarea(attrs={
                    'cols': 20, 
                    'rows': 3
                }),
        }
        fields = ['name', 'contact_type','phone_number','email_id','location','img','description','tags']        

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['name'].label = "Company/Person Name"
        self.fields['img'].label ="Image"
        self.fields['tags'].label = "#Tags"


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title']

        widgets = {
            'content': forms.Textarea(attrs={'cols': 20, 'rows': 3})
        }
