import pandas as pd
from music_library.models import MusicMetadata

def export_to_csv(output_path):
    # Query the database for all records in MusicMetadata
    data = MusicMetadata.objects.all().values()

    # Convert the data to a Pandas DataFrame
    df = pd.DataFrame(data)

    # Save the DataFrame as a CSV file to the specified path
    df.to_csv(output_path, index=False)
