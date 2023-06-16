from django.db import models

# Create your models here.

class Letter(models.Model):
    id = models.BigAutoField(primary_key=True)
    from_name = models.CharField(max_length=200)
    to_name = models.CharField(max_length=200)
    letter_text = models.TextField()
    created_at = models.DateTimeField('date published')
    def __str__(self):
        return self.letter_text