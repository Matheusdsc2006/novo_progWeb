from django.shortcuts import render
from loja.models import Produto

def home_view(request):
    # lê a caixa de texto de produtos pesquisados
    produto = request.GET.get("produto")
    #filtra no banco de dados os produtos pesquisados pelo usuário
    produtos = Produto.objects.all()
    if produto is not None:
        produtos = produtos.filter(Produto__contains=produto)
    # inserir resultado no contexto
    context = {
        'produtos': produtos
    }
    # envia o contexto para o template
    return render(request, template_name='home/home.html', context=context, status=200)