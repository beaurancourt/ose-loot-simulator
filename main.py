from random import randint

num_pcs = 10
xp = 0
treasure = 0
magic_items = {}

def roll(n, size): 
    ret = 0
    while n > 0:
        ret += randint(1, size)
        n -= 1
    return ret

def magic_item(level):
    r = roll(1, 100)
    base = {}
    if level <= 3:
        if r <= 10:
            return {'armor': 1}
        if r <= 15:
            return {'misc': 1}
        if r <= 40:
            return {'potion': 1}
        if r <= 45:
            return {'ring': 1}
        if r <= 50:
            return {'rod': 1}
        if r <= 70:
            return {'scroll': 1}
        if r <= 90:
            return {'sword': 1}
        return {'weapon': 1}
    else:
        if r <= 10:
            return {'armor': 1}
        if r <= 15:
            return {'misc': 1}
        if r <= 35:
            return {'potion': 1}
        if r <= 40:
            return {'ring': 1}
        if r <= 45:
            return {'rod': 1}
        if r <= 75:
            return {'scroll': 1}
        if r <= 95:
            return {'sword': 1}
        return {'weapon': 1}

def merge_magic(a, b):
    new_dict = {}

    for key, value in a.items():
        new_dict[key] = value

    for key, value in b.items():
        new_dict[key] = a.get(key, 0) + value
    return new_dict

def gen_magic(num, level):
    base = {}
    while num > 0:
        base = merge_magic(base, magic_item(level))
        num = num - 1
    return base

def merge_treasure(a, b):
    return {
        'treasure': a.get('treasure', 0) + b.get('treasure', 0),
        'magic': merge_magic(a.get('magic', {}), b.get('magic', {}))
    }

def gem():
    r = roll(1, 20)
    if r <= 4:
        return 10
    if r <= 9:
        return 50
    if r <= 15:
        return 100
    if r <= 19:
        return 500
    return 1000

def gems(num, dice):
    r = roll(num, dice)
    total = 0
    while r > 0:
        total += gem()
        r = r - 1
    return total

def jewels(num, dice):
    r = roll(num, dice)
    total = 0
    while r > 0:
        total += roll(3,6) * 100
        r = r - 1
    return total

def type_a():
    gp = 0
    magic = {}
    if roll(1, 100) <= 25:
        gp += roll(1, 6) * 10
    if roll(1, 100) <= 30:
        gp += roll(1, 6) * 100
    if roll(1, 100) <= 20:
        gp += roll(1, 4) * 500
    if roll(1, 100) <= 35:
        gp += roll(2, 6) * 1000
    if roll(1, 100) <= 25:
        gp += roll(1, 2) * 5000
    if roll(1, 100) <= 50:
        gp += gems(6, 6)
    if roll(1, 100) <= 50:
        gp += jewels(6, 6)
    if roll(1, 100) <= 30:
        magic = gen_magic(3, 1)

    return { 'treasure': gp, 'magic': magic }

def type_b():
    gp = 0
    if roll(1, 100) <= 50:
        gp += roll(1,8) * 10
    if roll(1, 100) <= 25:
        gp += roll(1,6) * 100
    if roll(1, 100) <= 25:
        gp += roll(1,4) * 500
    if roll(1, 100) <= 25:
        gp += roll(1,3) * 1000
    if roll(1, 100) <= 25:
        gp += gems(1, 6)
    if roll(1, 100) <= 25:
        gp += jewels(1, 6)

    magic = {}
    if roll(1, 100) <= 10:
        mroll = roll(1, 100)
        if mroll <= 33:
            magic = {'armor': 1}
        elif mroll <= 66:
            magic = {'sword': 1}
        else:
            magic = {'weapon': 1}

    return { 'treasure': gp, 'magic': magic }

