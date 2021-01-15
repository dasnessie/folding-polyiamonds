import multiprocessing
# from tqdm import tqdm
from math import comb

from polyiamond import *
from helpers import *
from data import *

def generate_next_set(list_prev: list = [Polyiamond([[[1,0]]])]) -> list: 
    new_polyiamonds = []
    small_set = []
    for prev in list_prev:
        # generate next polyiamonds
        interesting = prev.copy().pad()
        new = prev.copy().pad()
        small_set = [] # successors of prev
        for i in range(interesting.length_y()): # rows
            for j in range(interesting.length_x()): # cells
                for k in range(2): # fields
                    if interesting.polyiamond[i][j][k] == 1:
                        neighbors = interesting.get_neighbors(i, j, k)
                        for x, y, z in neighbors:
                            try: 
                                if interesting.polyiamond[x][y][z] == 0:
                                    interesting.polyiamond[x][y][z] = 2 # mark field as visited
                                    new.polyiamond[x][y][z] = 1 # this is now the new polyiamond
                                    add_polyiamond_to_list(new.copy().trim(), small_set) # add new to list
                                    new.polyiamond[x][y][z] = 0 # reset new
                            except IndexError:
                                pass
        for new in small_set:
            # add polyiamond to big list
            add_polyiamond_to_list(new, new_polyiamonds)
        
    return new_polyiamonds

def add_polyiamond_to_list(new_poly: Polyiamond, polyiamond_list: list) -> list:
    new_poly_list = new_poly.all_rotations()

    for poly in polyiamond_list:
        for new_poly_rotated in new_poly_list:
            if new_poly_rotated.equals(poly):
                return polyiamond_list

    return polyiamond_list.append(new_poly)