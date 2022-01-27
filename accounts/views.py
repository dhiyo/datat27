from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth import authenticate, login

from django.shortcuts import render
from django.shortcuts import redirect
from django.template import Context

from .forms import AccessorForm
LoginForm=AccessorForm

usernamek='kk'

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

def index(request):
    #latest_question_list = Question.objects.order_by('-pub_date')[:5]
    #context = {'latest_question_list': latest_question_list}
    return render(request, 'accounts/index.html')

def logind(request):
	if request.method == "POST" :
		print("hello")
		form=LoginForm()
		if form.is_valid() :
	      		form.save()
			
		else :
			print("error")



		username = request.POST.get('username','')
		password = request.POST.get('password','')
		#form=LoginForm(request.POST)
		print(username)
		global usernamek
		usernamek=username
		user = authenticate(username=username, password=password)
		contextr = {"a": "1", "b": "2"}
		if user is not None :
			if user.is_active:
				print("successful")
				return redirect('accounts:profile')
		else :
			pass 

	else :
		form=LoginForm()
		
	return render(request, 'accounts/login.html',{'form': form})



def profile(request):
    #latest_question_list = Question.objects.order_by('-pub_date')[:5]
    contextr = usernamek
 	
    return render(request, 'accounts\dashboard1.html',{'village':contextr})