#!/bin/bash

choice=$(printf "󰐥  Power Off\n󰜉  Restart\n󰒲  Suspend\n󰍃  Log Out\n󰜺  Cancel" | rofi -dmenu -i -theme ~/.config/rofi/power-menu.rasi)

case "$choice" in
    "󰐥  Power Off")
        systemctl poweroff
        ;;
    "󰜉  Restart")
        systemctl reboot
        ;;
    "󰒲  Suspend")
        systemctl suspend
        ;;
    "󰍃  Log Out")
        hyprctl dispatch exit
        ;;
esac
