import subprocess, platform, shlex

subprocess.call('echo "Körs i terminalen"', shell=True) # körs i både powershell och bash

def runCommand( command ):
    subprocess.call(shlex.split(command))

currentPlatform = platform.system()

if currentPlatform == "Linux":
    print("You are running Linux")
    print("# Genereate password")
    cmd = "openssl passwd -1 Elev123"
    passwd = subprocess.check_output(cmd, shell=True)
    cmd = "useradd -m -p {passwd} test" # should probably have -g option for adding to a specific group
    print("# Add user")
    subprocess.call(cmd, shell=True)
    cmd = "getent passwd | grep test"
    print("# Check if user exists")
    subprocess.call(cmd, shell=True)
    cmd = "userdel -fr test"
    print("# Remove user")
    subprocess.call(cmd, shell=True)
    print("# Check if user exists")
    cmd = "getent passwd | grep test"
    subprocess.call(cmd, shell=True)
elif currentPlatform == "Windows":
    print("You are running Windows")
else:
    print("You are running: {currentPlatform}")