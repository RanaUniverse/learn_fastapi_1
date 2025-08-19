from enum import Enum


from fastapi import FastAPI


from my_modules.need_extra import current_indian_time

app = FastAPI()


class ModelName(str, Enum):
    alexnet = "Alexnet"
    resnet = "REsnet"
    lenet = "leteT"
    planet = 234


def a_big_work():
    for i in range(9999):
        print(i)


fake_items_db = [
    {"item_name": "Foo"},
    {"item_name": "Bar"},
    {"item_name": "Baz"},
]


@app.get("/users/{user_id}/items/{item_id}")
async def read_user_item(
    user_id: int,
    item_id: str,
    q: str | None = None,
    short: bool = False,
):
    item: dict[str, str | int] = {"item_id": item_id.upper(), "owner_id": user_id}
    if q:
        item.update({"q": q.upper()})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a logn description."}
        )
    return item


@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]


@app.get("/items/{item_id}")
async def read_item2(item_id: str, q: str | None = None, short: bool = False):
    item = {"item_id": item_id}
    if q:
        item.update({"q": f"New_Value_{q}"})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description."}
        )
    return item


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
