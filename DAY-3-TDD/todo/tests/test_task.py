from unittest.mock import Mock

import pytest
from bson import ObjectId

from task import Task, add, task_db, read_owner_from_file

task_list = [
    ('do_something', 'igor', True, 21),
    (None, 'igor', True, 21),
    ('do_something', None, True, None),
    ('do_something', 'ala', False, 21),
]


# python -m pytest -m smoke
# DRY RUN: python -m pytest -m smoke --collect-only (shows how much tests are selected for running)
# python -m pytest -m smoke -x  Run tests and stop after first error
# @pytest.mark.smoke
@pytest.mark.skip
@pytest.mark.parametrize('args', task_list)
def test_create_task(args):
    t = Task(*args)
    assert isinstance(t, Task)


# Use @pytest.mark.skip if a test is not ready or should not be run on certain environment,
# not when you just want to skip tests
@pytest.mark.skip
def test_create_task_with_defaults():
    t = Task()
    assert isinstance(t, Task)


def test_add_task_returns_valid_id(prepare_task):
    # t = Task('task 1')

    task_stub = Mock(task_db)
    task_stub.add.return_value = ObjectId()

    task_id = add(prepare_task, task_stub)
    assert isinstance(task_id, ObjectId)


def test_read_owner_from_file(tasks_file_json):
    owner = read_owner_from_file(tasks_file_json)
    assert owner == 'Pawel'


# Execute with shadow processes output python -m pytest -rP
# -r show extra test summary info as specified by chars: (f)ailed, (E)rror, (s)kipped, (x)failed,
# (X)passed, (p)assed, (P)assed with output, (a)ll except, passed (p/P), or (A)ll. (w)arnings
# are enabled by default (see --disable-warnings), 'N' can be used to reset the list. (default: 'fE').
