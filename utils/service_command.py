import subprocess
import os


class ServiceCommand:
    def run(self, cmd, path=os.getcwd()):
        subprocess.call(cmd.split(" "), cwd=path,
                        stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)

    def run_with_output(self, cmd, path=os.getcwd()):
        return subprocess.run(cmd.split(" "), cwd=path, stdout=subprocess.PIPE, text=True).stdout

    def background(self, cmd, path=os.getcwd()):
        os.system(f"cd {path}; {cmd} >/dev/null 2>&1")

    def clear(self):
        subprocess.call("clear")

    def script(self, cmd, path=os.getcwd()):
        os.system(f"cd {path}; {cmd}; echo \n\n")

    def script_with_output(self, cmd, path=os.getcwd()):
        return os.popen(f"cd {path}; {cmd} >/dev/null 2>&1").read()
