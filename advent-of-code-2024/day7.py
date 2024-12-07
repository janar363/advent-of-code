with open("input") as file:
    equations = []

    for line in file.readlines():
        line = line.strip()
        equation = [int(line.split(':')[0])]
        for operand in line.split(':')[1].strip().split():
            equation.append(int(operand))

        equations.append(equation)



def correctEquation(operands, ans):
    try:
        if len(operands) > 2:

            newOperands = [operands[0] * operands[1]]
            newOperands.extend(operands[2:])
            if correctEquation(newOperands, ans): return True
            
            newOperands = [operands[0] + operands[1]]
            newOperands.extend(operands[2:])
            if correctEquation(newOperands, ans): return True
        else: 
            if operands[0] * operands[1] == ans: return True
            elif operands[0] + operands[1] == ans: return True
    except:
        print("failed for eqjuation ", operands, " ans : ", ans)

    return False

def correctEquation2(operands, ans):
    try:
        if len(operands) > 2:

            newOperands = [operands[0] * operands[1]]
            newOperands.extend(operands[2:])
            if correctEquation2(newOperands, ans): return True
            
            newOperands = [operands[0] + operands[1]]
            newOperands.extend(operands[2:])
            if correctEquation2(newOperands, ans): return True

            newOperands = [int(str(operands[0]) + str(operands[1]))]
            newOperands.extend(operands[2:])
            if correctEquation2(newOperands, ans): return True


        else: 
            if operands[0] * operands[1] == ans: return True
            elif operands[0] + operands[1] == ans: return True
            elif int(str(operands[0]) + str(operands[1])) == ans: return True
    except:
        print("failed for eqjuation ", operands, " ans : ", ans)

    return False

        


part1 = 0
for equation in equations:
    ans = equation[0]
    operands = equation[1:]

    if correctEquation(operands, ans): part1 += ans

print("part1 : ", part1)

part2 = 0
for equation in equations:
    ans = equation[0]
    operands = equation[1:]

    if correctEquation2(operands, ans): part2 += ans

print("part2 : ", part2)
