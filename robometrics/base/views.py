from django.shortcuts import render, redirect
from django.urls import reverse
from base.models import Corrida
from datetime import datetime
import json
from django.db.models import Count
from django.db.models.functions import TruncMonth

def home(request):
    current_year = datetime.now().year
    month_names = {
        'January': 'Janeiro',
        'February': 'Fevereiro',
        'March': 'Março',
        'April': 'Abril',
        'May': 'Maio',
        'June': 'Junho',
        'July': 'Julho',
        'August': 'Agosto',
        'September': 'Setembro',
        'October': 'Outubro',
        'November': 'Novembro',
        'December': 'Dezembro'
    }
    
    # Consultando o número de corridas criadas por mês no ano atual
    corrida_data = (Corrida.objects
                    .filter(created_at__year=current_year)
                    .annotate(month=TruncMonth('created_at'))
                    .values('month')
                    .annotate(count=Count('id'))
                    .order_by('month'))
    labels = [month_names[data['month'].strftime('%B')] for data in corrida_data]
    data = [data['count'] for data in corrida_data]
   
    context = {
        'labels': json.dumps(labels),
        'data': json.dumps(data),
    }
    return render(request, 'home.html', context)

