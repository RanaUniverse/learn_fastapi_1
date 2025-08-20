from enum import Enum


from fastapi import FastAPI, Request


from pydantic import BaseModel


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


class Item(BaseModel):
    name: str
    price: float
    description: str | None = None
    tax: float | None = None

    model_config = {
        # for extra key value in query it will not raise anything, rather use those value
        "extra": "allow"
        # # for extra key value in query it will do nothing
        # "extra": "ignore"
        # for extra key value in query it will reaise 422u
        # "extra": "forbid"
    }
    # 👈 new way in Pydantic v2


@app.post("/items/")
async def create_item(
    item: Item,
    request: Request,
    tax: float | None = None,
    # ) -> dict[str, str | float | None]:
) -> dict[str, float | int | str | dict[str, str]]:

    query_params = dict(request.query_params)
    print(query_params)
    # applied_tax = tax if tax is not None else (item.tax or 0)

    if tax is not None:
        applied_tax = tax
    else:
        if item.tax:
            applied_tax = item.tax
        else:
            applied_tax = 0
    # The upper logic is for give preference to the query tax value
    total_price = item.price + applied_tax
    return {
        **item.model_dump(),
        "applied_tax": applied_tax,
        "total_price": total_price,
        "execution_time": current_indian_time().strftime("%Y-%m-%d %H:%M:%S"),
        # **query_params
        "query_parameters": query_params,
    }


@app.get("/items/{item_id}")
async def red_user_item2(item_id: str, needy: str):
    item = {
        "item_id": item_id,
        "needy": "This is must need " + needy.upper(),
    }
    return item


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
