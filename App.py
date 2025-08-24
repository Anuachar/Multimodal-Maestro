import tkinter as tk
from tkinter import messagebox, ttk
from PIL import Image, ImageTk
import subprocess
import os
import threading


def start_hand_cursor_controller():
    """Start the hand cursor controller script in a separate process."""
    try:
        script_path = os.path.abspath("hand_controller.py")
        if not os.path.exists(script_path):
            messagebox.showerror("Error", "Hand controller script not found!")
            return
        subprocess.Popen(["python", script_path], shell=False)
        messagebox.showinfo("Hand Controller", "Hand controller started successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to start hand controller: {str(e)}")


def start_gaze_cursor_controller():
    """Start the gaze cursor controller script in a separate process."""
    try:
        script_path = os.path.abspath("gaze_controller.py")
        if not os.path.exists(script_path):
            messagebox.showerror("Error", "Gaze controller script not found!")
            return
        subprocess.Popen(["python", script_path], shell=False)
        messagebox.showinfo("Gaze Controller", "Gaze controller started successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to start gaze controller: {str(e)}")


def show_about_app():
    """Show information about the app."""
    messagebox.showinfo(
        "About App",
        "This application allows users to control their cursor using either hand gestures or eye gaze. "
        "Designed for accessibility and efficiency, it provides seamless control for everyone."
    )


def show_team_members():
    """Show information about the team members."""
    messagebox.showinfo(
        "Team Members",
        "1. Sandeep Telkar R\n2. Akanksha S\n3. Ananya R\n4. Dhanya M Bhat\n5. Nireeksha B"
    )


def start_slideshow(slideshow_label, images):
    """Start a slideshow of images."""
    def run_slideshow():
        idx = 0
        while True:
            try:
                img = Image.open(images[idx % len(images)])
                img = img.resize((400, 200), Image.ANTIALIAS)
                img_tk = ImageTk.PhotoImage(img)
                slideshow_label.configure(image=img_tk)
                slideshow_label.image = img_tk
                idx += 1
            except FileNotFoundError:
                messagebox.showerror("Error", f"Image file not found: {images[idx % len(images)]}")
                break
            slideshow_label.after(2000)  # Change every 2 seconds

    threading.Thread(target=run_slideshow, daemon=True).start()


