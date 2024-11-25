import uvicorn
from fastapi import FastAPI
import app.api.users.users_routes as users_router
import app.api.projects.projects_routes as project_router
import app.api.tasks.tasks_routes as task_router
import app.api.groups.groups_routes as group_router
from fastapi.middleware.cors import CORSMiddleware




app = FastAPI(
    title = 'Tasks Manager',
)

app.include_router(users_router.router)
app.include_router(project_router.router)
app.include_router(task_router.router)
app.include_router(group_router.router)


origins = [
    "http://127.0.0.1:8000/",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


if __name__ == '__main__':
    uvicorn.run(
        app,
        host="127.0.0.1",
        port=8000,
    )