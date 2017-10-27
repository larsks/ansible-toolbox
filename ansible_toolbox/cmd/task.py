from __future__ import absolute_import

import logging
import subprocess
import tempfile

from ansible_toolbox.base import BaseApp

LOG = logging.getLogger(__name__)


class TaskApp (BaseApp):
    '''Execute an Ansible task list.'''

    def build_argument_parser(self):
        p = super(TaskApp, self).build_argument_parser()
        p.add_argument('tasklist')
        return p

    def main(self):
        args = self.parse_args()
        template = self.get_template('tasklist.yml')
        version = self.probe_ansible_version()

        if (version[0] > 2) or (version[1] >= 4):
            include_action = 'import_tasks'
        else:
            include_action = 'include'

        with tempfile.NamedTemporaryFile(dir='.') as fd:
            fd.write(template.render(
                tasklist=args.tasklist,
                hosts=args.hosts,
                gather=args.gather,
                include_action=include_action
            ).encode('utf-8'))

            fd.flush()

            cmd = ['ansible-playbook', fd.name]
            cmd.extend(self.build_command_line(args))
            subprocess.check_call(cmd)


def main():
    TaskApp().main()
