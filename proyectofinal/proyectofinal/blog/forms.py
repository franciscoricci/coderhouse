from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post, Profile


# Create your forms here.

class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["titulo", "subtitulo", "cuerpo", "fecha", "imagen"]
        labels = {'titulo': "Titulo", 'subtitulo': "Subtitulo", 'cuerpo': "Cuerpo", 'fecha': "Fecha", 'imagen': "Imagen"}

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields['imagen'].required = False

class UpdateUserForm(forms.ModelForm):
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=True,
                             widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    first_name = forms.CharField(max_length=100, required=False,
                             widget=forms.TextInput(attrs={'class': 'form-control'}))

    last_name = forms.CharField(max_length=100, required=False,
                             widget=forms.TextInput(attrs={'class': 'form-control'}))
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']


class UpdateProfileForm(forms.ModelForm):
    avatar = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-file'}))
    descripcion = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))

    class Meta:
        model = Profile
        fields = ['avatar', 'descripcion']