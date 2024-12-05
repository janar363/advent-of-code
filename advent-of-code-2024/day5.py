with open('input') as f:
   data = f.read().split('\n\n')
   rules = {}
   for rule in data[0].split('\n'):
      n1, n2 = map(int, rule.split('|'))
      if n1 in set(rules.keys()): rules[n1].append(n2)
      else: rules[n1] = [n2]

   orderings = []
   for ordering in data[1].split('\n'):
      orderings.append([int(page) for page in ordering.split(',')])

part1 = 0

rightOrders = []
wrongOrders = []
for eachOrdering in orderings:
   rightOrder = True
   for i in range(len(eachOrdering)):
      for eachPage in eachOrdering[i+1:]:
         if eachOrdering[i] not in set(rules.keys()) or eachPage not in rules[eachOrdering[i]]: 
            rightOrder = False
            break
      if not rightOrder: break

   if rightOrder:  rightOrders.append(eachOrdering) 
   else: wrongOrders.append(eachOrdering)    

print("part 1 : ", sum([rightOrder[len(rightOrder) // 2] for rightOrder in rightOrders]))

correctedOrders = []
for wrongOrder in wrongOrders:
   correctedOrder = list(wrongOrder)
   for i in range(len(wrongOrder)):
      count = 0
      for page in wrongOrder[:i] + wrongOrder[i+1:]:
         if wrongOrder[i] in set(rules.keys()) and page in rules[wrongOrder[i]]: count += 1

      correctedOrder[count * -1 - 1] = wrongOrder[i]

   correctedOrders.append(correctedOrder)  

print("part2 : ", sum([correctOrder[len(correctOrder) // 2] for correctOrder in correctedOrders]))
      

   
    