from django.shortcuts import render, redirect, get_object_or_404
from . models import Livros
from django.contrib.auth.decorators import login_required


@login_required(redirect_field_name='login')
def index(request):
    livros = Livros.objects.all().order_by('-id')
    return render(request, 'pages/index.html', {'livros': livros})


@login_required(redirect_field_name='login')
def search(request):
    q = request.GET.get('search')
    livros = Livros.objects.filter(nome__icontains=q)
    return render(request, 'pages/index.html', {'livros': livros})


@login_required(redirect_field_name='login')
def detalhes(request, id):
    # contato = Contatos.objects.get(id=id)
    livro = get_object_or_404(Livros, id=id)
    return render(request, 'pages/detalhes.html', {'livro': livro})


@login_required(redirect_field_name='login')
def deletar(request, id):
    livro = Livros.objects.get(id=id)
    livro.delete()
    return redirect('home')


@login_required(redirect_field_name='login')
def adicionar(request):

    if request.method == 'POST':
        nome = request.POST.get('nome')
        autor = request.POST.get('autor')
        editora = request.POST.get('editora')
        ano = request.POST.get('ano')
        descricao = request.POST.get('descricao')
        imagem = request.FILES.get('imagem')
        novo_livro = Livros(nome=nome, autor=autor, editora=editora,
                            ano=ano, descricao=descricao, imagem=imagem, ativo=True)
        novo_livro.save()
        return redirect('home')
    else:
        return render(request, 'pages/adicionar.html')


@login_required(redirect_field_name='login')
def editar(request, id):
    livro = Livros.objects.get(id=id)
    if request.method == 'POST':
        nome = request.POST.get('nome')
        autor = request.POST.get('autor')
        editora = request.POST.get('editora')
        ano = request.POST.get('ano')
        descricao = request.POST.get('descricao')
        check = request.POST.get('check')
        if check == None:
            check = False
        else:
            check = True
        imagem = request.FILES.get('imagem')
        livro.nome = nome
        livro.autor = autor
        livro.editora = editora
        livro.ano = ano
        livro.descricao = descricao
        if imagem != None:
            livro.imagem = imagem
        livro.ativo = check
        livro.save()
        return redirect('home')
    else:
        return render(request, 'pages/editar.html', {'livro': livro})
