import random
import sys

class SkipList:
    def __init__(self, size, max_level):
        self.levels = [[i for i in range(1, size + 1)]]
        self.current_level = 0
        self.max_level = max_level
        self.algorithm_steps = [
            "j ← 1",
            "while the number of nodes at level j > 1 do",
            "    for each i'th node at level j do",
            "        if i is odd and i is not the last node at level j",
            "            randomly choose whether to promote it to level j+1",
            "        else if i is even and node i-1 was not promoted",
            "            promote it to level j+1",
            "        end if",
            "    repeat",
            "    j ← j + 1",
            "repeat"
        ]

    def promote(self):
        if self.current_level >= self.max_level - 1:
            print("Maximum level reached. No further promotions possible.")
            return False  # Return a flag indicating no further promotions are possible

        new_level = []
        last_promoted = False
        for i, node in enumerate(self.levels[self.current_level]):
            self.display(node, 3 if i % 2 == 1 else 5, True)  # Highlight node being processed
            decision = random.choice([True, False]) if i % 2 == 1 else True
            if decision:
                new_level.append(node)
                last_promoted = True
            else:
                last_promoted = False
                self.display(node, 4, False)  # Highlight non-promotion in red for odd nodes
            input(f"Press Enter to continue step for node {node} at level {self.current_level + 1}...")
        if new_level:
            self.levels.append(new_level)
            self.current_level += 1
        self.display(None, 9, True)  # Display incrementing j step
        input("Press Enter to increment j...")
        return True

    def display(self, node, step_index, promoted):
        sys.stdout.write("\033c")  # Clear the terminal screen
        print(f"Node: \033[32m{node if node else 'N/A'}\033[0m, Level: {self.current_level + 1}".ljust(40))
        for level in self.levels:
            level_display = ' '.join(f"\033[32m{x}\033[0m" if x == node else str(x) for x in level)
            print(level_display.ljust(40))
        print("\033[1mAlgorithm Steps:\033[0m")
        for idx, step in enumerate(self.algorithm_steps):
            if idx == step_index:
                color = "\033[32m" if promoted else "\033[91m"
                print(f"{color}{step}\033[0m")  # Green for active step, red if not promoted
            else:
                print(step)

def main(size, max_level, seed=None):
    if seed is not None:
        random.seed(seed)
    skip_list = SkipList(size, max_level)
    skip_list.display(None, 0, True)  # Display initial step before promotions
    input("Press Enter to start processing...")
    while len(skip_list.levels[skip_list.current_level]) > 1:
        if not skip_list.promote():  # Check if further promotions are possible
            break  # Exit the loop if maximum level reached

if __name__ == "__main__":
    size = int(sys.argv[1])
    max_level = int(sys.argv[2])
    seed = int(sys.argv[3]) if len(sys.argv) > 3 else None
    main(size, max_level, seed)

# python skiplish_visual.py 10 5 42