def type_c():
    gp = 0
    if roll(1, 100) <= 20:
        gp += roll(1, 12) * 10
    if roll(1, 100) <= 30:
        gp += roll(1, 4) * 100
    if roll(1, 100) <= 10:
        gp += roll(1, 4) * 500
    if roll(1, 100) <= 25:
        gp += gems(1, 4)
    if roll(1, 100) <= 25:
        gp += jewels(1, 4)

    magic = {}
    if roll(1, 100) <= 10:
        magic = gen_magic(2, 1)

    return { 'treasure': gp, 'magic': magic }

def type_d():
    gp = 0
    if roll(1, 100) <= 10:
        gp += roll(1, 8) * 10
    if roll(1, 100) <= 15:
        gp += roll(1, 12) * 100
    if roll(1, 100) <= 60:
        gp += roll(1, 6) * 1000
    if roll(1, 100) <= 30:
        gp += gems(1, 8)
    if roll(1, 100) <= 30:
        gp += jewels(1, 8)

    magic = {}
    if roll(1, 100) <= 15:
        magic = merge_magic(gen_magic(2, 1), {'potion': 1})

    return { 'treasure': gp, 'magic': magic }

def type_g():
    gp = 0
    if roll(1, 100) <= 50:
        gp += roll(1, 4) * 10000
    if roll(1, 100) <= 50:
        gp += roll(1, 6) * 5000
    if roll(1, 100) <= 25:
        gp += gems(3, 6)
    if roll(1, 100) <= 25:
        gp += jewels(1, 10)

    magic = {}
    if roll(1, 100) <= 35:
        magic = merge_magic(gen_magic(4, 1), {'scroll': 1})

    return { 'treasure': gp, 'magic': magic }

def type_j():
    gp = 0
    if roll(1, 100) <= 25:
        gp += roll(1, 4) * 10
    if roll(1, 100) <= 10:
        gp += roll(1, 3) * 100

    return { 'treasure': gp, 'magic': {} }

def type_l():
    gp = 0
    if roll(1, 100) <= 50:
        gp += gems(1, 4)

    return { 'treasure': gp, 'magic': {} }

def type_p():
    gp = roll(3, 8) / 100

    return { 'treasure': gp, 'magic': {} }

def type_r():
    gp = roll(2, 6) / 2

    return { 'treasure': gp, 'magic': {} }

def type_s():
    gp = roll(2, 4)

    return { 'treasure': gp, 'magic': {} }

def type_u():
    gp = 0
    if roll(1, 100) <= 10:
        gp += roll(1, 100) / 100
    if roll(1, 100) <= 10:
        gp += roll(1, 100) / 10
    if roll(1, 100) <= 5:
        gp += roll(1, 100)
    if roll(1, 100) <= 5:
        gp += gems(1, 4)
    if roll(1, 100) <= 5:
        gp += jewels(1, 4)

    magic = {}
    if roll(1, 100) <= 2:
        magic = magic_item(1)

    return { 'treasure': gp, 'magic': {} }

def type_v():
    gp = 0
    if roll(1, 100) <= 10:
        gp += roll(1, 100) / 10
    if roll(1, 100) <= 5:
        gp += roll(1, 100) / 2
    if roll(1, 100) <= 10:
        gp += roll(1, 100)
    if roll(1, 100) <= 5:
        gp += roll(1, 100) * 500
    if roll(1, 100) <= 10:
        gp += gems(1, 4)
    if roll(1, 100) <= 10:
        gp += jewels(1, 4)

    magic = {}
    if roll(1, 100) <= 5:
        magic = magic_item(1)

    return { 'treasure': gp, 'magic': {} }

def type_uv():
    return merge_treasure(type_u(), type_v())

def nil():
    return {
        'treasure': 0,
        'magic': {}
    }

def multiply_treasure(treasure, multiplier):
    new_treasure = {}
    i = 0
    while (i < multiplier):
        new_treasure = merge_treasure(new_treasure, treasure())
        i = i + 1
    return new_treasure

def gain_magic(loot):
    global magic_items
    magic_items = merge_magic(magic_items, loot)

