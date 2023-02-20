# Working with PyATS - Simple Examples

## Installing PyATS

Make sure you have Python 3.10 (recommended)

Create a virtual environment

```bash
mkdir pyats-examples
cd pyats-examples
python3 -m venv venv
source venv/bin/activate
```

Install PyATS Standard Library

```bash
pip3 install --default-timeout=100 'pyATS[library]'
```

**Note**: `--default-timeout=100` gives you 100 seconds for time-out. For some reason, PyATS takes a long time to download from PyPI.

Check PyATS version

```bash
$ pyats version check

You are currently running pyATS version: 23.1
Python: 3.10.10 [64bit]
```

## Testbed File (YAML)

Points to note:

1. `hostname` in the testbed file must match with actual device hostname
2. If your SSH connection needs options (old encryption or key-exchange algorithms etc.,), you must use `custom` block with `ssh-options` key (Check `/Testing/ssh-test/testbed-ssh.yaml` for example)
