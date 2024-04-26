from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Certificado
from django.http import Http404

class IndexView(TemplateView):
    template_name = 'index.html'
    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['Certificados'] = Certificado.objects.all()
        return context

class CertificadoView(TemplateView):
    template_name = 'certificado.html'

    def get_context_data(self, **kwargs):
        context = super(CertificadoView, self).get_context_data(**kwargs)
        slug = self.kwargs.get('slug')
        try:
            certificado = Certificado.objects.get(slug=slug)
        except Certificado.DoesNotExist:
            raise Http404("Certificado não encontrado")
        context['certificado'] = certificado
        return context
