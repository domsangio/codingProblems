//
//  Circle.hpp
//  JosephusProblem
//
//  Created by Domenic SanGiovanni on 5/30/20.
//  Copyright © 2020 Domenic SanGiovanni. All rights reserved.
//

#ifndef Circle_hpp
#define Circle_hpp

#include <stdio.h>
#include <iostream>
#include <vector>
using namespace std;

class Circle {
private:
    vector<bool> circle;
    int size;
    
    int kill_next(int index);
    int num_left();

    
public:
    Circle(int size);
    int execute();
    int last_alive();
    void print();
};




#endif /* Circle_hpp */
