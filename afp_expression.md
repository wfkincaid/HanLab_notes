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
"RT" = Room temperature
"O/N" - Overnight
"MQ" - Milli-Q system filtered

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
		- Dissolve with filtered H$_2$O in 50 mL falcon tube
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
- Once large cultures reach OD values between 0.6 and 0.8, remove them from the incubator and leave to cool on the counter (if all LCs finish at roughly the same time AND you plan to immediately induce) or in the cold room (4 $^o$C) to cool and pause any further growth
	- You may need to turn of the incubator at this time as well to let it cool to RT for induction purposes
- When ready for induction, add 1 mL of 1 M isopropyl-$\beta$-D-thiogalactopyranoside (IPTG) per 1 L large culture to each large culture flask, swirl, and place in a now RT incubator and leave to shake @ 200 rpm O/N.
	- Take an initial 100 $\mu$L sample in an eppendorf of each LC after induction, add 1 $\mu$L of 2x NuPAGE dye  per 0.1 OD. Leave in freeze for when prepared to run a gel on the expression's progress
- If able, take induction progress samples at 2, 3, and/or 4 hrs after induction as well as at the start of the next day (12 and/or 14 hr) to monitor overexpression of the AFP protein desired being generated in the LC. Similarly add the 2x NuPAGE dye solution as mentioned above

## "Day 3" - Pelleting, Lysis, Size-Exclusion Chromatograpy and Elution
- Take any induction samples mentioned in last bullet as well as a "final" induced LC sample (in an eppendorf, adding 2x NuPAGE dye as above) after the LC has spent 16 hrs shaking in the incubator O/N.
- Mark the large Beckman-Coulter 1000 mL PP bottles to be uniquely identifiable ("A", "B", "C", etc) and in your lab notebook write out the table below

| Bottle ID | empty bottle (g) | bottle + liquid (g) | bottle + pellet (g) | pellet (g) | 
|-----------|------------------|---------------------|---------------------|------------|
|     A     |                  |                     |                     |            |
|     B     |                  |                     |                     |            |
|     C     |                  |                     |                     |            | 
|     D     |                  |                     |                     |            |

- Using the large Beckman-Coulter 1000 mL PP culture bottles, mass each bottle empty (record) and them divide each LC in 500 mL aliqouts between the PP bottles
- Remass each bottle with LC added (record) and balance to the heaviest bottle (highlighted below) by adding small amounts of filtered and autoclaved MQ H$_2$O
- Spin down each (now balanced) LC in the Beckman-Coulter Avanti JXN-26 Centrifuge in the back equipment room which has a rotor designed for these bottles
	- Parameters are 4000 rcf speed for 30 minutes at 4 $^o$C
- After centrifuging, pour off supernatant into a waste container (the large culture flasks can be good for this), carefull not to pour off any of the pellet which should be stuck at the base of the PP bottles
- Reacquire a mass measuremnt for each bottle (with pellets in their bottom) to subtract from the bottle's initial mass to determine the pellet yields for each LC/LC aliquot using to fill-out the table as seen below

| Bottle ID | empty bottle (g) | bottle + liquid (g) | bottle + pellet (g) | pellet (g) | 
|-----------|------------------|---------------------|---------------------|------------|
|     A     |      280.68      |       773.71        |        283.83       |    3.15    |
|     B     |      280.59      |       752.71        |        284.02       |    3.43    |
|     C     |      280.60      | <mark>788.37</mark> |        283.35       |    2.75    | 
|     D     |      280.54      |       752.35        |        282.69       |    2.15    |

- If splitting into 2 days (otherwise skip to 'If/when continuing...' below):
	- resuspend each pellet in 10 mL filtered + autoclaved H$_2$O, vortex as needed
	- pour off into a labeled 50 mL falcon tube, wash the PP bottle with an additional 10 mL filtered + autoclaved H$_2$O, vortexing
	- pour wash into falcon tube, pipette any residual pellet solution that may remain in the PP bottle
	- Balance falcon tubes with $\mu$L amounts of filtered + autoclaved H$_2$O as needed
	- Centrifuge in Eppendorf 5804 R Centrifuge (front of lab) @ 4000 rcf for 10 minutes @ 4 $^o$C
	- Pour off supernatant into waste containers, parafilm falcon tubes with pellets and leave in -80 $^o$C freezer until ready to continue with lysis and purification

- If/when continuing with lysis:
- Resuspend pellet in 20 mL of HEPES buffer into falcon tubes if necessary, vortexing as needed
- to each resuspended pellet, add:
	- 1 protease inhibitor tablet
	- 1 flake (< 10 mg) of DNase

- Parafilm lids and incubate on rotiserrie oscillator in cold room (4 $^o$C) for 30 minutes
- While keeping all samples on ice, sonicate each one at a time using the larger hexagonal tipped sonicator within the soundproof box within the fumehood.
	- parameters to sonicate 10 min, 2 s on/ 2 s off (20 minutes total runtime per sample), with 60 % amplitude
	- Note that this is a rather rapid on/off cycle and high amplitude. YOU MUST monitor the sample in its ice bath as ice will melt before the 20 minutes is up, it is good to start with minimal water and a larger amount of ice in the beaker and add ice periodically every five minutes as it melts throughout the run    

- After sonication, transfer each sample to the 40 (?) mL polypropylene tubes stored above the JXN-26 centrifuge in the instrument lab, label directly on each tube in Sharpie as necessary
- Once each sample is sonicated and transferred, balance against the tube with the greatest mass by pipetting drops of filtered + autoclaved H$_2$O
- On ice, take the balanced samples down stairs to room 2560 (knock on the Meade lab door next door asking them politely to let you in)

- Centrifuge in the Thermo Sorvall RC 6 Plus Centrifuge using the Sorvall SS-34 rotor (it is most typically in the centrifuge already, there are an all black and a black and gold SS-34 rotor, use the all black one). The PP tubes that we transferred the lysate into are specifically designed to fit in this rotor.
	- Precool the centrifuge to 4 $^o$ C before loading samples into the rotor
	- Centrifuge @ 20,000 rcf (xg), for 30 min, @ 4 $^o$C
	- Bring with you/Bring down after:
		- 2x 50 mL falcon tubes for each lysate supernatant sample you will have
		- 0.2 $\mu$L Luer Lock syringe filters


