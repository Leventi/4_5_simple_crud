from django.db import models


class TimestampFields(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Project(TimestampFields):
    """Объект на котором проводят измерения."""

    name = models.TextField()
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return f'{self.pk} | {self.name} | {self.created_at} | {self.updated_at}'


class Measurement(TimestampFields):
    """Измерение температуры на объекте."""

    value = models.FloatField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media', max_length=250, blank=True, null=True)

    def __str__(self):
        return f'{self.pk} | {self.project} | {self.value}'
