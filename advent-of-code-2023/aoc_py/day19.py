import sys
from copy import deepcopy
from collections import deque
from heapq import heappush, heappop

class Condition:
    def __init__(self, condition, nextWorkFlow) -> None:
        self.part = None if condition == None else condition.split('<' if '<' in condition else '>')[0]
        self.condition = None if condition == None else '<' if '<' in condition else '>'
        self.value = None if condition == None else int(condition.split('<' if '<' in condition else '>')[1])
        self.nwf = nextWorkFlow

    def __repr__(self):
        return f'{self.part}{self.condition}{self.value}:{self.nwf}'

    

for arg in sys.argv[1:]:
    print('\n', arg)
    
    with open(arg) as f:
        data = f.read().split("\n\n")
        
    workflows = {}
    for wf in data[0].split('\n'):
        wfName, wf = wf.split('{')

        for each_condition in wf[:-1].split(','):
            if ':' in each_condition:
                condition, nextWorkflow = each_condition.split(':')
            else:
                condition = None
                nextWorkflow = each_condition

            if wfName in workflows:
                    workflows[wfName].append(Condition(condition, nextWorkflow))
            else:
                workflows[wfName] = [Condition(condition, nextWorkflow)]           

    def check_condition(condition, ratings):
        if condition.condition == '<':
            return ratings[condition.part] < condition.value
        else:
            return ratings[condition.part] > condition.value

    def check_workflow(ratings):
        curWf = 'in'

        while curWf not in 'AR':
            for condition in workflows[curWf]:
                if condition.part == None or check_condition(condition, ratings):
                    curWf = condition.nwf
                    break

        return curWf

    total = 0
    for rating_list in data[1].split('\n'):
        ratings = {rating.split('=')[0]:int(rating.split('=')[1]) for rating in rating_list[1:-1].split(',')}

        if check_workflow(ratings) == 'A':
            total += sum([val for _, val in ratings.items()])


    print("part 1: ", total)

    def prod(ranges):
        p = 1
        for _, r in ranges.items():
            p *= r[1]-r[0] + 1
        
        return p

    def split_ranges(ranges, condition):

        if condition.condition == '<':
            if condition.value <= ranges[condition.part][0]: return [ranges]
            elif ranges[condition.part][0] < condition.value < ranges[condition.part][1]: 
                first = dict(ranges)
                second = dict(ranges)

                first[condition.part] = (ranges[condition.part][0], condition.value-1)
                second[condition.part] = (condition.value, ranges[condition.part][1])
                
                return [first, second]

        elif condition.condition == '>':
            if condition.value >= ranges[condition.part][1]: return [ranges]
            elif ranges[condition.part][0] < condition.value < ranges[condition.part][1]: 
                first = dict(ranges)
                second = dict(ranges)

                first[condition.part] = (condition.value+1, ranges[condition.part][1])
                second[condition.part] = (ranges[condition.part][0], condition.value)
                
                return [first, second]


    prev = []
    def get_possible_ranges(ranges, curWf):
        global prev
        countA = 0

        if curWf == 'A':
            return prod(ranges)
        elif curWf == 'R':
            return 0
        
        for condition in workflows[curWf]:
            if condition.part == None:
                if condition.condition == 'A':
                    countA += prod(ranges)
                elif condition.condition != 'R':
                    countA += get_possible_ranges(ranges, condition.nwf)
            else:
                nranges = split_ranges(ranges, condition)

                if len(nranges) != 1:
                    countA += get_possible_ranges(nranges[0], condition.nwf)
                    countA += get_possible_ranges(nranges[1], curWf)
                    break
                else:
                    ranges = nranges[0]
        return countA

    print("part 2: ", get_possible_ranges({key: (1, 4000) for key in "xmas"}, 'in'))
