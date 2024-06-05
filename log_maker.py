import datetime
import time

my_date = datetime.date.today()
formatted_date = my_date.strftime("%Y-%m-%d")

class Console:

    def __init__(self) -> None:
        pass

    def logInfo(self,msg):
        print(f"🎯💡 [INFO] {formatted_date} -- {time.strftime('%H:%M:%S')} -- {msg}")    

    def logError(self,msg):
        print(f"🎯🚨 [ERROR] {formatted_date} -- {time.strftime('%H:%M:%S')} -- {msg}")    

    def log(self,msg):
        print(f"🎯🙋‍♂️ [CUSTOM] {formatted_date} -- {time.strftime('%H:%M:%S')} -- {msg}")    