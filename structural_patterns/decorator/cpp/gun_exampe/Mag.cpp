#include "Mag.hpp"

Mag::Mag(BaseGun * g) : Decorator(g){
}

Mag::~Mag(){}

int Mag::magazine(){
    return this->gun->magazine() + this->mag_extend;
}