from django.contrib.auth import get_user_model
from django.db import models

UserModel = get_user_model()


class Pet(models.Model):
    def __str__(self):
        return f'{self.name}, {self.age}, {self.type}'

    DOG = 'dog'
    CAT = 'cat'
    PARROT = 'parrot'
    PET_TYPE = (
        (DOG, "Dog"),
        (CAT, 'Cat'),
        (PARROT, 'Parrot')
    )

    type = models.CharField(max_length=6, choices=PET_TYPE)
    name = models.CharField(max_length=6)
    age = models.PositiveIntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to='images/pets')
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)


class Like(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)


from .signals import *
