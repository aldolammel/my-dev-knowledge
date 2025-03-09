from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from core import language as lng

from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa  # MODULE TO EXPORT TO PDF!
from datetime import date

from .models import EventAttack


def is_valid_queryparam(param):
    return param != '' and param is not None


def attack_list_pdf(request):
    # Initial values:
    user = request.user
    # Template and QuerySet:
    template_path = 'sub-app-name/attack_list_pdf.html'
    attack_list = EventAttack.objects.filter(created_by=user)
    attack_list = attack_list.order_by('-start_datetime')

    if 'start_datetime' in request.session:
        start_datetime = request.session['start_datetime']
    else:
        start_datetime = None

    if 'duration' in request.session:
        duration = request.session['duration']
    else:
        duration = None

    if is_valid_queryparam(start_datetime):
        attack_list = attack_list.filter(start_datetime__icontains=start_datetime)

    if is_valid_queryparam(duration):
        attack_list = attack_list.filter(duration__icontains=duration)
    context = {
        'page_title': lng.LB_REPORT_ATTK_TTL,
        'user_type': lng.LB_USER_TYPE_PATIENT,
        'user': user,
        'today': date.today(),
        'report_title': lng.LB_REPORT_ATTK_TTL,
        'report_length': 'Últimos 90 dias',
        'attack_list': attack_list,
        'table_headers': [
            lng.LB_ATTK_WHEN_FORM,
            lng.LB_ATTK_INTENS,
            lng.LB_ATTK_DURATION,
            lng.LB_ATTK_AREA,
            lng.LB_ATTK_MEDICINE,
            lng.LB_ATTK_PLACE,
            lng.LB_ATTK_WAS_SLEEP,
        ],
        'attributes': [
            'start_datetime',
            'intensity',
            'duration',
            'affected_areas',
            'medicines',
            'place',
            'was_during_sleep',
        ],
        'yes': lng.TX_YES,
        # 'no': lng.TX_NO,
        'ends': lng.LB_REPORT_ENDED,
    }
    response = HttpResponse(content_type='application/pdf')
    if start_datetime is None:
        response['Content-Disposition'] = "filename='Attack list.pdf'"
    elif start_datetime:
        response['Content-Disposition'] = 'filename='+ str(start_datetime.capitalize()) + ' ' + str('Attack list.pdf')
    elif duration:
        response['Content-Disposition'] = 'filename='+ str(duration) + ' ' + str('Attack list.pdf')
    # Find the template and render it.
    template = get_template(template_path)
    html = template.render(context)
    # Create a PDF
    pisa_status = pisa.CreatePDF(html, dest=response)
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response


@method_decorator(login_required, name="dispatch")
class AttackListView(ListView):
    """Responsible for showing the private list of user attacks on the front-end."""

    model = EventAttack
    template_name = 'sub-app-name/attack_list.html'
    context_object_name = 'attacks'

    def get_queryset(self):
        # Filters the attacks to show only the ones associated with the currently logged-in user:
        return EventAttack.objects.filter(created_by=self.request.user)

    def get_context_data(self, **kwargs):
        # Get the base context from the parent class:
        context = super().get_context_data(**kwargs)
        # Add custom context data:
        context["page_title"] = lng.S_I_ATTK_TTL
        return context