from django.db import models


class Graduate(models.Model):
    name = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='graduates_photos/', blank=True, null=True)

    class Meta:
        verbose_name = 'Выпускники'
        verbose_name_plural = 'Выпускники'


class Tip (models.Model):
    title = models.CharField(max_length=255)
    tip = models.TextField('Пожелания')

    class Meta:
        verbose_name = 'Совет'
        verbose_name_plural = 'Советы'


class AlumniAchievement(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField('Достижения')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Достижение'
        verbose_name_plural = 'Достижения'