import datetime
import time

def countdown(event_name, event_date):
    
    event_datetime = datetime.datetime.strptime(event_date, "%Y-%m-%d %H:%M:%S")
    
    time_diff = event_datetime - datetime.datetime.now()
    
    days = time_diff.days
    hours, remainder = divmod(time_diff.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
   
    print(f"Countdown to {event_name}: {days} days, {hours} hours, {minutes} minutes, {seconds} seconds")
    
    
    while time_diff.total_seconds() > 0:
        time.sleep(1)
        time_diff = event_datetime - datetime.datetime.now()
        days = time_diff.days
        hours, remainder = divmod(time_diff.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        print(f"Countdown to {event_name}: {days} days, {hours} hours, {minutes} minutes, {seconds} seconds", end='\r')
    print(f"\n{event_name} has started!")


event_name = "New Year's Eve"
event_date = "2024-12-31 23:59:59"
countdown(event_name, event_date)
