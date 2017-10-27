import os
import subprocess

from common import BaseTestCase

task_content = '''---
- name: test task 1
  debug:
    msg: 'this is task 1'

- name: test task 2
  tags:
    - task2
  copy:
    content: 'test task 2'
    dest: ./task2.txt

- name: test task 3
  tags:
    - task3
  copy:
    content: 'test task 3'
    dest: ./task3.txt
'''


class TestRole(BaseTestCase):
    def setup_method(self, method):
        super(TestRole, self).setup_method(method)
        os.makedirs('roles/testrole/tasks')
        with open('roles/testrole/tasks/main.yml', 'wb') as fd:
            fd.write(task_content.encode('utf-8'))

    def test_role(self):
        task2_file = 'task2.txt'
        task3_file = 'task3.txt'

        subprocess.check_call(['ansible-role', '--debug', 'testrole'])
        assert os.path.exists(task2_file)
        assert os.path.exists(task3_file)

    def test_role_tags(self):
        task2_file = 'task2.txt'
        task3_file = 'task3.txt'

        subprocess.check_call(['ansible-role', '--debug',
                               'testrole', '-t', 'task2'])
        assert os.path.exists(task2_file)
        assert not os.path.exists(task3_file)