def gain_treasure(state, level):
    if level == 1:
        gp = roll(1, 6) * 10
        if roll(1, 100) <= 50:
            gp += roll(1, 6) * 10
        if roll(1, 100) <= 5:
            gp += gems(1, 6)
        if roll(1, 100) <= 2:
            gp += jewels(1, 6)

        magic = {}
        if roll(1, 100) <= 2:
            magic = magic_item(1)

        return { 
            'treasure': gp,
            'xp': gp,
            'magic_items': magic
        }

def random_encounter(state, level):
    xp = 0
    r = roll(1, 20)
    tables = [
        [45, 45, 68, 35, 35,
         35, 63, 53, 33, 50,
         100, 50, 55, 75, 46,
         64, 63, 72, 55, 175]
    ]
    xp += tables[level - 1][r-1]

    loot_table = [
        [
            type_u, type_u, nil, nil, nil,
            lambda : multiply_treasure(type_r, 5), nil, type_v, nil,
            lambda : multiply_treasure(type_p, 10),
            nil, nil, nil, nil, nil,
            nil, lambda : multiply_treasure(type_s, 11), nil, type_uv, nil
        ]
    ]
    loot = loot_table[level-1][r-1]()
    xp += loot['treasure']

    return {
        'xp': xp,
        'treasure': loot['treasure'],
        'magic_items': loot['magic']
    }

def monster_lair(state, level):
    r = roll(1, 19)
    xp_table = [
        [
            110, 165, 105, 225, 225,
             165, 113, 105, 165,
             275, 350, 45, 165, 46,
             63, 135, 254, 105, 263
        ]
    ]
    xp = xp_table[level - 1][r-1]

    loot_table = [
        [
            type_u, type_a, nil, type_g, type_c,
            type_c, nil, type_b, nil, type_j,
            type_u, type_d, nil, nil, nil,
            type_u, lambda : multiply_treasure(type_s, 23), type_l,
            type_uv, nil
        ]
    ]
    loot = loot_table[level-1][r-1]()
    xp += loot['treasure']

    return {
        'xp': xp,
        'treasure': loot['treasure'],
        'magic_items': loot['magic']
    }

def merge_state(a, b):
    return {
        'treasure': a['treasure'] + b['treasure'],
        'xp': a['xp'] + b['xp'],
        'magic_items': merge_magic(a['magic_items'], b['magic_items'])
    }

def iteration():
    state = {'xp': 0, 'treasure': 0, 'magic_items': {}}
    while state['xp'] <= num_pcs * 2000:
        room_type = roll(1,6)
        has_treasure = roll(1, 6)
        new_state = {'xp': 0, 'treasure': 0, 'magic_items': {}}
        if room_type <= 2:
            if has_treasure == 1:
                print("empty with treasure")
                new_state = gain_treasure(state, 1)
            else:
                print("empty")
        elif room_type <= 4:
            if has_treasure <= 3:
                print("monster lair")
                new_state = monster_lair(state, 1)
            else:
                print("monster")
                new_state = random_encounter(state, 1)
        elif room_type == 5:
            print("special")
        elif room_type == 6:
            if has_treasure <= 2:
                print("trapped treasure")
                new_state = gain_treasure(state, 1)
            else:
                print("trap")

        print(new_state)
        state = merge_state(state, new_state)

        if roll(1, 6) == 1:
            print("random encounter")
            new_state = random_encounter(state, 1)
            print(new_state)
            state = merge_state(state, new_state)

        print()

    return state

def print_average(state, iterations):
    divisor = iterations * num_pcs
    magic_items = state['magic_items']
    magic_types = [
        'armor', 'misc', 'potion', 'ring', 'rod', 'scroll', 'sword', 'weapon'
    ]
    print('xp', state['xp'] / divisor)
    print('treasure', state['treasure'] / divisor)

    total_magic = 0
    for magic_type in magic_types:
        print(magic_type, magic_items[magic_type] / divisor)
        total_magic += magic_items[magic_type]

    print('total magic', total_magic / divisor)

def main():
    iterations = 10000
    state = {'xp': 0, 'treasure': 0, 'magic_items': {}}
    for _ in range(iterations):
        state = merge_state(state, iteration())
    print_average(state, iterations)

main()
