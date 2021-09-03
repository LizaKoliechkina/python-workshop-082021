import json
import time
from collections import namedtuple
from bson import ObjectId

Task = namedtuple('Task', ['summary', 'owner', 'done', 'id'])
Task.__new__.__defaults__ = (None, None, False, None)


# class Task:
#     def __init__(self, summary, owner, done, idx):
#         self.idx = idx
#         self.done = done
#         self.owner = owner
#         self.summary = summary


class TaskDB:
    def add(self, task):
        time.sleep(5)
        return ObjectId()


task_db = TaskDB()


def add(task, db):
    task_id = db.add(task)
    return task_id


def read_owner_from_file(path):
    with open(path, 'r') as f:
        data = json.load(f)

    return data['owner']

