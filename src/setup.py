import os
import shutil
from venv import create
from subprocess import run

venv_dir = "./stt-venv"
uv_path = shutil.which("uv")
assert uv_path, "uv not found in PATH"

# TODO(d809): re-sync packages if requirements.txt changes after venv is created
if not os.path.isdir(venv_dir):
    create(venv_dir, with_pip=True)
    run(
        [
            uv_path,
            "pip",
            "install",
            "--python",
            venv_dir,
            "-r",
            os.path.abspath("requirements.txt"),
        ],
        check=True,
    )

os.makedirs("private", exist_ok=True)

if not os.path.isfile("private/config.yaml"):
    shutil.copyfile("templates/config.yaml.example", "private/config.yaml")
