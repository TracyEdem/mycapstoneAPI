from fastapi import FastAPI
from routes.user import user
from routes.catalog import catalog
from routes.cut import cut
from routes.measurement import measurement
from routes.client import client
from routes.project import project
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.include_router(user, tags=["user"])
app.include_router(catalog, prefix="/catalog", tags=["catalog"])
app.include_router(cut, prefix="/cut", tags=["cut"])
app.include_router(measurement, prefix="/measurement", tags=["measurement"])
app.include_router(client, prefix="/client", tags=["client"])
app.include_router(project, prefix="/project", tags=["project"])

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)