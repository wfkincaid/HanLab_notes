---
title: Microscope Image Processing with ImageJ
author: Warren Kincaid
---	 
Microscope processing with ImageJ {-}
------------------------------
* You will need the image series for a microscope freeze-thaw experiment saved as .TIF images. It will most benefit you to use ones saved with available scale bars imprinted on them. 

* For insight into how these images were collected, see the modified splat assay protocol [here](microscope.html)

* ImageJ doesn't not seem to have an event history/logged actions to go back to previous points. <u>"Undo" will only go back 1 action</u> so make sure each click/action you make is precise. I also recommend saving after each step generally (beyond where indicated in the protocol below) and in the middle of steps if necessary.

In ImageJ;

#. Go to <span style="color:red">`File -> Open`</span> to open a file manager where the desire .tiff file can be selected.
#. Go to <span style="color:red">`Image -> Duplicate`</span> which will create a second copy of the selected image.
#. Save either the original or copy (I typically save the original) to the side/minimize to come back to later and use as a reference.
#. With the duplicate selected, go to <span style="color:red">`Image -> Color -> Split Channels`</span>. This will split the duplicated image into 3 B&W images of the 3 wavelength/color contributions in  the full RGB colored original TIF image.
#. Review the 3 channeled images for which one appears with the most contrast with defined crystal edges, most typically this is the '(red)' channeled images. Save all three outputs to come back to if you're unsure.
#. Select <span style="color:red">`Process -> Enhance Contrast`</span>. In the gui that appears, choose the default saturated pixels (for me this is 35%), and check Normalize and Equalize histogram.
#. Select <span style="color:red">`Process -> Binary -> Convert to Mask`</span>. There is no way to select a light background or which method is used to determine the mask. Because of this, the software will sometimes choose a dark background with the ice crystal boundaries in white. If this happens, select <span style="color:red">`Edit -> Invert`</span> to flip the dark and light colors that make up the image.
#. Select <span style="color:red">`Process -> Binary -> Close`</span>, which connects any pixels that are 1 pixel away from one another. If the backgrounds were flipped and the image is inverted like mentioned above, this can do the opposite of desired and open some boundaries between ice crystal. Keep an eye out for this.
#. This is a good point to save, prior to selecting an area for the actual touching up and analysis.
#. Go to <span style="color:red">`Edit -> Options -> Colors`</span> and for 'Selection:' pick 'Red'. This is for the rectangle/ellipse/text box/etc tools in the lower command panel. Click and draw a circle over the image, you will select dimensions for the circle next. If you find it is needed, you can also make a reference circle on the original image you have minimized by refollowing this and the following step for the upcoming ice crystal selection step.
#. Select <span style="color:red">`Edit -> Selection -> Specify`</span> and in the Specify gui that pops up choose the following dimensions for the circle:

		Width: 2000
		Height: 2000
		X coordinate: 1800
		Y coordinate: 1100
		[x] Oval
		[ ] Constrain square/circle
		[x] Centered
#. If you are performing this analysis on a sample which has many bubbles/speckles or has reflections/shadows, you will need to clean up the image as best you can. You want each ice crystal to be fully enclosed with a black border as best as possible. Using the original colored duplicated image as a reference, you can use the color picker and paintbrush tools to select white and black colors as needed to enclose each crystal (black) and color in each crystal (white) at least near the boundaries to be able to fill that crystal with gray color in the next step. Make these modifications within the circle you have defined first.
#. Save and again generate a duplicated image selecting <span style="color:red">`Image -> Duplicate`</span>. This duplicated image will now be a square defined by the specified circular selection above. 
#. Go again to <span style="color:red">`Edit -> Options -> Colors`</span> and for 'foreground' select 'gray'. Also confirm background is selected as 'black'. Fill in the white space with grey of each ice crystal using the Flood fill tool in the ImageJ tool bar. Do this slowly at first, and be prepared to click `[CTRL] + [Z]` to undo any last move if a crystal is not actually enclosed. You can go back to using the color picker and paintbrush tools to fix crystals as you go.
#. Once you have each crystal filled in with gray as you desired, save the file again as "...\_gray-filled.tif" or something similar/recognizable to you.
#. Select <span style="color:red">`Image -> Adjust -> Threshold`</span>, a gui window will pop up with 2 slider bars adjusting the contribution of white and black to the image based on the images hues already assigned (this is why the ice crystals were filled with grey). Ideally, you can adjust the two bars such that the background (liquid) and the ice crystal outlines are white leaving the previously grey-filled crystals in black. This does not always work and a second best option is to leave just the outlines in whit and to go back in with the Flood fill tool to turn the background from black to white. This can be time consuming and thus a 3rd option is to adjust the threshold slides such that the outlines and background are in black leaving the crystals white and then inverting the image. This can lead to the watershed function at the next step not working as intended because of the specified threshold being flipped after the image's inversion. No matter which method you choose be sure to save the file before and after this step.
#. Select <span style="color:red">`Process -> Binary -> Convert to Mask`</span> on the now threshold applied image.
#. ImageJ's built-in watershed algorithm may work for you to determine and separate a cluster of crystals into individuals but this seems to have worked much better for Candice than me. You can apply this algorithm by selecting <span style="color:red">`Process -> Binary -> Watershed`</span> just be prepared to use `[CTRL] + [Z]` if this does not do as you intend
#. 



