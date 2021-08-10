import win32com.shell.shell as shell
import subprocess



def go():
    try:
        pObj = subprocess.Popen('del /q/f/s %TEMP%\*', shell=True, stdout = subprocess.PIPE, stderr= subprocess.PIPE)
        rTup = pObj.communicate()
        rCod = pObj.returncode

        commands = 'del C:\Windows\Prefetch\*.* /Q'
        shell.ShellExecuteEx(lpVerb='runas', lpFile='cmd.exe', lpParameters='/c '+commands)

        print(""" 

░██╗░░░░░░░██╗██╗███╗░░██╗░░░░░░██████╗░░█████╗░░█████╗░░██████╗████████╗███████╗██████╗░
░██║░░██╗░░██║██║████╗░██║░░░░░░██╔══██╗██╔══██╗██╔══██╗██╔════╝╚══██╔══╝██╔════╝██╔══██╗
░╚██╗████╗██╔╝██║██╔██╗██║█████╗██████╦╝██║░░██║██║░░██║╚█████╗░░░░██║░░░█████╗░░██║░░██║
░░████╔═████║░██║██║╚████║╚════╝██╔══██╗██║░░██║██║░░██║░╚═══██╗░░░██║░░░██╔══╝░░██║░░██║
░░╚██╔╝░╚██╔╝░██║██║░╚███║░░░░░░██████╦╝╚█████╔╝╚█████╔╝██████╔╝░░░██║░░░███████╗██████╔╝
░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚══╝░░░░░░╚═════╝░░╚════╝░░╚════╝░╚═════╝░░░░╚═╝░░░╚══════╝╚═════╝░
            """)

        
    except:
        pass
