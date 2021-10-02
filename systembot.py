import os
import time
print()

print("\tWELCOME TO SYSTEM BOT")

print()
while True:
    cmd = input("what do you want to do? ")
    print()
    if ("execute" in cmd or "launch" in cmd or "open" in cmd) and ("notepad" in cmd or "editor" in cmd):
        if "don't" in cmd or "do not" in cmd:
            print("okay")
        else:
            os.system("notepad")
    elif ("execute" in cmd or "launch" in cmd or "open" in cmd or "surf" in cmd) and ("brave" in cmd or "browser" in cmd or "internet" in cmd):
        if "don't" in cmd or "do not" in cmd:
            print("okay")
        else:
            site = input("any particular site you wish to open? ")
            if "no" in site:
                os.system("start brave")
            else:
                os.system(f"start brave {site}")
    elif ("watch" in cmd or "launch" in cmd or "play" in cmd) and ("movies" in cmd or "documentaries" in cmd or "player" in cmd):
        if "don't" in cmd or "do not" in cmd:
            print("okay")
        else:
            os.system("start wmplayer")
    elif ("attend" in cmd or "join" in cmd) and ("meeting" in cmd or "class" in cmd):
        if "don't" in cmd or "do not" in cmd:
            print("okay")
        else:
            os.system("start update")
    elif ("make" in cmd or "build" in cmd or "code") and ("project" in cmd or "program" in cmd or "something" in cmd):
        if "don't" in cmd or "do not" in cmd:
            print("okay")
        else:
            os.system("start pycharm")
    elif ("clip" in cmd or "take" in cmd or "shot" in cmd or "capture") and ("window" in cmd or "screen" in cmd):
        if "don't" in cmd or "do not" in cmd:
            print("okay")
        else:
            os.system("start snippingtool")
    elif("listen" in cmd or "play" in cmd or "launch" in cmd) and ("music" in cmd or "spotify" in cmd):
        if "don't" in cmd or "do not" in cmd:
            print("okay")
        else:
            os.system("start spotify")
    elif cmd.upper() == "Q" or cmd == "nothing":
        print("quitting processes...")
        time.sleep(2)
        break
    else:
        print("sorry, i still don't know what to do with that but i am learning :). please try again or try different "
              "keywords")
        print()
