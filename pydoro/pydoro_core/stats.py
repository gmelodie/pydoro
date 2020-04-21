import time
from datetime import datetime, timezone

class Status():

    def __init__(self, pomo_type):
        # All times are POSIX timestamps
        self.date = datetime.now()
        self.unix_date = datetime.now(timezone.utc)
        self.pauses = 0
        self.pomo_type = pomo_type
        self.configured_time = 
        total

    def start(self):
        self.start_time = time.time() # POSIX timestamp

    def stop(self):
        pass

    def finish(self):
        self.end_time = 
        self.unix_end_time = time.time() # POSIX timestamp
        self.actual_time = 
