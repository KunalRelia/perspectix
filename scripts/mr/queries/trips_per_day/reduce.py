#!/usr/bin/python

import sys

current_day = None
current_day_sum = 0
current_day_total_distance = 0
current_day_tips = 0
current_day_toll = 0
current_day_total_amount = 0

# input comes from STDIN (stream data that goes to the program)
for line in sys.stdin:

    day, val = line.strip().split("\t", 1)
    values = val.split(",")

    try:
        count = 1
        total_distance = int(values[0])
        tips = int(values[1])
        toll = int(values[2])
        total_amount = int(values[3])

    except ValueError:
        continue

    if day == current_day:
        current_day_sum += count
        current_day_total_distance += total_distance
        current_day_tips += tips
        current_day_toll += toll
        current_day_total_amount += total_amount
    else:
        if current_day:
            print "%s\t%s,%s,%s,%s,%s" % (
                current_day, current_day_sum, current_day_total_distance, current_day_tips, current_day_toll,
                current_day_total_amount)

        current_day = day
        current_day_sum = count
        current_day_total_distance = total_distance
        current_day_tips = tips
        current_day_toll = toll
        current_day_total_amount = total_amount

# prints the following for each day:
# date - total trips, total distance traveled(to see the days when there is a rise/fall),
# total tips collected(to check if holiday season sees generosity),
# total toll paid(to see if certain periods have more visitors across the bridge),
# total amount collected(to see if weekends earn more money or holidays are more fruitful for drivers),
# fare per mile (to see if fares are spiked during holiday season)
print "%s\t%s,%s,%s,%s,%s" % (
    current_day, current_day_sum, current_day_total_distance, current_day_tips, current_day_toll,
    current_day_total_amount)
