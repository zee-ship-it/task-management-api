from abc import ABC, abstractmethod
# from app.database import get_db_connection
import sqlite3
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



class SqliteTaskRepository(TaskRepository):
    def __init__(self, db_path="tasks.db"):
        self.db_path = db_path
        self._initialize_db()

    def get_connection(self):
        connection = sqlite3.connect(self.db_path)
        connection.row_factory = sqlite3.Row
        return connection

    def _initialize_db(self):
        connection = self.get_connection()
        cursor = connection.cursor()
        cursor.execute(
            """CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                done BOOLEAN NOT NULL DEFAULT 0
            ); """
           
        )
        cursor.execute("SELECT COUNT(*) FROM tasks;")
        if cursor.fetchone()[0] == 0:
            cursor.executemany(
                "INSERT INTO tasks (title, done) VALUES (?, ?);",
                [
                    ("Go to gym", False),
                    ("Complete Assignment", True),
                    ("Read a book", False),
                ],
            )
        connection.commit()
        connection.close()

    def get_all_tasks(self):
        connection = self.get_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT id, title, done FROM tasks ORDER BY id ASC;")
        tasks = [dict(row) for row in cursor.fetchall()]
        connection.close()
        return tasks

    def get_by_id(self, task_id: int):
        connection = self.get_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT id, title, done FROM tasks WHERE id = ?;", (task_id,))
        row = cursor.fetchone()
        connection.close()
        return dict(row) if row else None

    def create_task(self, title: str):
        connection = self.get_connection()
        cursor = connection.cursor()
        cursor.execute(
            "INSERT INTO tasks (title, done) VALUES (?, 0) ;",
            (title,)
        )
        connection.commit()
        new_id = cursor.lastrowid
        connection.close()
        return self.get_by_id(new_id)

    def update_task(self, task_id: int, title: str, done: bool):
        connection = self.get_connection()
        cursor = connection.cursor()
        cursor.execute(
            "UPDATE tasks SET title = ?, done = ? WHERE id = ?;",
            (title, done, task_id)
        )
        connection.commit()
        updated= cursor.rowcount > 0
        connection.close()
        return self.get_by_id(task_id) if updated else None 

    def delete_task(self, task_id: int):
        connection = self.get_connection()
        cursor = connection.cursor()
        cursor.execute("DELETE FROM tasks WHERE id = ?;", (task_id,))
        connection.commit()
        deleted= cursor.rowcount > 0
        connection.close()
        return deleted