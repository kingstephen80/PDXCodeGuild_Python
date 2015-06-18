import time
import datetime


STARTTIME = time.time()


class StopWatch:
    def __init__(self):
        global STARTTIME
        self.ui()

    def starttime(self):
        global STARTTIME
        STARTTIME = time.time()
        return STARTTIME

    def stoptime(self):
        # global ENDTIME
        endtime = time.time()
        return endtime

    def time_between(self, endtime, STARTTIME):
        # global STARTTIME, ENDTIME
        time_between = endtime - STARTTIME
        return time_between()

    def format_time(self, new_time):
        formatted = datetime.datetime.fromtimestamp(new_time).strftime('%Y-%m-%d %H:%M:%S')
        return formatted

    def ui(self):
        global STARTTIME
        while True:
            choice = raw_input( 'Welcome to the stop watch!\n'
                                'Enter a command:\n'
                                '~~~~~~~~~~~~~~~\n'
                                '1 to START!\n'
                                '2 to STOP\n'
                                '3 to quit\n'
                                '>> ')
            if choice == 1:
                STARTTIME = self.starttime()
                self.ui()
            elif choice == 2:
                stop = self.stoptime()
                time_passed = self.time_bewtween(stop, STARTTIME)
                format_timepassed = self.format_time(time_passed)
                print format_timepassed, "has passed."
                raw_input("Press enter to continue...")
                self.ui()
            else:
                print "Thank you for using my stopwatch!"
                exit()


StopWatch()


# Reinas basic example
# class StopWatch(object):
#
#     def start(self):
#         self.start = time.time()
#
#
#     def stop(self):
#         self.end = time.time()
#         print '{} seconds'.format(self.end - self.start)



# stopwatch = StopWatch()
# stopwatch.start()
# stopwatch.stop()
