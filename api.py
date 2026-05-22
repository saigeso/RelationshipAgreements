import uuid
from fastapi import Depends, FastAPI, HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlmodel import create_engine, SQLModel, Session

from models import Accounts, Agreements

print("start")

DATABASE_URL = "postgresql+psycopg://postgres:admin@localhost:5432/postgres"
engine = create_engine(DATABASE_URL)

def get_session():
    with Session(engine) as session:
        yield session

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/accounts/{account_id}")
def get_account(account_id: uuid.UUID, session: Session = Depends(get_session)):
    account = session.get(Accounts, account_id)
    if not account:
        raise HTTPException(status_code=404, detail="Account not found")
    return account

@app.post("/accounts")
def create_account(account: Accounts, session: Session = Depends(get_session)):
    session.add(account)
    session.commit()
    session.refresh(account)
    return account

@app.get("/agreements/{agreement_id}")
def get_agreement(agreement_id: uuid.UUID, session: Session = Depends(get_session)):
    agreement = session.get(Agreements, agreement_id)
    if not agreement:
        raise HTTPException(status_code=404, detail="Agreement not found")
    return agreement

@app.post("/agreements")
def create_agreement(agreement: Agreements, session=Depends(get_session)):
    session.add(agreement)
    session.commit()
    session.refresh(agreement)
    return agreement
