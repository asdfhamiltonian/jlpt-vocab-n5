#!/usr/bin/awk -f

BEGIN {
    FS="\t";
}
{
	if (NF == 2) {
		print "{" $1 "#" $2 "}"
	}
	else if (NF == 3) {
		print "{" $1 "#" $2 "\\n" $3 "}"
	}
}
END {}
