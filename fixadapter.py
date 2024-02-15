import vlc
import time

url = 'http://inhold.org:8000/primvolna-nhk'

instance = vlc.Instance('--input-repeat=-1', '--fullscreen')

player = instance.media_player_new()

media = instance.media_new(url)

player.set_media(media)

player.audio_toggle_mute()

player.play()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    
    player.stop()
