all: main

circle: Circle.hpp Circle.cpp
	g++ -c Circle.cpp

main: Main.cpp Circle.o
	g++ -o josephus Main.cpp Circle.o
