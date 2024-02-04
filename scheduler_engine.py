""" Scheduler Engine: A script for creating, adding and checking schedules."""

import datetime
import os.path
import csv

# List of months for reference
month_list = ["january", "february", "march", "april", "may", "june", "july", "august", "september", "october",
              "november", "december"]


# Function to create a CSV file if it doesn't exist
def create_file():
    if os.path.exists("scheduler.csv"):
        return
    file_path = 'scheduler.csv'
    with open(file_path, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerows([["S.No", "Day", "Month", "Year", "Note"], [0, 0, 0, 0, 0]])


# Function to filter and remove past scheduled entries
def schedule_remover():
    current_day = datetime.date.today().day
    current_month = datetime.date.today().month
    current_year = datetime.date.today().year

    with open('scheduler.csv', 'r') as csvfile:
        csv_reader = list(csv.reader(csvfile))
    for row in csv_reader[2:]:
        if int(row[3]) < current_year:
            csv_reader.remove(row)
        else:
            if int(row[2]) < current_month:
                csv_reader.remove(row)

    return csv_reader


# Function to add a new schedule entry
def add_schedule(day, month, year, note):
    sch_list = schedule_remover()
    sch_list.append([int(sch_list[-1][0]) + 1, day, month, year, note])
    with open("scheduler.csv", 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerows(sch_list)


# Function to check if there is a scheduled note for the current date
def check_schedule():
    day = datetime.date.today().day
    month = datetime.date.today().month
    year = datetime.date.today().year

    with open('scheduler.csv', 'r') as csvfile:
        csv_reader = list(csv.reader(csvfile))
    for row in csv_reader[2:]:
        if row[1] == str(day) and row[2] == str(month) and row[3] == str(year):
            return row[4]

    return "No noted schedule today."


# Create the CSV file if it doesn't exist
create_file()
