import pytest
import subprocess


class TestEval(object):
    def test_eval_success(self):
        res = subprocess.check_output(['ansible-eval', '--debug', '-e', 'foo=bar',
                                       '{{ foo }}'])
        assert res.strip() == 'bar'


    def test_eval_error(self):
        with pytest.raises(subprocess.CalledProcessError):
            subprocess.check_call(['ansible-eval', '--debug', '-e', 'foo=bar',
                                     '{{ foo '])
