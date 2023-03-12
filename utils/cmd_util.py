import os
import shlex
import subprocess


def run_cmd(cmd, shlex_reformat=False, shell=False, logger=None, **kwargs):
    if shlex_reformat and shell:
        raise ValueError('shlex_reformat and shell are mutually exclusive')

    if shell:
        if not isinstance(cmd, str):
            raise ValueError('cmd must be str when shell=True')
        kwargs['shell'] = shell

    # reformat cmd
    if shlex_reformat:
        if isinstance(cmd, list):
            cmd_str = ' '.join(cmd)
        else:
            cmd_str = cmd
        cmd = shlex.split(cmd_str)

    if logger:
        logger.info('cmd: %s, %s', cmd, kwargs)

    extra_env = kwargs.pop('env', {})
    if extra_env:
        env = os.environ.copy()
        env.update(extra_env)
        kwargs['env'] = env

    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, **kwargs)
    out, err = p.communicate()
    out, err = out.decode(), err.decode()

    if logger:
        logger.debug('cmd=%s returncode=%s out=%s err=%s', cmd, p.returncode, out, err)
    return p.returncode, out, err
