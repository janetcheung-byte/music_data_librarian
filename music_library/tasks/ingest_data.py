import pandas as pd
from music_library.models import MusicMetadata

def ingest_csv(file):
    """Ingest a CSV file into the database.

    Args:
        file (str): The path to the CSV file.
    """
    try:
        # Check if the file is a CSV
        if not file.lower().endswith('.csv'):
            raise ValueError("The provided file is not a CSV file.")
        
        # Read the file into a Pandas DataFrame
        data = pd.read_csv(file)

        # Validate that required columns exist
        required_columns = ['title', 'artist']
        for col in required_columns:
            if col not in data.columns:
                raise ValueError(f"Missing required column: {col}")

        # Save each row as a record in the database
        for _, row in data.iterrows():
            MusicMetadata.objects.create(
                title=row['title'],
                artist=row['artist'],
                album=row.get('album', None),
                release_date=row.get('release_date', None),
                genre=row.get('genre', None),
            )
        print("Data ingestion completed successfully.")

    except ValueError as ve:
        print(f"ValueError: {ve}")
    except pd.errors.EmptyDataError:
        print("The provided CSV file is empty.")
    except pd.errors.ParserError:
        print("The provided file is not a valid CSV format.")
    except Exception as e:
        print(f"An error occurred: {e}")
