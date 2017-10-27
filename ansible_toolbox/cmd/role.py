from __future__ import absolute_import

import logging
import subprocess
import tempfile

from ansible_toolbox.base import BaseApp

LOG = logging.getLogger(__name__)


class RoleApp (BaseApp):
    '''Execute a single Ansible role.'''

    def build_argument_parser(self):
        p = super(RoleApp, self).build_argument_parser()
        p.add_argument('role')
        p.add_argument('-t', '--tags')
        return p

    def build_command_line(self, args):
        cmd = super(RoleApp, self).build_command_line(args)

        if args.tags:
            cmd.extend(('-t', args.tags))

        return cmd

    def main(self):
        args = self.parse_args()
        template = self.get_template('role.yml')

        with tempfile.NamedTemporaryFile(dir='.') as fd:
            fd.write(template.render(
                role=args.role,
                hosts=args.hosts,
                gather=args.gather,
            ).encode('utf-8'))

            fd.flush()

            cmd = ['ansible-playbook', fd.name]
            cmd.extend(self.build_command_line(args))
            subprocess.check_call(cmd)


def main():
    RoleApp().main()
