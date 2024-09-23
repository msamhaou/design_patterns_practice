#pragma once
#include <iostream>

//Target
class Iweapon{
public:
    virtual ~Iweapon() = default;
    virtual void attack() = 0;
};

class Sword : public Iweapon {
public:
    ~Sword() override = default;
    void attack() override;
};

class Hammer : public Iweapon {
public:
    ~Hammer() override = default;
    void attack() override;
};




