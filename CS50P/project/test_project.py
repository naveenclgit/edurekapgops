import pytest
import csv
import os
import random
from project import read_players_from_csv, read_parents_from_csv, distribute_players


@pytest.fixture
def csv_filenamea(tmp_path):
    csv_file = tmp_path / "playerstest.csv"
    with open(csv_file, "w") as f:
        writer = csv.writer(f)
        writer.writerow(["Alice", "Bob", "Charlie"])
    return csv_file

def test_read_players_from_csv(csv_filenamea):
    expected_players = ["Alice", "Bob", "Charlie"]
    players = read_players_from_csv(csv_filenamea)
    assert players == expected_players

def test_read_players_from_empty_csv(csv_filenamea):
    with open(csv_filenamea, "w") as f:
        pass  # Empty file
    players = read_players_from_csv(csv_filenamea)
    assert players == []

def test_read_players_from_nonexistent_csv():
    with pytest.raises(FileNotFoundError):
        read_players_from_csv("nonexistent.csv")

@pytest.fixture
def csv_filenameb(tmp_path):
    csv_file = tmp_path / "parentstest.csv"
    with open(csv_file, "w") as f:
        writer = csv.writer(f)
        writer.writerow(["naveencl@gmail.com", "naveencl@hotmail.com"])
    return csv_file

def test_read_parents_from_csv(csv_filenameb):
    expected_players = ["naveencl@gmail.com", "naveencl@hotmail.com"]
    players = read_parents_from_csv(csv_filenameb)
    assert players == expected_players

def test_read_players_from_empty_csv(csv_filenameb):
    with open(csv_filenameb, "w") as f:
        pass  # Empty file
    players = read_players_from_csv(csv_filenameb)
    assert players == []

def test_read_players_from_nonexistent_csv():
    with pytest.raises(FileNotFoundError):
        read_players_from_csv("nonexistent.csv")


def test_distribute_players_even_date():
    players = list(range(22))
    team1, team2 = distribute_players(players, False)
    assert len(team1) == 11
    assert len(team2) == 11
    assert set(team1 + team2) == set(players)

def test_distribute_players_odd_date():
    players = list(range(22))
    team1, team2 = distribute_players(players, True)
    assert len(team1) == 11
    assert len(team2) == 11
    assert set(team1 + team2) == set(players)

def test_distribute_players_different_length_input():
    players = list(range(15))
    with pytest.raises(IndexError):
        distribute_players(players, False)

def test_distribute_players_odd_date_swap():
    players = list(range(22))
    team1, team2 = distribute_players(players, True)
    team1_swapped, team2_swapped = distribute_players(players, False)
    assert team1 == team2_swapped
    assert team2 == team1_swapped
