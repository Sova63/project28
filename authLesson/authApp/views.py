from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from .forms import UserForm
from domain.models import User
from django.http import HttpResponse
from django.contrib import messages

'''def auth(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():# Проверяем, валидна ли форма
            username = form.cleaned_data['username']# Получаем введённые данные
            password = form.cleaned_data['password']# Получаем введённые данные
            user = User.objects.filter(username=username).first()
            #print( user.password == password,user.password,password)
            if user is not None and user.password == password: # Если пользователь найден и пароль совпадает
                return HttpResponse("Успешная аутентификация")
            else:# Если данные неправильные
                return HttpResponse("Аутентификация не удалась: пароль неверный")
        else: # Если форма не валидна
            return HttpResponse("Неудачно: неверная форма")
    else:
        form = UserForm()

    return render(request, 'index.html', {'form': form})'''

def auth(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = User.objects.filter(username=username).first()
            if user is not None and user.password == password:
                messages.success(request, 'Успешная аутентификация')
                #return redirect('some_redirect_path')  # Перенаправьте на нужный URL после успешной аутентификации
            else:
                messages.error(request,  'Аутентификация не удалась: пароль неверный')
        else:
            messages.error(request, 'Неудачно: неверная форма')
    else:
        form = UserForm()

    return render(request, 'index.html', {'form': form})


#def signup(request):
#	if request.method == "post":
#		pass
#	return render(request,'reg_index.html')

'''def auth(request):
	if request.method == "POST":
		form = UserForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponse("Successful")
		else:
			form.save()
			return HttpResponse("Unsuccessful")
	else:
		form = UserForm()
	return render(request,'index.html',{'form': form})'''