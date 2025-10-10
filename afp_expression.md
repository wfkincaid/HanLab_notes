---
title: AFP III Expression Protocol
author: Warren Kincaid
---	 
General expression protocol for AFP III
------------------------------
 run 'pandoc afp_expression.md -o afp_expression.html' followed by 'pydifft cpb afp_expression.md' to update and view as an html document to print as a pdf.

 This does not yet auto-update with the saving of the .md file

Abbreviations include:
"SC" - Small Culture
"LC" - Large Culture
"LB" - Laemmli Buffer
"Amp" - Ampicillin
"Kan" - Kanamycin

# AFP III Expression

## "Day 1" - Media Prep and Small Cultures
- Can be split into 2 days 

#### Media Prep -
<u>Small Culture</u>

- LB Media:
	- Use at 25 g LB Miller Broth / 1 L H$_2$O
	- typically make 20 mL volume small cultures in 125 mL Erlenmeyer flasks, this would require 0.5 g LB Broth Miller 
	- Cover tops of flasks with aluminum foil, apply autoclave tape to secure foil
	- Autoclave; Liquid 30 cycle - must reserve in advance!

<u>Large Culture</u>

- (LB Media or M9 Media)
- For LB Media LCs:
	- same as SC, use at 25 g LB Miller Broth / 1 L H$_2$O
	- If we perform an expression with LB media LCs, we will most commonly use LC of 500 mL volumes
	- Cover tops of flasks with aluminum foil, apply autoclave tape to secure foil
	- Autoclave; Liquid 30 cycle - must reserve in advance!
	- 1 M MgSO$_4$:
		- 0.602 g MgSO$_4$ in 5 mL H$_2$O
		- need 1 mL per 500 mL LC
	- 20 % Glucose:
		- 2.00 g glucose in 10 mL H$_2$O
		- need 8.75 mL per 500 mL LC

- For M9 Media LCs:
	- 10X M9 salts buffer:
			- 500 mM Na$_2$HPO$_4$
			- 200 mM KH$_2$PO$_4$
			- 90 mM NaCl
		- Make 1000 mL; 134.035 g Na$_2$HPO$_4$, 27.218 g KH$_2$PO$_4$, 5.2596 g NaCl
			- Weigh each of these out directly into a large beaker with a stirbar
			- Must be attentive, mass by subtraction
			- Once all 3 in beaker, add ~ 800 mL H$_2$0 SLOWLY while swirling beaker
			- Cover beaker with aluminum foil, place on stir plate with low heat and low stir speed
				- stir bar may not spin at first, this is okay, monitor until powders all dissolve
			- Balance pH to 7.4 - 7.5, calibrate probe if needed
				- Be sure to rinse probe and put back in holder securely
			- Transfer buffer solution into 1 L graduated cylinder to fill to 1000 mL
				- be careful to not transfer stir bar into graduated cylinder or buffer bottle
			- Pour back into 1 L beaker, filter buffer solution using Nalgene with Sartorius cellulose filter setup into an autoclaved 1000 mL borosilicate buffer bottle
			- Be sure to label bottle!
	- For M9 Media LCs
		- Commonly use 1000 mL LC; be sure to use the large (2800 mL) Fernbach flask
		- Mix 100 mL of premade 10X M9 salts buffer with 900 mL H$_2$O
		- Cover top with aluminum foil, apply autoclave tape to secure foil
		- Autoclave; Liquid 30 cycle - reservation necessary!
	
	- 2 M MgSO$_4$:
		- 12.037 g MgSO$_4$
		- Dissolve with filtered H$_2$0 in 50 mL falcon tube
		- MgSO$_4$ is exothermic (releases heat), add water slowly
		- vortex and label
	
	- 1 M CaCl$_2$:
		- 5.549 g CaCl$_2$
		- Dissolve with filtered H$_2$0 in 50 mL falcon tube
		- vortex and label

	- 1000X antibiotic stocks:
		- AFP III wt is encoded with ampicillin resistance
		- GB1 tagged AFP III wt and mutants are all encoded with kanamycin resistance
		- These stocks go bad rather quickly, store them in the fridge and make minimal amounts at a time (1-2 expressions worth)
		- For Kan: "1000X" = 50 mg/mL, make in 15 mL falcon tube
			- 250 mg in 5 mL H$_2$O
			- vortex to dissolve, label
		- For Amp: "1000X" = 125 mg/mL, make in 15 mL falcon tube
			- 625 mg in 5 mL H$_2$O
			- vortex to dissolve, label
--- If spliting into 2 days split here
#### Inoculate SCs, start expression (DO AFTER 5 pm)
- Make sure SCs are cooled after autoclaving if done on the same day
- Make sure to have an available incubator set to 37 $^o$C, shaking at 200 rpm
- Also make sure to swap in/out flask holders that fit the relevant flask being used

- In a sterile environment:
	- Add 20 $\mu$L of respective 1000X antibiotic solution, swirl solution to combine
	- Using a pipette tip, scoop a small amount from the glycerol stock of your current intended mutant for that culture in the expression
	- Drop tip with bacterial culture directly into flask
	- Recover with foil lid, place in incubator and leave to grow overnight. Don't leave in incubator > 16 hrs 

## "Day 2" - Large Cultures and Induction
- remove SCs from incubator, leave on counter if using ASAP. Otherwise place on shelf in cold room (4 $^o$C), make sure foil lid on tight.
- This day cannot be split into 2 days but some of the prep can be done beforehand. The supplemental reagents added to the M9 media below an be done the day prior <u>except the antibiotic solution</u> which we want to be as effective as possible and can go bad quickly when not refridgerated.

<u>Large Culture Prep</u>

- Preparing M9 minimal media LCs:
	- (if not done so already) To the autoclaved flasks from the day prior, add [all amounts given /1 L LC]:
		- 1 g NH$_4$Cl
		- 2 g glucose
		- 1000 $\mu$L 2 M MgSO$_4$
		- 100 $\mu$L 1 M CaCl$_2$
		- 10 mg thiamine hydrochloride
		- 10 mg biotin
		- 1000 $\mu$L 1000X antibiotic solution (either ampicillin or kanamycin)
	- Swirl LCs vigorously to dissolve
- Take blank sample (~3 mL) from one LC and save in parafilmed cuvette
- for each LC, prepare a cuvette with a small piece of tape of a specific color at the top of the cuvette as to avoid the spectrometer's path length
	- record which color you have associated with which LC
- Similarly label/indicate a 10 mL serological pipette for each LC to be used for taking LC samples after inoculating and during the monitoring of the large cultures growth	
- prepare in you lab notebook a table like the example below;
	
| time | t (min) | Blank | LC 1 | LC 2 | 
|------|---------|-------|------|------|
| 10:25 AM | 0 min | 0.00 | 0.08 | 0.10 |
| 11:30 AM | 65 min | 0.00 | 0.10 | 0.14 |
| 12:30 PM | 125 min | 0.00 | 0.24 | 0.44 |
.
.	
.
- Using a sterile 5 or 10 mL serological pipette (separate from the pipettes mentioned above), pipette 5 mL of each small culture (swirl before pipetting) into their respective large culture
- Place in incubator (37 $^o$C, 200 rpm) and take ~3 mL sample of LC for initial OD600 reading ("0 min"), return sample to LC after OD measurement
- Repeat sampling, measuring and replenishing large cultures hourly to monitor their growth. Once growth (OD600 value) begins to spike upward, decrease monitoring intervals to 30 min until OD600 values reach between 0.6 and 0.8. BE AWARE of how OD can change rapidly further into bacterial cells growth curve to avoid over growing cultures.



