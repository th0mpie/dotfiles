#!/bin/bash

# ===== Hoofdmenu =====
show_menu_main() {
    while true; do
        clear
        echo "My Command List"
	echo "========================="
        echo "1) System"
        echo "2) Configuration"
        echo "3) Fun Stuff"
        echo "0) Exit"
        echo "========================="

        read -p "Enter the number of the command to run: " choice

        case $choice in
            1) show_menu_system ;;
            2) show_menu_configuration ;;
            3) show_menu_funstuff ;;
            0) echo "Exiting Menu"; break ;;
            *) echo "Invalid choice."; read -p "Press Enter to continue..." ;;
        esac
    done
}

# ===== Submenu System =====
show_menu_system() {
    while true; do
        clear
        echo "System Commands"
	echo "========================="
        echo "1) Update & Upgrade System"
        echo "2) Clean Package Cache"
        echo "3) List Active Processes"
        echo "4) Show Disk Usage"
        echo "5) Show Memory Usage"
        echo "0) Back"
	echo "========================="

        read -p "Enter the number of the command to run: " choice

        case $choice in
            1) echo "Updating & Upgrading System"
               sudo apt update && sudo apt upgrade -y
               read -p "Press Enter to return to the menu..." ;;
            2) echo "Cleaning Package Cache"
               sudo apt autoremove -y && sudo apt clean
               read -p "Press Enter to return to the menu..." ;;
            3) echo "Listing Active Processes"
               ps aux | less ;;
            4) echo "Showing Disk Usage"
               df -h
               read -p "Press Enter to return to the menu..." ;;
            5) echo "Showing Memory Usage"
               free -h
               read -p "Press Enter to return to the menu..." ;;
            0) break ;;
            *) echo "Invalid choice."; read -p "Press Enter to return to the menu..." ;;
        esac
    done
}

# ===== Submenu Configuration =====
show_menu_configuration() {
    while true; do
        clear
        echo "Configuration"
	echo "========================="
        echo "1) i3"
        echo "2) Alacritty"
        echo "3) .bashrc"
        echo "4) vim"
        echo "5) Edit Command List"
        echo "0) Back"
        echo "========================="

        read -p "Enter the number of the command to run: " choice

        case $choice in
            1) vim ~/.config/i3/config ;;
            2) vim ~/.config/alacritty/alacritty.toml ;;
            3) vim ~/.bashrc ;;
            4) echo "command empty" ;;
            5) vim ~/scripts/my_command_list.sh ;;
            0) break ;;
            *) echo "Invalid choice."; read -p "Press Enter to return to the menu..." ;;
        esac
    done
}

# ===== Submenu Fun Stuff =====
show_menu_funstuff() {
    while true; do
        clear
        echo "Fun Stuff"
	echo "========================="
        echo "1) art"
        echo "2) cava"
        echo "0) Back"
        echo "========================="

        read -p "Enter the number of the command to run: " choice

        case $choice in
            1) echo "command empty" ;;
            2) cava ;;
            0) break ;;
            *) echo "Invalid choice."; read -p "Press Enter to return to the menu..." ;;
        esac
    done
}

# ===== Start het menu =====
show_menu_main
