import pandas as pd
from music_library.models import MusicMetadata

def export_to_csv(output_path):
    data = MusicMetadata.objects.all().values()
    df = pd.DataFrame(data)
    df.to_csv(output_path, index=False)
