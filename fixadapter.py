import vlc
import time

def play_radio_station(url):
    
    instance = vlc.Instance('--input-repeat=-1', '--fullscreen')

   
    player = instance.media_player_new()

   
    media = instance.media_new(url)

   
    player.set_media(media)

   
    player.play()

  
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        
        player.stop()


radio_url = 'http://inhold.org:8000/primvolna-nhk'
play_radio_station(radio_url)


