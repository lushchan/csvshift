from django.http import HttpResponse
from django.template import loader
import pandas as pd

def shifts(request):
    df1 = pd.read_csv('/home/lmr/Python/django/hsshifts/csv/shift.csv', index_col=False)
    df1.to_html("/home/lmr/Python/django/hsshifts/shifts/templates/shift.html", index=False)
    template = loader.get_template('shift.html')
    return HttpResponse(template.render())