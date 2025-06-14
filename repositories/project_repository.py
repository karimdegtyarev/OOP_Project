from typing import List, Optional
from models.project import Project


class ProjectRepository:
    def __init__(self):
        self.projects = []
        self.next_id = 1

    def get_all(self) -> List[Project]:
        return self.projects

    def get_by_id(self, project_id: int) -> Optional[Project]:
        for project in self.projects:
            if project.id == project_id:
                return project
        return None

    def create(self, project: Project) -> Project:
        project.id = self.next_id
        self.next_id += 1
        self.projects.append(project)
        return project

    def update(self, project_id: int, project_update: Project) -> Optional[Project]:
        for i, project in enumerate(self.projects):
            if project.id == project_id:
                updated_project = project.copy(update=project_update.dict(exclude_unset=True))
                self.projects[i] = updated_project
                return updated_project
        return None

    def delete(self, project_id: int) -> bool:
        for i, project in enumerate(self.projects):
            if project.id == project_id:
                del self.projects[i]
                return True
        return False