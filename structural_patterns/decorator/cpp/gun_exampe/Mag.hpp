#pragma once

#include <iostream>
#include "Decorator.hpp"
#include "Gun.hpp"

class Mag : public Decorator
{
private:
    int mag_extend = 5;
public:
    Mag(BaseGun * g);
    ~Mag();
    int magazine() override;
};