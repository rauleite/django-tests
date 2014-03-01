from django.db import models

class Cliente(models.Model):
    nome = models.TextField()

    def __str__(self):
        return self.nome
