#include "coffee.hpp"

int main(){
    SimpleCoffee *coffee =new  SimpleCoffee();
    Sugar milk = Sugar(coffee);
    std::cout << milk.cost() <<" " << milk.description() << std::endl;
}