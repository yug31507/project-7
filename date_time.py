import datetime
import time

def display_current_datetime():
    now = datetime.datetime.now()

    print("Current Date & Time:", now)
    print("=========================================")


def calculate_date_difference():
    s_date = input("Enter start date and time (DD-MM-YYYY HH:MM:SS): " )

    e_date = input( "Enter end date and time (DD-MM-YYYY HH:MM:SS): " )

    s_date = datetime.datetime.strptime(
        s_date,
        "%d-%m-%Y %H:%M:%S"
    )


    e_date = datetime.datetime.strptime(
        e_date,
        "%d-%m-%Y %H:%M:%S"
    )


    diff = e_date - s_date
    print("Difference:", abs(diff))
    print("===================================")


def format_date():
    date = input("Enter date and time (YYYY-MM-DD): " )

    custom_date = datetime.datetime.strptime(
        date,"%Y-%m-%d"
    )

    print("Custom Format:", custom_date.strftime("%d-%m-%Y"))
    print("========================================================")


def stopwatch():
    input("Press Enter to start the stopwatch...")
    start = time.time()
    input("Press Enter to stop the stopwatch...")


    end = time.time()
    difference = end - start
    print(f"Time elapsed: {difference:.4f} seconds")

    print("=========================================")




def countdown_timer():
    seconds = int(input("enter countdown second"))

    while seconds > 0:
        print(seconds)
        time.sleep(1)
        seconds -= 1


    print("Time up!")
    print("============================================")
