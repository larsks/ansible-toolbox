import pytest
import subprocess

from common import BaseTestCase


class TestEval(BaseTestCase):
    def test_eval_success(self):
        res = subprocess.check_output(['ansible-eval', '--debug',
                                       '-e', 'foo=bar', '{{ foo }}'])
        assert res.decode('utf-8').strip() == 'bar'

    def test_eval_error(self):
        with pytest.raises(subprocess.CalledProcessError):
            subprocess.check_call(['ansible-eval', '--debug',
                                   '-e', 'foo=bar', '{{ foo '])
