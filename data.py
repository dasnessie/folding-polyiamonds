from polyiamond import *

#known foldables
foldables = []

# nets N1
n1 = []

# nets N2
n2 = []

# all nets
nets = []

# convex
convex = []

# convex polyiamond c10
c10 = []


# convex Polyiamonds (in all orientations)
# A
c10.append(Polyiamond([[[0,1],[1,1],[1,1],[1,1],[1,1],[1,0]]]))
rotations = c10[-1].all_rotations()
for r in rotations:
    if r not in c10:
        c10.append(r)
for poly in c10:
    convex.append(poly)

# B
# irrelevant because it contains nets
# convex.append(Polyiamond([[[1,1],[1,1],[1,1]],
#                              [[1,1],[1,1],[1,1]]]))
# rotations = convex[-1].all_rotations()
# for r in rotations:
#     if r not in convex:
#         convex.append(r)

# C
# irrelevant because it contains nets
# convex.append(Polyiamond([[[0,0],[1,1],[1,1],[1,0]],
#                              [[0,0],[1,1],[1,1],[1,1]],
#                              [[0,1],[1,1],[1,1],[0,0]]]))
# rotations = convex[-1].all_rotations()
# for r in rotations:
#     if r not in convex:
#         convex.append(r)


# D
convex.append(Polyiamond([[[1,1],[1,1],[1,0]],
                             [[0,1],[1,1],[1,1]],
                             [[0,1],[1,1],[0,0]],
                             [[0,0],[0,1],[0,0]]]))
rotations = convex[-1].all_rotations()
for r in rotations:
    if r not in convex:
        convex.append(r)

# nets (in all orientations)
# A
n1.append(Polyiamond([[[0,0],[1,0],[0,0],[0,0]],[[0,0],[1,1],[1,1],[1,1]],[[0,1],[0,0],[0,0],[0,0]]]))
rotations = n1[-1].all_rotations()
for r in rotations:
    if r not in n1:
        n1.append(r)

# B
n1.append(Polyiamond([[[0,0],[0,0],[1,0],[0,0]],[[0,0],[1,1],[1,1],[1,1]],[[0,1],[0,0],[0,0],[0,0]]]))
rotations = n1[-1].all_rotations()
for r in rotations:
    if r not in n1:
        n1.append(r)

# C
n1.append(Polyiamond([[[0,0],[0,0],[0,0],[1,0]],
                             [[0,0],[1,1],[1,1],[1,1]],
                             [[0,1],[0,0],[0,0],[0,0]]]))
rotations = n1[-1].all_rotations()
for r in rotations:
    if r not in n1:
        n1.append(r)

# D
n1.append(Polyiamond([[[0,0],[1,0],[0,0]],[[1,1],[1,1],[1,1]],[[0,1],[0,0],[0,0]]]))
rotations = n1[-1].all_rotations()
for r in rotations:
    if r not in n1:
        n1.append(r)

# E
n1.append(Polyiamond([[[1,0],[0,0],[0,0]],[[1,1],[1,1],[1,1]],[[0,1],[0,0],[0,0]]]))
rotations = n1[-1].all_rotations()
for r in rotations:
    if r not in n1:
        n1.append(r)

# F
n2.append(Polyiamond([[[1,0],[0,0],[0,0]],[[1,1],[1,1],[1,1]],[[0,0],[0,1],[0,0]]]))
rotations = n2[-1].all_rotations()
for r in rotations:
    if r not in n2:
        n2.append(r)

# G
n2.append(Polyiamond([[[0,0],[0,0],[1,1],[0,0]],[[0,0],[1,1],[1,1],[1,0]],[[0,1],[0,0],[0,0],[0,0]]]))
rotations = n2[-1].all_rotations()
for r in rotations:
    if r not in n2:
        n2.append(r)

# H
n1.append(Polyiamond([[[0,0],[1,1],[0,0]],[[1,1],[1,1],[1,0]],[[0,0],[0,1],[0,0]]]))
rotations = n1[-1].all_rotations()
for r in rotations:
    if r not in n1:
        n1.append(r)

# I
n2.append(Polyiamond([[[0,0],[1,1],[0,0]],[[1,1],[1,1],[1,0]],[[0,1],[0,0],[0,0]]]))
rotations = n2[-1].all_rotations()
for r in rotations:
    if r not in n2:
        n2.append(r)

# J
n2.append(Polyiamond([[[0,0],[0,0],[1,1],[1,0]],[[0,0],[1,1],[1,1],[0,0]],[[0,1],[0,0],[0,0],[0,0]]]))
rotations = n2[-1].all_rotations()
for r in rotations:
    if r not in n2:
        n2.append(r)

# K
n2.append(Polyiamond([[[0,0],[1,1],[1,1]],[[1,1],[1,1],[0,0]]]))
rotations = n2[-1].all_rotations()
for r in rotations:
    if r not in n2:
        n2.append(r)

# additional foldable Polyiamonds

# A
foldables.append(Polyiamond([[[0,0],[0,0],[0,0],[1,0]],[[1,1],[1,1],[1,1],[1,1]]]))
rotations = foldables[-1].all_rotations()
for r in rotations:
    if r not in foldables:
        foldables.append(r)

