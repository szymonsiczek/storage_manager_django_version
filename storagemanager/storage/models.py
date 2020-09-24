from django.db import models

class Item(models.Model):
    category = models.CharField(max_length=100)
    type = models.CharField(max_length=160)
    model = models.CharField(max_length=160)
    serial_number = models.CharField(max_length=20)

    def __str__(self):
        return f'({self.category}) {self.type}, {self.model}, [SN: {self.serial_number}]'

    def say_hello(self):
        return f'My type is {self.type} my model is {self.model}.'

