from django.db import models


class Empresa(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    area = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Vaga(models.Model):
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    local = models.CharField(max_length=100)

    def __str__(self):
        return self.titulo


class Inscricao(models.Model):
    vaga = models.ForeignKey(Vaga, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    telefone = models.CharField(max_length=20)
    nascimento = models.DateField()
    descricao = models.TextField()
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nome} - {self.vaga}"
