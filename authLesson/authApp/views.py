from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from .forms import UserForm
from domain.models import User
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.hashers import check_password

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

'''def auth(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = User.objects.filter(username=username).first()
            if user is not None and user.isUserPasswordValid(password):
                messages.success(request, 'Успешная аутентификация')
                #return redirect('some_redirect_path')  # Перенаправьте на нужный URL после успешной аутентификации
            else:
                messages.error(request,  'Аутентификация не удалась: пароль неверный')
        else:
            messages.error(request, 'Неудачно: неверная форма')
    else:
        form = UserForm()

    return render(request, 'index.html', {'form': form})'''

'''def auth(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = User.objects.filter(username=username).first()
            if user is not None and user.isUserPasswordValid(password):  # Проверяем пароль через метод модели
                messages.success(request, 'Успешная аутентификация')
                #return redirect('some_redirect_path')  # Перенаправьте на нужный URL после успешной аутентификации
            else:
                messages.error(request, 'Аутентификация не удалась: пароль неверный')
        else:
            messages.error(request, 'Неудачно: неверная форма')
    else:
        form = UserForm()

    return render(request, 'index.html', {'form': form})'''


'''def auth(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = User.objects.filter(username=username).first()

            print(f"Username from form: {username}")
            print(f"Password from form: {password}")  # Не рекомендуется выводить пароль

            if user is not None:
                print(f"Username from DB: {user.username}")
                #print(f"Password from DB (hashed): {user.password}")  # Обычно хранится хэш
                print("Attempting password decryption...")

                # Декодирование пароля из базы данных
                if check_password(password, user.password):
                    print(f"Decoded password from DB: {password}")

                    messages.success(request, 'Успешная аутентификация')
                    # return redirect('some_redirect_path')
                else:
                    messages.error(request, 'Аутентификация не удалась: пароль неверный')
            else:
                messages.error(request, 'Пользователь не найден')
        else:
            messages.error(request, 'Неудачно: неверная форма')
    else:
        form = UserForm()

    return render(request, 'index.html', {'form': form})'''


'''def auth(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = User.objects.filter(username=username).first()

            # Печатаем имя пользователя и пароль из формы
            print(f"Username from form: {username}")
            print(f"Password from form: {password}")  # Не рекомендуется выводить пароль


            if user is not None:
                # Печатаем имя пользователя и пароль из базы данных (хэш)
                print(f"Username from DB: {user.username}")
                print(f"Password from DB (hashed): {user.password}")  # Обычно хранится хэш

                # Проверяем пароль - метод должен декодировать хэш
                if user.isUserPasswordValid(password):
                    messages.success(request, 'Успешная аутентификация')
                    # return redirect('some_redirect_path')
                else:
                    messages.error(request, 'Аутентификация не удалась: пароль неверный')
            else:
                messages.error(request, 'Пользователь не найден')
        else:
            messages.error(request, 'Неудачно: неверная форма')
    else:
        form = UserForm()

    return render(request, 'index.html', {'form': form})'''



'''def auth(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = User.objects.filter(username=username).first()

            print(f"Username from form: {username}")
            print(f"Password from form: {password}")  # Не рекомендуется выводить пароль

            if user is not None:
                print(f"Username from DB: {user.username}")
                print("Attempting password decryption...")

                # Декодирование пароля из базы данных
                if check_password(password, user.password):
                    print(f"Decoded password from DB: {password}")

                    messages.success(request, 'Успешная аутентификация')
                    # return redirect('some_redirect_path')
                else:
                    messages.error(request, 'Аутентификация не удалась: пароль неверный')
            else:
                messages.error(request, 'Пользователь не найден')
        else:
            messages.error(request, 'Неудачно: неверная форма')
    else:
        form = UserForm()

    return render(request, 'index.html', {'form': form})'''

def auth(request):
	if request.method == "POST":
		form = UserForm(request.POST)
		user = User.objects.get(username = form.data['username'])
		print(user.username,"hhshh")
		if user and user.isUserPasswordValid(form.data['password']):
			return HttpResponse("Valid")
	else:
		form = UserForm()
	return render(request,'index.html',{'form': form})