import subprocess, time
workspace_route = "/workspace"
cmds = f"ssh -R 0:localhost:25565 serveo.net > {workspace_route}/serveo_ip.txt".split(" ")
subprocess.Popen(cmds)
ip_txt = ""
time.sleep(5)
with open(f"{workspace_route}/serveo_ip.txt", 'r') as file:
    ip_txt = file.readlines()[0].split("from ")[1][:-1]
print(f"IP from serveo: {ip_txt}")