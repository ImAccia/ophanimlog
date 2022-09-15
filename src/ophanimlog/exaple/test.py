import ophanimlog
import time
from datetime import datetime

stamp = time.time()
dt_obj = datetime.fromtimestamp(stamp).strftime('%d-%m-%y')
ophanimlog.log(path=f"log{str(dt_obj)}.txt")