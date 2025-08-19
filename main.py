from enum import Enum

from fastapi import FastAPI

app = FastAPI()


class ModelName(str, Enum):
    alexnet = "Alexnet"
    resnet = "REsnet"
    lenet = "leteT"
    planet = 234


app = FastAPI()


@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path.upper()}


@app.get("/models/{model_name}")
async def get_model(model_name: ModelName) -> dict[str, str | ModelName]:

    if model_name is ModelName.alexnet:
        return {
            "model_name": model_name,
            "message": "Deep Learnig FTW!",
        }

    if model_name.value == "leteT":
        return {
            "model_name": model_name,
            "message": "LeCNN all the images",
        }

    return {
        "model_name": model_name,
        "message": "Have some residuals",
    }
