import os
import sys
import subprocess
from pathlib import Path
from typing import Union


def popen(cmd):
    startupinfo = subprocess.STARTUPINFO()
    startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
    process = subprocess.Popen(cmd, shell=True, startupinfo=startupinfo, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
    return process.stdout.read()


def get_path_exe(exe_name: str, x86: bool = True, folder: str = '') -> Union[str, None]:
    ''' Retorna a path de um executável '''

    path_exe = None

    if x86:
        path_program_files = os.path.join(os.environ['PROGRAMFILES(X86)'], folder)
    else:
        path_program_files =  os.path.join(os.environ['PROGRAMFILES'], folder)

    for path in Path(path_program_files).rglob(exe_name):
        path_exe = path

    return path_exe


def vlc_path() -> Union[str, bool]:
    path_vlc = get_path_exe("vlc.exe", folder='VideoLAN')
    if not path_vlc:
        path_vlc = get_path_exe("vlc.exe", x86=False, folder='VideoLAN')

    if not path_vlc:
        return False

    return path_vlc


def start_stream(url: str) -> bool:
    if sys.platform == 'win32':
        path_vlc = vlc_path()
    else:
        print('[!] A busca automática pelo VLC só funciona no Windows')
        print('[!] Sete a path do vlc (path_vlc) manulamente')
    
    if not path_vlc:
        print('[-] VLC não foi encontrado !!')
        return False

    popen(f'"{path_vlc}" "{url}"')
    return True
