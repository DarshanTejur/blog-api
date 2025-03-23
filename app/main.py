from fastapi import FastAPI
from app.database import engine
from app import models
from app.routers import user, auth, blog
import json

from fastapi.openapi.utils import get_openapi


models.Base.metadata.create_all(bind=engine)
app = FastAPI()


@app.get("/")
def root():
    return {"message": "hello"}


app.include_router(user.router)
app.include_router(auth.router)
app.include_router(blog.router)


with open("openapi.json", "w") as json_file:
    json.dump(
        get_openapi(
            title=app.title,
            version=app.version,
            openapi_version=app.openapi_version,
            description=app.description,
            routes=app.routes,
        ),
        json_file,
        indent=4,
    )
