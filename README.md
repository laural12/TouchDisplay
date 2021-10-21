# Touch Display

The python file TouchDisplay.py interfaces through a serial port with a Teensyduino device. The Teensyduino device runs the ReportQuadrant.ino code to report touch data it receives from a Cirque circular touch pad sensor. TouchDisplay then displays the touched quadrant in a simple graphical representation.

## Dependencies

TouchDisplay relies on pyserial and matplotlib (pyplot and patches).
