BEGIN {result = ""; openBlock = 0; shouldPrint = 0; lastVendorName = ""; lastModemName = ""; lastVendorID = ""; lastModemID = ""};
{
	if (/^[abcdef0123456789]+  /) {
		lastVendorID = $1;
		lastVendorName = substr($0, index($0,$2));
	} else if (/^\t[abcdef0123456789]+  .*[M,m]odem.*/) {
		lastModemID = $1;
		lastModemName = substr($0, index($0,$2));

		printf("%s%s:%s:%s:%s\n", result, lastVendorID, lastModemID, lastVendorName, lastModemName);
	}
}
