import time
import csv

from datetime import datetime, timezone


class StatsEntry():
    def __init__(self, ptype='WORK', configured_time=25*60):
        self.date = datetime.now(timezone.utc)
        # All times are POSIX timestamps
        self.start_time = None
        self.end_time = None
        self.actual_time = None
        if ptype is not 'WORK':
            self.pauses = 0
        self.ptype = ptype
        self.configured_time = configured_time

    def start(self):
        if not self.start_time: # first call to start
            self.start_time = time.time()

    def pause(self):
        pauses += 1

    def finish(self):
        self.end_time = time.time()
        self.actual_time = self.end_time - self.start_time

    def save(self):
        confdir = os.environ.get(
            "PYDORO_PATH", os.path.expanduser("~/.pydoro/")
        )
        filename = confdir + 'stats.csv'
        with open(filename, 'a') as statsfp:
            writer = csv.writer(statsfp, delimiter=',', \
                                quotechar='"', \
                                quoting=csv.QUOTE_MINIMAL)
            writer.writerow([self.date, self.start_time, \
                             self.end_time, self.pauses, \
                             self.ptype, \
                             self.configured_time, \
                             self.actual_time])

