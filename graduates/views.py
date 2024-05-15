from django.shortcuts import render, redirect
from .forms import AlumniAchievementForm



def index(request):
    return render(request,'graduates/index.html')


from .models import Tip


def wishes_universities(request):
    tips = Tip.objects.all()
    return render(request,'graduates/wishes_universities.html',{'title': 'Советы выпускников', 'tips': tips})


from .models import AlumniAchievement


def alumni_achievements(request):
    descriptions = AlumniAchievement.objects.all()
    return render(request, 'graduates/alumni_achievements.html',{'title': 'Достижения выпускников', 'descriptions': descriptions})


def create(request):
    error = ''
    if request.method == 'POST':
        form = AlumniAchievementForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('achievement')
        else:
            error = 'Форма была неверной'

    form = AlumniAchievementForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request,'graduates/create.html',context)