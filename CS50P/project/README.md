Community Kids Soccer Training Weekly Team assignments

# Community Kids Soccer Training Weekly Team assignments
#### Video Demo:  https://youtu.be/kK7P19WvzUM
#### Description:
This script generates team assignments  from 22 player names listed in CSV file.
This is used to generate differnet teams every week, our of group of 22 community kids. Local Kids Soccer coaches uses it to generate mix and match kids for every weekend match, and emails parents with the team assignment. This helps parents to get the kids ready in respective jersy and attire as predefiend for team. (there are only  Team 1 - home and Team 2 - away jersy)


##### Applicaiton Features
1. Following are the functions in this module
    - read_players_from_csv(filename)
        > Accepts input file and reads each player names to a list
    - read_parents_from_csv(filename)
        > Accepts input file and reads each parents email to a list
    - distribute_players(players, is_odd_date)
        > Distribute players to two teams 11 each for the game
    - write_teams_to_file(team1, team2, filename)
        > Write team assignments to output file
    - send_email(subject, message, recipients)
        > Send emails to parents email ids,
        > Configure the parameters - email, password, server
    - shuffle_file(indata, outfile):
        > This function shuffles the data in the list and saves the file.
        > The saved file to be used for next weeks game, so that the team is newly set every week.



##### Files:
+ project.py
    > Main project file
+ test_project.py
    > Pytest File
+  requirements.txt
    > Any pip-installable libraries  - None
+ parents.csv
    > Email list of parents - csv format
+ players.csv
    > List of players
+ players.csv2023-08-19
    > Sample schuffled list
+ team_assignments.txt
    > Team assingment output
+ README.md
    > This file.
