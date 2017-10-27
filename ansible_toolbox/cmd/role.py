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
        p.add_argument('-t', '--tags')
        p.add_argument('role')
        return p

    def build_command_line(self, args):
        cmd = super(RoleApp, self).build_command_line(args)

        if args.tags:
            cmd.extend(('-t', args.tags))

        return cmd

    def main(self, args):
        template = self.get_template('role.yml')

        with tempfile.NamedTemporaryFile(dir='.') as fd:
            playbook = template.render(
                role=args.role,
                hosts=args.hosts,
                gather=args.gather,
            )

            LOG.debug('playbook: %s', playbook)
            fd.write(playbook.encode('utf-8'))
            fd.flush()

            cmd = ['ansible-playbook', fd.name]
            cmd.extend(self.build_command_line(args))
            LOG.debug('running command: %s', cmd)
            subprocess.check_call(cmd)


app = RoleApp()


def main():
    app.run()
