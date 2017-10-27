This repository contains a collection of tools that I find useful in
working with [Ansible][].

[ansible]: http://ansible.com/

## ansible-role

The `ansible-role` script allows you to run a role from the command line.

For example, if you have a role `roles/testrole`, you can run it like
this:

    ansible-role testrole

This will target `localhost` by default, but you can use `--inventory`
and `--host` to modify the target of the role.

## ansible-task

The `ansible-task` script allows you to run a task list directly from
the command line.

If you have a tasklist `mytasks.yml`, you can run it like this:

    ansible-task mytasks.yml

## ansible-eval

The `ansible-eval` script will return the result of evaluating a
Jinja2 template with ansible.  For example, the result of running:

    ansible-eval '{{ ansible_eth0.ipv4 }}'

Might look something like:

    TASK [debug] *******************************************************************
    ok: [localhost] => {
        "msg": {
            "address": "192.168.1.74", 
            "broadcast": "192.168.1.255", 
            "netmask": "255.255.255.0", 
            "network": "192.168.1.0"
        }
    }

## Common options

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
