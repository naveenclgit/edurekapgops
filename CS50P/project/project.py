#CS50P Final Proejct by Naveen Calappurackal naveencl@gmail.com
#from California, Mountain House.

import csv
import datetime
import random
import smtplib
import datetime
import sys
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText



def main():

    if len(sys.argv) < 3:
        sys.exit("Usage: ./project.py players.csv parentsemail.csv")

    input_filename = sys.argv[1]
    email_filename = sys.argv[2]
    output_filename = "team_assignments.txt"

    players = read_players_from_csv(input_filename)

    current_date = datetime.date.today().day
    is_odd_date = current_date % 2 != 0
    todays = str(datetime.date.today())

    team1, team2 = distribute_players(players, is_odd_date)

    write_teams_to_file(team1, team2, output_filename)
    print(f"Team assignments written to, {output_filename}")

    outfilename = input_filename + todays
    shuffle_file(players, outfilename)

    recipients = read_parents_from_csv(email_filename)
    subject = "Teams for match day: " + str(datetime.date.today())
    message = "Teams have been formed. Please check the attached file."

    send_email(subject, message, recipients)
    print(subject, message, recipients)




def read_players_from_csv(filename):
    """
    Read player names from CSV file given as input and
    add them to a list called players to be returned
    """

    players = []
    with open(filename, "r") as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            players.extend(row)
    return players


def read_parents_from_csv(filename):
    """
    Read parents emails from CSV file given as input and
    add them to a list called parents to be returned
    """

    parents = []
    with open(filename, "r") as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            parents.extend(row)
    return parents



def distribute_players(players, is_odd_date):
    """
    Distribute players to two teams 11 each for the game
    """
    if len(players) != 22:
        raise IndexError

    team1 = players[:11]
    team2 = players[11:]
    if is_odd_date:
        team1, team2 = team2, team1  # Swap teams if it's an odd date
    return team1, team2



def write_teams_to_file(team1, team2, filename):
    """
    Write team assignments to output file
    """

    with open(filename, "w") as output_file:
        output_file.write("Team 1:\n")
        for player in team1:
            output_file.write(player + "\n")

        output_file.write("\nTeam 2:\n")
        for player in team2:
            output_file.write(player + "\n")


def send_email(subject, message, recipients):
    """
    Send emails to parents email ids,
    Configure the parameters for email access password is masked
    """
    email = "youremail@gmail.com"
    password = "yourpassword"
    

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email, password)

    for recipient in recipients:
        msg = MIMEMultipart()
        msg["From"] = email
        msg["To"] = recipient
        msg["Subject"] = subject
        msg.attach(MIMEText(message, "plain"))
        server.sendmail(email, recipient, msg.as_string())

    server.quit()


def shuffle_file(indata, outfile):
    """
    This function shuffles the data in the list and saves the file.
    The saved file to be used for next weeks game, so that the team is newly set every week.
    """

    shuffled_list = sorted(indata, key=lambda x: random.random())
    print(shuffled_list)

    with open(outfile, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows([shuffled_list])

    print(f"CSV file shuffled and saved as : {outfile}.  Use this file next week")



if __name__ == "__main__":
    main()
