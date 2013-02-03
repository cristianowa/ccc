CC= gcc
COVER= -coverage
#COVER=-ftest-coverage #I've founded that this option also works 
all: main
	$(CC) main.o $(COVER) -o program
main: main.c
	$(CC) -c main.c $(COVER)
report:
	lcov -c -d ./ -o coverage.info
	lcov --remove coverage.info "/usr*" -o coverage.info
	genhtml coverage.info -o coverage
	firefox coverage/index.html
clean:
	rm *.o *.gcda *.gcno *.info program
	rm -R coverage
