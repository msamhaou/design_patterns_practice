#include "WoodenHandle.hpp"

WoodenHandle::WoodenHandle(BaseGun * g): Decorator(g), _accuracy(0.2){

}
WoodenHandle::~WoodenHandle(){}

double WoodenHandle::accuracy(){
    return this->gun->accuracy() + this->_accuracy;
}