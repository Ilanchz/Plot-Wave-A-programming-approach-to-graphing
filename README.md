I-Grapher-Overview:

A simple python application with Tkinter GUI and Mysql connector to main record and therfore to generate and plot explicit mathematics functions on a canvas along with built in methods to email (for bug fixes(SMTP)).


Notes on patches:

(I-Grapher Version 8.0.0 Last Updated: 30th June 2021)(Note: Web browser may block the application due to unknown source installation, to run the it select keep file through advanced settings and continue)

Independent value finder and Grapher (I-Grapher)
Python program to convert input into python readable format and finding coordinates using Loops and "connecting the dots".
Data density of each graphed curve directly proportional to the precision given by user. It is the difference between successive x values taken to find the Y-coordinates. High precision leads to error in computer with less processor speeds.

How to Use:

1.


A) Enter the Explicit Functions into the text box and press enter or give "Execute". e.g sin(x) cos(x) tan(x) log(x^2+5x-x^3) xsin(x)

B) Enter Functions in the form of (f1(x),f2(x)) (parametric form). e.g (cos(x),sin(x)) (x^2,x^3)

C) Enter Coordinate of a point to Drop a Dot and two coordinates to draw a line from point 1 to point 2.
e.g, (3,4): Drops a red dot at (3,4)
(3,4),(6,7) Draws a line from (3,4) to (6,7)
Similarly adding further points draws line to those points.

D) All the above mentioned can also be done using the variable "y" by using invert variable function which interchages x and y axis of the graph.
e.g. (1,4),(-3,5),(5,-8),(0,3),(-9,-4)... On executing a line will be drawn from (1,4) to (-3,5) and (-3,5) to (5,-8) and so on.

2. Use precision to increase or decrease the datapoints. (Note high precision requires more time for rendering graphs)
3. Use Domain grid to increase or decrease range of function.
4. Right click to mark a point and left click on the point upto where the line should be drawn. Click the scroll button to get rid of a marked point in case a line is not required.
5. Also freehand drawing can be drawn by clicking and dragging the mouse.
6. Use scroll to zoom in and out of the graph.
7. Select Marker colour for changing the colour of to-be-doodled-upon works(mouse pen) and plotter colour for changing colour of function's graphs(rendered graphs).
8. Help function is to enter comments and messages.
a. The search box allows to search comments (Simple Word Matching Process)
b. FeedBack Entered is Emailed to Creater. (SMTP)

9.

A) Check the "Effect" box to see the on going progress of the potting process.

B) To cancel the implementation of a function while effects is ON, click on the "X" button near the completition status bar.

10. Dark Mode can be turned on and off for better User Interface
11. Settings can be accessed to:

A) Change the backlight of canvas.

B) Change the Size of the given canvas.

C) To save Inputted memory in MySql local Database. (Optional)

12. Use Help Button to Post Comments/Feedback/Bugs to me. Make sure Internet is connected. (Received via gmail)
13. Make Sure Logo and The EXE file are on same folder>
14. Use Settings to Optimise User Interface.

Have Fun! :)

Recent Fixes:
Improved Dark Mode.
Improved Efficiency in CPU usage.
Improved all Functions.
Improved Settings and Included more Features
Improved Colour Selection
Improved Loading Bar
Shifting Origin
