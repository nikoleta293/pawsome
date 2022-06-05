from datetime import date, datetime
from django.shortcuts import render
from django.views import generic
from django.utils.safestring import mark_safe
from .models import *
from .models import Events
#from django.http import HttpResponse
from .utils import Calendar

def index(request):
    return render(request,'calendar_base.html')

class CalendarView(generic.ListView):
    model = Events
    template_name = 'Calendar/calendar_base.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # use today's date for the calendar
        d = get_date(self.request.GET.get('day', None))

        # Instantiate our calendar class with today's year and date
        cal = Calendar(d.year, d.month)

        # Call the formatmonth method, which returns our calendar as a table
        html_cal = cal.formatmonth(withyear=True)
        context['calendar'] = mark_safe(html_cal)
        return context

def get_date(req_day):
    if req_day:
        year, month = (int(x) for x in req_day.split('-'))
        return date(year, month, day=1)
    return datetime.today()