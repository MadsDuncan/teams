#!/usr/bin/env python3

import sys
import random
from math import ceil
from typing import List
from random import shuffle
from dataclasses import dataclass
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIntValidator


team_names = (
    "Team Mis Mis",
    "The A Team",
    "Gone With the Win",
    "Team Awesome",
    "Team Beer Belly",
    "Victorious Secret",
    "The Bench Warmers",
    "Team Scrambled Legs",
    "Team Broflakes",
)


@dataclass
class Team:
    name: str
    players: List[str]


def generate_teams(no_teams: int, players: List[str]) -> List[Team]:
    global team_names
    random_team_names = list(team_names)
    random_players = players[:]
    shuffle(random_team_names)
    shuffle(random_players)

    teams = []
    team_size = ceil(len(players) / no_teams)

    for i in range(no_teams):
        teams.append(Team(f"{i + 1}) " + random_team_names[i], []))

        for __ in range(team_size):
            if random_players:
                teams[i].players.append(random_players.pop(0))                

    return teams


def gui():
    def btn_clicked():
        input_teams = int(teams_number_field.text())
        input_players = input_box.toPlainText().splitlines()
        teams = generate_teams(input_teams, input_players)

        output_str = ""

        for t in teams:
            output_str += f"{t.name}:\n"

            for i, p in enumerate(t.players):
                output_str += p

                if i != len(t.players) - 1:
                    output_str += ", "

            output_str += "\n\n"

        output_box.setPlainText(output_str)
        output_box.show()

    app = QApplication([])

    teams_number_label = QLabel("Number of teams")
    teams_number_field = QLineEdit()
    teams_number_field.setValidator(QIntValidator(1, 9))
    teams_number_layout = QHBoxLayout()
    teams_number_layout.addWidget(teams_number_label)
    teams_number_layout.addWidget(teams_number_field)

    btn = QPushButton("Generate!")
    btn.clicked.connect(btn_clicked)

    input_box = QPlainTextEdit()
    top_left_layout = QVBoxLayout()
    top_left_layout.addWidget(input_box)
    top_left_layout.addLayout(teams_number_layout)

    output_box = QPlainTextEdit()
    output_box.setReadOnly(True)
    top_layout = QHBoxLayout()
    top_layout.addLayout(top_left_layout)
    top_layout.addWidget(output_box)

    layout = QVBoxLayout()
    layout.addLayout(top_layout)
    layout.addLayout(teams_number_layout)
    layout.addWidget(btn)

    window = QWidget()
    window.setWindowTitle("Generate teams")
    window.setLayout(layout)
    window.show()

    app.exec_()


if __name__ == "__main__":
    gui()
