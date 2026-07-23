import tkinter as tk
from tkinter import messagebox

def find_empty(grid):
    """Find an empty cell in the Sudoku grid (0 = empty)."""
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                return i, j
    return None

def is_valid(grid, num, pos):
    """Check if placing 'num' at position 'pos' is valid."""
    row, col = pos

    
    if num in grid[row]:
        return False

    
    if num in [grid[i][col] for i in range(9)]:
        return False


    box_x, box_y = col // 3, row // 3
    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if grid[i][j] == num:
                return False
    return True

def solve(grid):
    """Solve Sudoku puzzle using backtracking."""
    find = find_empty(grid)
    if not find:
        return True
    row, col = find

    for num in range(1, 10):
        if is_valid(grid, num, (row, col)):
            grid[row][col] = num

            if solve(grid):
                return True

            grid[row][col] = 0
    return False



class SudokuSolverApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🧩 Sudoku Solver")
        self.root.geometry("600x700")
        self.root.configure(bg="#f2f2f2")
        self.entries = [[None for _ in range(9)] for _ in range(9)]
        self.create_grid()
        self.create_buttons()

    def create_grid(self):
        frame = tk.Frame(self.root, bg="black")
        frame.place(x=80, y=50)

        for i in range(9):
            for j in range(9):
                entry = tk.Entry(
                    frame,
                    width=3,
                    font=("Arial", 20),
                    justify="center",
                    relief="ridge",
                    borderwidth=1,
                )
                entry.grid(row=i, column=j, padx=1, pady=1, ipady=10)
                if (i // 3 + j // 3) % 2 == 0:
                    entry.configure(bg="#e8f0fe")  # Light blue squares
                else:
                    entry.configure(bg="white")
                self.entries[i][j] = entry

    def create_buttons(self):
        btn_solve = tk.Button(
            self.root,
            text="Solve",
            font=("Arial", 16, "bold"),
            bg="#4CAF50",
            fg="white",
            width=10,
            command=self.solve_puzzle,
        )
        btn_solve.place(x=150, y=630)

        btn_clear = tk.Button(
            self.root,
            text="Clear",
            font=("Arial", 16, "bold"),
            bg="#f44336",
            fg="white",
            width=10,
            command=self.clear_grid,
        )
        btn_clear.place(x=330, y=630)

    def get_grid(self):
        """Read numbers from entry boxes into a 2D list."""
        grid = []
        for i in range(9):
            row = []
            for j in range(9):
                val = self.entries[i][j].get()
                row.append(int(val) if val.isdigit() else 0)
            grid.append(row)
        return grid

    def set_grid(self, grid):
        """Display solved Sudoku on GUI."""
        for i in range(9):
            for j in range(9):
                self.entries[i][j].delete(0, tk.END)
                if grid[i][j] != 0:
                    self.entries[i][j].insert(0, str(grid[i][j]))

    def solve_puzzle(self):
        grid = self.get_grid()
        if solve(grid):
            self.set_grid(grid)
            messagebox.showinfo("✅ Success", "Sudoku solved successfully!")
        else:
            messagebox.showerror("❌ Error", "No valid solution found!")

    def clear_grid(self):
        for i in range(9):
            for j in range(9):
                self.entries[i][j].delete(0, tk.END)



if __name__ == "__main__":
    print("Launching Sudoku Solver GUI...")
    root = tk.Tk()
    app = SudokuSolverApp(root)
    root.mainloop()
