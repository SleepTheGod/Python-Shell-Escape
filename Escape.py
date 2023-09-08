import subprocess

# Define the VAR variable
VAR = "."  # Replace with the actual path

# Construct the command
command = f'echo Herro; cd /etc/; chown --recursive root {VAR}; chown -R root {VAR}'

# Run the command
try:
    subprocess.run(command, shell=True, check=True, executable='/bin/bash')
except subprocess.CalledProcessError as e:
    print(f"Error: {e}")
