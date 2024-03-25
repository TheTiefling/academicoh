from django.db import models

class Cidade(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome")
    uf = models.CharField(max_length=2, verbose_name="UF")

    def __str__(self):
        return f'{self.nome}, {self.uf}'
    
    class Meta:
        verbose_name="Cidade"
        verbose_name_plural="Cidades"


class Pessoa(models.Model):
    professor = models.CharField(max_length=100, verbose_name="Nome dos professores")
    estudante = models.CharField(max_length=100, verbose_name="Nome dos estudantes")
    coord = models.CharField(max_length=100, verbose_name="Nome do coord")
    nome = models.CharField(max_length=100, verbose_name="Nome")
    pai = models.CharField(max_length=100, verbose_name="Nome do pai")
    mae = models.CharField(max_length=100, verbose_name="Nome da mae")
    cpf = models.CharField(max_length=100, verbose_name="CPF")
    data_nasc = models.DateField(verbose_name="Data de nascimento")
    email = models.CharField(max_length=100, verbose_name="Email")
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE, verbose_name="Cidade")
    ocupacao = models.CharField(max_length=100, verbose_name="Ocupação")

    def __str__(self):
        return f'{self.professor}, {self.estudante}, {self.coord}, {self.nome}, {self.pai}, {self.mae}, {self.cpf}, {self.data_nasc}, {self.email}, {self.cidade}, {self.ocupacao}'
        
    class Meta:
        verbose_name = "Pessoa"
        verbose_name_plural = "Pessoas"

class Ocupacao(models.Model):
    professor = models.CharField(max_length=100, verbose_name="Nome dos professores")
    estudante = models.CharField(max_length=100, verbose_name="Nome dos estudantes")
    cordenador = models.CharField(max_length=100, verbose_name="Nome do coord")
    diretor = models.CharField(max_length=100, verbose_name="Diretor")
    nome = models.CharField(max_length=100, verbose_name="Nome")

    def __str__(self):
        return f'{self.professor}, {self.estudante}, {self.cordenador}, {self.diretor}, {self.nome}, '
    
    class Meta:
        verbose_name="Ocupação"
        verbose_name_plural="Ocupações"
    
class Escola(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome")
    site = models.CharField(max_length=100, verbose_name="Site")
    telefone = models.CharField(max_length=100, verbose_name="Telefone")
    cidade = models.ForeignKey(max_length=100, verbose_name="Cidade")

    def __str__(self):
        return f'{self.nome}, {self.site}, {self.telefone}, {self.cidade}'
        
    class Meta:
        verbose_name = "Instituição de Ensino"
        verbose_name_plural = "Instituições de Ensino"