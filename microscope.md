---
title: Microscope Notebook
author: Warren Kincaid
---	 
Notes and new protocol for using Linkam THMS600 stage with microscope
------------------------------
 run 'pandoc microscope.md -o microscope.html' followed by 'pydifft cpb microscope.md' to update and view as an html document to print as a pdf.

 This does not yet auto-update with the saving of the .md file

## Notebook - Olympus Microscope

### Reworked Modified Splat Assay tests 10/8

Jim from McCrone (Sales rep/ Technician) came into the lab:
- Aligning stage using the pinhole and centering using the eyepieces first before transitioning to the camera
- how to calibrate the eyepieces to make focus with the camera
- went through steps for setting up the stage, preparing and inserting the sample
- discussed wet-mounting and using ring with smaller coverslips instead of balancing the larger coverslips on top of the ring

#### Candice's protcol: Out-of-date
1. 40 $^o$C/min, 40 $^o$C, manually adjust LNP;
	- Purge line and chamber of water vapor, perform manual 'burp' of system
	- Need to use PTC connecting pieces to open (and thereby close) valves
	- This will take 5-10 minutes to perform
		- I have come to realize this also uses quite a bit of N$_2$
2. 40 $^o$C/min, -50 $^o$C, 5 min LNP auto;
	- Longer flash-freeze step, rapid cooling
3. 10 $^o$C/min, -6 $^o$C, no hold LNP auto;
	- Relatively rapid warming * This is what was contributing to the temperature discrepencies seen recently
	- This confounded with lack of airflow due to me trying to raise cover slips up inside of chamber (This is my current speculation)
4. 10 $^o$C/min, -6 $^o$C, 125 min (2 hr 5min) hold LNP auto
	- This and the above step could be combined, also has the issue of the above step with too high of a rate

#### Updated Modified Splat Assay (on 10/8/2025)
Beyond modifying the protocol, 

1. 40 $^o$C/min, 40 $^o$C, 3 min hold LNP auto;
	- same as original first step
	- a protocol for this is also in the Linkam THMS600 User Guide
		- [View Manual](MANUAL_CONTINUUM_IN10_DXR_LINKAM_FTIR600_THMS600_AND_HFS600_USERGUIDE.pdf)
2. 40 $^o$C/min, -50 $^o$C, 1 min hold LNP auto;
	- 
3. 5 $^o$C/min, -25 $^o$C, no hold LNP auto;
	- for heating/thawing, want slower rate of temerature change. Better for confidenc ein temperature sensor reading to make intended temperature


