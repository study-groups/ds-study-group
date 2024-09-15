#!/usr/bin/env python
import math
from paper import Paper
from folder import Folder

def main():
    paper = Paper()
    folder = Folder(paper)
    folder.apply_random_fold()
    folder.apply_random_fold()
    folder.apply_random_fold()
    paper.draw("four.svg")

if __name__ == '__main__':
    main()

