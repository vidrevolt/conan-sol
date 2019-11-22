#include <iostream>

// Sol (OSC)
#include <sol/sol.hpp>

int main() {
    sol::state lua;
    int x = 0;
    lua.set_function("beep", [&x]{ ++x; });
    lua.script("beep()");

    if (x != 1) {
        return 1;
    }

    sol::function beep = lua["beep"];
    beep();
    if (x != 2) {
        return 1;
    }

    return 0;
}
