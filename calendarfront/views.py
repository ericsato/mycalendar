from django.shortcuts import render_to_response
from mycal.models import Date, Type, Relationship
from collections import OrderedDict
import datetime

# Create your views here.
def home_screen(request):

    query = {
        'month': "strftime('%m', date)",
        'day': "strftime('%d', date)"
    }

    dates_by_month = OrderedDict()
    dates = Date.objects.all().extra(select=query).order_by('month', 'day')

    for event in dates:

        readable_month = event.date.strftime('%B')

        if dates_by_month.get(readable_month, None) is None:
            dates_by_month[readable_month] = list()

        dates_by_month[readable_month].append(event)

    todays_date = datetime.datetime.now()
    this_month = todays_date.strftime('%B')
    todays_day = todays_date.strftime('%d')



    return render_to_response('landing/landing.html', {
        'types': Type.objects.all(),
        'dates': dates,
        'relationships': Relationship.objects.all(),
        'dates_by_month': dates_by_month,
        'todays_date': todays_date,
        'this_month': this_month,
        'todays_day': todays_day
    })
