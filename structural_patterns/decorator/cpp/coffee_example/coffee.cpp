#include "coffee.hpp"

CoffeBase::~CoffeBase(){}
double SimpleCoffee::cost(){
    return 1.0;
}

std::string SimpleCoffee::description(){
    return "Simple Coffee";
}

CoffeeDecorator::CoffeeDecorator(CoffeBase * c){
    this->coffee = c;
}

CoffeeDecorator::~CoffeeDecorator(){
    delete this->coffee;
}

Milk::Milk(CoffeBase * c) : CoffeeDecorator(c){}

double Milk::cost(){
    return this->coffee->cost() + 0.5;
}

std::string Milk::description(){
    return this->coffee->description() + ", Milk";
}

Sugar::Sugar(CoffeBase * c) : CoffeeDecorator(c){}
double Sugar::cost(){
    return this->coffee->cost() + 0.2;
}

std::string Sugar::description(){
    return this->coffee->description() + ", sugar";
}