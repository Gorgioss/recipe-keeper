import tkinter as tk  # Import the tkinter module for GUI creation
from tkinter import messagebox, scrolledtext  # Import messagebox and scrolledtext submodules
from PIL import Image, ImageTk  # Import Image and ImageTk submodules from PIL library
import os  # Import the os module for file operations

# Main window class
class MainWindow(tk.Tk):
    """Main window of the Recipe Keeper application."""

    def __init__(self):
        """Initialize the main window."""
        super().__init__()  # Call the constructor of the parent class
        self.title("Recipe Keeper")  # Set the window title
        self.geometry('400x400')  # Set the window size

        # Labels
        self.title_label = tk.Label(self, text="Recipe Keeper", font=("Arial", 24))  # Create a label for the title
        self.title_label.grid(row=0, column=0, sticky='w', padx=20, pady=10)  # Place the title label on the grid

        self.recipe_label = tk.Label(self, text="Enter your recipe:", font=("Arial", 14))  # Create a label for recipe entry
        self.recipe_label.grid(row=1, column=0, sticky='w', padx=20)  # Place the recipe label on the grid

        # Text entry with scrollbar
        self.recipe_entry = scrolledtext.ScrolledText(self, width=40, height=10)  # Create a scrolled text box for recipe entry
        self.recipe_entry.grid(row=2, column=0, padx=20, pady=10)  # Place the text box on the grid

        # Buttons
        self.save_button = tk.Button(self, text="Save Recipe", command=self.save_recipe)  # Create a button to save recipe
        self.save_button.grid(row=3, column=0, sticky='w', padx=20)  # Place the button on the grid

        self.view_button = tk.Button(self, text="View Recipes", command=self.view_recipes)  # Create a button to view recipes
        self.view_button.grid(row=3, column=0, sticky='e', padx=20)  # Place the button on the grid

        self.exit_button = tk.Button(self, text="Exit", command=self.destroy)  # Create a button to exit the application
        self.exit_button.grid(row=4, column=0, padx=20, pady=10)  # Place the button on the grid

        # Image
        img = Image.open("recipe1.png")  # Open the recipe image
        img = img.resize((100, 100), Image.LANCZOS)  # Resize the image
        self.recipe_image = ImageTk.PhotoImage(img)  # Convert image to Tkinter format
        self.image_label = tk.Label(self, image=self.recipe_image, text="", compound="bottom")  # Create a label for the image
        self.image_label.grid(row=5, column=0, padx=20, pady=10)  # Place the image label on the grid

        # Recipe list
        self.recipes = self.load_recipes()  # Load saved recipes from file

    def load_recipes(self):
        """Load saved recipes from a text file."""
        if os.path.exists("recipes.txt"):  # Check if the recipes file exists
            with open("recipes.txt", "r") as file:  # Open the recipes file in read mode
                return file.read().split("\n---\n")  # Read and split the file content by recipe separator
        return []  # Return an empty list if file doesn't exist

    def save_recipe(self):
        """Save a recipe entered by the user."""
        recipe = self.recipe_entry.get("1.0", tk.END).strip()  # Get the recipe text from the text box
        if recipe:  # Check if the recipe is not empty
            self.recipes.append(recipe)  # Add the recipe to the list of recipes
            self.recipe_entry.delete("1.0", tk.END)  # Clear the recipe text box
            messagebox.showinfo("Saved", "Your recipe has been saved!")  # Show a confirmation message
            with open("recipes.txt", "a") as file:  # Open the recipes file in append mode
                file.write(recipe + "\n---\n")  # Write the recipe to the file with separator
        else:
            messagebox.showwarning("Empty", "Recipe box cannot be empty. Please enter a recipe.")  # Show an error message if recipe is empty

    def view_recipes(self):
        """Display saved recipes in a new window."""
        ViewWindow(self)  # Open a new window to display saved recipes

# View window class
class ViewWindow(tk.Toplevel):
    """Window to view saved recipes."""

    def __init__(self, main):
        """Initialize the view window."""
        super().__init__(main)  # Call the constructor of the parent class
        self.title("View Recipes")  # Set the window title

        # Labels
        self.title_label = tk.Label(self, text="Your Recipes:", font=("Arial", 14))  # Create a label for recipe list
        self.title_label.pack()  # Pack the label

        # Text area with scrollbar
        self.scrollbar = tk.Scrollbar(self)  # Create a vertical scrollbar
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)  # Pack the scrollbar to the right side of the window

        self.recipe_text = scrolledtext.ScrolledText(self, yscrollcommand=self.scrollbar.set)  # Create a scrolled text box
        self.recipe_text.pack(expand=True, fill="both")  # Pack the text box to expand and fill the available space
        self.scrollbar.config(command=self.recipe_text.yview)  # Configure the scrollbar to scroll the text box

        # List all recipes
        for i, recipe in enumerate(main.recipes, start=1):  # Iterate through the list of recipes
            self.recipe_text.insert(tk.END, f"Recipe {i}:\n")  # Insert recipe title
            self.recipe_text.insert(tk.END, recipe + "\n\n")  # Insert recipe text with separator

        # Button
        self.close_button = tk.Button(self, text="Close", command=self.destroy)  # Create a button to close the window
        self.close_button.pack()  # Pack the button

        # Image
        img = Image.open("recipe2.png")  # Open the recipe image
        img = img.resize((100, 100), Image.LANCZOS)  # Resize the image
        self.recipe_image = ImageTk.PhotoImage(img)  # Convert image to Tkinter format
        self.image_label = tk.Label(self, image=self.recipe_image, text="", compound="bottom")  # Create a label for the image
        self.image_label.pack()  # Pack the image label

if __name__ == "__main__":
    window = MainWindow()  # Create an instance of the main window class
    window.mainloop()  # Run the main event loop