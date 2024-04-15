from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('cidade/', CidadeView.as_view(), name='cidade'),
    path('ocupacao/', OcupacaoView.as_view(), name='ocupacao'),
    path('pessoa/', PessoaView.as_view(), name='pessoa'),
    path('instituicao/', InstituicaoView.as_view(), name='instituicao'),
    path('area/', AreaView.as_view(), name='area'),
    path('curso/', CursoView.as_view(), name='curso'),
    path('periodo/', PeriodoView.as_view(), name='periodo'),
    path('disciplina/', DisciplinaView.as_view(), name='disciplina'),
    path('matricula/', MatriculaView.as_view(), name='matricula'),
    path('avaliacao/', AvaliacaoView.as_view(), name='avaliacao'),
    path('frequencia/', FrequenciaView.as_view(), name='frequencia'),
    path('turma/', TurmaView.as_view(), name='turma'),
    path('ocorrencia/', OcorrenciaView.as_view(), name='ocorrencia'),
    path('disciplinacurso/', Disciplina_por_cursoView.as_view(), name='disciplinacurso'),
    path('tipoavaliacao/', TipoavaliacaoView.as_view(), name='tipoavaliacao'),
]