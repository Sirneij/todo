from django.db import models

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=2000)
    content = models.TextField()

    class Meta:
        ordering = ('title',)
        verbose_name_plural = 'Todos'

    def __str__(self):
        return self.title