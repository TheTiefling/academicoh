from django.shortcuts import render,redirect, get_object_or_404
from .models import *
from django.views import View

class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')

class CidadeView(View):
    def get(self, request, *args, **kwargs):
        cidade = Cidade.objects.all()
        return render(request, 'cidade.html', {'cidade': cidade})

    # def post(self, request, *args, **kwargs):

class OcupacaoView(View):
    def get(self, request, *args, **kwargs):
        ocupacao = Ocupacao.objects.all()
        return render(request, 'ocupacao.html', {'ocupacao': ocupacao})

class PessoaView(View):
    def get(self, request, *args, **kwargs):
        pessoa = Pessoa.objects.all()
        return render(request, 'pessoa.html', {'pessoa': pessoa})

class InstituicaoView(View):
    def get(self, request, *args, **kwargs):
        instituicao = Instituicao.objects.all()
        return render(request, 'instituicao.html', {'instituicao': instituicao})

class AreaView(View):
    def get(self, request, *args, **kwargs):
        area = Area.objects.all()
        return render(request, 'area.html', {'area': area})

class CursoView(View):
    def get(self, request, *args, **kwargs):
        curso = Curso.objects.all()
        return render(request, 'curso.html', {'curso': curso})

class PeriodoView(View):
    def get(self, request, *args, **kwargs):
        periodo = Periodo.objects.all()
        return render(request, 'periodo.html', {'periodo': periodo})
    
class DisciplinaView(View):
    def get(self, request, *args, **kwargs):
        disciplina = Disciplina.objects.all()
        return render(request, 'disciplina.html', {'disciplina': disciplina})
    
class MatriculaView(View):
    def get(self, request, *args, **kwargs):
        matricula = Matricula.objects.all()
        return render(request, 'matricula.html', {'matricula': matricula})    

class AvaliacaoView(View):
    def get(self, request, *args, **kwargs):
        avaliacao = Avaliacao.objects.all()
        return render(request, 'avaliacao.html', {'avaliacao': avaliacao})
    
class FrequenciaView(View):
    def get(self, request, *args, **kwargs):
        frequencia = Frequencia.objects.all()
        return render(request, 'frequencia.html', {'frequencia': frequencia})

class TurmaView(View):
    def get(self, request, *args, **kwargs):
        turma = Turma.objects.all()
        return render(request, 'turma.html', {'turma': turma})
    
class OcorrenciaView(View):
    def get(self, request, *args, **kwargs):
        ocorrencia = Ocorrencia.objects.all()
        return render(request, 'ocorrencia.html', {'ocorrencia': ocorrencia})

class Disciplina_por_cursoView(View):
    def get(self, request, *args, **kwargs):
        disciplinacurso = Disciplina_por_curso.objects.all()
        return render(request, 'disciplinacurso.html', {'disciplinacurso': disciplinacurso})
    
class TipoavaliacaoView(View):
    def get(self, request, *args, **kwargs):
        tipoavaliacao = Tipo_avaliacao.objects.all()
        return render(request, 'tipoavaliacao.html', {'tipoavaliacao': tipoavaliacao})

