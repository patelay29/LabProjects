from Flowrate import flowrate
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import filedialog

def upload_file():
    global selected_file_path
    selected_file_path = filedialog.askopenfilename()
    if selected_file_path:
        selected_file_label.config(text=f"Selected File: {selected_file_path}")





categories = []
values = []
ask = "yes"
while ask == "yes":
    # Create a GUI window
    root = tk.Tk()
    root.title("File Upload")

    # Create a button to open the file dialog
    upload_button = tk.Button(root, text="Upload File", command=upload_file)
    upload_button.pack(pady=20)

    # Create a label to display the selected file path
    selected_file_label = tk.Label(root, text="Selected File: ")
    selected_file_label.pack()

    # Initialize the selected_file_path variable
    selected_file_path = None

    # Start the GUI event loop
    root.mainloop()
    data = flowrate(selected_file_path)
    flow = input("What is the flowrate ratio in this video?")
    stringthreshold = input("what is your threshold value, brighter needs larger value?")
    threshold = int(stringthreshold)
    data.setThreshold(threshold)
    data.showFrame()
    print("what is your x1, first detection point, make sure it isn't within a droplet initially?")
    data.setx1()
    print(f"{data.x1}")
    print("what is your x2, second detection point, make sure it isn't within a droplet initially?")
    data.setx2()
    print(f"{data.x2}")
    print("what is your y, top left corner, make sure it is outside of droplet?")
    data.sety()
    print(f"{data.y}")
    print("what is your height of rectangle, choose point at the botoom of rectangle, make sure it is larger than height of droplet?")
    data.setHeight()
    print(f"{data.height}")
    data.showRectangle()
    data.showCheck()
    print(f"your RO1 and ROI2 number of pixels should = {data.height}!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    change = input("Do you need to change any parameters?")
    while change == "yes":
        askx1 = input("Do you need to change x1?")
        while askx1 == "yes":
            print("what is your x1, first detection point, make sure it isn't within a droplet initially?")
            data.setx1()
            data.showRectangle()
            askx1 = input("Do you need to change x1?")
        askx2 = input("Do you need to change x2?")
        while askx2 == "yes":
            print("what is your x2, second detection point, make sure it isn't within a droplet initially?")
            data.setx2()
            data.showRectangle()
            askx2 = input("Do you need to change x2?")
        asky = input("Do you need to change y?")
        while asky == "yes":
            print("what is your y, top left corner, make sure it is outside of droplet?")
            data.sety()
            data.showRectangle()
            asky = input("Do you need to change y?")
        askHeight = input("Do you need to change the height?")
        while askHeight == "yes":
            print(
                "what is your height of rectangle, choose point at the botoom of rectangle, make sure it is larger than height of droplet?")
            data.setHeight()
            data.showRectangle()
            askHeight = input("Do you need to change the height?")
        askt = input("Do you need to change threshold?")
        while askt == "yes":
            stringthreshold = input("what is your threshold value?")
            threshold = int(stringthreshold)
            data.setThreshold(threshold)
            data.showFrame()
            askt = input("Do you need to change threshold?")
        data.showCheck()
        print(f"your RO1 and ROI2 number of dark pixels should = {data.height}!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        change = input("Do you need to change any parameters?")
    frameRateString = input("what is framerate?")
    framerate = float(frameRateString)
    data.dropletPerSecond(framerate)
    categories.append(flow)
    values.append(data.droplet_per_second)
    ask = input("Do you have another flowrate?")

# Create a bar graph
plt.bar(categories, values)

# Add labels and a title
plt.xlabel('Flowrate Ratio')
plt.ylabel('Droplet per Second')
plt.title('Microfluidics')


save = input("Do you want to save plot?")
if save == "yes":
    file = input("file name: ")
    aspect_ratio = 16 / 9
    fig = plt.gcf()
    fig.set_size_inches(fig.get_size_inches() * aspect_ratio)
    plt.savefig(file, dpi=300)
    plt.show()
else:
    plt.show()
