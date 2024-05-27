from django.db import models


class Worker(models.Model):
    """Model representing a worker."""
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Unit(models.Model):
    """Model representing a unit linked to a worker."""
    name = models.CharField(max_length=255)
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE, related_name='units', null=False)

    def __str__(self):
        return self.name


class Visit(models.Model):
    """Model representing a visit to a unit."""
    date_time = models.DateTimeField(auto_now_add=True)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE, related_name='visits')
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return f"Visit to {self.unit.name} at {self.date_time}"
