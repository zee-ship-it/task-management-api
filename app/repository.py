from abc import ABC, abstractmethod
from app.database import get_db_connection

class TaskRepository(ABC):
    @abstractmethod
    def get_all_tasks(self):
        pass

    @abstractmethod
    def get_by_id(self, task_id: int):
        pass

    @abstractmethod
    def create_task(self, title: str):
        pass

    @abstractmethod
    def update_task(self, task_id: int, title: str, done: bool):
        pass

    @abstractmethod
    def delete_task(self, task_id: int):
        pass

class InmemoryTaskRepository(TaskRepository):
    def __init__(self):
        self._tasks = [
            {"id": 1, "title": "Go to gym", "done": False},
            {"id": 2, "title": "Complete Assignment", "done": True},
            {"id": 3, "title": "Read a book", "done": False},
        ]

    def get_all_tasks(self):
        return self._tasks

    def get_by_id(self, task_id: int):
        for task in self._tasks:
            if task["id"] == task_id:
                return task
        return None

    def create_task(self, title: str):
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

class PostgresTaskRepository(TaskRepository):
    def get_all_tasks(self):
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT id, title, done FROM tasks ORDER BY id ASC;")
        tasks = cursor.fetchall()
        cursor.close()
        connection.close()
        return tasks

    def get_by_id(self, task_id: int):
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT id, title, done FROM tasks WHERE id = %s;", (task_id,))
        task = cursor.fetchone()
        cursor.close()
        connection.close()
        return task

    def create_task(self, title: str):
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute(
            "INSERT INTO tasks (title, done) VALUES (%s, %s) RETURNING id, title, done;",
            (title, False),
        )
        task = cursor.fetchone()
        connection.commit()
        cursor.close()
        connection.close()
        return task

    def update_task(self, task_id: int, title: str, done: bool):
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute(
            "UPDATE tasks SET title = %s, done = %s WHERE id = %s RETURNING id, title, done;",
            (title, done, task_id),
        )
        updated_task = cursor.fetchone()
        connection.commit()
        cursor.close()
        connection.close()
        return updated_task

    def delete_task(self, task_id: int):
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute("DELETE FROM tasks WHERE id = %s RETURNING id;", (task_id,))
        deleted_row = cursor.fetchone()
        connection.commit()
        cursor.close()
        connection.close()
        return deleted_row is not None