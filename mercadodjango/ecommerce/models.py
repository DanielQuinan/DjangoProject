import uuid
from django.db import models

class Produtos(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nome = models.CharField(max_length=200)
    descricao = models.CharField(max_length=500)
    preco = models.IntegerField()

class Fotos(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    url = models.CharField(max_length=1000)
    produtos_id = models.ForeignKey(Produtos, on_delete=models.CASCADE)

class Estados(models.Model):
  estado = models.CharField(max_length=2)

class Enderecos(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  endereco = models.CharField(max_length=200)
  numero = models.IntegerField()
  complemento =  models.CharField(max_length=64)
  bairro = models.CharField(max_length=64)
  cidade = models.CharField(max_length=64)
  estado = models.ForeignKey(Estados, on_delete=models.CASCADE)
  cep = models.CharField(max_length=9)

class Usuarios(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  nome = models.CharField(max_length=200)
  enderecos_id = models.ForeignKey(Enderecos, on_delete=models.CASCADE)

class Carrinho(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  usuarios_id = models.ForeignKey(Usuarios, on_delete=models.CASCADE)
  produtos_id = models.ForeignKey(Produtos, on_delete=models.CASCADE)

class Status_Pedidos(models.Model):
  status = models.CharField(max_length=64)

class Pedidos(models.Model):
  id = models.BigIntegerField(primary_key=True, unique=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  status = models.ForeignKey(Status_Pedidos, on_delete=models.CASCADE)
  produtos = models.ManyToManyField(Produtos)
  usuarios_id = models.ForeignKey(Usuarios, on_delete=models.CASCADE)
  enderecos_id = models.ForeignKey(Enderecos, on_delete=models.CASCADE)

class Status_Pagamentos(models.Model):
  status = models.CharField(max_length=64)

class Pagamentos(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  status = models.ForeignKey(Status_Pagamentos, on_delete=models.CASCADE)
  pedidos_id = models.ForeignKey(Pedidos, on_delete=models.CASCADE)
