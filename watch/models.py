from django.db import models

class Watch(models.Model):
    name = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    description = models.TextField()
    TYPE_CHOICES = [
        ('a', 'Analog'),
        ('d', 'Digital'),
        ('h', 'Hybrid'),
    ]
    is_mine = models.BooleanField(default=False)
    main_image = models.CharField(max_length=300)
    second_image = models.CharField(max_length=300)
    type = models.CharField(max_length=1, choices=TYPE_CHOICES)
    def __str__(self):
        return self.name