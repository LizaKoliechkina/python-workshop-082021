import json

import pytest

from task import Task

# Fixture scopes: module, session, function, class, package


@pytest.fixture(scope='session')
def prepare_task():
    task = Task('Task 1', 'Andy', 'True', 38)
    yield task
    print('Clean up')


@pytest.fixture(scope='module')
def tasks_file_json(tmpdir_factory):  # It is a fake (type of doubler) because imitate all methods of the class
    tasks = {
        "summary": "task 3",
        "owner": "Pawel",
        "done": True,
        "id": 25
    }
    file_ = tmpdir_factory.mktemp('data').join('tasks.json')  # saved in RAM

    with file_.open('w') as f:
        json.dump(tasks, f)

    print('Tmp json file', file_)
    return file_
