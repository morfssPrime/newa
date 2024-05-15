from django.contrib import admin
from .models import Graduate


admin.site.register(Graduate)


from .models import Tip


admin.site.register(Tip)


from .models import AlumniAchievement


admin.site.register(AlumniAchievement)