import subprocess

def ping(host):
    try:
        process = subprocess.Popen(["ping", "-c", "4", host], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()

        if process.returncode == 0:
            return True, stdout.decode()
        else:
            return False, stderr.decode()
    except Exception as e:
        return False, str(e)
