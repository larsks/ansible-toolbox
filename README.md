This repository contains a collection of tools that I find useful in
working with [Ansible][].

[ansible]: http://ansible.com/

The `ansible-role` script allows you to run a role from the command line.

The `ansible-task` script allows you to run a task list directly from
the command line.

For example, if you have a role `roles/testrole`, you can run it on
localhost like this:

    ansible-role testrole

This will target `localhost` by default, but you can use `--inventory`
and `--host` to modify the target of the role.

The `ansible-task` script works similarly:

    ansible-task my-task-list.yml

The following options are unique to these commands:

- `--hosts`, `-H` *hosts*  -- The value of this argument will be applied
  to the `hosts:` line in the generated playbook.  Defaults to
  `localhost`.
- `--gather`, `-g` -- Enable fact gathering (this is the default)
- `--no-gather`, `-G` -- Disable fact gathering

The following additional options are simply proxies to the equivalent
`ansible-playbook` options:

- `--verbose`, `-v`
- `--sudo`, `-s`
- `--become`, `-b`
- `--user`, `-u` *user*
- `--inventory`, `-i` *inventory*
- `--extra-vars`, `-e` *vars*

## Installation

You can run:

    python setup.py install

