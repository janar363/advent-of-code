with open("input") as file:
    fileSizes = []
    spaceSizes = []
    fileidx = 0
    for ch in file.read().strip():
        if len(fileSizes) == len(spaceSizes):
            fileSizes.append((int(ch), fileidx))
            fileidx += 1
        else: 
            spaceSizes.append(int(ch))


i = 0
relocateIdx = len(fileSizes) - 1
relocatedFiles = {} # maps relocated relocated file values to spaceids

while i < relocateIdx:
    if fileSizes[relocateIdx][0] <= spaceSizes[i]:
        spaceSizes[i] -= fileSizes[relocateIdx][0]
        if i not in relocatedFiles.keys(): relocatedFiles[i] = []

        relocatedFiles[i].append((fileSizes[relocateIdx][0], fileSizes[relocateIdx][1])) 
        relocateIdx -= 1
    else:
        if i not in relocatedFiles.keys(): relocatedFiles[i] = []
        relocatedFiles[i].append((spaceSizes[i], fileSizes[relocateIdx][1]))
        fileSizes[relocateIdx] = (fileSizes[relocateIdx][0]-spaceSizes[i], fileSizes[relocateIdx][1])
        spaceSizes[i] = 0
        i += 1

part1 = 0
prefix = 0
for i in range(len(list(relocatedFiles.keys()))):
    for j in range(fileSizes[i][0]):
        part1 += (fileSizes[i][1] * (j + prefix))

    prefix += fileSizes[i][0]

    for eachReloactedFileInSpace in relocatedFiles[i]:
        for j in range(eachReloactedFileInSpace[0]):
            part1 += eachReloactedFileInSpace[1] * (j + prefix)
        
        prefix += eachReloactedFileInSpace[0]

for j in range(fileSizes[len(list(relocatedFiles.keys()))][0]):
        part1 += (fileSizes[len(list(relocatedFiles.keys()))][1] * (j + prefix))


print("part1 : ", part1)

with open("input") as file:
    fileSizes = []
    spaceSizes = []
    fileidx = 0
    for ch in file.read().strip():
        if len(fileSizes) == len(spaceSizes):
            fileSizes.append((int(ch), fileidx))
            fileidx += 1
        else: 
            spaceSizes.append(int(ch))


part2 = 0
            
relocateIdx = len(fileSizes) - 1
relocatedFiles = {}
while relocateIdx >= 0:
    for i in range(len(spaceSizes)):
        if i >= relocateIdx: continue
        if fileSizes[relocateIdx][0] <= spaceSizes[i]:
            spaceSizes[i] -= fileSizes[relocateIdx][0]
            if i not in relocatedFiles.keys(): relocatedFiles[i] = []

            relocatedFiles[i].append((fileSizes[relocateIdx][0], fileSizes[relocateIdx][1])) 
            break
    relocateIdx -= 1

part2 = 0
prefix = 0
visited = set()
for i in range(len(fileSizes)):

    if fileSizes[i][1] not in visited:
        for j in range(fileSizes[i][0]):
            part2 += (fileSizes[i][1] * (j + prefix))
            visited.add(fileSizes[i][1])

    prefix += fileSizes[i][0]
    
    if i in set(relocatedFiles.keys()):
        for eachReloactedFileInSpace in relocatedFiles[i]:
            if eachReloactedFileInSpace[1] not in visited:
                for j in range(eachReloactedFileInSpace[0]):
                    part2 += eachReloactedFileInSpace[1] * (j + prefix)
                    visited.add(eachReloactedFileInSpace[1])
            
                prefix += eachReloactedFileInSpace[0]
        prefix += spaceSizes[i]
    else:
        if i < len(spaceSizes):
            prefix += spaceSizes[i]


print("part2 : ", part2)