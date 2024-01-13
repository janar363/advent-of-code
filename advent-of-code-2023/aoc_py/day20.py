import sys
from copy import deepcopy
from collections import deque
from heapq import heappush, heappop
import math

class Module:
    def __init__(self, type, dest, state):
        self.type = type
        self.dest = dest
        self.state = state
        self.pulse = {}

    def __eq__(self, other):
        return self.type == other.type and self.dest == other.dest and self.state == other.state and self.pulse == other.pulse

    def __repr__(self) -> str:
        return f" -> {self.dest} cur = {self.state} pulse = {self.pulse}"

for arg in sys.argv[1:]:
    print('\n', arg)
    
    with open(arg) as f:
        lines = [line.strip() for line in f.readlines()]

    original_modules = {}
    inputs = {}
    mf_inps = []

    for line in lines:
        name, dest = line.split(' -> ')
        original_modules[name[1:] if not name[0].isalpha() else name] = Module(name[0] if not name[0].isalpha() else name, dest.split(', '), 0)
        inputs[name[1:] if not name[0].isalpha() else name] = 0

        if 'mf' in original_modules[name[1:] if not name[0].isalpha() else name].dest:
            mf_inps.append(name[1:] if not name[0].isalpha() else name) 

    for _, module in original_modules.items():
        module.pulse = dict(inputs)

    seen = {}
    def button_pushed(modules):
        global seen
        q = deque([('broadcaster', 0)])
        h = 0
        l = 0
        c = 1
        while len(q) != 0:
            module, inp = q.popleft()

            if inp == 0:
                l += 1
            else:
                h += 1

            if module in modules:
                dest_inp = -1
                if modules[module].type == 'broadcaster':
                    dest_inp = inp
                elif modules[module].type == '%':

                    if inp == 0:
                        if modules[module].state == 0:
                            modules[module].state = 1
                        elif modules[module].state == 1:
                            modules[module].state = 0
                        
                        dest_inp = modules[module].state
                else:
                    lo = 0

                    for key, val in modules[module].pulse.items():
                        if module in modules[key].dest and val == 0:
                            lo += 1

                    if lo == 0:
                        dest_inp = 0
                    else:
                        dest_inp = 1
                
                if dest_inp != -1:
                    for dest in modules[module].dest:
                        if dest in modules and modules[dest].type == '&':
                            modules[dest].pulse[module] = dest_inp
                        q.append((dest, dest_inp))
                        if dest == 'mf' and dest_inp == 1 and module not in seen:
                            seen[module] = -1

            c += 1
        
        return modules, l, h
    
    def get_cycle(modules, button_presss=1000):
        global original_modules

        count = 0
        h = 0
        l = 0

        while True:
            if button_presss == count:
                break
            modules, cl, ch = button_pushed(modules)
            count += 1
            h += ch
            l += cl

            if modules == original_modules:
                break
    
        return count, l, h

    cycle, clo, chi = get_cycle(deepcopy(original_modules))

    _, rlo, rhi = get_cycle(deepcopy(original_modules), 1000%cycle)

    print("part 1: ", (clo * (1000 // cycle) + rlo) * (chi * (1000 // cycle) + rhi))

    def get_mf_inps():
        global original_modules, seen
        
        modules = deepcopy(original_modules)
        count = 0
        while len(seen) != len(mf_inps):
            modules, _, _ = button_pushed(modules)
            count += 1

            for k, v in seen.items():
                if v == -1:
                    seen[k] = count

    get_mf_inps()
    
    steps = list(seen.values())

    lcm = 0
    if len(steps) != 0:
        lcm = steps[0]
        for val in steps[1:]:
            lcm = math.lcm(lcm, val)

    print("part 2: ", lcm)
