from enum import Enum


from fastapi import FastAPI


from my_modules.need_extra import current_indian_time

app = FastAPI()


class ModelName(str, Enum):
    alexnet = "Alexnet"
    resnet = "REsnet"
    lenet = "leteT"
    planet = 234


app = FastAPI()


def a_big_work():
    for i in range(9999):
        print(i)


@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    a_big_work()
    return {
        "file_path": file_path.upper(),
        "execution_time": current_indian_time().strftime("%Y-%m-%d %H:%M:%S"),
    }


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
