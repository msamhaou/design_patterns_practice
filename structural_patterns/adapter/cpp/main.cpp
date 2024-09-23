#include "adapter.hpp"
#include "Spells.hpp"
#include "weapon.hpp"
int main(){
    Sword s = Sword();
    Fireball spell = Fireball();
    SpellAdapter swordtoFire = SpellAdapter(spell);
    swordtoFire.attack();
}