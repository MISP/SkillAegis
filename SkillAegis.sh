#!/bin/bash

APP_MAIN="Main"
APP_EDITOR="Editor"
APP_DASHBOARD="Dashboard"
SESSION="SkillAegis"

screen -dmS $SESSION

screen -S $SESSION -X screen -t "$APP_MAIN" bash -c "python3 app.py; read x;"
screen -S $SESSION -X screen -t "$APP_EDITOR" bash -c "cd SkillAegis-Editor && bash start.sh; read x;"
screen -S $SESSION -X screen -t "$APP_DASHBOARD" bash -c "cd SkillAegis-Dashboard && bash start.sh; read x;"

screen -r $SESSION
