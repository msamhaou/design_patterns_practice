#include "adapter.hpp"

SpellAdapter::SpellAdapter(Spell &spell){
    this->spell = &spell;
}

void SpellAdapter::attack(){
    this->spell->cast();
}