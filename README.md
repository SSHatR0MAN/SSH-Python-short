# SSH-Python-short
#A short script to allow ssh connection between computers on a local network using rsync and port 22

# Development Setup for Ubuntu 
1. Install Pyenv (Python Version Manager: https://github.com/pyenv/pyenv).
    - `curl https://pyenv.run | bash`
2. Add the pyenv cmd to your Bash.
    ```
    export PYENV_ROOT="$HOME/.pyenv"
    [[ -d $PYENV_ROOT/bin ]] && export PATH="$PYENV_ROOT/bin:$PATH"
    eval "$(pyenv init -)"
    ```
3. Restart your shell
    - `exec "$SHELL"`
4. Update Pyenv
    - `pyenv update`
5. Install Python 3.12.3
    - `pyenv install 3.12.3`
    - You can view all the python versions with `pyenv install -l`
6. Create your virtual environment (Be sure to `cd` to the correct path you want it in, if not enter full path).
    - `python -m venv <my_env_name>`
7. Initialize your virtual environment (Verify you're in via `which python`).
    - `source <my_env_name>/bin/activate`
8.  Install requirements (`requirements.txt`).
    - `pip install -r requirements.txt`