from fastapi import FastAPI

from pydantic import BaseModel


class Item(BaseModel):
    name: str
    price: float
    description: str | None = None
    tax: float | None = None


app = FastAPI()


@app.post("/items/")
async def create_item(
    item: Item,
    tax: float | None = None,
) -> dict[str, str | float | None]:

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
    }
