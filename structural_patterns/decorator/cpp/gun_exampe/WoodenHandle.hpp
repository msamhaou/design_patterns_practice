#pragma once
#include <iostream>
#include "Decorator.hpp"
#include "Gun.hpp"

class WoodenHandle : public Decorator{
private:
    double _accuracy;
public:
    WoodenHandle(BaseGun * g);
    ~WoodenHandle();
    double accuracy() override;
};