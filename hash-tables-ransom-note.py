import math
import os
import random
import re
import sys
from collections import Counter

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    try:
        magazine_dict = Counter(magazine)
        note_dict = Counter(note)
        for key, value in note_dict.items():
            if value <= magazine_dict[key]:
                continue
            else:
                print("No")
                return
        print("Yes")
    except KeyError as ke:
        print("No")

if __name__ == '__main__':
    # mn = input().split()
    #
    # m = int(mn[0])
    #
    # n = int(mn[1])

    # magazine = input().rstrip().split()
    magazine = ["give", "me", "one", "grand", "today", "night"]

    # note = input().rstrip().split()
    note = ["give", "one", "grand", "today"]

    checkMagazine(magazine, note)