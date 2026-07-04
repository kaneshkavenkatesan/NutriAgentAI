from time import sleep

from scheduler import scheduler

print("===================================")
print(" NutriAgent AI Reminder Worker")
print(" Worker Started Successfully")
print("===================================")

try:
    while True:
        sleep(60)
except (KeyboardInterrupt, SystemExit):
    scheduler.shutdown()