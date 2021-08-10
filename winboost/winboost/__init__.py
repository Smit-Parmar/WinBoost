import win32com.shell.shell as shell
import os

def go():
    commands = 'del C:\Windows\Prefetch\*.* /Q'

    shell.ShellExecuteEx(lpVerb='runas', lpFile='cmd.exe', lpParameters='/c '+commands)

    #For clear TEMP
    os.system("del /q/f/s %TEMP%\*")

    #For clear TEMP
    os.system("del /q/f/s TEMP\*")

    #For DISK CLEANER
    os.system("cleanmgr.exe")