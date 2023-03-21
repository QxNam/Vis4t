from django.shortcuts import render
from .forms import LoginForm
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.
def index(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect(reverse('home:index'))
    return render(request, 'login/login_form.html', 
                  {'form': LoginForm})

    