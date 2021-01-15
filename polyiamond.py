from copy import deepcopy
from typing import List, Tuple

class Polyiamond:
    """
    Polyiamonds are represented as 3 dimensional arrays 
    containing boolean variables to indicate if the cell is part of the polyiamond.
    To keep the arrays smaller and easier to handle, there is a shift added every two rows.
    """
    polyiamond = [[[]]]

    def __init__(self, poly: list = [[[]]]) -> None:
        self.polyiamond = poly

    def length_y(self) -> int:
        return len(self.polyiamond)

    def length_x(self) -> int:
        i = 0
        for row in self.polyiamond:
            if i < len(row):
                i = len(row)
        return i

    def __eq__(self, other) -> bool:
        return self.trim().polyiamond == other.trim().polyiamond

    def __str__(self) -> str:
        out = ""
        i = 0
        for row in self.polyiamond:
            if i % 2 == 1:
                out = out + u'\u25BD'
            else:
                out = out + u'\u25B3' + u'\u25BD'
            for cell in row:
                if cell[0]:
                    out = out + u'\u25B2'
                else:
                    out = out + u'\u25B3'
                if cell[1]:
                    out = out + u'\u25BC'
                else:
                    out = out + u'\u25BD'                   
            i += 1
            out = out + "\n"
        out = out + "\n"
        return out

    def mirror(self) -> 'Polyiamond':

        # mirror the polyiamond
        m_poly = Polyiamond([[[]]])
        i = 0
        j = 0
        x = self.length_x()
        y = self.length_y()

        for row in self.polyiamond:
            if i > 0:
                m_poly.polyiamond.append([])
            for cell in row[::-1]:
                if i+j > 0: #if either i or j > 0
                    m_poly.polyiamond[i].append([])
                m_poly.polyiamond[i][j].append(cell[1])
                m_poly.polyiamond[i][j].append(cell[0])
                j += 1
            i += 1
            j = 0

        # shift one field to the right to get everything nice an aligned
        # first, shift a whole cell to the right, then one field to the left

        for row in m_poly.polyiamond:
            row.insert(0, [0,0])
            row.append([0,0])

        # fix row shift:
        for i in range(0, m_poly.length_y()):
            if i % 2 == 1: 
                m_poly.polyiamond[i].insert(0, [0,0])
            else:
                m_poly.polyiamond[i].append([0,0])

        for row in m_poly.polyiamond:
            i = 0
            for cell in row[1::]:
                row[i][1] = cell[0]
                i += 1
                row[i][0] = cell[1]
        
        # it's propably way to big, so let's trim it
        m_poly = m_poly.trim()

        return m_poly

    # remove the rowshift 
    def deshift(self) -> 'Polyiamond':
        noshift_poly = self.trim().copy()
        i = 0
        y = self.length_y()
        shift = int(y/2-0.5)

        for row in noshift_poly.polyiamond:
            for j in range(int(i/2)):
                row.insert(0, [0,0])
            for j in range(int(i/2), shift):
                row.append([0,0])
            i += 1

        return noshift_poly.trim(True)

    # re-apply the rowshift
    def reshift(self) -> 'Polyiamond':
        shift_poly = self.copy().trim(True)
        i = 0
        y = self.length_y()
        shift = int(y/2-0.5)

        for row in shift_poly.polyiamond:
            for j in range(int(i/2)):
                row.append([0,0])
            for j in range(int(i/2), shift):
                row.insert(0, [0,0])
            i += 1

        return shift_poly.trim()

    # rotate the polyiamond 60° clockwise
    def rotate(self, times: int = 1) -> 'Polyiamond':

        # prepare empty polyiamond
        deshift_poly = self.deshift()
        rotation_poly = deshift_poly.copy()

        for t in range(times):

            x = deshift_poly.length_x()
            y = deshift_poly.length_y()
        
            rotation_poly = Polyiamond([[[0,0] for col in range(y)] for row in range(x)])

            # rotate array clockwise
            for i in range(y):
                for j in range(x):
                    rotation_poly.polyiamond[j][i] = deshift_poly.polyiamond[y-i-1][j]

            # shift to the right
            x = rotation_poly.length_x()
            y = rotation_poly.length_y() # avoid confusion with switched x and y variables

            # first, shift whole cells
            for i in range(y):
                for j in range(i):
                    rotation_poly.polyiamond[i].insert(0, [0,0])
                for k in range(i, y):
                    rotation_poly.polyiamond[i].append([0,0])

            x = rotation_poly.length_x() # width changed by shifting

            # then, shift the cell content
            for row in rotation_poly.polyiamond:
                for i in range(x-1, 0, -1):
                    row[i][1] = row[i][0]
                    row[i][0] = row[i-1][1]
                row[0][1] = row[0][0]
                row[0][0] = 0

            deshift_poly = rotation_poly.copy()

        return rotation_poly.reshift()

    def trim(self, deshifted: bool = False) -> 'Polyiamond':

        copy = self.copy()

        try: # In case copy is empty, return copy
            # delete empty rows on top
            b = False
            while not b:
                row = copy.polyiamond[0]
                for cell in row:
                    if cell != [0,0]:
                        b = True
                if not b:
                    copy = copy.cut(0, 0, 1, 0, deshifted)

            # delete empty rows on bottom
            b = False
            while not b:
                row = copy.polyiamond[-1]
                for cell in row:
                    if cell != [0,0]:
                        b = True
                if not b:
                    copy = copy.cut(0, 0, 0, 1, deshifted)

            # delete empty columns on left side
            b = False
            while not b:
                i = 0
                for i in range(0,copy.length_y()):
                    cell = copy.polyiamond[i][0]
                    if cell != [0,0]:
                        b = True
                if not b:
                    copy = copy.cut(1, 0, 0, 0, deshifted)

            # delete empty columns on right side
            b = False
            while not b:
                i = 0
                for i in range(0,copy.length_y()):
                    cell = copy.polyiamond[i][-1]
                    if cell != [0,0]:
                        b = True
                if not b:
                    copy = copy.cut(0, 1, 0, 0, deshifted)
        except IndexError:
            return copy
        return copy

    def trim_deshifted(self) -> 'Polyiamond':

        copy = self.copy()

        try: # In case copy is empty, return copy
            # delete empty rows on top
            b = False
            while not b:
                row = copy.polyiamond[0]
                for cell in row:
                    if cell != [0,0]:
                        b = True
                if not b:
                    copy = copy.cut(0,0,1,0)

            # delete empty rows on bottom
            b = False
            while not b:
                row = copy.polyiamond[-1]
                for cell in row:
                    if cell != [0,0]:
                        b = True
                if not b:
                    copy = copy.cut(0,0,0,1)

            # delete empty columns on left side
            b = False
            while not b:
                i = 0
                for i in range(0,copy.length_y()):
                    cell = copy.polyiamond[i][0]
                    if cell != [0,0]:
                        b = True
                if not b:
                    copy = copy.cut(1,0,0,0)

            # delete empty columns on right side
            b = False
            while not b:
                i = 0
                for i in range(0,copy.length_y()):
                    cell = copy.polyiamond[i][-1]
                    if cell != [0,0]:
                        b = True
                if not b:
                    copy = copy.cut(0,1,0,0)
        except IndexError:
            return copy
        return copy

    def copy(self) -> 'Polyiamond':
        copy = Polyiamond()
        copy.polyiamond = deepcopy(self.polyiamond)
        return copy

    # cut off rows/columns
    def cut(self, left: int, right: int, top: int, bottom: int, deshifted: bool = False) -> 'Polyiamond':
        copy = self.copy()

        # delete rows on top
        for i in range(0,top):
            del copy.polyiamond[0]

        # fix indentation
        if not deshifted:
            if top % 2 == 1:
                for i in range(1,copy.length_y(),2):
                    copy.polyiamond[i].insert(0,[0,0])
                for i in range(0,copy.length_y(),2):
                    copy.polyiamond[i].append([0,0])

        # delete empty rows on bottom
        for i in range(0,bottom):
            del copy.polyiamond[-1]

        # delete columns on left side
        for i in range(0,left):
            for j in range(0,copy.length_y()):
                del copy.polyiamond[j][0]

        # delete empty columns on right side
        for i in range(0,right):
            for j in range(0,copy.length_y()):
                del copy.polyiamond[j][-1]
        
        return copy

    def contains(self, other: 'Polyiamond') -> bool:
        outer = self.copy().trim()
        inner = other.copy().trim()
        diff_x = outer.length_x() - inner.length_x()
        diff_y = outer.length_y() - inner.length_y()
        if not (diff_x < 0 or diff_y < 0):
            candidates = []
            for i in range(0,diff_y+1):
                candidates.append(outer.cut(0, 0, i, diff_y - i))
            for candidate in candidates:
                diff_x = candidate.length_x() - inner.length_x()
                for j in range(0,diff_x+1):
                    if inner.leq(candidate.cut(j, diff_x - j, 0, 0)):
                        return True
        return False

    # Is self less or equal to other in all fields?
    def leq(self, other) -> bool:
        if self.length_x() > other.length_x() or self.length_y() > other.length_y():
            return False
        for rowself, rowother in zip(self.polyiamond, other.polyiamond):
            for cellself, cellother in zip(rowself, rowother):
                if cellself[0] > cellother[0] or cellself[1] > cellother[1]:
                    return False
        return True

    def is_connected(self) -> bool:
        # make trimmed copy of self
        bigger = self.trim()

        smaller = Polyiamond([ [ [0,0] for cell in row ] for row in bigger.polyiamond ])

        # find one filled cell of bigger, copy to smaller
        for i in range(0,bigger.length_y()):
            for j in range(0,bigger.length_x()):
                if bigger.polyiamond[i][j] != [0,0]:
                    smaller.polyiamond[i][j] = bigger.polyiamond[i][j]
                    break
            else: 
                continue
            break

        # iterate to find all cells connected to first one
        c = True
        while c:
            c = False
            for i in range(0,smaller.length_y()): # rows
                for j in range(0,smaller.length_x()): # cells
                    for k in range(0,2): # fields
                        if smaller.polyiamond[i][j][k] != 0:
                            neighbors = smaller.get_neighbors(i, j, k)
                            for x, y, z in neighbors:
                                try: 
                                    if smaller.polyiamond[x][y][z] != bigger.polyiamond[x][y][z]:
                                        smaller.polyiamond[x][y][z] = 1
                                        c = True
                                except IndexError:
                                    pass

        # compare results
        return smaller == bigger

    def get_neighbors(self, i: int, j: int, k: int) -> List[Tuple[int,int,int]]:
        neighbors = []
        # odd rows
        if i % 2 == 1:

            # lower field
            if k == 0:
                # left
                neighbors.append((i, j-1, 1))

                # right
                neighbors.append((i, j, 1))

                # bottom
                neighbors.append((i+1, j-1, 1))
            
            # upper field
            else:
                # left
                neighbors.append((i, j, 0))

                # right
                neighbors.append((i, j+1, 0))

                # top
                neighbors.append((i-1, j, 0))
        
        # even rows
        else:

            # lower field
            if k == 0:
                # left
                neighbors.append((i, j-1, 1))

                # right
                neighbors.append((i, j, 1))

                # bottom
                neighbors.append((i+1, j, 1))
            
            # upper field
            else:
                # left
                neighbors.append((i, j, 0))

                # right
                neighbors.append((i, j+1, 0))

                # top
                neighbors.append((i-1, j+1, 0))

        neighbors = [n for n in neighbors if all(v > -1 for v in n)]
            
        return neighbors

    def size(self) -> int:
        i = 0
        for row in self.polyiamond:
            for cell in row:
                for field in cell:
                    i = i + field
        return i

    def equals(self, other) -> bool:
        return self.copy().trim().polyiamond == other.copy().trim().polyiamond

    def all_rotations(self) -> list:
        rotations = [self.copy(), self.copy().mirror()]
        for poly in [self.copy(), self.copy().mirror()]:
            for i in range(5):
                poly = poly.rotate(1)
                b = False
                for p in rotations:
                    if p.equals(poly):
                        b = True
                        break
                if not b:
                    rotations.append(poly.copy())

        return rotations

    def pad(self):
        for row in self.polyiamond:
            row.append([0,0])
            row.insert(0, [0,0])

        self.polyiamond.append([[0,0] for col in range(self.length_x())])
        self.polyiamond.insert(0, [[0,0] for col in range(self.length_x())])
        self.polyiamond.insert(0, [[0,0] for col in range(self.length_x())])

        return self