from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from .models import Product
from django.http import JsonResponse
from django.shortcuts import get_object_or_404


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirecione para a página principal ou para onde você quiser
        else:
            return render(request, 'login.html', {'error': 'Usuário ou senha incorretos.'})  # Altere aqui para 'login.html'
    else:
        return render(request, 'login.html')  # Altere aqui para 'login.html'

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def home_view(request):
    return render(request, 'home.html')


def cadastro_usuario_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            print("Formulário de cadastro válido.")  # Adicione esta instrução de depuração
            form.save()
            return redirect(reverse_lazy('login'))  # Redireciona para a página de login após o cadastro bem-sucedido
        else:
            print("Formulário de cadastro inválido:", form.errors)  # Adicione esta instrução de depuração para imprimir quaisquer erros de validação do formulário
    else:
        form = UserCreationForm()
    return render(request, 'formUsuario.html', {'form': form})

def index_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        return redirect('login')

def home(request):
    return render(request, 'home.html')

def add_product(request):
    if request.method == 'POST':
        name = request.POST['name']
        quantity = request.POST['quantity']
        price = request.POST['price']
        Product.objects.create(name=name, quantity=quantity, price=price)
        return redirect('home')  # Redireciona para a página inicial após adicionar o produto
    return render(request, 'add_product.html')

def buy_product(request, product_id):
    # Obtenha o produto do banco de dados
    product = get_object_or_404(Product, pk=product_id)

    # Verifique se há quantidade disponível para compra
    if product.quantity > 0:
        # Decrementa a quantidade disponível
        product.quantity -= 1
        product.save()

        # Retorne uma resposta de sucesso
        return JsonResponse({'message': 'Produto comprado com sucesso!'})

    else:
        # Retorne uma resposta de erro se não houver quantidade disponível
        return JsonResponse({'error': 'Produto esgotado.'}, status=400)