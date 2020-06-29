#!/bin/bash
# simple script menu
function tesschi {
clear
sudo apt install tesseract-ocr tesseract-ocr-chi-tra
}
function penv {
clear
sudo apt install python3 python3-venv python3-dev build-essential
python3 -m venv venv
}
function pipir {
clear
pip install -r reqirement.txt
}
function menu {
clear
echo
echo -e "\t\t\ MENU of Install Requirements \n"
echo -e "\t1. Install Tesseract"
echo -e "\t2. Python Virtual Enviroment"
echo -e "\t3. PIP Reqirements"
echo -e "\t0. Exit menu\n\n"
echo -en "\t\tEnter an option: "
read -n 1 option
}
while [ 1 ]
do
menu
case $option in
0)
break ;;
1)
tesschi ;;
2)
penv ;;
3)
pipir ;;
*)
clear
echo "Sorry, wrong selection" ;;
esac
echo -en "\n\n\t\t\tHit any key to continue"
read -n 1 line
done
clear