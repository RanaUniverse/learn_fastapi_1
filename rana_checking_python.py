from pydantic import BaseModel

class Address(BaseModel):
    street: str
    city: str
    zip_code: str

class User(BaseModel):
    id: int
    name: str
    address: Address

# Create a Pydantic model instance
user_address = Address(street="123 Main St", city="Anytown", zip_code="12345")
user = User(id=1, name="Alice", address=user_address)

# Convert the Pydantic model to a dictionary
user_dict = user.model_dump()

# print(user_dict)
print(user_address)
print(user)

print(user_address.model_dump())
print(type(user.model_dump()))