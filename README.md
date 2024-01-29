<h1>Motion Visualizer</h1>

This repository contains scripts which allow for basic visualization of motion on a camera stream. Motion is detected by the difference between pixels between frames. This means that if the updated pixel has the same value as the previous cycle, no motion will be detected in that pixel. As a result, when objects and backgrounds of similar colors are used, the highlighting of motion may not be as intense.

<h2>Dependencies</h2>
At present, this repository only makes use of the <strong>numpy</strong> and <strong>CV2</strong> python libraries.


<h2>Examples</h2>
To run the following examples enter the provided command in a terminal who's current working directory is <code>path/to/motion_visualizer</code>

<h3>basic_visualizer_Grayscale.py</h3>
This script turns the image into grayscale and subtracts the old frame from the new frame. As a result, the more difference there is, the higher the value and the more white the pixels where motion occurs will appear. (Note: given the use of uints there is a need to protect against overflow. This is not yet fully implemented).<br>
<code>python3 basic_visualizer_Grayscale.py</code><br>
![Result of Grayscale Visualizer](images/example_of_grayscale.png?raw=true)

<h3>basic_visualizer_RGB.py</h3>
This script directly subtracts the old image from the new image. This still results in areas with greater change appearing more, but can also result in artifacts due to overflow (such as color inversion). (Note: given the use of uints there is a need to protect against overflow. This is not yet fully implemented).<br>
<code>python3 basic_visualizer_RGB.py</code><br>
![Result of RGB Visualizer](images/example_of_rgb.png?raw=true)

<h3>highlight_movement_visualizer.py</h3>
This script takes the output from the grayscale visualizer and adds it to the <strong>Red</strong> channel of the new image. This results in the areas with motion being highlighted in red based on the amount of motion. There is currently an issue where there will also be a teal after image. This is likely an overflow issue and will be corrected in the future.
<code>python3 highlight_movement_visualizer.py</code><br>
![Result of Highlight Visualizer](images/example_highlight.png?raw=true)