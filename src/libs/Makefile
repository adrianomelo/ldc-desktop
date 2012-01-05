LIBS_PATH=$(PWD)/../../bin

export CFLAGS=-g -Wall -fPIC -I $(PWD)/core/libsrc -I/usr/include/dbus-1.0 -I/usr/lib/dbus-1.0/include
export LDFLAGS=-g -Wall -L $(LIBS_PATH) -lhd -lhal -lldc_core

export OUTPUT_PATH=$(LIBS_PATH)

all:
	@for i in `echo *`; do \
		if [ -d $$i ]; then \
			if [ -f $$i/Makefile ]; then \
				(cd $$i; make all) \
			fi; \
		fi; \
	done

bin:
	@for i in `echo *`; do \
		if [ -d $$i ]; then \
			if [ -f $$i/Makefile ]; then \
				(cd $$i; make bin) \
			fi; \
		fi; \
	done

lib:
	@for i in `echo *`; do \
		if [ -d $$i ]; then \
			if [ -f $$i/Makefile ]; then \
				(cd $$i; make lib) \
			fi; \
		fi; \
	done

run:
	@for i in `echo *`; do \
		if [ -d $$i ]; then \
			if [ -f $$i/Makefile ]; then \
				(make -C $$i run) \
			fi; \
		fi; \
	done

clean:
	@for i in `echo *`; do \
		if [ -d $$i ]; then \
			if [ -f $$i/Makefile ]; then \
				(cd $$i; make clean) \
			fi; \
		fi; \
	done

ui:
	@for i in `echo *`; do \
		if [ -d $$i ]; then \
			if [ -f $$i/Makefile ]; then \
				(cd $$i; make ui) \
			fi; \
		fi; \
	done
