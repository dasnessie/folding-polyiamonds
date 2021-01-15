import multiprocessing
import pickle
import datetime

from polyiamond import *
from helpers import *
from data import *
from polyiamond_generation import *

def do_the_processing(sub):    
    # Does sub contain a foldable polyiamond?
    interesting = True
    for foldable in z6:
        if sub.contains(foldable):
            interesting = False
            break
    for foldable in p6plus:
        if sub.contains(foldable):
            interesting = False
            break
    for foldable in pu:
        if sub.contains(foldable):
            interesting = False
            break
    for foldable in px:
        if sub.contains(foldable):
            interesting = False
            break
    for foldable in c10:
        if sub.contains(foldable):
            interesting = False
            break

    # Does sub fit into one of the areas?
    # 
    # fits_area = False
    # for area in area_symmetrical:
    #     if area.contains(sub):
    #         fits_area = True
    #         break
    # for area in area_difficult:
    #     if area.contains(sub):
    #         fits_area = True
    #         break
    # if not fits_area:
    #     interesting = False
    return sub, interesting

if __name__ == '__main__':
    size = 1 # size of polyiamonds to start with (use one you have already done!)
    picklejar = open(f"Pickles/jar{size}",'rb')
    old_polyiamonds = pickle.load(picklejar)
    picklejar.close()

    while True:
        new_polyiamonds = generate_next_set(old_polyiamonds)
        new_interesting_polyiamonds = []
        size = size + 1

        file = open(f"Result_files/results{size}", "a")
        with multiprocessing.Pool(processes=multiprocessing.cpu_count() - 1) as p:
            for poly, interesting in p.imap_unordered(do_the_processing, new_polyiamonds, chunksize=100):
                if interesting:
                    new_interesting_polyiamonds.append(poly)

        for p in new_interesting_polyiamonds:
            file.write(p.__str__())
        file.write(f"Finished the run for size {size} with {len(new_interesting_polyiamonds)} polyiamonds. Excluding polyiamonds containing px, pu, z6 and p6.")
        file.close()

        picklejar = open(f"Pickles/jar{size}",'wb')
        pickle.dump(new_interesting_polyiamonds, picklejar)
        picklejar.close()

        print(f"Finished run for size {size} with {len(new_interesting_polyiamonds)} polyiamonds at {datetime.datetime.now()}")

        if len(new_interesting_polyiamonds) == 0:
            break

        old_polyiamonds = new_interesting_polyiamonds
