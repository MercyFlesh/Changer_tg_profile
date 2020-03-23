from telethon import TelegramClient, sync, errors
from telethon.tl.functions.account import UpdateProfileRequest
from telethon.tl.functions.photos import UploadProfilePhotoRequest, DeletePhotosRequest
from config import *
import datetime
import time_util
import image_util
import time


def main():
    previous_time = None
    with TelegramClient(session_name,  API_ID, API_HASH) as client:
        while True:
            try:
                curr_time = time_util.get_time()
                if previous_time != curr_time:
                    previous_time = curr_time
                    temp = time_util.time_progress()
                    image_util.draw_time(curr_time)
                    
                    client(UpdateProfileRequest(about=temp))
                    
                    image = client.upload_file(time_av)
                    client(DeletePhotosRequest(client.get_profile_photos('me')))
                    client(UploadProfilePhotoRequest(image))
            except errors.FloodWaitError as er:
                print('Flood wait for ', er.seconds)
                time.sleep(int(er.seconds))


if __name__ == "__main__":
    main()