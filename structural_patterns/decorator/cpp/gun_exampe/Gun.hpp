#pragma once
#include <iostream>

class BaseGun {
public:
    virtual ~BaseGun() = default;
    virtual double range() = 0 ;
    virtual double accuracy() = 0;
    virtual int zoom() = 0;
    virtual int magazine() = 0;
};

class SimpleGun : public BaseGun{
public:
    ~SimpleGun();
    double range()override{return 0;};
    double accuracy() override{return 0;};
    int magazine() override {return 10;};
    int zoom() override;
};
//base decorator


