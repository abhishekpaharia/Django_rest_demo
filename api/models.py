from django.db import models

class Drink(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)

    @property
    def new_name(self):
        return "new" + self.name 
    def __str__(self) -> str:
        return self.name