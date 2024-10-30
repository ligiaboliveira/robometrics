from django.shortcuts import render, redirect
from base.models import Corrida, Pista, Robo
import pandas as pd 
from .forms import UploadFileForm
from django.core.serializers import serialize
from algoritmo_genetico.views import run_genetic_algorithm

def corridas(request):
    corridas = Corrida.objects.all()
    # print(serialize('json', corridas))
    return render(request, 'corridas/corridas.html', {'corridas': corridas})

def create_pid(request):
    if request.method == 'POST':
        print(request.POST)
        p_values = request.POST.getlist('P')
        i_values = request.POST.getlist('I')
        d_values = request.POST.getlist('D')
        print(d_values)
        population = []
        for P,I,D in zip(p_values, i_values, d_values):
            population.append({'P': float(P), 'I': float(I), 'D': float(D), 'time': '0:00'})  # You can modify 'time' as needed
            # Optionally, you can save other fields like tempo here if needed
            # corrida.tempo = ...
            # corrida.save()
            
        return run_genetic_algorithm(request, population)
        return redirect('corridas')
    else:
        return redirect('corridas')
    

def handle_uploaded_file(file):
    # Read the Excel file
    df = pd.read_excel(file)

    # Ensure the correct columns are present
    expected_columns = ['ID', 'P', 'I', 'D', 'tempo']
    if not all(column in df.columns for column in expected_columns):
        raise ValueError(f"The file must contain the following columns: {', '.join(expected_columns)}")
    
    print(df['ID'])
    # Convert the columns to appropriate data types
    df['ID'] = df['ID'].astype(int)
    df['P'] = df['P'].astype(float)
    df['I'] = df['I'].astype(float)
    df['D'] = df['D'].astype(float)
    
    # Convert the 'tempo' column from a string with commas to a float
    df['tempo'] = df['tempo'].apply(lambda x: float(str(x).replace(',', '')))

    corridas = []
    for _, row in df.iterrows():
        corrida = Corrida(
            P=row['P'],
            I=row['I'],
            D=row['D'],
            tempo=row['tempo']
        )
        corridas.append(corrida)
    print(corridas)
    # Bulk create Corrida instances to improve efficiency
    Corrida.objects.bulk_create(corridas)
    return df

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            df = handle_uploaded_file(request.FILES['file'])
            corridas = Corrida.objects.all()
            return render(request, 'corridas/corridas.html', {'corridas': corridas})
    else:
        form = UploadFileForm()
    return render(request, 'home.html')
