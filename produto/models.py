from django.db import models

# Model para categoria

class Categoria(models.Model):
    nome = models.CharField(max_length=255, primary_key=True)
    
    def __str__(self):
        return self.nome

# Model do produto 

class Produto(models.Model):
    nome = models.CharField(null=False, blank=False, max_length=255)
    descricao = models.TextField(blank=True, null=True)
    preco = models.FloatField(null=False, default = 0.0)
    categoria = models.ForeignKey(Categoria, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.nome