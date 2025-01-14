import fire
from music_library.tasks.ingest_data import ingest_csv

if __name__ == "__main__":
    fire.Fire(ingest_csv)
