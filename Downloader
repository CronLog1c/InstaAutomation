import instaloader
import os
import keyboard

output_folder = 'Videos'


loader = instaloader.Instaloader(
    download_comments=False,
    download_geotags=False,
    download_video_thumbnails=False,  
    save_metadata=False 
)

loader.download_caption = False

while True:
    url = input('Enter the Instagram URL: ')
    
    try:
        shortcode = url.split('/')[-2]
        
        post = instaloader.Post.from_shortcode(loader.context, shortcode)
        loader.download_post(post, target=output_folder)
        
        print(f"Downloaded post from {url}")
    except Exception as e:
        print(f'Something went wrong: {e}')
    
    if keyboard.is_pressed('esc'):
        print("Exiting...")
        break
