from fastapi import FastAPI
from endpoints.user_endpoints import router as UserRouter
from endpoints.email_endpoints import router as EmailRouter
from endpoints.phone_endpoints import router as PhoneRouter
from db.database import Base, engine


def get_application() -> FastAPI:
    route = FastAPI()
    route.include_router(UserRouter, tags=["User"], prefix="/user")
    route.include_router(PhoneRouter, tags=["Phone"], prefix="/phone")
    route.include_router(EmailRouter, tags=["Email"], prefix="/email")
    return route

app = get_application()

@app.on_event("startup")
async def startup_event():
    """Drop and create DB"""
    async with engine.begin() as conn:
        # await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


@app.get("/")
def healthcheck():
    return {"message": "success"}

# For debugging
# if __name__ == "__main__":
#     uvicorn.run(app, host="0.0.0.0", port=8000)
