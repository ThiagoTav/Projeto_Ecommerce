from datetime import timezone  # Importa o objeto timezone do módulo datetime
from django.db import models  # Importa o módulo de modelos do Django
from django.contrib.auth.models import User  # Importa o modelo de usuário padrão do Django

class Product(models.Model):
    """
    Modelo para representar um produto no sistema.

    Campos:
    - name: Nome do produto (CharField)
    - quantity: Quantidade disponível do produto (IntegerField)
    - price: Preço do produto (DecimalField)

    Métodos:
    - __str__(): Retorna o nome do produto como representação em string.
    """

    name = models.CharField(max_length=100)  # Nome do produto
    quantity = models.IntegerField()  # Quantidade disponível do produto
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Preço do produto

    def __str__(self):
        """
        Retorna o nome do produto como representação em string.

        Exemplo:
        Se o nome do produto for 'Camiseta', retorna 'Camiseta'.
        """
        return self.name