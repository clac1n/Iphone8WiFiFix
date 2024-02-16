import os
import sys
import subprocess
import ctypes

def check_vlc_installed():
    try:
        import vlc
        return True
    except ImportError:
        return False

def install_vlc():
    user_response = ctypes.windll.user32.MessageBoxW(
        0,
        "VLC не обнаружен на вашей системе. Хотите установить VLC?",
        "Установка VLC",
        1 | 48  
    )
    if user_response == 1:  
        try:
           
            vlc_installer_path = r"Сам влс установщик или же путь к нему"
            subprocess.run([vlc_installer_path, "/S"]) 
            return True
        except FileNotFoundError:
            print("Ошибка: Файл установщика VLC не найден.")
    return False

def main():
    if not check_vlc_installed():
        if install_vlc():
            print("VLC успешно установлен.")
            
            subprocess.run(["python", "fixadapter.py"])
        else:
            print("Установка VLC отменена.")
    else:
        print("VLC уже установлен на вашей системе.")

if __name__ == "__main__":
    main()
