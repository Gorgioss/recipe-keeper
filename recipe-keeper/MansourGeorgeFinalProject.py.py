import tkinter as tk
from tkinter import messagebox, scrolledtext
from PIL import Image, ImageTk
import os

# Main window class
class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Recipe Keeper")
        self.geometry('400x400')

        # Labels
        self.title_label = tk.Label(self, text="Recipe Keeper", font=("Arial", 24))
        self.title_label.grid(row=0, column=0, sticky='w', padx=20, pady=10)

        self.recipe_label = tk.Label(self, text="Enter your recipe:", font=("Arial", 14))
        self.recipe_label.grid(row=1, column=0, sticky='w', padx=20)

        # Text entry with scrollbar
        self.recipe_entry = scrolledtext.ScrolledText(self, width=40, height=10)
        self.recipe_entry.grid(row=2, column=0, padx=20, pady=10)

        # Buttons
        self.save_button = tk.Button(self, text="Save Recipe", command=self.save_recipe)
        self.save_button.grid(row=3, column=0, sticky='w', padx=20)

        self.view_button = tk.Button(self, text="View Recipes", command=self.view_recipes)
        self.view_button.grid(row=3, column=0, sticky='e', padx=20)

        self.exit_button = tk.Button(self, text="Exit", command=self.destroy)
        self.exit_button.grid(row=4, column=0, padx=20, pady=10)

        # Image
        img = Image.open("recipe1.png")
        img = img.resize((100, 100), Image.LANCZOS)
        self.recipe_image = ImageTk.PhotoImage(img)
        self.image_label = tk.Label(self, image=self.recipe_image, text="", compound="bottom")
        self.image_label.grid(row=5, column=0, padx=20, pady=10)

        # Recipe list
        self.recipes = self.load_recipes()

    def load_recipes(self):
        if os.path.exists("recipes.txt"):
            with open("recipes.txt", "r") as file:
                return file.read().split("\n---\n")
        return []

    def save_recipe(self):
        recipe = self.recipe_entry.get("1.0", tk.END).strip()
        if recipe:
            self.recipes.append(recipe)
            self.recipe_entry.delete("1.0", tk.END)
            messagebox.showinfo("Saved", "Your recipe has been saved!")
            with open("recipes.txt", "a") as file:
                file.write(recipe + "\n---\n")
        else:
            messagebox.showwarning("Empty", "Recipe box cannot be empty. Please enter a recipe.")

    def view_recipes(self):
        ViewWindow(self)

# View window class
class ViewWindow(tk.Toplevel):
    def __init__(self, main):
        super().__init__(main)
        self.title("View Recipes")

        # Labels
        self.title_label = tk.Label(self, text="Your Recipes:", font=("Arial", 14))
        self.title_label.pack()

        # Text area with scrollbar
        self.scrollbar = tk.Scrollbar(self)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.recipe_text = scrolledtext.ScrolledText(self, yscrollcommand=self.scrollbar.set)
        self.recipe_text.pack(expand=True, fill="both")
        self.scrollbar.config(command=self.recipe_text.yview)

        # List all recipes
        for i, recipe in enumerate(main.recipes, start=1):
            self.recipe_text.insert(tk.END, f"Recipe {i}:\n")
            self.recipe_text.insert(tk.END, recipe + "\n\n")

        # Button
        self.close_button = tk.Button(self, text="Close", command=self.destroy)
        self.close_button.pack()

        # Image
        img = Image.open("recipe2.png")
        img = img.resize((100, 100), Image.LANCZOS)
        self.recipe_image = ImageTk.PhotoImage(img)
        self.image_label = tk.Label(self, image=self.recipe_image, text="", compound="bottom")
        self.image_label.pack()

if __name__ == "__main__":
    window = MainWindow()
    window.mainloop()