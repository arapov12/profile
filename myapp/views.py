from django.shortcuts import render
def my_view(request):
    return render(request, 'index.html')
def index(request):
    return render(request, 'myapp/index.html')

from django.shortcuts import render, redirect
from .models import UserProfile  # Подключите вашу модель данных UserProfile
from .forms import UserProfileForm  # Подключите вашу форму UserProfileForm

def register_user(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
            form.save()  # Сохраняем данные в базе данных
            return redirect('/')  # Перенаправляем пользователя на страницу успешной регистрации
    else:
        form = UserProfileForm()  # Создаем новую форму для отображения на странице
    
    return render(request, 'your_template.html', {'form': form})
