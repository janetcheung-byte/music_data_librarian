from django.shortcuts import render

from django.http import HttpResponse

from django.core.files.storage import FileSystemStorage
from .tasks.ingest_data import ingest_csv

from .tasks.generate_reports import export_to_csv
from django.http import FileResponse


import os
import pandas as pd
from .models import MusicMetadata


def index(request):
    return HttpResponse("Welcome to the main page")



def ingest_data_view(request):
    if request.method == "POST" and request.FILES['csv_file']:
        csv_file = request.FILES['csv_file']

        # Save the file temporarily on the server
        fs = FileSystemStorage()
        file_path = fs.save(csv_file.name, csv_file)
        file_path = fs.path(file_path)  # Get the full file path

        # Pass the uploaded file to the ingestion script
        ingest_csv(file_path)

        # Optionally, delete the file after processing
        fs.delete(file_path)

        return HttpResponse("Data ingestion completed!")
    return render(request, "ingest_data.html")




def generate_report_view(request):
    if request.method == "POST":
        # Get the output directory from the user input
        output_dir = request.POST.get("output_dir", "").strip()

        # Validate the directory path
        if not output_dir:
            return HttpResponse("Error: No output directory specified.")

        # Ensure the directory exists
        try:
            os.makedirs(output_dir, exist_ok=True)
        except Exception as e:
            return HttpResponse(f"Error: Unable to create or access the directory. {e}")

        # Define the file path for the report
        output_path = os.path.join(output_dir, "report.csv")

        # Generate the report
        try:
            export_to_csv(output_path)
            return HttpResponse(f"Report successfully generated and saved to: {output_path}")
        except Exception as e:
            return HttpResponse(f"Error generating report: {e}")

    return render(request, "generate_report.html")
