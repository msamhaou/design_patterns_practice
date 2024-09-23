#include <iostream>

//Component interface
class CoffeBase {
public:
    virtual ~CoffeBase();
    virtual double cost() =0;
    virtual std::string description() = 0;
};

//Concrete Component
class SimpleCoffee : public CoffeBase{
public:
    double cost() override;
    std::string description() override;
};

//Decorator base class
class CoffeeDecorator : public CoffeBase{
protected:
    CoffeBase * coffee;
public:
    CoffeeDecorator(CoffeBase * c);
    virtual ~CoffeeDecorator();
};

//Concrete Decorator

class Milk : public CoffeeDecorator{
public:
    Milk(CoffeBase *c);
    double cost() override;
    std::string description() override;
    
};


class Sugar: public CoffeeDecorator{
    public:
    Sugar(CoffeBase * c);
    double cost() override;
    std::string description() override;
};