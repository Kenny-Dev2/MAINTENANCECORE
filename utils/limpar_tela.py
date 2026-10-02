import os
import subprocess


def limpar_tela():
    if os.name == "nt":
        subprocess.run(["cmd", "/c", "cls"])
    else:
        subprocess.run(["clear"])