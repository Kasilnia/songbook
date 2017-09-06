from django.http import HttpResponse
from django.shortcuts import render
from django.template import RequestContext
from django.template.loader import get_template
from django.views.generic import FormView

from weasyprint import HTML

from main.forms import SongBookForm, SongBookFormSet


from django.forms import formset_factory


class SongBookView(FormView):
    """Show songbook form."""

    template_name = 'main/songbook_form.html'
    form_class = SongBookFormSet
    success_url = '/'

    def form_valid(self, form):
        html_template = get_template('main/pdf.html')
        context = {}
        context['title'] = form.data['title'] \
            if 'title' in form.data else None
        context['songs'] = [
            single_form.cleaned_data['song'] for single_form in form
            if 'song' in single_form.cleaned_data]
        rendered_html = html_template.render(
            RequestContext(self.request, context)).encode(encoding="UTF-8")
        pdf_file = HTML(string=rendered_html).write_pdf()
        http_response = HttpResponse(pdf_file, content_type='application/pdf')
        filename = 'songbook.pdf'
        http_response['Content-Disposition'] = 'inline; filename="{}"'.format(
            filename)
        return http_response
