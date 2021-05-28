from django.db import models
from django.urls import reverse

GRADES = (
    ('A', 'Excellent'),
    ('B', 'Great'),
    ('C', 'Above Average'),
    ('D', 'Average'),
    ('E', 'Mediocre'),
    ('F', 'Failure')
)
class Store(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('stores_detail', kwargs={'pk': self.id})

# Create your models here.
class Game(models.Model):
    name = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    release_year = models.IntegerField()
    stores = models.ManyToManyField(Store)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'game_id': self.id})

class Review(models.Model):
    date = models.DateField('Date Reviewed')
    grade = models.CharField(max_length = 1, choices=GRADES, default=GRADES[0][0])
    comment = models.CharField(max_length=250)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_grade_display()} on {self.date}: {self.comment}"

    class Meta:
        ordering = ['-date']

