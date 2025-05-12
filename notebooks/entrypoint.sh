export PYENV_ROOT="$HOME/tetra/pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"
export PORT=${PORT:-8888}
eval "$(pyenv init --path)"
eval "$(pyenv virtualenv-init -)"

jupyter lab --no-browser \
 --port=${PORT} \
 --notebook-dir=./
