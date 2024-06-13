from django.shortcuts import render, redirect  # Funções para renderizar templates e redirecionar URLs
from django.contrib.auth import authenticate, login, logout  # Funções para autenticação de usuário
from django.contrib.auth.decorators import login_required  # Decorador para exigir autenticação
from django.contrib.auth.forms import UserCreationForm  # Formulário pré-definido para criação de usuário
from django.urls import reverse_lazy  # Função para resolução reversa de URLs
from project.forms import ProductForm  # Formulário personalizado para produtos
from .models import Product  # Importa o modelo Product do diretório atual
from django.http import JsonResponse  # Respostas HTTP em formato JSON
from django.shortcuts import get_object_or_404  # Função para obter um objeto do banco de dados ou 404 (não encontrado)


def login_view(request):
    """
    View para autenticar usuários no sistema.

    Recebe requisições POST com dados de login e autentica o usuário se válido.
    Redireciona para a página principal ('home') se autenticado ou exibe mensagem de erro.

    Template utilizado: 'login.html'.
    """
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Redireciona para a página principal após login
        else:
            return render(request, 'login.html', {'error': 'Usuário ou senha incorretos.'})
    else:
        return render(request, 'login.html')


@login_required
def logout_view(request):
    """
    View para deslogar usuários do sistema.

    Requer autenticação prévia (decorador @login_required).
    Redireciona para a página de login ('login') após o logout.
    """
    logout(request)
    return redirect('login')


@login_required
def home_view(request):
    """
    View da página inicial do sistema.

    Requer autenticação prévia (decorador @login_required).
    Renderiza o template 'home.html'.
    """
    return render(request, 'home.html')


def cadastro_usuario_view(request):
    """
    View para cadastrar novos usuários.

    Recebe requisições POST com dados do formulário de criação de usuário.
    Salva o usuário se o formulário for válido e redireciona para a página de login ('login').
    Renderiza o template 'formUsuario.html' para entrada de dados.

    Template utilizado: 'formUsuario.html'.
    """
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            print("Formulário de cadastro válido.")
            form.save()
            return redirect(reverse_lazy('login'))  # Redireciona para o login após cadastro
        else:
            print("Formulário de cadastro inválido:", form.errors)
    else:
        form = UserCreationForm()
    return render(request, 'formUsuario.html', {'form': form})


def index_view(request):
    """
    View para a página inicial ('index').

    Redireciona para 'home' se o usuário estiver autenticado, senão redireciona para 'login'.
    """
    if request.user.is_authenticated:
        return redirect('home')
    else:
        return redirect('login')


@login_required
def add_product(request):
    """
    View para adicionar um novo produto.

    Recebe requisições POST com dados do produto e salva no banco de dados.
    Redireciona para 'home' após adicionar o produto.
    Renderiza o template 'add_product.html' para entrada de dados.

    Template utilizado: 'add_product.html'.
    """
    if request.method == 'POST':
        name = request.POST['name']
        quantity = request.POST['quantity']
        price = request.POST['price']
        Product.objects.create(name=name, quantity=quantity, price=price)
        return redirect('home')
    return render(request, 'add_product.html')


def buy_product(request, product_id):
    """
    View para comprar um produto.

    Recebe o ID do produto como parâmetro na URL.
    Verifica se há estoque disponível para o produto e decrementa a quantidade se possível.
    Retorna uma resposta JSON com mensagem de sucesso ou erro.

    Respostas:
    - {'message': 'Produto comprado com sucesso!'}: Se a compra foi bem-sucedida.
    - {'error': 'Produto esgotado.'}: Se não há estoque disponível para o produto.

    Requer autenticação para acessar esta função.
    """
    product = get_object_or_404(Product, pk=product_id)
    if product.quantity > 0:
        product.quantity -= 1
        product.save()
        return JsonResponse({'message': 'Produto comprado com sucesso!'})
    else:
        return JsonResponse({'error': 'Produto esgotado.'}, status=400)


@login_required
def edit_product(request, pk):
    """
    View para editar um produto existente.

    Recebe requisições POST com dados atualizados do produto.
    Salva as alterações se o formulário for válido e redireciona para 'product-list'.
    Renderiza o template 'edit_product.html' para edição de dados.

    Requer autenticação prévia (decorador @login_required).

    Template utilizado: 'edit_product.html'.
    """
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product-list')
    else:
        form = ProductForm(instance=product)
    return render(request, 'edit_product.html', {'form': form})


@login_required
def delete_product(request, pk):
    """
    View para deletar um produto existente.

    Recebe requisições POST para confirmar a exclusão do produto.
    Deleta o produto do banco de dados e redireciona para 'product-list'.
    Renderiza o template 'confirm_delete.html' para confirmação de exclusão.

    Requer autenticação prévia (decorador @login_required).

    Template utilizado: 'confirm_delete.html'.
    """
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('product-list')
    return render(request, 'confirm_delete.html', {'product': product})


@login_required
def product_list_view(request):
    """
    View para listar todos os produtos cadastrados.

    Obtém todos os produtos do banco de dados e renderiza o template 'card.html' para exibição.
    Passa a lista de produtos como contexto para o template.

    Requer autenticação prévia (decorador @login_required).

    Template utilizado: 'card.html'.
    """
    products = Product.objects.all()
    return render(request, 'card.html', {'products': products})