#!/usr/bin/python

import sys

current_key = None
trip_count = 0
current_num_passengers = 0
current_total_time = 0
current_total_distance = 0
current_total_amount = 0
current_total_toll = 0
current_total_tips = 0
current_cash_payments = 0
current_card_payments = 0


def emit():
    print "%s\t%d,%d,%d,%d,%d,%d,%d,%d,%d" % (current_key, trip_count, current_num_passengers, current_total_time,
                                              current_total_distance, current_total_amount, current_total_toll,
                                              current_total_tips, current_cash_payments, current_card_payments,
                                              )


print "pickup_date,medallion\ttotal_trips,total_passengers_driven,total_time_driven,total_distance,total_amount," \
      "total_toll_paid,total_tips_collected,total_cash_payments_received,total_card_payments_received"

# input comes from STDIN (stream data that goes to the program)
for line in sys.stdin:

    key, values = line.strip().split("\t", 1)
    values = values.strip().split(',', 6)
    payment = values[-1]
    try:
        values = list(map(int, values[:-1]))
    except ValueError:
        continue
    if len(values) != 6:
        continue
    if key == current_key:
        trip_count += 1
        current_num_passengers += values[0]
        current_total_time += values[1]
        current_total_distance += values[2]
        current_total_amount += values[3]
        current_total_toll += values[4]
        current_total_tips += values[5]
        if "CSH" in payment:
            current_cash_payments += 1
        if "CRD" in payment:
            current_card_payments += 1
    else:
        if current_key:
            emit()
        current_key = key
        trip_count = 1
        current_num_passengers = values[0]
        current_total_time = values[1]
        current_total_distance = values[2]
        current_total_amount = values[3]
        current_total_toll = values[4]
        current_total_tips = values[5]
        if "CSH" in payment:
            current_cash_payments = 1
        if "CRD" in payment:
            current_card_payments = 1

emit()
