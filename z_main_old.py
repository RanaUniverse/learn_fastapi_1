from typing import Union

from fastapi import FastAPI

from pydantic import BaseModel


from my_modules.need_extra import current_indian_time


app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None) -> dict[str, int | str | None]:
    if q is None:
        return_query = None
    else:
        return_query = q.upper()

    now_time = current_indian_time().strftime("%Y-%m-%d %H:%M:%S (IST)")

    return {
        "item_id": item_id,
        "query": return_query,
        "processing_time": now_time,
    }


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item) -> dict[str, str | int]:
    return {
        "item_name": item.name,
        "item_id": item_id,
    }
