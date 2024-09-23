#pragma once
#include <iostream>

class Spell{
public:
    virtual ~Spell() = default;
    virtual void cast() = 0;
};

class Fireball: public Spell{
public:
    ~Fireball() override = default;
    void cast() override;
};