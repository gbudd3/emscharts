#!/usr/bin/perl
#

while(<>) {
	if (/"49248733"/) { s/Marold,b/Bob Marold/ }
	if (/"50656215"/) { s/Chloe Cavanaugh/\(\1\)/ }
	if (/"49846917"/) { s/, Cliff Mendham Boro EMT// }
	if (/"50145004"/) { s/harriett zimmerman Dan Wood/harriett zimmerman, Dan Wood/ }
	if (/"50083738"/) { s/Jesse smitth Marlene russel Janet Wood/jesse smith, marlene russell, janet wood/ }
	if (/"50384378"/) { s/Nick Monaghan Barbara Nelson/Nick Monaghan, Barbara Nelson/ }
	print;
}
	
