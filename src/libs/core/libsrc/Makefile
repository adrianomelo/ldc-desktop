include Rules.make

CFLAGS=-g -Wall -fpic
LDFLAGS=-g -Wall -shared -Wl,-soname,lib$(NAME).so.0

LIBRARY_FILE=$(OUTPUT_PATH)/lib$(NAME).so

# Main build types

all: bin lib

bin: $(TEST_OBJS)

lib: enable_fpic $(LIBRARY_FILE)

$(BINARY_FILE): $(OBJS) $(TEST_OBJS)
	$(CC) $(LDFLAGS) -o $(BINARY_FILE) $(OBJS) $(TEST_OBJS)

$(LIBRARY_FILE): $(LIBRARY_FILE).0
	@ln -sf lib$(NAME).so.0 $(LIBRARY_FILE)

$(LIBRARY_FILE).0: $(LIBRARY_FILE).0.0
	@ln -sf lib$(NAME).so.0.0 $(LIBRARY_FILE).0

$(LIBRARY_FILE).0.0: $(OBJS)
	$(CC) $(LDFLAGS) -shared -Wl,-soname,lib$(NAME).so.0 -o $(LIBRARY_FILE).0.0 $(OBJS)

.c.o:
	$(CC) $(FPIC) $(CFLAGS) -c $<

enable_fpic:
	@export FPIC=-fPIC

clean:
	@$(RM) -Rf *.o
