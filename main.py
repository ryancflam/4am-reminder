from datetime import datetime
from pathlib import Path
from time import sleep

from playsound import playsound

path = str(Path(__file__).parent.resolve()).replace("\\", "/")


def main():
    while True:
        sleep(1)
        time = datetime.now().time()
        if time.hour == 4 and time.minute == 0 and time.second == 0:
            print("The time is 4AM!")
            playsound(path + "/assets/reminder.mp3")


if __name__ == "__main__":
    main()
