# Create your models here.

from django.db import models

class Cidade(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da cidade")
    uf = models.CharField(max_length=2, verbose_name="UF")
    def __str__(self):
        return f"{self.nome}, {self.uf}"
    class Meta:
        verbose_name = "Cidade"
        verbose_name_plural = "Cidades"

class Ocupacao(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Ocupação")
    def __str__(self):
        return f"{self.nome}"
    class Meta:
        verbose_name = "Ocupação"
        verbose_name_plural = "Ocupações"

class Pessoa(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da pessoa")
    cpf = models.CharField(max_length=100, verbose_name="Cpf")
    data_nasc = models.DateField(max_length=100, verbose_name="Data de Nascimento")
    email = models.CharField(max_length=100, verbose_name="email")
    cidade = models.CharField(max_length=100, verbose_name="Cidade da pessoa")
    ocupacao = models.ForeignKey(Ocupacao, on_delete=models.CASCADE, verbose_name="Ocupação da pessoa")
    def __str__(self):
        return f"{self.nome}, {self.cpf}, {self.data_nasc}, {self.email}, {self.cidade}"
    class Meta:
        verbose_name = "Pessoa"
        verbose_name_plural = "Pessoas"


class Instituicao(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da Instituição")
    site = models.CharField(max_length=100, verbose_name="Site da Instituição")
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE, verbose_name="Cidade da Instituição")
    def __str__(self):
        return f"{self.nome}, {self.site}, {self.cidade}"
    class Meta:
        verbose_name = "Instituição"
        verbose_name_plural = "Instituições"

class Area(models.Model):
    area = models.CharField(max_length=100, verbose_name="Área do saber")
    def __str__(self):
        return f"{self.area}"
    class Meta:
        verbose_name = "Área"
        verbose_name_plural = "Áreas"


class Curso(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome do curso")
    carga_horaria = models.CharField(max_length=100, verbose_name="Carga horária total do curso")
    duracao_meses = models.CharField(max_length=100, verbose_name="Duração de meses do curso")
    area_saber = models.ForeignKey(Area, on_delete=models.CASCADE, verbose_name="área do saber")
    instituicao = models.ForeignKey(Instituicao, on_delete=models.CASCADE, verbose_name="Instituição")
    def __str__(self):
        return f"{self.nome}, {self.carga_horaria}, {self.duracao_meses}, {self.area_saber}, {self.instituicao}"
    class Meta:
        verbose_name = "Curso"
        verbose_name_plural = "Cursos"
    
class Periodo(models.Model):
    periodo = models.CharField(max_length=100, verbose_name="Período do curso")
    def __str__(self):
        return f"{self.periodo}"
    class Meta:
        verbose_name = "Período"
        verbose_name_plural = "Períodos"

class Disciplina(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da disciplina")
    area_saber = models.ForeignKey(Area, on_delete=models.CASCADE, verbose_name="área do saber")
    def __str__(self):
        return f"{self.nome}, {self.area_saber}"
    class Meta:
        verbose_name = "Disciplina"
        verbose_name_plural = "Disciplinas"

class Matricula(models.Model):
    instituicao = models.ForeignKey(Instituicao, on_delete=models.CASCADE, verbose_name="Nome da instituição")
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, verbose_name="Nome do curso")
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE, verbose_name="Nome do aluno")
    data_inicio = models.DateField(max_length = 100, verbose_name="Data de início")
    data_previsao_termino = models.DateField(max_length = 100, verbose_name="Data de término")
    def __str__(self):
        return f"{self.instituicao}, {self.curso}, {self.pessoa}, {self.data_inicio}, {self.data_previsao_termino}"
    class Meta:
        verbose_name = "Matrícula"
        verbose_name_plural = "Matrículas"

class Avaliacao(models.Model):
    descricao = models.CharField(max_length=100, verbose_name="Descrição da Avaliação")
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, verbose_name="Nome do curso")
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE, verbose_name="Nome da disciplina")
    def __str__(self):
        return f"{self.descricao}, {self.curso}, {self.disciplina},"
    class Meta:
        verbose_name = "Avaliação"
        verbose_name_plural = "Avaliações"

class Frequencia(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, verbose_name="Nome do curso")
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE, verbose_name="Nome da disciplina")
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE, verbose_name="Nome do aluno")
    numero_de_faltas = models.CharField(max_length=100, verbose_name="Número de faltas")
    def __str__(self):
        return f"{self.curso}, {self.disciplina},{self.pessoa}, {self.numero_de_faltas}"
    class Meta:
        verbose_name = "Frequência"
        verbose_name_plural = "Frequências"

class Turma(models.Model):
    nome= models.CharField(max_length=100, verbose_name="Nome da turma")
    periodo = models.CharField(max_length=100, verbose_name="Período das aulas")
    def __str__(self):
        return f"{self.nome},{self.periodo}"
    class Meta:
        verbose_name = "Turma"
        verbose_name_plural = "Turmas"

class Ocorrencia(models.Model):
    descricao = models.CharField(max_length=100, verbose_name="Descrição da ocorrência")
    data = models.DateField(max_length = 100, verbose_name="Data da ocorrência")
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, verbose_name="Nome do curso")
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE, verbose_name="Nome da disciplina")
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE, verbose_name="Nome do aluno")
    def __str__(self):
        return f"{self.descricao},{self.data}, {self.curso}, {self.disciplina}, {self.pessoa}"
    class Meta:
        verbose_name = "Ocorrência"
        verbose_name_plural = "Ocorrências"

class Disciplina_por_curso(models.Model):
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE, verbose_name="Nome da disciplina")
    carga_horaria = models.CharField(max_length=100, verbose_name="Carga horária")
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, verbose_name="Nome do curso")
    periodo = models.ForeignKey(Periodo, on_delete=models.CASCADE, verbose_name="Período")
    def __str__(self):
        return f"{self.disciplina},{self.carga_horaria}, {self.curso}, {self.periodo}"
    class Meta:
        verbose_name = "Disciplina por curso"
        verbose_name_plural ="Disciplina por cursos"



class Tipo_avaliacao(models.Model):
    tipo= models.CharField(max_length=100, verbose_name="Tipo de avaliação")
    def __str__(self):
        return f"{self.tipo}"
    class Meta:
        verbose_name = "Tipo de avaliação"
        verbose_name_plural = "Tipos de avaliações"






