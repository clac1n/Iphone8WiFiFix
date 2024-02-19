import vlc
import time
import requests
import tkinter as tk
from tkinter import messagebox

url = 'http://inhold.org:8000/primvolna-nhk'

instance = vlc.Instance('--input-repeat=-1', '--fullscreen')
player = instance.media_player_new()
media = instance.media_new(url)
player.set_media(media)
player.audio_set_mute(True)
player.play()

def check_traffic():
    if not traffic_is_active():
        show_warning_window()

def traffic_is_active():
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return True
        else:
            return False
    except requests.ConnectionError:
        return False
    except requests.RequestException as e:
        print(f"Произошла ошибка при запросе к сайту {url}: {e}")
        return False

def show_warning_window():
    root = tk.Tk()
    root.withdraw()
    messagebox.showwarning("Трафик прервался", "Трафик с сайта прекратился.")
    root.destroy()

try:
    while True:
        time.sleep(5)  # Проверка каждые 5 секунд
        check_traffic()
except KeyboardInterrupt:
    player.stop()
