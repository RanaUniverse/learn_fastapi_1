from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None) -> dict[str, int | str | None]:
    if q is None:
        return_query = None
    else:
        return_query = q.upper()

    return {
        "item_id": item_id,
        "query": return_query,
    }
