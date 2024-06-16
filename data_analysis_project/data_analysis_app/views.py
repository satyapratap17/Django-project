from django.shortcuts import render

# Create your views here.
import pandas as pd
from django.shortcuts import render, redirect
from django.conf import settings
from .forms import UploadFileForm
from .models import UploadedFile
import os
import matplotlib.pyplot as plt

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file_instance = form.save()
            return redirect('data_analysis', file_id=file_instance.id)
    else:
        form = UploadFileForm()
    return render(request, 'data_analysis_app/upload.html', {'form': form})

def data_analysis(request, file_id):
    file_instance = UploadedFile.objects.get(id=file_id)
    file_path = os.path.join(settings.MEDIA_ROOT, file_instance.file.name)
    
    df = pd.read_csv(file_path)

    # Perform data analysis
    head = df.head().to_html()
    describe = df.describe().to_html()
    missing_values = df.isnull().sum().to_frame().to_html()

    # Create visualizations
    histograms = []
    for column in df.select_dtypes(include=['float64', 'int64']).columns:
        plt.figure()
        df[column].plot(kind='hist')
        plot_path = os.path.join(settings.MEDIA_ROOT, f'{column}_hist.png')
        plt.savefig(plot_path)
        histograms.append(f'{settings.MEDIA_URL}{column}_hist.png')
        plt.close()

    context = {
        'head': head,
        'describe': describe,
        'missing_values': missing_values,
        'histograms': histograms,
    }

    return render(request, 'data_analysis_app/analysis.html', context)
