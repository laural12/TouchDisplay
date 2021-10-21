import serial
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

# Define some constants
width = 0.5
height = 0.5
x0 = 0
y0 = height
x1 = width
y1 = height
x2 = width
y2 = 0
x3 = 0
y3 = 0

# Set up serial port
serialPort = serial.Serial(port="COM4", baudrate=9600)
serialString = ""  # Used to hold data coming over UART

# Set up plot
plt.ion()
plt.show()
fig = plt.figure()
ax = fig.add_subplot(111, aspect='equal')
patch = ax.add_patch(Rectangle((0, 0), 0.5, 0.5,
    alpha=0,color="white")) # Create the patch that we will update
fig.canvas.draw()
fig.canvas.flush_events()

while 1:
    # Wait until there is data waiting in the serial buffer
    if serialPort.in_waiting > 0:
        # Read data out of the buffer until a carraige return / new line is found
        serialString = serialPort.readline()
        # Print the contents of the serial data
        try:
            print(x:=serialString.decode("Ascii"), end='')
            
            # Extract the quadrant number from the ascii string
            str = x[1:2:]
            quadrant = -1
            if str.isnumeric():
                quadrant = int(str)
            

            # Draw a new square in the corresponding quadrant
            ax.clear()
            if quadrant == 0:
                patch = ax.add_patch(Rectangle((x0, y0), width, height,
                    alpha=1,color="red"))
                plt.text(x0 + width/2, y0 + height/2, "Q0", ha="center", fontsize="xx-large")
            elif quadrant == 1:
                patch = ax.add_patch(Rectangle((x1,y1), width, height,
                    alpha=1,color="yellow"))
                plt.text(x1 + width/2, y1 + height/2, "Q1", ha="center", fontsize="xx-large")
            elif quadrant == 2:
                patch = ax.add_patch(Rectangle((x2, y2), width, height,
                    alpha=1,color="lime"))
                plt.text(x2 + width/2, y2 + height/2, "Q2", ha="center", fontsize="xx-large")
            elif quadrant == 3:
                patch = ax.add_patch(Rectangle((x3, y3), width, height,
                    alpha=1,color="blue"))
                plt.text(x3 + width/2, y3 + height/2, "Q3", ha="center", fontsize="xx-large")
            fig.canvas.draw()
            fig.canvas.flush_events()

        except Exception as e:
            print(e)
            pass