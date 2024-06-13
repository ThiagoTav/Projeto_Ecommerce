from django import forms  # Importa o módulo de formulários do Django
from .models import Product  # Importa o modelo Product do diretório atual

class ProductForm(forms.ModelForm):
    """
    Formulário para criação e edição de produtos.

    Campos:
    - name: Nome do produto (CharField)
    - quantity: Quantidade disponível do produto (IntegerField)
    - price: Preço do produto (DecimalField)

    Meta:
    - model: Define o modelo vinculado ao formulário (Product)
    - fields: Define os campos do modelo a serem incluídos no formulário ('name', 'quantity', 'price')
    """

    class Meta:
        model = Product  # Define o modelo vinculado ao formulário
        fields = ['name', 'quantity', 'price']  # Define os campos do modelo a serem incluídos no formulário