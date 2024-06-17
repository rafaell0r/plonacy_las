import tkinter as tk
from pozar import forest_fire_simulation

def start_simulation():
    size = int(size_entry.get())
    p = float(p_entry.get())
    f = float(f_entry.get())
    r = float(r_entry.get())
    steps = int(steps_entry.get())

    forest_fire_simulation(size, p, f, r, steps)


root = tk.Tk()
root.title("Forest Fire Simulation Parameters")


tk.Label(root, text="Size:").grid(row=0, column=0, padx=10, pady=5, sticky='w')
size_entry = tk.Entry(root)
size_entry.grid(row=0, column=1, padx=10, pady=5)
size_entry.insert(tk.END, '100')

tk.Label(root, text="Tree Density (p): [0.00-1.00]").grid(row=1, column=0, padx=10, pady=5, sticky='w')
p_entry = tk.Entry(root)
p_entry.grid(row=1, column=1, padx=10, pady=5)
p_entry.insert(tk.END, '0.4')

tk.Label(root, text="Lightning Probability (f): [0.00-1.00]").grid(row=2, column=0, padx=10, pady=5, sticky='w')
f_entry = tk.Entry(root)
f_entry.grid(row=2, column=1, padx=10, pady=5)
f_entry.insert(tk.END, '0.001')

tk.Label(root, text="Regrowth Probability (r): [0.00-1.00]").grid(row=3, column=0, padx=10, pady=5, sticky='w')
r_entry = tk.Entry(root)
r_entry.grid(row=3, column=1, padx=10, pady=5)
r_entry.insert(tk.END, '0.01')

tk.Label(root, text="Steps:").grid(row=4, column=0, padx=10, pady=5, sticky='w')
steps_entry = tk.Entry(root)
steps_entry.grid(row=4, column=1, padx=10, pady=5)
steps_entry.insert(tk.END, '1000')


start_button = tk.Button(root, text="Start Simulation", command=start_simulation)
start_button.grid(row=5, column=0, columnspan=2, pady=10)


root.mainloop()
