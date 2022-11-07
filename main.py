from enum import Enum
from typing import Union

import uvicorn
from fastapi import FastAPI
from routers.project_router import router as project
from routers.environment_router import router as environment
from routers.group_router import router as group
from routers.api_router import router as api

app = FastAPI()
app.include_router(project)
app.include_router(environment)
app.include_router(group)
app.include_router(api)

if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)
