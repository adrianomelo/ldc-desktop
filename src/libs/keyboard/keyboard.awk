BEGIN {result = ""; openBlock = 0; shouldPrint = 0};
{
	if (/Section "InputDevice"/) {
		openBlock = 1;
	} else if (/EndSection/) {
		openBlock = 0;
		result = sprintf("%s %s", result, $0);

		if (shouldPrint == 1) {
			shouldPrint = 0;
			print result
		} else {
			result = sprintf("");
		}

	} else if (/Option.*"Xkb.*/) {
		shouldPrint = 1;
	}

	if (openBlock == 1) {
		result = sprintf("%s %s\n", result, $0);
	}
}
