from typing import Optional
from fastapi import BackgroundTasks, FastAPI
from main import download, DIRECTORY

app = FastAPI()


@app.get("/{video_id}")
def read_root(video_id: str, bgTask: BackgroundTasks):
    bgTask.add_task(download, video_id, DIRECTORY)
    return {"response": "Download iniciado"}
