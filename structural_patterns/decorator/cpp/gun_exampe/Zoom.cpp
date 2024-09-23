#include "Zoom.hpp"

OpticalZoom::OpticalZoom(BaseGun *b) : Decorator(b){
    this->zoom_percent = 20;
}
OpticalZoom::~OpticalZoom(){}

int OpticalZoom::zoom()
{
    return this->gun->zoom() + this->zoom_percent;
}

