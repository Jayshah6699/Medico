from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Shift(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    start_time = models.DateTimeField()

