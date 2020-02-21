from telethon import TelegramClient, sync, errors
from telethon.tl.functions.account import UpdateProfileRequest
from config import *
import datetime
import utils
import time


def main():
    previous_minutes = None
    with TelegramClient(session_name,  API_ID, API_HASH) as client:
        while True:
            try:
                minutes = utils.now_minutes()
                if previous_minutes != minutes:
                    previous_minutes = minutes
                    temp = utils.time_progress()
                    client(UpdateProfileRequest(about=temp))

            except errors.FloodWaitError as er:
                print('Flood wait for ', er.seconds)
                time.sleep(int(er.seconds))


if __name__ == "__main__":
    main()