# Stage 1
## Components:
- [Motion Sensor](https://www.componentsinfo.com/hc-sr501-module-pinout-datasheet/)

## Description:
At this stage, the device's function is very simple. Upon detecting motion, it continually prints alarm to the screen along with the number of times the word alarm has been printed to the screen, starting at 0. The motion sensor, being a complex circuit itself, has three adjustable elements: 2 potentionmeters adjusting the **sensitivity** and the **off-time**, and a pair of three pins that set the sensor to either **repeatable** mode or **non-repeatable** mode. Repeatable mode will set the Dout pin to high temporarily regardless of whether the thing that triggered it is still in range.  Non-Repeatable mode will set the Dout pin to high for as long as the triggering object is within range. For my circuit, I set the **sensitivity** to *3 meters* (the minimum), the **off-time** to *0.3 seconds* (the minimum), and the mode to **Repeatable(H)** mode.
## Diagram
![Circuit Diagram](CircuitDiagrams/CIS-220-Fundamentals-of-Unix-Final-Project-Stage-1.png)
## Topdown Photo
![Top Down Photo](TopDownPhotos/CIS-220-Final-Project-Stage-1-Top-Down-Photo.JPG)
## Video Demonstration
![Video Demonstration](VideoDemonstrations/CIS-220-Final-Project-Stage-1.mp4)