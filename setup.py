from setuptools import setup, find_packages
from ansible_toolbox import __version__ as version

with open('requirements.txt') as fd:
    setup(name='ansible-toolbox',
          author='Lars Kellogg-Stedman',
          author_email='lars@oddbit.com',
          url='https://github.com/larsks/ansible-role',
          version=version,
          install_requires=fd.readlines(),
          packages=find_packages(),
          package_data={'ansible_toolbox': [
              'templates/*'
          ]},
          entry_points={'console_scripts': [
              'ansible-role = ansible_toolbox.cmd.role:main',
              'ansible-task = ansible_toolbox.cmd.task:main',
              'ansible-eval = ansible_toolbox.cmd.eval:main',
          ]},
          )
