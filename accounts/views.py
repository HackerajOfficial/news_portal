from django.shortcuts import render
from django.views import View
from accounts.forms import UserSignUpForm


class UserSignUpView(View):
    def get(self, request):
        form = UserSignUpForm()
        print(request)
        return render(request,'accounts/signup.html', {'form':form} )

    def post(self, request):
        form = UserSignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            raw_password = form.cleaned_data['password1']
            username = form.cleaned_data['username']
            user.set_password(raw_password)
            user.save()
            return render(request,'accounts/success.html')
        return render(request,'accounts/signup.html', {'form':form})





