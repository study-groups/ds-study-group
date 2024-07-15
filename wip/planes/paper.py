from typing import Tuple
import svgwrite
from svgwrite.container import Group
from svgwrite.shapes import Line
from svgwrite.text import Text

from typing import List, Tuple, NamedTuple

class Mark(NamedTuple):
    start: Tuple[float, float]
    end: Tuple[float, float]

class Paper:
    def __init__(self, width: float =300, height: float = 400):
        self.width = width
        self.height = height
        self.svg = svgwrite.Drawing(size=(f"{width}mm",
            f"{height}mm"), viewBox=f"0 0 {width} {height}")
        self.marks = []

    def add_mark(self, mark: Mark) -> None:
        """
        Adds a mark to the paper.
        """
        self.marks.append(mark)

    def draw(self, filename: str) -> None:
        """
        Draws the paper with its folds to an SVG file.
        """
        for mark in self.marks:
            line = Line(start=mark.start, end=mark.end,
                    stroke='black', stroke_width=0.2)
            self.svg.add(line)
            
        self.svg.saveas(filename)
