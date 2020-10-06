//
//  Circle.cpp
//  JosephusProblem
//
//  Created by Domenic SanGiovanni on 5/30/20.
//  Copyright © 2020 Domenic SanGiovanni. All rights reserved.
//

#include <vector>
#include "Circle.hpp"
using namespace std;

    
Circle::Circle(int n) :
    size(n), circle(n, true) {}

void Circle::print() {
    cout << "Circle\n";
    for (int i = 0; i < circle.size(); i++) {
        cout << circle[i] << " ";
    }
    cout << "\n";
}
    
int Circle::execute() {
    int index = 0;
    
    while (size > 1) {
        
        // if youre alive, kill next person
        if (circle[index] == true) {
            // kill next person
            index = kill_next(index);
        } else {
            // else find next alive person
            index++;
            if (index == circle.size()) {
                index = 0;
            }
        }
            // print();
    }
    
    return last_alive();
}


// method to kill the next person
int Circle::kill_next(int index) {
    index++;
    if (index >= circle.size()) {
        index = 0;
    }
    
    while (true) {
        // if this persons alive kill them
        if (circle[index] == true) {
            circle[index] = false;
            size --;
            return (index + 1) % circle.size();
        } else {
            index++;
            if (index >= circle.size()) {
                index = 0;
            }
        }
    }
}

// method to find the num left
int Circle::num_left() {
    return size;
}

//method to get the last alive
int Circle::last_alive() {
    if (size != 1) {
        return -1;
    }
    
    for (int i = 0; i < circle.size(); i++) {
        if (circle[i] == true) {
            return i + 1;
        }
    }
}
