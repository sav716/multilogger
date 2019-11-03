from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm

def logout_view(request):
    """Log user out"""
    logout(request)
    return HttpResponseRedirect(reverse('learning_logs:index'))

def register(request):
    """Registers users"""
    if request.method != 'POST':
        # No data so make form
        form = UserCreationForm()
    else:
        # Data submitted!
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            # Auto-login the new user, redirect to homepage
            authenticated_user = authenticate(username=new_user.username,
                                    password=request.POST['password1'])
            login(request, authenticated_user)
            return HttpResponseRedirect(reverse('learning_logs:index'))

    context = {'form': form}
    return render(request, 'users/register.html', context)
            
