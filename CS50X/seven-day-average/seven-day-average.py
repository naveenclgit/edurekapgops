import csv
import requests


def main():
    # Read NYTimes Covid Database
    download = requests.get(
        "https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-states.csv"
    )
    decoded_content = download.content.decode("utf-8")
    file = decoded_content.splitlines()
    reader = csv.DictReader(file)

    # Construct 14 day lists of new cases for each states
    new_cases = calculate(reader)
    #print(new_cases)

    # Create a list to store selected states
    states = []
    print("Choose one or more states to view average COVID cases.")
    print("Press enter when done.\n")

    while True:
        state = input("State: ")
        if state in new_cases:
            states.append(state)
        if len(state) == 0:
            break

    print(f"\nSeven-Day Averages")

    # Print out 7-day averages for this week vs last week
    comparative_averages(new_cases, states)


# TODO: Create a dictionary to store 14 most recent days of new cases by state
def calculate(reader):

    #print(reader)
    new_cases = dict()
    old_cases = dict()

    for row in reader :
        state = row["state"]
        date = row["date"]
        cases = int(row["cases"])
        new_case = cases
        if state not in old_cases:
            old_cases[state] = cases
            new_cases[state] = []
        else:
            new_case = cases - old_cases[state]
            old_cases[state] = cases

        if state not in new_cases:
            new_cases[state] = []
        if len(new_cases[state]) >= 14:
            new_cases[state].pop(0)
        new_cases[state].append(new_case)
    return new_cases


# TODO: Calculate and print out seven day average for given state
def comparative_averages(new_cases, states):
    for state in states:
        recent_cases = new_cases[state][7:]
        lastweek_cases = new_cases[state][:7]
        avg_recent = sum(recent_cases)/7
        avg_old = sum(lastweek_cases)/7
        diff = avg_recent - avg_old
        if diff > 0:
            msg = "Increased"
        else:
            msg = "Decreased"

        try:
            d= diff / avg_old
            p = round(d * 100,2)
        except ZeroDivisionError:
            raise ZeroDivisionError

        print(f"{state} has a 7 day average of {avg_recent} and {msg} by {p}")



main()
