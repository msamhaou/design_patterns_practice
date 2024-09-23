#pragma once
#include "Gun.hpp"

class Decorator : public BaseGun
{
protected:
    BaseGun * gun;
public:
    Decorator(BaseGun * g);
    int zoom() override{return 0;}
    double range() override{return 0;};
    double accuracy() override{return 0;};
    int magazine() override {return 0;};
    virtual ~Decorator();

};
