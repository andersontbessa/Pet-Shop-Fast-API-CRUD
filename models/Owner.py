from pydantic import BaseModel

class Owner(BaseModel):
    Name: str
    Address1: str
    Address2: str
    City: str
    State: str
    ZipCode: str
    Country: str
    UpdatedOn: str