import os
import asyncio
import random
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, StreamingResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pathlib import Path

app = FastAPI()


app.mount("/static", StaticFiles(directory="static"), name="static")


templates = Jinja2Templates(directory="templates")


def get_image_files():
    image_dir = Path("static/images")
    image_files = [f.name for f in image_dir.glob("*.jpg") + image_dir.glob("*.png") + image_dir.glob("*.jpeg")]
    return image_files


@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


async def sse_generator():
    while True:

        image_files = get_image_files()
        if image_files:

            random_image = random.choice(image_files)

            yield f"data: {random_image}\n\n"
        else:
            yield f"data: no_images_found.jpg\n\n"

        await asyncio.sleep(7)


@app.get("/sse")
async def sse(request: Request):
    return StreamingResponse(sse_generator(), media_type="text/event-stream")