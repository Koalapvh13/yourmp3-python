from typing import Optional
from fastapi import BackgroundTasks, FastAPI
from main import download, DIRECTORY
import uvicorn

app = FastAPI()


@app.get("/{video_id}")
def read_root(video_id: str, bgTask: BackgroundTasks):
    bgTask.add_task(download, video_id, DIRECTORY)
    return {"response": "Download iniciado"}


if __name__ == "__main__":
    uvicorn.run("api:app", port=8000, reload=True)

