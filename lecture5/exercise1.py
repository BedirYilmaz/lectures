import time

seconds_since_epoch = time.time()

hours_in_a_day = 24
minutes_in_an_hour = 60
seconds_in_a_minute = 60
total_seconds_in_a_day = seconds_in_a_minute * minutes_in_an_hour * hours_in_a_day

hours_since_epoch = seconds_since_epoch // (minutes_in_an_hour * seconds_in_a_minute)
minutes_since_epoch = seconds_since_epoch // (minutes_in_an_hour)

hour_of_day = hours_since_epoch % hours_in_a_day
minute_of_hour = minutes_since_epoch % minutes_in_an_hour
second_of_minute = seconds_since_epoch % seconds_in_a_minute

print(f"{int(hour_of_day)}:{int(minute_of_hour)}:{int(second_of_minute)}")
