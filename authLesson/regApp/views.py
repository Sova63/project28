from django.shortcuts import render, redirect, get_object_or_404
from .forms import UserForm
from domain.models import User
from django.contrib import messages





# Create your views here.
def signup(request):
	if request.method == "POST":
		form = UserForm(request.POST)
		if form.is_valid():
			user = form.save(commit=False)
			user.password = form.cleaned_data['password']  # Получаем пароль из формы
			user.save()  # Сохраняем пользователя с зашифрованным паролем
			messages.success(request, "Регистрация прошла успешно!")
			return redirect('signup')
	else:
		form = UserForm()
	return render(request,'reg_index.html',{'form': form})
