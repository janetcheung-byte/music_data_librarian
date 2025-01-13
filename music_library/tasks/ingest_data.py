import pandas as pd
from music_library.models import MusicMetadata

def ingest_csv(file_path):
    data = pd.read_csv(file_path)
    for _, row in data.iterrows():
        MusicMetadata.objects.create(
            title=row['title'],
            artist=row['artist'],
            album=row.get('album'),
            release_date=row.get('release_date'),
            genre=row.get('genre'),
        )
