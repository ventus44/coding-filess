import time
import datetime
import tkinter as tk

root = tk.Tk

def start_timer(duration):
    time.sleep(duration)

def print_with_dots(text, repetitions, delay):
    for i in range(repetitions):
        print(text, end="")
        for _ in range(3):
            time.sleep(delay)
            print(".", end="", flush=True)
        print("\r", end="", flush=True)

def study_timer():
    daily_goal = int(input("What's your daily study goal (in minutes)? : ")) * 60
    study_duration = 0
    break_duration = 0
    total_study_time = 0
    daily_streak = 0
    total_study_days = 0  # Counter for the total days studied

    while True:
        # Get the current date to check for a new day
        today = datetime.date.today()

        if daily_streak == 0 or daily_streak < today.toordinal():
            # If it's a new day, reset the daily streak and total_study_time
            daily_streak = today.toordinal()
            total_study_time = 0

        # Prompt for study duration
        study_input = input("How long do you want to study for (in minutes)? Type 'stop' to end the session: ")

        if study_input.lower() == "stop":
            break
        else:
            study_duration = int(study_input) * 60
            print_with_dots("Study session begins...", repetitions=3, delay=1)
            start_timer(study_duration)
            total_study_time += study_duration
            print("Study session ended. Total study time so far is {} minutes.".format(total_study_time // 60))

            if total_study_time >= daily_goal:
                print("Congratulations! You've reached your daily study goal.")
                daily_streak = today.toordinal()
                total_study_days += 1  # Increment the total study days counter
                break  # End the loop when the goal is achieved

        # Prompt for break duration
        break_input = input("How long should the breaks be (in minutes)? Type 'stop' to end the session: ")

        if break_input.lower() == "stop":
            break
        else:
            break_duration = int(break_input) * 60
            print_with_dots("Break time...", repetitions=3, delay=1)
            start_timer(break_duration)

    print("Total days studied:", total_study_days)
    print("Thank you for using the study timer. Great work!")

study_timer()
