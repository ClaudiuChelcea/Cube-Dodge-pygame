# Introduction-In-Informatics-Course
# Chelcea Claudiu-Marian
# Contact at: chelceaclaudiu01@gmail.com

This repository is for the Introduction In Informatics Course from the faculty.

#!/bin/bash


if [[ $1 == "MOUNT" ]]
then
	#calea catre imaginea ce trebuie montata
	cale=$2

	#director auxiliar
	mkdir /home/student/aux

	#loc de montare
	sudo mount -o loop $cale /home/student/aux
	
	#numele imaginii
	NUME_IMAGINE=$(basename $cale | cut -d"." -f1)

	#locul de montare default
	destinatie="/home/student/extracted/$NUME_IMAGINE"

	#conditii:
	# 1.nu primim argumente
	if [[ $3 == "" ]]
	then
		sudo cp -r /home/student/aux $destinatie
		sudo umount /home/student/aux
		sudo rm -rf /home/student/aux
	fi

	# 2.primim doar destinatie
	if [[ ($3 == "--destination" || $3 == "-destination")  && $5 == "" ]]
	then
		destinatie=$4
		sudo cp -r /home/student/aux $destinatie
		sudo umount /home/student/aux
		sudo rm -rf /home/student/aux
	fi
	
	# 3.primim destinatie si directoare
	if [[ ($3 == "--destination" || $3 == "-destination") && $5 != "" ]]
	then
		destinatie=$4
		j=1
		while [[ $(echo $5 | cut -d"=" -f2 | cut -d" " -f$j) ]]
		do
			sudo cp -r /home/student/aux/$(echo $5 | cut -d"=" -f2 | cut -d" " -f$j) $destinatie
			let j="j+1"
		done
		sudo umount /home/student/aux
		sudo rm -rf /home/student/aux
	fi

	# 4.primim intai directoare si apoi destinatie
	if [[ ($3 != "--destination" && $3 != "-destination" && $3 != "" && ($4 ==  "-destination" || $4 == "--destination")  ]] 
	then
		destinatie=$5
		k=1
		while [[ $(echo $3 | cut -d"=" -f2 | cut -d" " -f$k) ]]
		do
			sudo cp -r /home/student/aux/$(echo $3 | cut -d"=" -f2 |  cut -d" " -f$k) $destinatie
			let k="k+1"
		done
		sudo unmount /home/student/aux
		sudo rm -rf /home/student/aux
	fi
	
	# 5.primim doar directoare
	if [[ $3 != "--destination" && $3 == "-destination" && $3 != "" && $4 ==  "" ]]
	then
		i=1
		while [[ $(echo $3 | cut -d"=" -f2 | cut -d" " -f$i) ]]
		do
			sudo cp -r /home/student/aux/$(echo $3 | cut -d"=" -f2 | cut -d" " -f$i) $destinatie
			let i="i+1"
		done
		sudo umount /home/student/aux
		sudo rm -rf /home/student/aux
	
	fi
elif [[ $1 == "CREATE" ]]
then
	genisoimage -o $3 $2
fi
