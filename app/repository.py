from abc import ABC, abstractmethod
#Base- interfcae 
class TaskRepository(ABC):
    @abstractmethod
    def get_all_tasks(self):
        pass

    @abstractmethod
    def get_by_id(self, task_id: int):
        pass

    @abstractmethod
    def create_task(self, task_id: int):
        pass

    @abstractmethod
    def update_task(self, task_id: int, title:str, done:bool):
        pass

    @abstractmethod
    def delete_task(self, task_id: int):
        pass

    class Inmemorytaskrepo(TaskRepository):
        def __init__(self):
            self._tasks = [
               { "id": 1, "title": "Go to gym","done":False },
  { "id": 2, "title": "Complete Assignment","done":True },
  { "id": 3, "title": "Read a book","done":False }
  
            ]

        def get_all(self):
            return self._tasks
        

        def get_by_id(self, task_id: int):
            for task in self._tasks:
                if task["id"] == task_id:
                    return task
            return None

        def create_task(self, title:str):
            new_id = max(task["id"] for task in self._tasks) + 1 if self._tasks else 1
            new_task = {"id": new_id, "title": title, "done": False}
            self._tasks.append(new_task)
            return new_task

        def update_task(self, task_id: int, title: str, done: bool):
            for task in self._tasks:
                if task["id"] == task_id:
                    task["title"] = title
                    task["done"] = done
                    return task
            return None

        def delete_task(self, task_id: int):
            for i, task in enumerate(self._tasks):
                if task["id"] == task_id:
                    self._tasks.pop(i)
                    return True
            return False