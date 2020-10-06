//
//  Main.cpp
//  JosephusProblem
//
//  Created by Domenic SanGiovanni on 5/30/20.
//  Copyright © 2020 Domenic SanGiovanni. All rights reserved.
//

#include <stdio.h>
#include <iostream>
#include <vector> 
using namespace std;
#include "Circle.hpp"


int main (int argc, char *argv[]) {
    if (argc != 2) {
        cout << "Error in the program\n";
        return -1;
    } else {
        Circle circ = Circle(atoi(argv[1]));
        circ.execute();
        cout << circ.last_alive() << "\n";
        return 1;
    }
}
