//ADAPTER
#pragma once
#include <iostream>
#include "weapon.hpp"
#include "Spells.hpp"

class SpellAdapter : public Iweapon{
    Spell *spell;
public:
    SpellAdapter(Spell &spell);
    void attack() override;
};