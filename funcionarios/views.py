from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, UpdateView, DeleteView, CreateView
from .models import Funcionario
#bibliotecas para o reportlab
import io
from reportlab.pdfgen import canvas
#bibliotecas para o xhtml2pdf
from django.template.loader import get_template
import xhtml2pdf.pisa as pisa

# Create your views here.
#def home(request):
#    return HttpResponse('Olá!')

class FuncionarioList(ListView):
    model = Funcionario
    #paginate_by = 10

    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        return Funcionario.objects.filter(empresa=empresa_logada)

class FuncionarioEdit(UpdateView):
    model = Funcionario
    fields = ['nome','departamentos']

class FuncionarioDelete(DeleteView):
    model = Funcionario
    success_url = reverse_lazy('list_funcionarios')

class FuncionarioNovo(CreateView):
    model = Funcionario
    fields = ['nome','departamentos']

    def form_valid(self, form):
        funcionario = form.save(commit=False)
        username = funcionario.nome.split(' ')[0] + funcionario.nome.split(' ')[-1]
        funcionario.empresa = self.request.user.funcionario.empresa
        funcionario.user = User.objects.create(username=username)
        funcionario.save()
        return super(FuncionarioNovo, self).form_valid(form)

def pdf_reportlab(request):
    #fonte da estrutura: https://docs.djangoproject.com/en/4.0/howto/outputting-pdf/
    response = HttpResponse(content_type="application/pdf")
    response['Content-Disposition'] = 'attachment; filename="meupdf.pdf"'
    # Create a file-like buffer to receive PDF data.
    buffer = io.BytesIO()

    # Create the PDF object, using the buffer as its "file."
    p = canvas.Canvas(buffer)

    p.drawString(10, 810, "Hello world.")
    palavras = ['Mauricio','Monteiro','Almeron']
    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    y = 790
    for palavra in palavras:
        p.drawString(10, y, palavra)
        y -= 40

    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()

    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)
    # FileResponse sets the Content-Disposition header so that browsers
    # present the option to save the file.
    #buffer.seek(0)
    return response #FileResponse(buffer, as_attachment=True, filename='hello.pdf')

class Render:
    @staticmethod
    def render(path: str, params: dict, filename: str):
        template = get_template(path)
        html = template.render(params)
        response = io.BytesIO()
        pdf = pisa.pisaDocument(
            io.BytesIO(html.encode("UTF-8")),response)
        if not pdf.err:
            response = HttpResponse(
                response.getvalue(), content_type='application/pdf')
            response['Content-Disposition'] = 'attachment;filename=%s.pdf' % filename
            return response
        else:
            return HttpResponse("Error Rendering PDF", status=400)

class Pdf(View):
    def get(self,request):
        params = {
            'today' : 'Variável today',
            'sales' : 'Variável sales',
            'request': request,
        }
        # é um método estático, por isso não precisou instanciar
        return Render.render('funcionarios/relatorio.html',params,'meuArquivo')