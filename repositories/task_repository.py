from typing import List, Optional
from models.task import Task


class TaskRepository:
    def __init__(self):
        self.tasks = []
        self.next_id = 1

    def get_all(self) -> List[Task]:
        return self.tasks

    def get_by_id(self, task_id: int) -> Optional[Task]:
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None

    def create(self, task: Task) -> Task:
        task.id = self.next_id
        self.next_id += 1
        self.tasks.append(task)
        return task

    def update(self, task_id: int, task_update: Task) -> Optional[Task]:
        for i, task in enumerate(self.tasks):
            if task.id == task_id:
                updated_task = task.copy(update=task_update.dict(exclude_unset=True))
                self.tasks[i] = updated_task
                return updated_task
        return None

    def delete(self, task_id: int) -> bool:
        for i, task in enumerate(self.tasks):
            if task.id == task_id:
                del self.tasks[i]
                return True
        return False

    def get_by_project(self, project_id: int) -> List[Task]:
        return [task for task in self.tasks if task.project_id == project_id]

    def get_by_user(self, user_id: int) -> List[Task]:
        return [task for task in self.tasks if task.user_id == user_id]