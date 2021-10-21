# Touch Display

The python file CirqueTouchPadPlot.py interfaces through a serial port with a Teensyduino device. The Teensyduino device runs the ReportQuadrant.ino code to report touch data it receives from a Cirque circular touch pad sensor. CirqueTouchPadPlot then displays the touched quadrant in a simple graphical representation.

## Dependencies

CirqueTouchPadPlot.py relies on pyserial and matplotlib (pyplot and patches).
