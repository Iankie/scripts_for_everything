#!/bin/bash

print_help() {
	echo -e "Usage: $0 -m (int|ext) /path/to/crate\n"
	echo "Options:"
	echo "	-h	Print this help page and exit"
	echo "	-m	Mode. Can be int (internal) or ext (external)"
	echo "	-o	Open directory in VScode (if exists)"

}

if [ $# -eq 0 ]; then
	print_help
	exit 1
fi

while getopts ":m:h:o" opt;do
	case $opt in
		m)
			mode=$OPTARG
			;;
		h)
			print_help
			exit 0
			;;
		
		o)
			code ${!#}
			;;

		\?)
			echo "Wrong arg for -$OPTARG" >&2
			print_help
			exit 1
			;;
		:)
			echo -e "Missing arg after -$OPTARG \n" >&2
			print_help
			exit 1
	esac
done

shift $((OPTIND -1))

if [ "$mode" != "ext" ] && [ "$mode" != "int" ]; then 
	echo "Wrong mode value. Mode can be 'ext' or 'int'." >&2
	exit 1
fi

if [ $# -ne 1 ]; then 
	echo "Missing path." >&2
	print_help
	exit 1
fi

if [ "$mode" == "ext" ]; then 
	
	mkdir -p "$1/recon"
	mkdir -p "$1/recon/passive"
	mkdir -p "$1/recon/active"
	mkdir -p "$1/recon/screens"
	mkdir -p "$1/handle_check"
	mkdir -p "$1/handle_check/PoCs_check"
	mkdir -p "$1/handle_check/burp_files"
	mkdir -p "$1/handle_check/screens"
	touch $1/notes.txt
	touch $1/to_do.txt

	echo "Made extFS in $(realpath $1 | rev | cut -d '/' -f1 | rev) dir!"

	tree $1

elif [ "$mode" == "int" ]; then
	
	echo "In Progress..."

	#echo "Made intFS in $(realpath $1 | rev | cut -d '/' -f1 | rev) dir!"

fi

exit 0