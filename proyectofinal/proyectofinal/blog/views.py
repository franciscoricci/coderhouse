from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from .forms import NewUserForm, PostForm, UpdateUserForm, UpdateProfileForm
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm

from .models import Post
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeView
from django.contrib.messages.views import SuccessMessageMixin



# Create your views here.
def home(request):
    posts_list = Post.objects.all()
    context = {
        'posts_list': posts_list
    }
    template = loader.get_template('index.html')
    return HttpResponse(template.render(context, request))

def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration successful." )
            return redirect('login')
        else:
            messages.error(request, "Unsuccessful registration. Invalid information.")
    else:
        form = NewUserForm()
    return render(request, 'register.html', {'form': form})

def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("homepage")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="login.html", context={"login_form":form})

def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("homepage")

def postear(request):
    if request.method == "POST":
        post_form = PostForm(request.POST, request.FILES)
        if post_form.is_valid():
            instance = post_form.save(commit=False)
            instance.autor = request.user
            instance.save()
            # post_form.save()
            messages.success(request, "Se ha subido el post!." )
            return redirect('homepage')
        else:
            messages.error(request, "No se ha podido subir el post.")
    else:
        post_form = PostForm()
    return render(request, 'postear.html', {'post_form': post_form})

def delete(request, post_id):
    post = Post.objects.get(pk=post_id)
    post.delete()
    return redirect('homepage')


def ver_post(request, post_id):
    post = Post.objects.get(pk=post_id)
    template = loader.get_template('post.html')
    context = {
        'post': post,
    }
    return HttpResponse(template.render(context, request))


def profile(request):
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile is updated successfully')
            return redirect(to='users-profile')
    else:
        user_form = UpdateUserForm(instance=request.user)
        profile_form = UpdateProfileForm(instance=request.user.profile)

    return render(request, 'profile.html', {'user_form': user_form, 'profile_form': profile_form})


class ChangePasswordView(SuccessMessageMixin, PasswordChangeView):
    template_name = 'change_password.html'
    success_message = "Successfully Changed Your Password"
    success_url = reverse_lazy('homepage')


def about(request):
    info = "Hola! Soy José Francisco Ricci. Vivo en Mendoza, Argentina. Estudio Ingeniería Industrial en la Universidad de Mendoza. \nEn este proyecto creé una aplicación web con Django, la cual consiste en una página web simil blog en la que cada usuario puede subir su blog y ver el de los demás usuarios."
    context = {
        'info': info
    }
    template = loader.get_template('about.html')
    return HttpResponse(template.render(context, request))