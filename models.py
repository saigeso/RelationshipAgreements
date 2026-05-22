import datetime
import uuid
from sqlmodel import SQLModel, Field


class Accounts(SQLModel, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    name: str = Field(index=True)
    email: str = Field(index=True)
    hashed_password: str = Field()
    phone_number: str | None = Field()
    created_at: datetime.datetime = Field(default_factory=datetime.datetime.utcnow)
    updated_at: datetime.datetime = Field(default_factory=datetime.datetime.utcnow)
    account_preferences: uuid.UUID = Field(default_factory=uuid.uuid4)

class Agreements(SQLModel, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    agreement_text: str | None = Field()