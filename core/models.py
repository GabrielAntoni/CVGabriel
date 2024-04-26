from django.db import models
from stdimage import StdImageField

from django.db.models import signals
from django.template.defaultfilters import slugify


# Create your models here.

class Base(models.Model):
    criado = models.DateField('Data de Criação', auto_now_add=True)
    modificado = models.DateField('Data de Atualização', auto_now=True)
    ativo = models.BooleanField('Ativo?', default=True)

    class Meta:
        abstract = True


class Certificado(Base):
    nomeCert = models.CharField('Nome do Certificado', max_length=100)
    dataCert = models.DateField('Data de Conclusão')
    LinkCert = models.CharField('Link do Certificado', max_length=100)
    duracaoCert = models.DurationField('Duração do Curso')
    imagem = StdImageField('Imagem', upload_to='certificados', variations={'thumb': (124, 124)})
    slug = models.SlugField('Slug', max_length=100, blank=True, editable=False)

    def __str__(self):
        return self.nomeCert

    def duracao_em_horas(self):
        # Isso assume que a duração está armazenada como um timedelta
        # total_seconds() retorna o total de segundos da duração
        total_seconds = self.duracaoCert.total_seconds()
        # Converter segundos em horas
        horas = total_seconds / 3600
        return horas

    class Meta:
        verbose_name = 'Certificado'
        verbose_name_plural = 'Certificados'


def certificado_pre_save(signal, instance, sender, **kwargs):
    instance.slug = slugify(instance.nomeCert)


signals.pre_save.connect(certificado_pre_save, sender=Certificado)
