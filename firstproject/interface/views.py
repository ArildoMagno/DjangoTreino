import math
import wn
from django.http import HttpResponse
from django.views import generic
from django.utils import timezone
from django.shortcuts import render
from .models import Interface, File
from django.core.files.storage import FileSystemStorage

import os


class IndexView(generic.ListView):
    model = Interface
    template_name = 'interface/index.html'


class FileView(generic.ListView):
    model = File
    template_name = 'interface/file.html'


class TesteView(generic.ListView):
    template_name = 'interface/index.html'
    context_object_name = 'interface_list'

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Interface.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]


# coloca o request como parametro quando vem via requisição, a propria requisição ja vira um parametro
def print_function(request):
    print(request)
    chama_f2 = func2()
    calc = chama_f2 + 6
    print("assim funciona o print, calc:", calc)
    return HttpResponse(calc)


# Printa o dir atual
directory = os.getcwd()
print("DIRETORIO:", directory)

# configure: adicionando o banco local
wn.config.data_directory = 'wn_data'


# 1- CONSEGUI CHAMAR O BANCO COM O WN ARRUMANDO  O LOCAL JA
# 2- CONSEGUI CRIAR FUNCOES E MANIPULAR ELAS

# WN funcionou, aqui chamou meu banco db
def func2():
    synset1 = wn.synsets("cavalo")
    print("teste wn:", synset1[1])
    print("funcoes sao chamadas como codigo em python mesmo")
    print(math.pow(3, 6))
    return 3


# CONSEGUI ENVIAR OS ARQUIVOS TXT
def upload(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        uploaded_file2 = request.FILES['document2']
        print("File1:", uploaded_file.name)
        print(uploaded_file.size)
        print("File2:", uploaded_file2.name)
        print(uploaded_file2.size)

        for i in uploaded_file:
            print(i)
            test_string = i.decode("utf-8")
            print(test_string)

        for j in uploaded_file2:
            print(j)
            test_string = j.decode("utf-8")
            print(test_string)

        # fs = FileSystemStorage()
        # fs.save(uploaded_file.name, uploaded_file)
    return render(request, 'interface\\upload.html')
