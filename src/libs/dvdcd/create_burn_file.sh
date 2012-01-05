TMP_LDC=/var/tmp/LDC
BURN_FILE=ldc_burn_test.tar

mkdir -p $TMP_LDC/mnt
mkdir -p $TMP_LDC

if [ $? == 0 ]; then \
	if [ ! -f $TMP_LDC/$BURN_FILE ]; then \
		tar -cf $TMP_LDC/$BURN_FILE /usr/bin 2> /dev/null
		
		if [ $? == 0 ]; then
			exit 0
		else
			exit 1
		fi
	else
		exit 0
	fi
fi
