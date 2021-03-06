from django.db import models


class Item(models.Model):
    EXTRA = 'Extra'
    LIGHT = 'Light'
    POWER = 'Power'
    SOUND = 'Sound'
    STAGE = 'Stage'
    
    CATEGORIES = (
        (EXTRA, 'Extra'),
        (LIGHT, 'Light'),
        (POWER, 'Power'),
        (SOUND, 'Sound'),
        (STAGE, 'Stage'),
    )
    category = models.CharField(
        max_length=10,
        choices=CATEGORIES,
        default=EXTRA,
    )
    type = models.CharField(max_length=160)
    model = models.CharField(max_length=160)
    serial_number = models.CharField(max_length=20)

    def __str__(self):
        return f'({self.category}) {self.type}, {self.model}, [SN: {self.serial_number}]'