def main():
    """Create the main application window."""
    app = tk.Tk()
    app.title("Multimodal Cursor Controller")

    # Make window flexible
    app.geometry("600x600")
    app.minsize(400, 400)

    # Create a canvas for scrollable content
    canvas = tk.Canvas(app)
    canvas.pack(side="left", fill="both", expand=True)

    # Create a scrollbar for vertical and horizontal scrolling
    scrollbar_y = tk.Scrollbar(app, orient="vertical", command=canvas.yview)
    scrollbar_y.pack(side="right", fill="y")
    scrollbar_x = tk.Scrollbar(app, orient="horizontal", command=canvas.xview)
    scrollbar_x.pack(side="bottom", fill="x")

    # Configure the canvas to work with the scrollbars
    canvas.configure(yscrollcommand=scrollbar_y.set, xscrollcommand=scrollbar_x.set)

    # Create a frame that will hold the content inside the canvas
    scrollable_frame = tk.Frame(canvas)

    # Create a window in the canvas that can be scrolled
    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

    # Add a tabbed interface
    notebook = ttk.Notebook(scrollable_frame)

    # Home Tab
    home_tab = ttk.Frame(notebook)
    notebook.add(home_tab, text="Home")

    # About Tab
    about_tab = ttk.Frame(notebook)
    notebook.add(about_tab, text="About App")

    # Team Tab
    team_tab = ttk.Frame(notebook)
    notebook.add(team_tab, text="Team Members")

    notebook.pack(expand=True, fill="both")

    # Add a slideshow to the Home Tab
    slideshow_label = tk.Label(home_tab)
    slideshow_label.pack(pady=10)
    slideshow_images = ["hand1.jpg", "hand2.jpg", "hand3.jpg"]  # Add your image paths here
    start_slideshow(slideshow_label, slideshow_images)

    # Add description boxes with detailed information
    frame = tk.Frame(home_tab)
    frame.pack(pady=20)

    # Hand gestures description box
    hand_box_heading = tk.Label(frame, text="Control your cursor using hand gestures.", bg="lightblue", font=("Arial", 12, "bold"), padx=10, pady=10)
    hand_box_details = tk.Label(frame, text="The Hand Controller in your web app is a feature that allows users to control their computer using simple hand gestures, much like using a mouse or keyboard. Instead of touching a screen or using a traditional input device, the app tracks the movement of your hands and translates that into actions on the computer.\n\n"
                                            "Here’s how it works:\n\n"
                                            "Left Click: If you bring your thumb and index finger close together, it's like clicking the mouse to select things.\n"
                                            "Right Click: If your index finger is above your thumb, it simulates a right-click, just like on a regular mouse.\n"
                                            "Scroll: If you make specific hand gestures, you can scroll up or down, just like using a mouse wheel.\n"
                                            "Draw: If you keep your thumb and index finger together, you can draw on the screen, like using a paintbrush.\n\n"
                                            "The Hand Controller is designed to make it easier for people to interact with their devices without using a traditional mouse or keyboard, making it more accessible, especially for users with disabilities or those who prefer hands-free control. It's intuitive, simple to use, and just requires hand movements in front of your camera to get started.", 
                                            wraplength=400, bg="lightblue", font=("Arial", 10), padx=10, pady=10)

    # Eye gaze description box
    gaze_box_heading = tk.Label(frame, text="Control your cursor using eye gaze.", bg="lightgreen", font=("Arial", 12, "bold"), padx=10, pady=10)
    gaze_box_details = tk.Label(frame, text="The Gaze Controller in this web application is designed to let you control the cursor on your screen just by using your eyes! Instead of using a mouse or keyboard, the system tracks your eye movements and blinks to perform actions like moving the cursor, clicking, and even capturing images of your eye when you blink.\n\n"
                                             "Here’s how it works in simple terms:\n\n"
                                             "Cursor Movement: The app tracks where you’re looking with your eyes and moves the cursor smoothly in that direction, just like moving the mouse with your hand.\n"
                                             "Clicking: If you blink with one eye (left or right), it triggers a click. A left blink will simulate a left-click, and a right blink will simulate a right-click.\n"
                                             "Eye Image Capture: The app also saves images of your eyes when you blink, which can be useful for various applications or training purposes.\n\n"
                                             "This technology is especially helpful for people who may have difficulty using a traditional mouse or keyboard, offering a hands-free way to interact with the computer. It makes tasks like browsing, gaming, or drawing much easier using just your eyes.", 
                                             wraplength=400, bg="lightgreen", font=("Arial", 10), padx=10, pady=10)

    hand_box_heading.grid(row=0, column=0, padx=10, pady=10)
    hand_box_details.grid(row=1, column=0, padx=10, pady=10)
    gaze_box_heading.grid(row=0, column=1, padx=10, pady=10)
    gaze_box_details.grid(row=1, column=1, padx=10, pady=10)

    # Add action buttons below description boxes
    button_frame = tk.Frame(home_tab)
    button_frame.pack(pady=20)
    hand_button = tk.Button(button_frame, text="Start Hand Controller", command=start_hand_cursor_controller, bg="blue", fg="white", font=("Arial", 12))
    gaze_button = tk.Button(button_frame, text="Start Gaze Controller", command=start_gaze_cursor_controller, bg="green", fg="white", font=("Arial", 12))
    hand_button.pack(side="left", padx=10)
    gaze_button.pack(side="left", padx=10)

    # About App Tab Content
    about_label = tk.Label(about_tab, text="This app provides cursor control using hand gestures and eye gaze.\n"
                                           "Designed for accessibility and precision control.", font=("Arial", 12), wraplength=400)
    about_label.pack(pady=20)

    # Team Members Tab Content
    team_button = tk.Button(team_tab, text="Show Team Members", command=show_team_members, font=("Arial", 12))
    team_button.pack(pady=20)

    # Update scroll region whenever the window content changes
    scrollable_frame.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))

    # Run the application
    app.mainloop()


if __name__ == "__main__":
    main()
