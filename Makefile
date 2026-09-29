CC=gcc
CFLAGS=-std=c11 -Wall -Wextra -Wpedantic -Wconversion -g

Q ?= questions/Q0001_bit_operations

build:
	$(CC) $(CFLAGS) $(Q)/solution.c $(Q)/test.c -o $(Q)/test

run: build
	./$(Q)/test

clean:
	find questions -type f \( -name test -o -name '*.exe' -o -name '*.o' \) -delete
