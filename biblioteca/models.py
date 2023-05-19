from django.db import models


class Livros(models.Model):
    nome = models.CharField(max_length=255)
    autor = models.CharField(max_length=255)
    editora = models.CharField(max_length=255)
    ano = models.IntegerField()
    descricao = models.TextField()
    ativo = models.BooleanField()
    imagem = models.ImageField()

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = 'Livros'
