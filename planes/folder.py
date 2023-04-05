import math
import random
from typing import List, Tuple
from paper import Paper, Mark


class Folder:
    def __init__(self, paper: Paper):
        self.paper = paper
        self.marks: List[Mark] = []

        
    def apply_fold(self, a: float, alpha: float) -> None:
        """
        Applies a fold to the current set of marks.
        """
        # Compute the intersection points of the fold
        # with the left and right edges of the paper
        x2 = a / math.tan(alpha)
        
        # Create a new mark and add it to the list of marks
        mark = Mark((a, 0), (x2, self.paper.height))
        self.paper.marks.append(mark)   

    def apply_random_fold(self):
        """
        Applies a random fold to the current folded paper.
        Adds the mark representing the fold to the list of marks.
        """
        a = random.uniform(0, max(self.paper.width, self.paper.width))
        alpha = random.uniform(0, math.pi)
        self.apply_fold(a,alpha)
