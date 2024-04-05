import uvicorn
from fastapi import FastAPI
import app.api.users.routes as users_router
import app.api.projects as project_router
from fastapi.middleware.cors import CORSMiddleware




app = FastAPI(
    title = 'Tasks Manager'
)

app.include_router(users_router.router)
app.include_router(project_router.router)


origins = [
    "http://127.0.0.1:8000/"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


if __name__ == '__main__':
    uvicorn.run(app,
                host="127.0.0.1",
                port=8000,
                )