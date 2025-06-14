from fastapi import FastAPI, HTTPException, status
from typing import List
from models.task import Task
from models.project import Project
from models.user import User
from repositories.task_repository import TaskRepository
from repositories.project_repository import ProjectRepository
from repositories.user_repository import UserRepository
from schemas.task import TaskCreate, TaskUpdate, TaskResponse
from schemas.project import ProjectCreate, ProjectUpdate, ProjectResponse
from schemas.user import UserCreate, UserUpdate, UserResponse

app = FastAPI()

task_repo = TaskRepository()
project_repo = ProjectRepository()
user_repo = UserRepository()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/tasks/", response_model=TaskResponse, status_code=status.HTTP_201_CREATED)
def create_task(task: TaskCreate):
    new_task = task_repo.create(Task(**task.dict()))
    return new_task


@app.get("/tasks/", response_model=List[TaskResponse])
def read_tasks():
    return task_repo.get_all()


@app.get("/tasks/{task_id}", response_model=TaskResponse)
def read_task(task_id: int):
    task = task_repo.get_by_id(task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return task


@app.put("/tasks/{task_id}", response_model=TaskResponse)
def update_task(task_id: int, task: TaskUpdate):
    updated_task = task_repo.update(task_id, Task(**task.dict()))
    if updated_task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return updated_task


@app.delete("/tasks/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: int):
    if not task_repo.delete(task_id):
        raise HTTPException(status_code=404, detail="Task not found")


@app.get("/projects/{project_id}/tasks", response_model=List[TaskResponse])
def read_project_tasks(project_id: int):
    return task_repo.get_by_project(project_id)


# Projects endpoints
@app.post("/projects/", response_model=ProjectResponse, status_code=status.HTTP_201_CREATED)
def create_project(project: ProjectCreate):
    new_project = project_repo.create(Project(**project.dict()))
    return new_project


@app.get("/projects/", response_model=List[ProjectResponse])
def read_projects():
    return project_repo.get_all()


@app.get("/projects/{project_id}", response_model=ProjectResponse)
def read_project(project_id: int):
    project = project_repo.get_by_id(project_id)
    if project is None:
        raise HTTPException(status_code=404, detail="Project not found")
    return project


@app.put("/projects/{project_id}", response_model=ProjectResponse)
def update_project(project_id: int, project: ProjectUpdate):
    updated_project = project_repo.update(project_id, Project(**project.dict()))
    if updated_project is None:
        raise HTTPException(status_code=404, detail="Project not found")
    return updated_project


@app.delete("/projects/{project_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_project(project_id: int):
    if not project_repo.delete(project_id):
        raise HTTPException(status_code=404, detail="Project not found")


# Users endpoints
@app.post("/users/", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def create_user(user: UserCreate):
    try:
        new_user = user_repo.create(User(**user.dict()))
        return new_user
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )


@app.get("/users/", response_model=List[UserResponse])
def read_users():
    return user_repo.get_all()


@app.get("/users/{user_id}", response_model=UserResponse)
def read_user(user_id: int):
    user = user_repo.get_by_id(user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@app.put("/users/{user_id}", response_model=UserResponse)
def update_user(user_id: int, user: UserUpdate):
    updated_user = user_repo.update(user_id, User(**user.dict()))
    if updated_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return updated_user


@app.delete("/users/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(user_id: int):
    if not user_repo.delete(user_id):
        raise HTTPException(status_code=404, detail="User not found")


@app.get("/users/{user_id}/tasks", response_model=List[TaskResponse])
def read_user_tasks(user_id: int):
    return task_repo.get_by_user(user_id)
