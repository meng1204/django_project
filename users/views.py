from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm

# Create your views here.

# Message Types
# message.debug
# message.information
# message.success
# message.warning
# message.error


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()  # save it to DB
            # or form.cleaned_data.get('username')
            username = form.cleaned_data['username']
            messages.success(
                request, f'Your Account has been created! You are able to login now!')
            return redirect('login')
    else:
        form = UserRegisterForm()

    return render(request, 'users/register.html', {'form': form})


# @ add functionality to function
@login_required
def profile(request):

    return render(request, 'users/profile.html')