# B
foldables.append(Polyiamond([[[0,0],[0,0],[1,0],[0,0]],[[1,1],[1,1],[1,1],[1,1]]]))
rotations = foldables[-1].all_rotations()
for r in rotations:
    if r not in foldables:
        foldables.append(r)

# C
foldables.append(Polyiamond([[[0,0],[1,0],[0,0],[0,0]],[[1,1],[1,1],[1,1],[1,1]]]))
rotations = foldables[-1].all_rotations()
for r in rotations:
    if r not in foldables:
        foldables.append(r)

for p in n1:
    if p not in foldables:
        foldables.append(p)

for p in n2:
    if p not in foldables:
        foldables.append(p)

for p in convex:
    if p not in foldables:
        foldables.append(p)

p6 = [Polyiamond([[[1,1],[1,1],[1,1]]])]
rotations = p6[-1].all_rotations()
for r in rotations:
    if r not in p6:
        p6.append(r)

p6plus = [Polyiamond([[[1,1],[1,1],[1,1]],[[0,1],[0,0],[0,0]]])]
rotations = p6plus[-1].all_rotations()
for r in rotations:
    if r not in p6plus:
        p6plus.append(r)

z6 = [Polyiamond([[[1,1],[1,0],[0,0]],[[0,0],[0,1],[1,1]]])]
rotations = z6[-1].all_rotations()
for r in rotations:
    if r not in z6:
        z6.append(r)


area_symmetrical = []
area_difficult = []

area_symmetrical.append(Polyiamond([[[0,0],[0,0],[1,1],[1,0],[0,0]],
                                    [[0,0],[1,1],[1,1],[1,1],[1,1]],
                                    [[1,1],[1,1],[1,1],[1,1],[1,0]],
                                    [[0,1],[1,1],[1,1],[1,1],[1,1]],
                                    [[0,1],[1,1],[1,1],[1,1],[1,0]],
                                    [[0,0],[0,0],[0,1],[1,1],[0,0]]]))
rotations = area_symmetrical[-1].all_rotations()
for r in rotations:
    if r not in area_symmetrical:
        area_symmetrical.append(r)

area_symmetrical.append(Polyiamond([[[0,0],[0,0],[0,0],[1,1],[1,0]],
                                    [[0,0],[0,0],[1,1],[1,1],[1,1]],
                                    [[1,1],[1,1],[1,1],[1,1],[1,0]],
                                    [[0,1],[1,1],[1,1],[1,1],[1,1]],
                                    [[0,0],[0,1],[1,1],[1,1],[1,0]],
                                    [[0,0],[0,0],[0,0],[0,1],[1,1]]]))
rotations = area_symmetrical[-1].all_rotations()
for r in rotations:
    if r not in area_symmetrical:
        area_symmetrical.append(r)

area_symmetrical.append(Polyiamond([[[0,0],[1,1],[1,0],[0,0],[0,0],[0,0]],
                                    [[0,0],[1,1],[1,1],[1,1],[1,0],[0,0]],
                                    [[0,1],[1,1],[1,1],[1,1],[1,1],[0,0]],
                                    [[0,0],[1,1],[1,1],[1,1],[1,1],[1,0]],
                                    [[0,1],[1,1],[1,1],[1,1],[0,0],[0,0]],
                                    [[0,0],[0,1],[1,1],[0,0],[0,0],[0,0]]]))
rotations = area_symmetrical[-1].all_rotations()
for r in rotations:
    if r not in area_symmetrical:
        area_symmetrical.append(r)

area_difficult.append(Polyiamond([[[0,0],[0,0],[0,0],[1,0],[0,0]],
                                  [[0,0],[0,0],[1,1],[1,1],[1,0]],
                                  [[1,1],[1,1],[1,1],[1,1],[0,0]],
                                  [[1,1],[1,1],[1,1],[1,1],[1,0]],
                                  [[0,1],[1,1],[1,1],[1,1],[0,0]],
                                  [[0,0],[0,0],[0,1],[1,1],[1,0]]]))
rotations = area_difficult[-1].all_rotations()
for r in rotations:
    if r not in area_difficult:
        area_difficult.append(r)

area_difficult.append(Polyiamond([[[0,0],[0,0],[1,0],[0,0],[0,0]],
                                  [[0,0],[1,1],[1,1],[1,1],[1,0]],
                                  [[1,1],[1,1],[1,1],[1,1],[1,0]],
                                  [[0,1],[1,1],[1,1],[1,1],[1,1]],
                                  [[1,1],[1,1],[1,1],[1,1],[1,0]],
                                  [[0,0],[0,1],[1,1],[1,1],[0,0]]]))
rotations = area_difficult[-1].all_rotations()
for r in rotations:
    if r not in area_difficult:
        area_difficult.append(r)

px = []
px.append(Polyiamond([[[0,1],[1,1],[0,0]],[[0,0],[1,1],[1,0]]]))
rotations = px[-1].all_rotations()
for r in rotations:
    if r not in px:
        px.append(r)

pu = []
pu.append(Polyiamond([[[1,0],[0,0],[1,0]],[[0,1],[1,1],[1,1]]]))
rotations = pu[-1].all_rotations()
for r in rotations:
    if r not in pu:
        pu.append(r)