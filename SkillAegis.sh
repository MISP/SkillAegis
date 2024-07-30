#!/bin/bash

CONFIG_FILE="config.json"

function get_config_value() {
    local path=$1
    echo $(jq -r "$path" config.json)
}

usage() {
    echo "Usage: $0 [--scenario_folder <folder>]"
    exit 1
}

PARAM_SCENARIO_FOLDER=""
CONFIG_SCENARIO_FOLDER=$(get_config_value ".main.scenario_folder")

while [ "$#" -gt 0 ]; do
    case "$1" in
        --scenario_folder)
            PARAM_SCENARIO_FOLDER="$2"
            shift 2
            ;;
        *)
            usage
            ;;
    esac
done


SESSION="SkillAegis"


APP_MAIN="Main"
MAIN_HOST=$(get_config_value ".main.host")
MAIN_PORT=$(get_config_value ".main.port")
if [ ! -z "$PARAM_SCENARIO_FOLDER" ]; then
    SCENARIO_FOLDER="$PARAM_SCENARIO_FOLDER"
else
    SCENARIO_FOLDER="$CONFIG_SCENARIO_FOLDER"
fi
SCENARIO_FOLDER_ABSOLUTE=$(realpath "$SCENARIO_FOLDER" 2>/dev/null)

if [ ! -d "$SCENARIO_FOLDER_ABSOLUTE" ]; then
    echo "Error: The folder '$SCENARIO_FOLDER_ABSOLUTE' does not exist."
    exit 1
fi

APP_EDITOR="Editor"
EDITOR_HOST=$(get_config_value ".editor.host")
EDITOR_PORT=$(get_config_value ".editor.port")

APP_DASHBOARD="Dashboard"
DASHBOARD_HOST=$(get_config_value ".dashboard.host")
DASHBOARD_PORT=$(get_config_value ".dashboard.port")

EDITOR_URL=$(get_config_value ".main.editor_url")
DASHBOARD_URL=$(get_config_value ".main.dashboard_url")


screen -dmS $SESSION

screen -S $SESSION -X screen -t "$APP_MAIN" bash -c "python3 app.py --host $MAIN_HOST --port $MAIN_PORT --editor_url $EDITOR_URL --dashboard_url $DASHBOARD_URL; read x;"
screen -S $SESSION -X screen -t "$APP_DASHBOARD" bash -c "cd SkillAegis-Dashboard && bash start.sh --host $DASHBOARD_HOST --port $DASHBOARD_PORT --exercise_folder $SCENARIO_FOLDER_ABSOLUTE; read x;"
screen -S $SESSION -X screen -t "$APP_EDITOR" bash -c "cd SkillAegis-Editor && bash start.sh --host $EDITOR_HOST --port $EDITOR_PORT --exercise_folder $SCENARIO_FOLDER_ABSOLUTE; read x;"

screen -r $SESSION
