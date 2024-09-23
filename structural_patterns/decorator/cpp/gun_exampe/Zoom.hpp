#pragma once
#include "Decorator.hpp"

class OpticalZoom: public Decorator
{
private:
    int zoom_percent;
public:
    OpticalZoom(BaseGun * g);
    ~OpticalZoom();
    int zoom() override;
};