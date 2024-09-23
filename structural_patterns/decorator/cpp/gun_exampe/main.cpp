#include "Gun.hpp"
#include "Zoom.hpp"
#include "WoodenHandle.hpp"
#include "Mag.hpp"

int main(){
    SimpleGun *gun = new SimpleGun();
    OpticalZoom *z = new OpticalZoom(gun);
    WoodenHandle *hanndle = new WoodenHandle(gun);
    Mag *mag = new Mag(gun);
    std::cout << z->zoom() << std::endl;
    std::cout << hanndle->accuracy() << std::endl;
    std::cout << mag->magazine() << std::endl;
    delete z;
    delete hanndle;
    delete mag;
    delete gun;
}