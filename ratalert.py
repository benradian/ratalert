import os
import shlex, subprocess
from colorama import Fore, Style

cmd = "/bin/ps -A" # list of processes

runningprox = subprocess.check_output(shlex.split(cmd)) # returns output as byte string

rpstring = runningprox.decode("utf-8") # converts byte string to string and puts it in a variable

vnc = "VNC"
realvnc = "RealVNC"
tightvnc = "TightVNC"
ultravnc = "UltraVNC"
logmein = "LogMeIn"
gotomypc = "GoToMyPC"
teamviewer = "TeamViewer"
print("\n")
if vnc in rpstring.split():
    print(Fore.RED + "WARNING! Remote Access Trojan \'VNC\' has been detected in your PC.")
elif realvnc in rpstring.split():
    print(Fore.RED + "WARNING! Remote Access Trojan \'RealVNC\' has been detected in your PC.")
elif tightvnc in rpstring.split():
    print(Fore.RED + "WARNING! Remote Access Trojan \'TightVNC\' has been detected in your PC.")
elif ultravnc in rpstring.split():
    print(Fore.RED + "WARNING! Remote Access Trojan \'UltraVNC\' has been detected in your PC.")
elif logmein in rpstring.split():
    print(Fore.RED + "WARNING! Remote Access Trojan \'LogMeIn\' has been detected in your PC.")
elif gotomypc in rpstring.split():
    print(Fore.RED + "WARNING! Remote Access Trojan \'GoToMyPC\' has been detected in your PC.")
elif teamviewer in rpstring.split():
    print(Fore.RED + "WARNING! Remote Access Trojan \'TeamViewer\' has been detected in your PC.")
else:
    print(Fore.GREEN + "No RAT has been found among your running processes.")

print(Style.RESET_ALL)

CPU_Pct=str(round(float(os.popen('''grep 'cpu ' /proc/stat | awk '{usage=($2+$4)*100/($2+$4+$5)} END {print usage }' ''').readline()),2))

print("Your CPU usage is: " + CPU_Pct)
if float(CPU_Pct) >= 80:
    print(Fore.RED + "WARNING! Your CPU usage is unusually high. If you are not running many programs, this may indicate the presence of a spyware in your PC.")
else:
    print(Fore.GREEN + "Your CPU usage is average.")

print(Style.RESET_ALL)
