import math
import wn
from django.http import HttpResponse
from django.views import generic
from django.utils import timezone
from django.shortcuts import render, redirect
from .models import Interface, File
from django.core.files.storage import FileSystemStorage
import os
from django.template import loader
from interface.textdata import TextManipulation
from interface.similarity import Similarity


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


def get_content(request):
    print(result_analyse)
    return HttpResponse('')


# Printa o dir atual
# directory = os.getcwd()
# print("DIRETORIO:", directory)

# configure: adicionando o banco local
wn.config.data_directory = 'wn_data'


def func2():
    synset1 = wn.synsets("cavalo")
    print("teste wn:", synset1[1])
    print("funcoes sao chamadas como codigo em python mesmo")
    print(math.pow(3, 6))
    return 3


# CONSEGUI ENVIAR OS ARQUIVOS TXT
result_analyse = []


# This a Analyse object
class Analyse:
    name_file1 = None
    name_file2 = None
    similar_sets_log1 = None
    similar_sets_log2 = None
    percent_plagiarism = None


def upload(request):
    data = {}

    # Aí se ele receber uma requisicao tipo POST faz o metodo
    # caso contrario apenas uma GET nao executa
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        uploaded_file2 = request.FILES['document2']
        doc1_name = uploaded_file.name
        doc2_name = uploaded_file2.name
        doc1 = ""
        doc2 = ""
        # No momento lendo o conteudo dos arquivo online (Dps ver se vou salva-los e ler dos arquivos salvos)
        for i in uploaded_file:
            doc1 += i.decode("utf-8") + " "

        for j in uploaded_file2:
            doc2 += j.decode("utf-8") + " "

        doc1 = doc1[:-1]
        doc2 = doc2[:-1]

        result_analyse.append(analyse_docs(doc1_name, doc2_name, doc1, doc2))

        data['result_analyse'] = result_analyse

        return render(request, 'interface\\resultlog.html', data)

    # fs = FileSystemStorage()
    # fs.save(uploaded_file.name, uploaded_file)
    # pelo render da para passar o context, (clica p exibir a funcao ai que vai aparecer)
    # terceiro argumento, vou testar isso ainda, para eu renderizar e mandar p la se pa

    return render(request, 'interface\\upload.html')


# REPLICANDO AS FUNÇÕES DE MANEIRA FEIA E NAO MODULARIZADA:


def analyse_docs(file_name1, file_name2, doc1, doc2):
    text_manipulation = TextManipulation()
    similarity = Similarity()

    # # FEM REPLICA ESSE ALGORITMO DE LA AQUI
    doc1_segmented = text_manipulation.segmentation_based_sentences(doc1)
    doc2_segmented = text_manipulation.segmentation_based_sentences(doc2)

    # #  SIMILARITY 1: (doc1 em relação ao doc2) SÓ REPLICAR O METODO AQUI:
    qntd_similar_sets1, similar_sets_log1 = similarity.calculate_similar_sets_in_docs(doc1_segmented, doc2_segmented)
    degree_resemblance1 = similarity.degree_resemblance(qntd_similar_sets1, len(doc1_segmented))

    #  SIMILARITY 2: (doc2 em relação ao doc1)
    qntd_similar_sets2, similar_sets_log2 = similarity.calculate_similar_sets_in_docs(doc2_segmented, doc1_segmented)
    degree_resemblance2 = similarity.degree_resemblance(qntd_similar_sets2, len(doc2_segmented))

    percent_plagiarism = similarity.odds_ratio_in_percent(degree_resemblance1, degree_resemblance2)

    analyse = Analyse()
    analyse.name_file1 = file_name1
    analyse.name_file2 = file_name2
    analyse.similar_sets_log1 = similar_sets_log1
    analyse.similar_sets_log2 = similar_sets_log2
    analyse.percent_plagiarism = percent_plagiarism

    return analyse
    # retornando so o nome dos arquvios e a porcentagem
    # return (file_name1, file_name2, percent_plagiarism)
