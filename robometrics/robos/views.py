from django.shortcuts import render, redirect
from base.models import Robo, Equipe

def robos(request):
    robos = Robo.objects.all()
    return render(request, 'robos/robos.html', {'robos': robos})

def create_robos(request):
     if request.method == 'POST':
        equipe_name = request.POST.get('equipe')
        tipo = request.POST.get('tipo')

#         # # Perform validation
#         # if not pista_id or not robos_id or not log_corrida:
#         #     return JsonResponse({'error': 'Missing fields'}, status=400)

#         # try:
#         # except Pista.DoesNotExist:
#         #     return JsonResponse({'error': 'Invalid Pista ID'}, status=400)
#         # except Robo.DoesNotExist:
#         #     return JsonResponse({'error': 'Invalid Robo ID'}, status=400)

#         # Create a new Corrida instance and save it to the database
        equipe = Equipe.objects.get(equipe=equipe_name)
        robos = Robo(id_equipe=equipe, tipo=tipo)
        robos.save()

        # Redirect to the 'corridas' view after successful creation
        return redirect('robos/')
    # else:
    #     return redirect('robos')