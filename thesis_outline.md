---
title: "Investigations of Interfacial Water at Multiple Scales of View: from Optical Spectroscopy to Spin Physics"
bibliography: Thesis.bib
pairDelim: '&#32;and&#32;'
author: |
    Warren Kincaid
linkReferences: true
WKcolor: "#d05aff"
---

# Introduction

Water is a ubiquitous compound, in high percentage across our planet as well as
with our bodies and cells.
It is essential to nearly all life on our planet and
is largely considered the most important substance in the world [Kontogeorgis
2022].
And yet there are still part's of water's behavior and properties that
are not fully understood.

One thing that makes water so unique is that unlike many other molecules of
similar shape and size, water is far more cohesive due to its ability to form
hydrogen bonds.
This enables competing properties of cohesion and adhesion in
water.
In bulk solution, water forms a dispersed tetrahedral structure
influenced by its own cohesive hydrogen bonding capabilities but as water is in
close vicinity with other species in solution these same hydrogen bonding
properties also interact with those species, affecting the structure of the
hydration network in these regions [Lang 2024].

The properties of water affect dynamic processes as water's behavior affects
nearly all interactions in aqueous solutions, including protein-protein
interactions, protein-ligand binding events, and protein folding.
We want a signature of water's behavior at a surface and these dynamics can't be fully
predicted through simulations.

## Ice & Ice Recrystallization Inhibition

<WKcom> Include:
- PVA is most effective synthetic chemical ice-inhibition molecule currently
	widely available [Burkey 2018, proabably others as well]
- 



## Magnetic Resonance

Magnetic resonance offers a broad avenue of spectroscopic techniques to
investigate and measure the magnetic spins engaged in complex chemical and
biological systems.
Dynamic Nuclear Polarization is a hyperpolarization method
that serves as a tool to enhance NMR sensitivity through the enhancement of
the NMR signal by pulling polarization from electron spins [Griesinger 2012].
In the liquid state, ODNP relies on molecular motion for the measure of
translation dynamics, which serves as a handle for the enthalpy,
residual
entropy, activation energy, etc of the aqueous system.

Overhauser Dynamic Nuclear Polarization is a tool, which in the liquid state is
used as a measure of translation dynamics.
ODNP can give us insight into the
thermodynamics and kinetics at a macromolecular surface and assist in capturing
a signature of water's behaviors in these localities.
Determining differences
in water's dynamics along a molecule's surface can go on to support broader
understandings of water's structure.

## ODNP

ODNP spectroscopy combines NMR and EPR techniques to study the hydration
dynamics along the surfaces of large molecules.
The structure of liquid water
is comprised of a network of hydrogen bonds that exhibit different properties
relative to the water molecules’ proximity to and along the surface of
macromolecules.
The macromolecule fundamentally alters the dynamics of this
hydrogen bond matrix within 2-3 layers from the macromolecular surface known as
the hydration layer.
The properties of a hydration layer exhibits
explicitly different dynamics and hydrogen bond configurations than that of
bulk water [Griesinger 2012, Franck 2019].

With our current instrumentation setup, we can perform ODNP on a range of
systems but are limited by samples of low spin concentration and/or low aqueous
content, which can lead to small ODNP enhancement and limited NMR sensitivity
respectively.
We would like to address these challenges with better integrated
NMR detection that does not sacrifice sample size without causing sample
heating or compromise proton signal detection.
We are designing an ODNP
resonator which integrates a higher filling-factor, solenoid NMR coil in a
rectangular EPR cavity and to perform this investigation, we are using a novel
eigenmode-based design strategy that investigates both the integration of the
solenoid NMR probe into the EPR cavity as well as the coupling of a waveguide
to the ODNP resonator in an nontraditional way.

# Investigations of poly(vinyl alcohol) ice recrystallization inhibition activities
## Prelude

The content of the following chapter is a part of the upcoming publication
"Water structuring on poly(vinyl alcohol) surfaces underlies ice
recrystallization inhibition activity" by Pravin P. Taware, Warren F. Kincaid,
Maria-Jose Ferre, Candice Crilly, Emma Gubbins, Zachary W. Brotherton,
Lokeswara Rao, Alison Karis Kim, Rajat Kumar, Brady Axtell, Nathaniel A. lynd,
Valeria Molinero, Baron Peters, Konrad Meister, Mary Shultz, Songi Han

<WKcom>
Include description of chapter being from currently (soon to be/hopefully submitted) manuscript

Include my contributions to studies - Mod splat assay
</WKcom>

## Introduction

Ice recrystallization inhibition (IRI) plays a pivotal role in various
applications where controlling ice crystal growth is essential
(1-6; Hedir 2017, Zhao 2023, Rajan 2021, Liu 2021, Biggs 2019, Elliot 2017).
In
cryopreservation, a principal challenge is to prevent cellular damage caused by
ice crystal formation and growth during freeze-thaw cycles.
Cryoprotective
solutes, such as dimethyl sulfoxide (DMSO), glycerol, ethylene glycol,
propylene glycol, and trehalose, are widely used in cryopreservation mixtures
to mitigate intracellular ice formation and protect cells and tissues from
damage (6–10; Elliot 2017, Best 2015, Cypser 2018, Ghafari 2011, Phillips 2016).
However, at the concentrations necessary for efficacy, often
exceeding 10% by volume (v/v), these agents can induce cytotoxicity,
oxidative
damage, osmotic imbalances, and functional impairments of the preserved
materials (7–9).
Antifreeze proteins (AFPs), sourced from freeze-tolerant
organisms, offer superior capability compared to PVA for inhibiting ice growth
and recrystallization at substantially lower concentrations,
typically in the
micromolar range (11–14).
Despite their potency, AFPs are not viable solutions
for widespread applications because of challenges in large-scale purification
and shelf stability.
Applications affected by ice formation span across length
scales, from sub-micrometers to meters, for protein and cell preservation (3,
15, 16), the control over texture and sensory qualities of frozen food products
(17), or mitigating ice accumulation on airplane wings, wind turbines,
and in
concrete infrastructure, thereby enhancing material durability and
performance(4).
Hence, synthetic, scalable, and biocompatible materials with
robust IRI effects are needed to address and fulfill these demands.

Poly (vinyl alcohol) (PVA) is one of the few synthetic polymers that exhibits a
robust inhibitory effect on ice recrystallization and has been extensively
studied for its applications in cryopreservation.
It prevents small ice
crystals from growing into larger ones (1, 4, 18), but it is not widely used in
practice.
This is likely because PVA typically requires concentrations
~1,000-fold higher than those of natural AFPs to achieve comparable effects as
AFPs.
Development efforts to optimize PVA’s IRI activity is an active area of
research, given that PVA is cost-effective, readily scalable,
and
biocompatible(4), rendering it particularly attractive for cryobiology
applications.
Improving PVA's IRI activity through chemical modifications has
shown limited success, and some approaches have yielded marginal improvements
in enhancing activity (10, 15).
Studies investigating the structure–function
relationship of PVA have demonstrated that polymer chain length (19, 20),
degree of hydrolysis, and side-chain modifications influence its IRI activity.
These observations have been interpreted to suggest that the alignment of PVA’s
hydroxyl motifs with ice lattice features enables hydrogen bonding that is the
defining mechanism for suppressing ice growth and recrystallization.
However,
the precise binding modality, interaction strength, and interfacial geometry
are debated (21–24).
The discovery of the role of tacticity (i.e.,
stereochemical arrangement of hydroxyl groups along the polymer chain) (22),
introduction of electron-withdrawing substituents, and incorporation of
copolymers (25) significantly influence IRI activity (24, 26–29).
Consistent
with this, the interfacial structuring and dynamics of water at the
polymer-water interface are increasingly implicated in the IRI action of PVA
rather than direct PVA–ice contacts.
Furthermore, ordering of the hydration
layer at ice-binding protein surfaces has been proposed to contribute to
antifreeze activity (such as in proteins) (30, 31).
Despite these insights,
direct studies of interfacial water under IRI conditions are rare,
and
strategies to systematically tune the chemical modifications and physical
properties of PVA have not yielded consistent, generalizable enhancements in
IRI activity, nor have they provided a rational design framework for improved
synthetic IRI agents (3, 23).

A mechanistic understanding of PVA’s IRI activity at the molecular level is
essential to enhance its performance and expand its utility in cryopreservation
and related technologies (13, 21, 32).
This study aims to elucidate the
molecular nature of the PVA–ice interface using experimental methods that
simultaneously characterize both the polymer and water properties under
ice-water coexistence conditions.
The objective is to understand whether there
is a polymer population engaging in strong PVA-ice interactions and to
characterize the structural properties of liquid water at the ice-water
interface in the presence of PVA—one or both factors may be key to the IRI
activity of PVA, but direct and simultaneous measurements of polymer and water
dynamics under ice-water coexistence conditions are needed.

It has long been proposed that water adopts distinct local structural
populations in the liquid state, with population weights shifting as a function
of temperature (33–35), cosolutes or ions addition (36), and proximity to
macromolecules or solid surfaces (37).
A robust descriptor of liquid water
structure is the H-O...H three-body angle distribution (3bad)
of the
hydrogen-bond network (38), while water structural property also shows subtler
correlations with water dynamics and entropy (39).
The 3bad denotes the angle
made or subtended by the H–O···H triplets within the hydrogen-bond network,
providing a geometric descriptor of local water structure.
Liquid water with
tetrahedral 3bad of 109.5° hydrating a surface, unlike in ice crystals,
does
not  imply that all four hydrogen bonds are saturated, and undergoes rapid
breaking and formation on a sub-nanosecond timescale.
Water molecules proximal
to small hydrophobic functional groups, sites or solute surfaces that disrupt
direct, continuous hydrogen bonding preferentially adopt tetrahedral 3bads of
~109.5° to form a clathrate-like, two-dimensional and lower density,
water
structure that wraps over or around hydrophobic moieties that are smaller than
~1 nm and flanked by hydrophilic groups that serve as anchoring points for
hydrogen bonding.
A wide range of chemical groups and geometries can serve
effectively as a hydrophobic site when direct, continuous hydrogen bonding to
water is sterically or electronically unfavorable; thus, the effect of
hydrophobicity of the site is strongly influenced by the chemical nature of the
neighboring groups.
The so structured liquid with tetrahedral 3bads is a
crucial motif due to the considerable entropy stored within these water
molecules.
Notably, water molecules closest to the ice surface adopt greater
tetrahedral 3bad compared to bulk water (40).
It is possible that tetrahedral
pre-structuring of liquid water near ice-binding species facilitates their
association with the ice surface and stabilizes the interface (30,
41).
Water
with icosahedral 3bad of 60° adopts geometries characteristic of dense simple
fluid packing and constitutes the other significant population of bulk water
besides tetrahedral 3bads (42, 43).

The specific focus of our study is the structural property of water hydrating
the PVA surface near the ice-water interface, and whether the population of
hydration water with tetrahedral 3bads increases.
Even if tetrahedrally
structured hydration accumulates around PVA and promotes engagement with ice,
it is unknown whether these populations remain non-frozen or transform into ice
(44).
While numerous spectroscopic methods can probe water near surfaces (38,
41, 45–47), few experimental approaches enable simultaneous characterization of
the dynamical and structural properties of hydration water and PVA polymer
under ice-water coexistence in the liquid state.
Magnetic resonance
spectroscopy methods are particularly well suited for this purpose.

This study will directly examine the dynamics of water and the polymer at the
ice-water-PVA interface using a combination of electron paramagnetic resonance
(EPR) and nuclear magnetic resonance (NMR) techniques.
$^{17}$O NMR chemical shift
analysis of water, which reports on the water oxygen’s electronic structure,
will be performed to probe local hydrogen bond structural property of liquid
water.
Recent studies have highlighted that 17O NMR chemical shifts are
exceptionally sensitive to subtle changes in local hydrogen bond length and
coordination number, which, in turn, depend on the local hydrogen-bonded
geometries of liquid water (48–50).
In fact, a prior 17O NMR study of water in
freeze–thaw PVA hydrogels observed downfield chemical shifts,
attributed to
enhanced tetrahedral ordering(51).
We employed these measurements to quantify
interfacial hydration structure and dynamics in the presence of PVA in
pre-cooled solution state and under ice-water coexistence, thereby assessing
the molecular dynamics of water around PVA under IRI-active conditions.
Concurrently with water dynamics, polymer tumbling dynamics will be probed by
continuous-wave (CW) EPR lineshape analysis of PVA sparsely functionalized with
stable nitroxide radical-based spin labels, providing complementary information
on polymer mobility at the interface.

We further examined the IRI activity of PVA in the presence of cosolutes known
to modulate hydration water structure and bulk viscosity, such as glycerol,
sucrose or trehalose as additives (21, 52).
These additives are widely used
constituents of biocompatible cryoprotectant mixtures (53–55).
Importantly,
these cosolutes increase water viscosity, which may be an important factor in
slowing the kinetics of IRI activity exerted by PVA, and thereby establishing
conditions that strongly suppress ice particle growth and enable steady-state
magnetic resonance measurement under ice-water coexistence.
This experimental
design aims to decouple the effects of viscosity-driven diffusional slowdown of
water from that of structural organization of interfacial water on the IRI
activity of PVA.
All analyses explicitly account for temperature and
viscosity-dependent contributions to the 17O NMR and EPR observables,
enabling
rigorous interpretation of cosolute effects beyond simple diffusional slowdown
and isolating the role of interfacial water structure in the IRI mechanism.

## Experimental Methods
### Thermal Hysteresis Measurements

Thermal hysteresis (TH) activity was measured to evaluate the ice-binding
properties of PVA using a Clifton Nanoliter Cryoscope (Clifton Technical
Physics, Hartford, NJ) as previously described (56).
PVA solutions at 10 mg/mL
were prepared in HEPES buffer containing 150 mM NaCl (pH 7.5)
with or without
cosolutes (sucrose or trehalose at 18% w/w).
Samples were filtered to remove
particulates, and nanoliter aliquots were loaded into wells filled with heavy
microscope immersion oil on a temperature-controlled Peltier stage.
Ice crystal
formation and morphology were monitored by optical microscopy throughout the
measurement.
Samples were cooled to induce ice nucleation, then slowly warmed
until only a single small ice crystal remained.
The melting point (Tm) of this
seed crystal was recorded as the equilibrium freezing point.
The sample was
subsequently cooled slowly while monitoring ice crystal morphology and growth
behavior, and the freezing point (Tf) was determined as the temperature at
which rapid ice crystal growth occurred.
Thermal hysteresis was calculated as
TH = Tm – Tf and expressed in both °C and osmolality units.
Concentration-dependent TH data were fitted to the Langmuir equation:
(ΔT/ΔTmax)=(C〖/C〗_(1\/2))/[(C〖/C〗_(1\/2)) +1]  where C1/2 corresponds to
the concentration at half-maximum activity (56).
Experiments were performed
with a cooling rate of 0.075 °C/min without annealing.
Measurements were
repeated 2–4 times on independent samples.
<WKcom>
Fix equation
</WKcom>

### Modified Splat Assay

A modified splat assay was used to evaluate the IRI activity of PVA in
combination with cryoprotective cosolutes such as glycerol, sucrose,
and
trehalose.
Aqueous solutions containing PVA at 0.20 mg/mL dissolved in HEPES
buffer (20 mM HEPES, 150 mM NaCl, pH 7.5), combined with each cosolute at the
same molar concentration of 0.57 M were prepared.
This corresponds to glycerol
at 5% w/w (molarity matched to 18% w/w sugar solutions), sucrose at 18% w/w,
or
trehalose at 18% w/w.
IRI measurements were also performed using 2%
spin-labelled PVA (≈340 monomer repeat units), with the corresponding assay
details and results provided in the SI (SI figs 7, 8, 9).
A heating and cooling
stage with associated liquid nitrogen pump and system controls.

These solutions were then rapidly frozen to -40 °C to initiate ice nucleation,
ensuring uniform ice crystal formation across samples.
Following this rapid
freezing, the samples were equilibrated at the ice-water coexistence
temperature, a critical point where both ice and liquid water are in
equilibrium (see SI Figure 2).
For example, solutions containing 18% w/w
sucrose or trehalose were equilibrated at -6 °C, a temperature suitable for
observing ice growth under controlled conditions.
Once equilibrated, ice
crystal growth was monitored in real time using light microscopy at subzero
temperatures (full microscope specifications and imaging conditions are
detailed in the SI sec 4).
Sequential cryomicrographs were captured at 5-minute
intervals over 120 minutes to track changes in ice crystal size and shape,
providing insights into how PVA and the cosolutes affected crystal growth.
Image analysis was performed with the ImageJ software to determine parameter
averages across ice populations in an image.
Such parameters include ice
crystal area, circularity, solidity, and Feret diameter.
The Feret diameter was
especially useful for evaluating growth inhibition.
The field of view was set
to 800 × 800 pixels (1940 μm × 1940 μm or 3.76*10^6 $\mum^2$)
and was calibrated
using the microscope’s scale bar for precise measurements.

### Morphological Analysis

The quantitative morphological analysis of ice crystals was conducted using
ImageJ software, providing detailed measurements of key parameters related to
their shape and size distribution.
This includes conventional values like
average particle area and perimeter as well as average circularity (C),
solidity (S), and the minimum and maximum Feret diameters (ΦF),
each offering
valuable insights into the physical characteristics of the ice crystals and the
effectiveness of IRI.

Circularity, defined as C = 4π × (Area/Perimeter²), measures how closely a
crystal's shape resembles a perfect circle.
Values approaching 1 indicate more
spherical crystals, whereas lower values suggest more irregular or branched
forms.
This parameter helps evaluate the degree of control over crystal
morphology and the inhibition of irregular crystal growth.

Solidity, calculated as S = Area of object / Area of convex hull,
assesses the
density of an ice crystal by comparing its area to that of its convex hull.
Crystals with high solidity values (close to 1) are dense and unbranched,
whereas lower values indicate more irregular and fragmented crystals.
This
measurement provides insight into the crystals' uniformity and structural
integrity, which are critical for assessing the effectiveness of
recrystallization-inhibition agents.

Feret diameter (ΦFmin/ΦFmax), defined as the minimum/maximum distance between
two parallel tangent lines on opposite sides of the crystal,
measures the
minimum/maximum distance across a crystal and provides a straightforward way
to gauge the size of each crystal.
Analyzing the minimum and maximum ΦF
enables us to assess the overall size distribution, indicating whether crystal
growth was suppressed or promoted.
Combining these measurements provide a
comprehensive understanding of how different formulations affect the
morphology of ice crystals.
This analysis establishes a direct link between
the presence of PVA and cryoprotective cosolutes and the observed changes in
crystal size and shape, thereby quantifying their role in reducing ice
recrystallization.

### EPR Spectroscopy

We used CW-EPR spectroscopy to examine the local mobility and dynamic behavior
of PVA.
This technique showed detailed insights into how the polymer responds
in various environments, especially when cryoprotective cosolutes are present.
For EPR analysis, we used TEMPO (2,2,6,6-tetramethylpiperidine-1-oxyl)
spin-labelled PVA, in which the nitroxide probe TEMPO is covalently attached to
the polymer chain to serve as a site-specific reporter of local dynamics.
As
described by Henry & Keith (57), sharp, narrow resonances with minimal
anisotropic broadening indicate rapid, isotropic tumbling, whereas broader and
anisotropic spectral lines suggest slower reorientation or immobilization.
This
approach proved essential in studying how PVA interacts with various cosolutes,
including glycerol, sucrose, and trehalose.
Using CW-EPR, we assessed how these
cryoprotectants influence the polymer’s flexibility and mobility,
particularly
under freezing conditions.
To ensure that spin labelling did not alter
function, the IRI activity of TEMPO-labelled PVA was directly compared with
non-labelled PVA; the corresponding IRI assay conditions and comparative
results are provided in the SI.
Additionally, this technique provided insights
into the effects of IRI on PVA’s local dynamics, aiding in understanding the
polymer’s role in preventing ice crystal growth.
The EPR analysis allowed us to
measure changes in the local motion of the polymer chains, offering a deeper
understanding of how PVA's interactions with ice surfaces and its molecular
environment influence its effectiveness in IRI.

### Ice boule Growth

Ice boule growth experiments were conducted to assess the kinetics and
morphology of ice crystal development in PVA-containing solutions under
controlled conditions.
Ultrapure water (18 MΩ, degassed and UV-irradiated) was
used for all experiments.
PVA solutions (0.5 mg/mL) were prepared with 18%
(w/w) trehalose, and control solutions containing 18% (w/w)
trehalose without
PVA were also prepared.
The growth tubes consisted of a bulb at one end for
seed formation, a narrow capillary section, and a constricted neck region,
with
ethylene glycol (100%) serving as the viscous heat-transfer medium to suppress
convective currents and maintain stable temperature gradients(58)
(additional
experimental details are provided in the SI sec 7).
Polycrystalline ice seeds
were created by controlled nucleation in the bulb region, and ice boule growth
was initiated at a shelf temperature of -0.5°C using pure water.
The growth
tube was translated through a stable solidification zone using a
computer-controlled stepper motor.
The temperature was maintained by a
PID-controlled system with a precision of ±2 mK.
A resistive counter-heater
compensated for heat flow changes during ice formation.
After the pure water
ice boule reached a predetermined size (typically 2.4–3.4 million steps),
growth was paused, and residual water was carefully removed using a glass
pipette.
Growth was then continued at -0.5°C for 15 minutes to establish a
stable interface, after which the shelf temperature was lowered to -3.0°C.
Test
solutions containing either trehalose alone or trehalose with PVA were then
introduced, and growth was resumed for an additional 1.0–2.0 million steps to
assess morphological changes at the ice-solution interface.
Ice boule growth
and interface morphology were continuously monitored using brightfield optical
microscopy, with high-resolution images captured at regular intervals to
document interface characteristics, including smoothness, dendritic extension,
and whisker formation.

### $^{17}O$ NMR Spectroscopy

We employed 17O NMR spectroscopy to examine water structures around PVA and its
interactions with cryoprotective cosolutes.
All NMR experiments utilized
17O-enriched water (40% atom, Cambridge Isotope Labs), with spectra collected
at 25°C and -6°C using a Bruker Avance III 400 MHz spectrometer.
The 17O
isotope is sensitive to shifts in water's hydrogen-bonding network,
making it
well-suited for analyzing how PVA and cosolutes like glycerol, sucrose,
and
trehalose influence water at the molecular level.
The NMR spectra showed
changes in the hydrogen-bonding network when water interacts with PVA and how
cosolutes modify this network during freezing.
During freezing, 17O NMR detects
shifts in spectral peaks, indicating changes in water’s electronic environment
due to ice formation.
These shifts provide detailed insights into how PVA
affects water structure, indicating whether water remains more ordered or
becomes more disordered in the presence of cosolutes and PVA.
The technique
also distinguishes between water in the ice phase and the unfrozen liquid phase
by analyzing changes in the chemical shifts and line widths of NMR signals.
This approach has proven valuable for understanding how PVA modulates water
structure to prevent ice recrystallization.
The 17O NMR enhances our
understanding of how PVA and various cosolutes affect water structure,
providing key insights into the mechanisms behind PVA's cryoprotective effects.
By examining water molecules at the molecular level, this method enhances our
comprehension of how PVA and cosolutes work together to inhibit ice crystal
growth during cryopreservation, supporting their applications in biological and
material preservation.

### Computational Study

To quantify how PVA influences the local structuring of water in bulk solution
and at the ice–water interface, we calculate the local tetrahedral order
parameter Qtet for water molecules (i) in the hydration shell of PVA and (ii)
as a function of distance normal to the ice–water interface.
For this, we use
configurations from three molecular dynamics simulations employing the mW water
model, which represents the hydrogen bonding of water through short-range
three-body interactions that favor tetrahedral local order,
and a compatible
united-atom PVA model.
The mW model has been extensively used to investigate
the properties of liquid water, ice, hydrophobic interactions,
as well as the
interaction and binding of PVA to ice.
We present results of simulations for
three systems
		
		# A simulation cell with 1 PVA 30-mer chain equilibrated in the presence of a
		liquid-water interface at 273 K and 1 bar, evolved for 50 ns (Figure 1a, b),
		sampling every 50 ps.
		This simulation was initiated from a configuration from
		ref.
		(59),  with dimensions 91 × 53 × 115 Å3.
		We melted the slab of ice at the
		end, away from the PVA, for this analysis.
		Because there is only a single PVA
		30-mer in the cell and most of the chain is bound to ice, most of the
		interfacial area remains PVA-free and can serve as an internal “pure interface”
		reference region for comparison.
		Moreover, the Qtet was computed only for water
		molecules in the vicinity of PVA bound to ice and, separately,
		for interfacial
		regions without nearby PVA at matched distance from the interface.
		
		# A simulation cell with one PVA 30-mer chain equilibrated in liquid water at 273K
		and 1 bar, evolved for 50 ns (Figure 1c), sampling every 50 ps,
		with dimensions
		with dimensions 91 × 53 × 115 Å3.
		This simulation was initiated from
		configuration (59) and melted all the ice in the system, ensuring that PVA was
		immersed in liquid water.
		
		# Bulk liquid water reference - A simulation cell
		with 8000 molecules of liquid water, evolved at 273 K and 1 bar for 10 ns,
		sampling every 100 ps.
		The initial configuration for this simulation was
		prepared by randomly generating 8000 particles in a cell using Packmol(60)

We perform molecular dynamics simulations using LAMMPS(61).
The equation of motion are integrated with the Velocity-Verlet algorithm using
a timestep of 5 fs.
The simulation cells are periodic in three cartesian directions.
Simulations for i) and ii) are performed in the isobaric isoenthalpic ensemble
(NpH) before equilibrating the system in the isobaric isothermal ensemble (NpT)
at 273 K and 1 bar.
Simulation for iii) is performed in NpT ensemble at 273 K
and 1 bar.
The pressure and temperature are regulated with the Nose-Hoover
thermostat and barostat(62, 63)  with time constants 2.5 ps and 12.5 ps,
respectively, in i) and ii), and 1 ps and 5 ps for iii).
Calculation of Qtet We
quantify local tetrahedral order using the standard four-body order parameter
Qtet (64) for each water molecule, i:  <WKcom> Add q_tet equation </WKcom>
Where $\psi_{jik}$ is the angle between the central water site and the four
closest proximal water or OH neighbors?
The Qtet reported in this work
represents spatial averages over all water molecules within each region.
Qtet
has been computed taking both CH and OH beads for the PVA backbone,
with a
cut-off distance of 3.5 Å and 6 Å for OH and CH, respectively.
These cut-off
distances have been selected from the first minima in the radial distribution
functions, as shown in Figure 2.
These hydration-shell definitions (including
neighboring OH environments) were applied consistently across systems;
earlier
exploratory comparisons that did not fully account for hydration-shell
definitions should be disregarded in favor of the analyses reported here.
The
molecular interactions between mW and OH of PVA beads in simulations have been
modeled as mW water interactions and both these beads have been considered in
Qtet calculations.

<WKcom> Add Simulations Figure </WKcom>

at the ice–water interface (water, cyan).
(B) Same configuration viewed from
the bottom of the ice.
(C) Configuration with PVA (red) fully immersed in
liquid water (cyan).
(D) Radial distribution functions (g(r)) between PVA
hydroxyl groups (OH–mW, blue) and PVA methylene groups (CH–mW, red)
and mW
water.
Dashed vertical lines at 3.5 Å and 6.0 Å indicate the first minima of
the respective RDFs and were used as distance cutoffs to select water molecules
for (Qtet) calculations.


## Results
### Ice Recrystallization Inhibition (IRI) Activity and Morphological Analysis

The IRI activity of an aqueous solution of PVA (0.2 mg/mL), 5% (w/w) glycerol,
18% (w/w) sucrose, or 18% (w/w) trehalose, and of PVA in the presence of each
cosolute, was evaluated using a modified splat assay (described in Methods).
The cosolute concentration was selected to match the molarity between the
different cosolutes (0.57 M) to exert the same osmotic pressure,
while their
effects on viscosity and hence water structuring are known to be different
(η ≈
1.04 mPa·s for 5% glycerol, η ≈ 1.62 mPa·s for 18% sucrose,
η ≈ 1.75 mPa·s for
18% trehalose)(65, 66).

In the absence of PVA, the baseline performance of each cosolute was observed
(Figure 2E, 2G, 2I).
Water solutions containing glycerol (5% w/w), sucrose (18%
w/w), or trehalose (18% w/w) resulted in large, irregular ice crystals with
rounded edges, indicating poor inhibition of recrystallization.
To observe the
IRI effect under steady-state conditions, samples were annealed at −6 °C
(below
the equilibrium freezing points of these solutions).
These cosolute
concentrations correspond to phase transition temperatures of -0.8°C, -2.7°C,
and -2.2°C, respectively (SI Fig.
S2).
Annealing was performed for 120 minutes
at -6°C to reach the thermodynamic steady-state condition for ice-water
coexistence before quantitative analysis (67–71).
Based on the phase diagrams
(SI Fig.
S2), during the initial freezing period at -6°C, the ice mass fraction
should increase until reaching steady-state values of 77%, 48%,
and 51% for the
glycerol, sucrose, and trehalose solutions, respectively.
Among the tested
cosolutes, glycerol (Figure 2E) showed the weakest inhibition,
resulting in a
mean ice crystal cross-sectional area of 12,289 ± 3588.48 μm².
The ice crystal
cross-sectional area was reduced to 1021.18 ± 144.66 μm² in sucrose solution
(Figure 2G), while trehalose (Figure 2I) exhibited the best standalone
performance with the smallest average ice crystal cross-sectional areas of
766.42 ± 32.12 μm².
Typically, the control conditions produced 19 to 68
crystals per field of view.

The addition of PVA to these solutions at a concentration of 0.20 mg/mL
significantly impeded the recrystallization process, resulting in much smaller
ice crystals after annealing (Figure 2F, 2H, 2J).
The mean crystal
cross-sectional area decreased by about 90 % upon addition of PVA:
659.78 ±
342.57 μm² in the presence of glycerol (94.63 % reduction from controls),
34.99
± 11.93 μm² in the presence of sucrose (96.57 % reduction),
and to 31.25 ± 5.49
μm² in the presence of trehalose (95.92 % reduction) (Figure 2K-M).
This
indicates that the relative size reduction in the respective co-solute solution
upon PVA addition is comparable, while the absolute ice crystal size varies
significantly, by ~32-fold in the presence of trehalose compared to glycerol
and ~4-fold compared to sucrose.

When the PVA concentration was increased from 0.2 mg/mL to 1.0 mg/mL,
the ice
morphology changed even more significantly from the reference cosolute
solution.
In the glycerol–PVA system, increasing PVA from 0.2 to 1.0 mg/mL
produced comparatively modest additional refinement, with crystal sizes
remaining broadly comparable to those observed at 0.2 mg/mL.
In contrast,
sucrose–PVA and trehalose–PVA formed dense networks of extremely fine ice
grains at 1.0 mg/mL, with individual crystals becoming increasingly difficult
to distinguish by image analysis.
This fine-grained structure, along with low
image contrast, makes detailed analysis challenging; however,
it clearly
demonstrates that higher PVA concentrations drive extensive ice refinement and
IRI activity, while the same relative order of effects was observed with
cosolutes at both PVA concentrations examined.
The evolution of ice size and
morphology is discussed in greater detail for the PVA concentration of 0.20
mg/mL PVA, because quantitative image analysis was accessible only at this
concentration.

The addition of PVA at 0.20 mg/mL significantly altered ice crystal morphology
across all cosolute systems.
We start with a report on changes in circularity.
All three cosolute systems when combined with PVA showed reduced circularity
values relative to the PVA absent counterparts.
The glycerol-PVA system showed
circularity changes of C = 0.752 ± 0.030 in controls to 0.475 ± 0.252 with PVA
showing the most substantial drop in circularity but also the largest variance
in resulting circularities across 3 trials (Figure 2E, 2F).
The other two
cosolute systems also showed circularity reductions but with much greater
consistency: in sucrose from C = 0.832 ± 0.006 for the controls to C = 0.620 ±
0.041 with PVA and in trehalose from C= 0.836 ± 0.006 for the controls to C=
0.658 ± 0.042 with PVA (Figure 2G-J).
These changes reflect a transition from
large, rounded crystals observed for the cosolute controls to smaller,
non-spherical ice crystal forms in the PVA-introduced samples.
Circularity
values over the course of ice recrystallization for the cosolute-PVA solutions
are visually represented in SI Figure S7D.

<WKcom> IRI figure here </WKcom>

The solidity analysis quantifies the crystal density and structural integrity
across all experimental conditions.
Control crystals across all cosolutes
exhibited solidity values approaching unity (glycerol, S = 0.960 ± 0.009;
sucrose, S = 0.965 ± 0.002; trehalose, S = 0.966 ± 0.002), indicating dense,
unbranched ice crystal structures.
Upon addition of PVA, ice crystals showed
reduced solidity, with S = 0.801 ± 0.172 in glycerol, S = 0.805 ± 0.029 in
sucrose, and S = 0.817 ± 0.025 in trehalose.
Reduced solidity indicates more
fragmented ice crystal structures with decreased structural integrity.
The
magnitude of solidity reduction is greatest in glycerol-PVA solution,
suggesting that while ice crystals remain large, the structural integrity of
ice is weakened by the PVA’s presence in the cosolute solution
(see SI Figure
S7F).

Ice crystals in cosolute-PVA solutions also exhibited strong faceting,
characterized by flat, well-defined crystal faces that produce sharp edges and
planar surfaces.
The increased aspect ratios (ratio between maximum and minimum
Feret diameters) seen in the cosolute-PVA solutions in SI Figure 7E support
increased ice crystal faceting.
Sharp-edged ice crystals are often taken as
evidence that ice-binding molecules bind directly to ice to exert antifreeze
activity.
Following this observation, the thermal hysteresis (TH) of the PVA
(10 mg/mL) + sucrose and PVA (10 mg/mL) + trehalose solution was measured.
However, we observed negligible TH, which is inconsistent with a strong
ice-lattice-matched binding of PVA observed with antifreeze proteins.
Assuming
the ice phase is pure and hence does not change its surface lattice structure,
the non-frozen interfacial water structure must differ between ice crystal
facets in the trehalose-PVA solution (SI Fig 6A and 6B).
In fact, PVA has been
shown to preferably interact with the prismatic plane, while the interaction
with the basal plane is weaker (24, 29, 32).
The observed faceting, indicating
anisotropic ice growth kinetics for the basal and prism planes,
suggests that
the rate of incorporation of water to grow ice occurs at different rates
between the basal and prism planes.

The growth pattern of ice crystals reaching ice-liquid equilibration at the
select annealing temperature of -6 °C, shown in Figure 2 (and SI Fig.
S3, S4,
S5), revealed monotonic crystal coarsening in control solutions of glycerol,
sucrose, and trehalose, in the absence of PVA.
The cubed average radius (R)
increases linearly with time, and the crystal number decreases monotonically
during the 120-minute annealing period.
The results were compared to
predictions derived by Marqusee (72) for Ostwald ripening in two dimensions
(shown in Figures 2M, 2O, and 2Q).
This theory predicts that the ripening rate
is proportional to the ice-solution interfacial free energy (2),
where the
adsorption of a solute lowers the interfacial free energy, thereby reducing the
growth rate.
It thus predicts a characteristic linear relationship between the
cubed radius of ice, R3, and time if ice growth is governed by direct
interaction between ice and the solvent, as observed in the absence of PVA
(Fig.
2N, 2P, and 2R).

During the initial annealing period at -6°C, ice formation concentrates the
cosolute in the shrinking liquid phase until concentration equilibrium is
reached (within minutes).
At steady state, the cosolute concentration in the
unfrozen liquid phase stabilizes; according to the phase diagram, 5% (w/w)
glycerol solution concentrates to 20.2%, 18% (w/w) sucrose to 31.6%, and 18%
(w/w) trehalose to 34.1%, while the liquid mass fractions (with respect to the
entire sample, including ice) at steady state are 23%, 52%,
and 49% for
glycerol, sucrose, and trehalose solutions, respectively (SI Figure 2).
Once
steady state is established, the relative total volume of ice and liquid remain
constant during the 0–120 min.
observation window.
Still, the ice crystal size
steadily grows because concentration equilibrium is reached,
but not the
equilibrium of the total system encompassing ice-water interfacial free energy.
[SH1.1]The linearity of R3 of ice crystals versus time suggested that
coarsening proceeds at a constant driving force during this steady-state
period.
The results show that between 0 and 120 min, the ice area growth with
time is linear, following the Marqusee theory, suggesting that Ostwald ripening
is occurring during steady state with the local cosolute concentration
remaining constant over time, further supporting the validity of our analysis.
Deviation of the annealing temperature by ±1 °C to -5 or -7 °C results in
different solute concentrations in the unfrozen liquid phase and, consequently,
different ice and liquid fractions than predicted by the phase diagram.
Irregular ice packing can also result in the deviation from the steady state
ice and liquid fractions and hence steady state liquid solute concentration.
The adherence to Marqusee theory for ice crystal growth in solutions of
glycerol, sucrose, and trehalose, in the absence of PVA, however,
suggests that
steady state conditions are fulfilled during our observation window.

Once PVA is added to the mixture, the ice crystal growth trends are
dramatically altered (Fig.2O and SI Fig.
S3, S4, S5).
The ice crystal area
growth over time in the presence of PVA is linear only within the first 20-60
minutes.
Beyond that, the ice crystal growth analysis based on the Feret
diameter measurements revealed strong deviations from the linear relationship
between the cubed radius of ice over time.
The PVA-containing solution also
exhibited greater inter-trial variability compared to the consistent linear
behavior of control solutions without PVA.
The rate at which non-linearity of
dimensional change is observed differed between glycerol, sucrose,
and
trehalose solutions, with the trehalose-PVA solution achieving the most
consistently rapid stabilization of ice crystal size across replicate trials.

At the annealing temperature of -6°C, PVA exhibits much greater IRI activity in
trehalose compared to sucrose or glycerol solutions.
Notably, sucrose and
trehalose are structural isomers, and the osmotic pressure exerted by 18% (w/w)
is the same, while they are also known to have distinct effects on water
viscosity and structure.
We hypothesize that the enhanced IRI activity results
from PVA altering the liquid water structure at the PVA-water-ice interface,
while higher water viscosity and lower diffusivity may hinder freezable water
supply to the ice surface.
We will test this hypothesis by measuring PVA and
water dynamics near the ice-water interface, ice crystal purity,
and non-frozen
liquid water structure at the interface.

### EPR Spectroscopy

Magnetic resonance studies under ice-water coexistence require a sample with
ice particles suspended in liquid water under steady-state conditions.
The ice
recrystallization inhibition results established above provide the experimental
framework and allow direct comparison of PVA dynamics in (i) a precooled,
unfrozen sucrose solution at −6 °C (prior to nucleation; supercooled liquid)
and (ii) the ice–water coexistence state at −6 °C after freezing/annealing.

To investigate the PVA mobility, we employed continuous-wave (CW)
EPR lineshape
analysis of sparsely (~2% of the hydroxyl groups of PVA) labeled PVA with
nitroxide spin probes (see Methods).
This low labelling density was selected to
minimally perturb the polymer’s physicochemical properties,
and the IRI
activity of spin-labelled PVA was directly compared with the non-labelled
parent polymer (see SI).
Importantly, the parent PVA chain length (≈340 monomer
repeat units) is far above the reported onset threshold for IRI activity
(DP ≈
15–20)(24, 29) , ensuring that the EPR-labelled polymer remains well within the
IRI-active size regime rather than near the minimum chain-length limit.
The
established IRI conditions can be used for EPR spectroscopic studies of PVA in
sucrose solutions at their equilibrium freezing temperature of -6°C,
under
ice-water coexistence, compared with precooled solutions at the same -6°C.

The EPR lineshapes of stable nitroxide radicals directly report on molecular
motion due to the sensitivity of the g factor and hyperfine coupling(A)
anisotropy to tumbling dynamics: rapid tumbling produces sharp, narrow lines,
whereas motional restriction broadens the features and alters their relative
intensities.
We evaluated the dynamics of spin labels attached to PVA through a
multicomponent analysis.
In sugar–water matrices, PVA presents a heterogeneous
dynamic environment characterized by distributed hydrogen bonding,
transient
clustering, and entanglements(73).
Single-component motional models were
insufficient to reproduce the experimental spectra; therefore,
we analyzed each
spectrum using two-component slow/intermediate-motion lineshape simulations,
yielding coexisting “fast” and “slow” motional populations (Figure 2A–D)
(74).
In 18% sucrose (pre-freeze), the spectrum is described by a fast population
with τ_(c,fast)=0.20ns (44%) and a slow population with τ_(c,slow)=2.45ns (56%)
(τ_(c,avg)=1.32ns).
Increasing sucrose to 30% (pre-freeze) produces a modest
redistribution and slowdown  τ_(c,avg)=1.38 ns (τ_(c,fast)=0.47 ns, 52%;
τ_(c,slow)=2.29ns, 48%).
At 45% sucrose (pre-freeze), both components shift to
slower dynamics, with the dominant “fast” population moving into the nanosecond
regime (〖 τ〗_(c,fast)=1.44 ns, 67%) and a more restricted slow population
(τ_(c,slow)=3.92 ns, 33%), consistent with crowding/viscosity-driven
constraints at higher sucrose content.

Upon freezing and annealing the 18% sucrose sample to reach ice–water
coexistence at −6 °C, ice formation excludes solutes into the unfrozen liquid
fraction, concentrating sucrose and PVA.
Notably, the CW-EPR spectrum under
coexistence remains well described by two components with only a modest shift
relative to pre-freeze 18% sucrose (τ_(c,fast)=0.35 ns, 45%; τ_(c,slow)=2.62ns,
55%).
Independently, 17O NMR spin counting (ice is effectively NMR-silent)
shows a 2.97-fold reduction in liquid volume, corresponding to an unfrozen
liquid composition of ~53.5% (w/w) sucrose under coexistence.
Critically, if a
substantial fraction of PVA were tightly adsorbed to the ice surface,
one would
expect the emergence of a strongly immobilized spectral contribution
(or a far
larger shift toward very slow motion) beyond what is attributable to freeze
concentration in a highly viscous unfrozen phase.
Instead, the two-component
fits show no dominant immobilized population associated with ice–water
coexistence, indicating that PVA does not undergo extensive,
strong ice-surface
binding under these conditions.

<WKcom> EPR and Ice boule fig </WKcom>

### Controlled ice boule crystal propagation

To determine whether some population of PVA persistently binds to ice we
performed ice crystal boule growth.
We performed a near-equilibrium ice growth
experiment to examine whether the advancing front of a growing ice crystal
boule grows over PVA or maintains PVA in a non-freezing liquid phase,
floating
atop the growing ice front.
Large, single crystals of ice can be grown at 0 °C
if a seed is present to circumvent the supercooling of water (75,
76).
It has
been shown that PVA alone does not modify which face (e.g., basal,
primary
prism, etc) preferably grows at the ice-water interface.
Here, we examined the
impact of trehalose to determine if there is a synergistic impact of sugar or
trehalose on PVA-ice binding properties (see SI sec-9).
First, we allowed ice
growth to start to form a single-crystal foundation.
The unfrozen liquid water
was removed, growth was continued for 15 min to ensure a fully solidified
substrate, then a pre-chilled trehalose solution was added and ice growth was
resumed.
The first observation is that while ice grows at 0 °C, the addition of
18% w/w trehalose not only stops crystal growth but also melts the foundational
crystal.
Lowering the growth front temperature to –4 °C in an 18% w/w trehalose
solution caused ice to rapidly advance and solidify the entire boule in a
single, uncontrolled event, disrupting the single crystal structure.
In
contrast, at –3 °C, the ice front expands more gradually, but branches from the
pre-formed single crystal, extending into the liquid phase and producing
larger, multidomain crystals.
This demonstrates that milder freezing conditions
promote slower ice growth and help preserve crystal organization,
but also that
trehalose interacts with ice growth in a somewhat uncontrolled fashion.
The
addition of PVA to the pre-cooled liquid solution containing 18% w/w trehalose
at 0.20 mg/ml and at –3 °C modified the ice-solution interface that this time
forms a visually flat growth front, indistinguishable from that of a
single-crystal ice front interfacing pure liquid water.
Growth extension into
the liquid phase of 18% w/w trehalose in the presence of PVA hence contrasts
with the dendritic behavior observed in the 18% w/w trehalose solution without
PVA.
We hypothesize that PVA migrates to the ice-water interface without
strongly binding to ice and hence floating atop.
If PVA were strongly bound to
ice, it would be overgrown by the growing ice front.
The observation that the
advancing front of a growing ice crystal boule maintains PVA in the liquid
phase, while this mixture has been shown to exert reproducibly strong IRI
activity, suggests that PVA must be strongly and evenly modifying the property
of the ice-water interface.
Based on this, we hypothesize that PVA modifies the
structure of liquid water at the ice interface to stabilize a non-freezing
liquid phase that encompasses the entire interface to the growing ice
surface(77) .
We next focus on the direct characterization of this non-freezing
water layer property using 17O NMR chemical shift analysis with enriched H₂¹⁷O.
<WKcom> SH has note here about adding ice growth kinetics discussion </WKcom>

### $^{17}O$ NMR Spectroscopy

To assess polymer-water interactions, ¹⁷O NMR spectra were acquired first of
solutions of 15 kDa PVA or 20 kDa PEG at equal concentrations (1 mg/mL)
at room
temperature.
PVA induced a 3.0 ppm downfield shift in 17O chemical shift
relative to bulk water, whereas HEPES buffer (20 mM HEPES, 150 mM NaCl, pH 7.5)
or PEG yields a smaller 2.3 ppm downfield shift relative to pure water
(Figure
3A).
Downfield shifts of the 17O water resonance are consistent with changes in
the local hydrogen-bonding/polarization environment of liquid water and,
in
many systems, correlate with more “ice-like” (more strongly hydrogen-bonded)
local structure.
In this comparison, PVA produces a larger Δδ than PEG,
consistent with PVA exerting a stronger perturbation on the liquid-water
environment under these conditions (Figure 3A).
Analysis of spectral linewidths
further distinguished the polymer-dependent water environments.
PEG solutions
exhibited 1.63-fold broader full-width at half maximum (FWHM = 488.8 Hz)
compared to PVA (FWHM = 301.1 Hz), indicating slower water dynamics and higher
solution viscosity (Figure 3A).
Broader linewidths are consistent with reduced
motional averaging and/or exchange broadening in the liquid phase; however,
linewidths can also reflect instrumental and sample-related contributions,
so
we interpret them qualitatively.
The broader PEG linewidth is consistent with a
more slowly fluctuating and/or less exchange-averaged liquid-water environment
under these conditions.
In contrast, the narrower PVA linewidth is consistent
with a liquid-water environment that remains more dynamically averaged on the
17O timescale.
While spectral deconvolution is not uniquely constrained from 1D
lineshapes alone, the linewidth difference suggests distinct hydration
environments around PVA versus PEG.

Adding PVA (such that the final concentration of PVA is 20% w/w)
to the
buffered HEPES solution causes an additional 0.34 ppm downfield ¹⁷O NMR shift.
In 5% (w/w) glycerol solution, a 0.39 ppm downfield shift is seen upon addition
of PVA.
In 18% (w/w) sucrose solution a 0.45 ppm downfield shift and in 18%
(w/w) trehalose a 0.56 ppm downfield shift is seen upon addition of PVA
(Figure
3F, G).
Thus, Δδ isolates the incremental PVA-dependent shift at fixed cosolute
composition.

<WKcom> Add figure of 17O NMR data </WKcom>

The 17O NMR chemical shift measurements were repeated at −6 °C under ice-water
coexistence conditions upon addition of PVA to buffered solutions containing 5%
(w/w) glycerol, 18% (w/w) sucrose, and 18% (w/w) trehalose.
Substantially
larger downfield chemical shifts were observed compared to those measured at
room temperature: 0.56 ppm for PVA-glycerol, 2.42 ppm for PVA-sucrose,
and 3.15
ppm for PVA-trehalose, all measured relative to a solution at the same buffered
cosolute concentration and temperature (Figure 3 I-K).
These increased shifts
indicate that structured water populations are stabilized and amplified in the
presence of PVA and ice.
It is a non-obvious result that the structured water
phase remains in the liquid phase in the presence of ice, rather than this
water phase getting incorporated into the ice crystals (measurable 17O NMR
signal only observed in liquid water).
We conclude that PVA stabilizes a
non-frozen interfacial water layer with enhanced tetrahedral order whose
population is further enhanced in the presence of ice.
We hypothesize that PVA
polymer segments hydrated with greater tetrahedral ordering orient towards the
ice interface.
This also implies that PVA is more localized near the ice-water
interface to exert such a distinct surface effect.
Both aspects will be
discussed in greater detail below.

The T₁ relaxation times of ¹⁷O NMR provide complementary information on water
dynamics (SI Table 1).
At room temperature (22.5°C), T₁ values range from 2–5
ms, corresponding to relatively mobile water with rapid molecular tumbling.
Under ice-water coexistence at –6 °C, the ¹⁷O NMR T₁ values of the liquid water
fraction decreased substantially to the sub-millisecond range:
0.138 ms for
water in PVA-trehalose solution, 0.143 ms in PVA-sucrose solution,
and 0.303 ms
in PVA-glycerol solution.
These shortened ¹⁷O NMR T₁ values under ice-water
coexistence reflect increased local field fluctuations and potential
contributions from surface-mediated relaxation mechanisms at the ice-liquid
interface and is consistent with the formation of a structured interfacial
water layer.
The observation of the shortest T₁ values in PVA-trehalose
solutions under ice-water coexistence is consistent with the most extensive
water structuring effect observed in the non-frozen interfacial layer,
as
evidenced by the largest chemical shift changes.

### Molecular Dynamics Simulations: Molecular simulations reveal enhanced water structuring around PVA bound to ice compared with solvated PVA and bulk water

Coarse-grained molecular dynamics simulations with the mW water model (78)
were
used to evaluate how PVA modifies water structure at the ice–water interface.
Local ordering was quantified with the tetrahedral order parameter, Qtet,
which
measures the degree to which water molecules adopt ice-like coordination.
In
bulk liquid water at 298 K, the mW model typically yields Qtet values of
~0.65–0.7(79, 80).
Our simulations with bulk mW liquid water at 273 K show Qtet
values of 0.72, providing a useful reference point for comparing local
structuring of the simulation cell.
Coarse-grained molecular dynamics
simulations using the mW water model were performed to quantify how PVA
modifies local water structure in different physical environments.
Separate
simulations were conducted for bulk liquid water, PVA immersed in bulk liquid
water, and PVA bound at the ice–water interface.
Local water ordering was
quantified using the tetrahedral order parameter, Qtet which measures the
degree of ice-like coordination in the local hydrogen-bond network.
In bulk
liquid mW water at 273 K, the average tetrahedrality is Qtet = 0.72 which
serves as a reference for comparison.

Water molecules in the vicinity of PVA were identified using distance cutoffs
derived from the first minima of the radial distribution functions between mW
water beads and the OH and CH beads of PVA.
A cutoff of 3.5 Å was used for
OH–mW interactions and 6 Å for CH–mW interactions.
These physically motivated
criteria were applied consistently across all systems to characterize
polymer-associated water structure.

When PVA is immersed in bulk liquid water, the tetrahedrality of nearby water
molecules is comparable to or slightly lower than that of bulk water.
Water
molecules within 3.5 Å of PVA oxygen atoms exhibit Qtet = 0.69. Using a 6 Å
cutoff from PVA carbon atoms yields Qtet = 0.71, while water within 6 Å of PVA
oxygen atoms yields Qtet = 0.69. A combined criterion including water within 6
Å of either PVA oxygen or carbon atoms gives Qtet = 0.69. All of these values
are equal to or lower than the bulk liquid reference, indicating that unbound
PVA does not promote enhanced ice-like ordering and instead modestly disrupts
local tetrahedral structure.

At the ice–water interface, water is intrinsically more tetrahedrally ordered
than in bulk liquid water, and this interfacial ordering largely explains the
higher q_tetvalues observed near ice-bound PVA.
Water identified near PVA bound
to ice shows elevated tetrahedrality (e.g., water within 3.5 Å of PVA oxygen
atoms at the interface exhibits q_tet=0.76, and water within 6 Å of PVA carbon
or oxygen atoms exhibits q_tet=0.78).
However, comparing water at the same
distance from the interface in regions with bound PVA versus regions without
nearby PVA (matched-offset “PVA-contact” vs “PVA-free” interfacial windows)
shows that the q_tetvalues are indistinguishable within the resolution of this
metric.
Thus, in these simulations PVA binds to the ice–water interface but
does not measurably distort the interfacial tetrahedrality profile as
quantified by q_tet; hydration water reports the tetrahedrality expected for
its position within the intrinsic interfacial region.

Because water adjacent to ice is intrinsically more ordered than bulk liquid
water, the spatial extent of this ordering was assessed using one-dimensional
profiles of ⟨q_tet⟩(x)along the direction normal to the interface.
The profile
exhibits a smooth transition from bulk liquid values to interfacial values over
a finite interfacial width (a few Å), rather than a sharp boundary.
Given that
most of the interfacial area in the simulation cell is not impacted by the
single PVA chain, the laterally averaged ⟨q_tet⟩(x)is dominated by PVA-free
regions and therefore provides an internal reference for the “pure” interface
at the same temperature and pressure.

Taken together, the simulations indicate that PVA slightly lowers water
tetrahedrality in bulk solution, whereas at the ice–water interface the local
q_tetis dominated by interfacial structuring and is not detectably altered by
the presence of ice-bound PVA under the simulated conditions.
If both solvated
and interfacially associated PVA populations coexist, they would be expected to
report distinct q_tetsignatures (~0.71 in bulk hydration shells versus ~0.78 at
the interface), even without requiring additional polymer-induced enhancement
beyond the interfacial baseline.

<WKcom> Add figure of Qtet of water </WKcom>

## Discussion

This study reports that PVA inhibits ice recrystallization through a mechanism
distinct from natural antifreeze proteins (AFPs).
While AFPs generate
measurable thermal hysteresis (0.5–1.5 °C) (81) through face-specific
adsorption, PVA shows negligible thermal hysteresis (< 0.02 °C at 10 mg mL⁻¹)
yet achieves comparably effective suppression of ice coarsening
(86-96% grain
size reduction), but only in the presence of sucrose or trehalose.
This shows
an IRI mechanism exerted by PVA that is distinct from AFP relying on an
adsorption–inhibition process, and utilizes the structure and thermodynamics of
interfacial water in which PVA perturbs the properties of the unfrozen liquid
adjacent to ice.

Multiple lines of evidence support a primarily non-binding mechanism.
PVA
changes ice morphology from rounded to more faceted crystals; however,
faceting
can also result from anisotropic interfacial growth kinetics and does not prove
adsorption.
EPR lineshape analysis of sparsely (2%) spin labeled PVA at −6 °C,
under ice-water coexistence, shows two motional components that remain overall
dynamic without the appearance of a dominant immobilized population.
This
behavior is consistent with PVA dynamics being governed by the local solvent
viscosity and water structure in the unfrozen liquid fraction that increases
under ice-water coexistence relative to pre-freezing, rather than by extensive
tight binding to the ice surface.
Near-equilibrium ice-boule growth experiments
provide a complementary, macroscopic observable: unlike trehalose,
PVA
suppresses dendritic instabilities and restores a planar growth front,
yet the
advancing ice front does not overgrow or trap PVA over days of growth,
indicating that PVA remains largely excluded from the ice surface and floats in
the liquid phase.
Taken together, these observations are most consistent with
weak and/or transient interfacial interactions (or low interfacial occupancy)
rather than extensive, irreversible adsorption.

17O NMR spectroscopy provided direct evidence for water structuring induced by
PVA.
Under ice-water coexistence at -6°C, PVA addition produced substantial
downfield chemical shifts (Δδ = 0.56-3.15 ppm depending on cosolute),
which
indicate enhanced tetrahedral coordination and a strengthened hydrogen-bond
networks.
The structuring hierarchy (trehalose > sucrose > glycerol) closely
matched IRI effectiveness, consistent with a causal correlation between
interfacial water structuring and IRI.
Complementary T₁ relaxation measurements
confirmed restricted water dynamics under ice-water coexistence under
conditions exerting strong IRI effects, further corroborating the structuring
of interfacial water.
Given that the main IRI effect and water structuring
effects originate from and scales with the PVA content under ice-water
coexistence, we posit that PVA concentrates near the ice-water interface and is
surface active despite not strongly binding.
The concept is that PVA enhances
the structuring and thickness of an interfacial liquid water layer that
blankets the ice surface and creates a kinetic barrier to molecular
incorporation of water into ice.

Molecular dynamics simulations quantified this structuring via the tetrahedral
order parameter Qtet (1.0 = perfect ice; ~0.65–0.70 = bulk liquid).
Water
directly contacting ice-bound PVA segments showed the highest tetrahedrality
(Qtet = 0.77 ± 0.03), corresponding to ~11% enhancement relative to the bare
ice interface.
This enhanced structuring extended laterally, creating an
extended structured domain, while water near unbound PVA segments showed
reduced order, indicating that the solvated polymer disrupts the bulk
structure.
PVA thus creates a spatially heterogeneous interfacial water
landscape that collectively impedes ice grain coarsening.

Do we have experimental proof that PVA rearranges its configuration near the
ice-water interface to reorganize the water structuring?
We do.
We took a
frozen sample prepared under IRI conditions in the presence of PVA and
trehalose and melted the ice away.
It turns out multiple freeze-thaw cycles is
how physically cross-linked PVA hydrogel is made.
The liquid water property in
the pore of such a PVA hydrogel, generated by the melting of ice,
shows
dramatically enhanced water structuring in the absence of ice (data not shown),
suggesting that PVA reorganized towards the ice interface to achieve water
ordering that is maintained even after the ice is melted.
This will be subject
of future studies.

Our study suggests that PVA operates through a mechanism distinct from
classical AFP mechanisms.
Thermal hysteresis reflects lattice perturbations
caused by surface-bound molecules, altering the ice-water equilibrium.
In the
concentration regime examined here (0.20 mg/mL), equilibrium effects are
negligible, and PVA primarily acts by molecular reorganization of structured
interfacial water that does not readily transform to match the ice lattice.
The
kinetic barrier to achieve ice lattice matching explains why PVA inhibits
ripening without measurable thermal hysteresis.
The cosolutes modulate the
barrier height through intrinsic water-structuring capacity,
reconciling
paradoxical observations: potent IRI with negligible hysteresis,
critical
cosolute dependence despite similar viscosities, and faceted morphology without
persistent binding.

These insights suggest that effective IRI need not require ice-binding motifs
but can be achieved through interfacial water structuring.
Simple,
biocompatible polymers with balanced hydroxyl spacing and maintained
flexibility can suppress ice recrystallization when co-formulated with
tetrahedral water-promoting cosolutes.
This expands the design space beyond AFP
mimetics to synthesized materials optimized for dynamic interfacial water
organization, suggesting the optimal synthetic antifreeze may resemble
flexible, hydroxyl-rich PVA more than rigid, ice-binding AFPs.

## Conclusion

We present a mechanism in which PVA achieves ice recrystallization inhibition
through the engineering of interfacial liquid water structure at the ice-water
interface.
While PVA does not irreversibly bind to ice, it shows strong surface
activity, likely by PVA accumulating at the ice-water interface that excludes
sucrose or trehalose.
This mechanism offers a new design principle for
synthetic cryoprotectants: rational selection of water-structuring cosolutes,
such as trehalose, in combination with an IRI-active and biocompatible polymer
such as PVA.
The quantitative relationship between ¹⁷O NMR downfield chemical
shifts and IRI activity provides a practical, predictive metric for screening
and optimizing cryoprotectant formulations across diverse applications,
including cryopreservation, food technology, and materials protection.

## Acknowledgement

This work was supported by the Air Force Office of Scientific Research (AFOSR)
under award FA9550-20-1-0351, with additional support from MURI and RUHR
(award
number required).
We appreciate the MURI-Ice collaboration led by F.
Paesani
for many years of discussions and constructive feedback that enhanced this
study.
We also gratefully acknowledge access to the IMSERC NMR facility.

## Supporting Information

<WKcom>
After talk with SH, include. Provide context in prelude for SI section as well
(my specialization was in processing the IRI images...)
</WKcom>

# Method of incorporating the Perfectly Matched Layer boundary condition to enable Eigenmode Simulations of a Coupling Device
## Introduction:

Traditional design strategies jump from
eigenmode simulations of closed resonators to
waveport simulations of well-coupled designs.
However,
by modeling a dissipative element attached to a section of transmission
line,
an eigenmode simulation can accurately model
the operation of a coupling device,
and even predict the geometry that leads to critical (impedance-matched)
coupling with the transmission line.
In particular, here,
a PML embedded at the opened end in a waveguide
models the radiative losses from the resonator
into the waveguide,
and standard theory can then quantify the
exact coupling constant.
This paper has two overall foci (1)
maximizing the benefits of traditional eigenmode
simulations and (2)
providing a transitional bridge between
eigenmode simulations of closed designs and
waveport simulations of well-coupled designs.
In particular,
in the example reported here,
the developing liquid-state ODNP
spectroscopy technique requires a device that functions as both
an ESR resonator
and an NMR probe.

The ODNP resonator
thus represents a specific example of a more general
design case that incorporates two or more conflicting
sets of requirements.
The design criteria for a
high-sensitivity ESR μw resonator *vs.* for
an incorporation of a high-sensitivity NMR rf resonator
(the NMR probe)
conflict.
ESR resonators focus the μw (9&nbsp;GHz) magnetic
field on the sample in order to efficiently
generate and to efficiently read out an electron
spin transition [@Poole1996EleSpiRes].
ODNP transfers the spin orientation from this
transition onto the nuclear spins of water
and then reads out the resulting magnetic
field from the nuclear spins in a NMR experiment
with a low-frequency rf (15&nbsp;MHz)
resonant circuit
[@Prisner2016LiqDNP; @Maly2025; @franckOverhauserDynamicNuclear2019].
The inductor of this rf circuit (the NMR probe)
must surround the sample and
has the potential to dramatically disrupt the
μw fields[@Han2015RFChaMag].
For this reason,
many designs rely on a saddle or hairpin loop
coil that avoids placing wires parallel to the
μw electric fields -- sacrificing NMR
sensitivity to achieve ESR compatibility.
It is known that a solenoidal coil tightly
wrapped around the sample would provide a much
larger NMR signal by better concentrating the
rf magnetic field into the sample volume
[@Hoult1976SigRatNuc;@Guinness2025SepDetCha].
However,
a solenoid more easily disrupts the resonant
μw field essential to ESR.
Furthermore,
ESR and NMR both place restrictions on the
orientation of the μw and rf
(respectively) magnetic fields that can in turn place geometric constraints on
the device that couples the resonator to the waveguide.

The three main obstacles overcome here are
expected to recur for almost all resonator
design problems.
First,
the literature already makes it clear how
comprehensive eigenmode simulations can offer insight into
perturbations of
the desired resonator mode [@Lin2006CavMeaCom;
@Sklyuyev2006MeaComPer; @Meidlinger2009GenPerThe;
@Gorgizadeh2018; @Dombrowski1984],
but a systematic method for analyzing how the
eigenmode map (and therefore the perturbations)
vary as a function of design parameters must
be developed.
Second,
clear algebra must explain the
relationship between the resonator efficiency
factor ($\Lambda$ in units of $\text{T}/\sqrt{\text{W}}$)
*vs.* the fields and $Q$
factor reported by the eigenmode
simulation [@Hyde2019UniFieRes; @Rinard1994RelBenOve].
Third and finally,
while waveport simulations can simulate coupling
to the transmission line,
a method for investigating and optimizing very
sub-optimal coupling devices must be developed.

As a specific example here of this first obstacle,
inspired by uses of solenoid NMR coils in
similar DNP applications
[@Bennati1999; @Neudert2014AldGraRes; @He2021; @Dorio1979],
a solenoid NMR coil can be integrated within
a rectangular ESR cavity.
For some modes,
this inclusion can be viewed as a perturbation.
However,
the solenoid also
introduces new, undesired resonant modes
that hybridize with the desired resonant mode
of the cavity,
sometimes with extremely drastic and detrimental
effects (see @sec:avoidHybr, @fig:BadPitch0p8mmCoupled).
Simulations that track how variations in
design parameters affect the resonance
frequency, $Q$-factor, and fields of the
eigenmodes offer the information needed to
avoid such hybridization.
However,
while popular simulation software
(*e.g.* Ansys Electronics Desktop, née HFSS)
offers automated methods for tracking the response of a
waveport simulation to variations of design
parameters,
these techniques
do not extend to eigenmode
simulations that track multiple eigenmodes.
@Sec:avoidHybr,
(See
@fig:MappingModesByFreqvPitchUncoupled; @fig:MappingModesByFreqvPitchCoupled
for uncoupled and coupled examples
respectively)
 overcomes this obstacle by leveraging the
scripting capabilities of HFSS and
and implementing some
basic post-processing scripts to
interpolate mode properties between discrete
steps of design (*i.e.* geometry) parameters.

The second challenge met during the resonator design process for a which a
solution is generally desired is the ability to extract a reliable value of the
fields at the sample's location for a particular resonator design.
In the
eigenmode setup, we can get a sense of a resonator's quality factor (Q)
and
some overall field strength values directly from the ANSYS eigenmode solution
setup.
Because we desire a term more relative to the actual strength of the
resonator's design for its dual resonance purpose like the resonator's
efficiency parameter ($\Lambda$) with respect to the sample's location a
theoretical bridge was desired between these accessible values like Q and field
strength and desired value like $\Lambda$.
Within an eigenmode solution setup,
existing protocols require closed structures and avoid the crucial design
problem of coupling the resonator to a transmission line that supplies power --
*i.e.* a coaxial cable or (here) a waveguide[@Mett2008DieMicRes].
This results
in a bottleneck in the design process when eigenmode simulations are converted
to waveport simulations (where the waveport represents the transmission line);
this step requires not only a change of simulation type, but the simultaneous
addition of physical design elements (the "coupling device")
that efficiently
couple to the waveport[@Neudert2014AldGraRes].
By having a method for
approximating $\Lambda$ within the eigenmode setup we can take advantage of the
ability to model a coupled design and maximize the benefits of traditional
eigenmode solutions (see @Sec:couplingPower).

This third obstacle (developing a coupling
design from scratch)
requires further discussion.
Cavity resonators require some method of
supplying power to the device,
referred to as a "coupling device": *e.g.*,
a coupling iris controlling the entry/exit of
power to a resonator through a waveguide,
or a coupling loop that controls entry/exit
of power through a coaxial line [@Poole1996EleSpiRes].
While
driven waveport simulations model coupling, the first choice of coupling device
design might either dramatically undercouple
or dramatically overcouple to the transmission
line.
Poorly coupled designs of
either type
can yield a null result (little to no
transmission of power into the resonator)
in a waveport simulation [@Rinard1994RelBenOve].
Of greater import,
a waveport simulation cannot detect
nearby "dark" modes
(modes that do not couple to the
transmission line,
in contrast to the "bright" modes that do);
however,
as will be shown in @sec:avoidHybr, @fig:MappingModesByFreqvPitchCoupled
their lack of coupling does *not* mean
that they do not affect the resonator
performance and resilience.
Finally, both issues are complicated by the fact that
the coupling device affects the resonance
frequency to an unknown extent.
Thus, even in simulations,
resonator designs frequently rely on well-tested
coupling devices that are already known to
couple well to a particular mode [@Doll2012LiqStaDNP;
@Mett2008DieMicRes].
Unless they are required by unusual geometric
constraints,
unconventional coupling devices are often
disregarded for more
traditional designs in the adaptation of a resonator design for realistic use.

This paper overcomes
the third obstacle
with a simulation protocol that bridges
between closed eigenmode simulations and
driven modal waveport simulations.
Specifically,
adding a matched dissipative element to a
section of transmission line
allows an eigenmode simulation to
accurately model the operation of a coupling device.
Standard theory can then quantify the
exact coupling constant,
even at extreme values of over- or under-coupling
[@Rinard1994RelBenOve].
In particular,
this strategy can rapidly explore different
classes of coupling designs
[@Poole1996EleSpiResCh4Iris],
visualize the evanescent fields involved
(@sec:couplingBeta),
optimize one to critical coupling
[@Rinard1994RelBenOve],
and finally guide the addition of design
elements to enable tunability of the
impedance matching
(@sec:couplingBeta).
Once optimized, the critical coupling can also
be validated by a standard waveport
simulation.

## Theory

### Relationship Between $Q$ Factor and Coupling

Cavity resonators are physically hollow
structures enclosed by boundaries of a conducting
material used to generate a specifically
desired standing electromagnetic field pattern
at a particular resonance frequency.
An eigenmode simulation predicts
the resonator's
quality factor ($Q$):
$$
Q = \frac{2 \pi \nu_{0} E_{stored}}{P_{loss}}
$$
where $\nu_{0}$ is the resonance frequency,
$E_{stored}$ is the energy stored inside the
μw resonator, and $P_{loss}$
is the power loss by the resonator
[@Poole1996EleSpiRes].
Because $P_{loss}/2\pi \nu_0$
can be thought of as the energy lost per radian, $Q$ is a unitless quantity.
Furthermore, $Q$
can be related to the complex frequency as:
$$
Q = \frac{\text{Re}[\tilde{\nu}]}{2\;\text{Im}[\tilde{\nu}]}
= \frac{\nu_0}{\Delta\nu}
$$
where
the eigenmode solver returns the
complex eigenfrequency
$\nu = \nu_{0} + i\Delta\nu/2$,
$\nu_0$ is the real portion of the resonance
frequency and $\Delta\nu$ is the full width
at half maximum of the resonance.

When a resonating structure with an initial $Q$ factor of
$Q_u$ (for "uncoupled") connects via a coupling
device to a transmission
line,
the cavity electromagnetically "opens" to the waveguide,
and leaks ("radiates") energy into the waveguide.
This leaking/radiation
lowers coupling factor to $Q_c$
(for "coupled" -- also sometimes called "loaded"):
$$
\frac{1}{Q_{c}} = \frac{1}{Q_{u}} + \frac{1}{Q_{r}}
.
$$
Here, $1/Q_{r}$ represents the fraction of the
total stored energy lost every radian
as the resonator radiates through the
coupling device into the
transmission line [@Poole1996EleSpiRes].

<!-- Moved up from below and significantly
edited -->
Generally,
the design of a coupling device
aims to achieve a condition of impedance
match -- *i.e.* critical coupling.
This is the condition where no power
incident on the cavity reflects from the
cavity.
In the current framework,
this is equivalent to insuring that the power
exchanged with the attached transmission line at
resonance exactly balances the power
dissipated internally.
Because the resonator is a passive device,
$1/Q_r$ is the energy radiated
per radian during the discharging of the resonator,
but also the energy accepted into
the resonator per radian
during charging (loading) of the resonator.
Phrased differently,
$Q_r$ is the $Q$-factor of an idealized
lossless resonator attached to a coupling
device,
and a transmission line
that in turn attaches (opposite the
resonator) to a load perfectly matched to the
characteristic impedance of the transmission
line.
Therefore,
to achieve critical coupling and impedance
match,
$1/Q_r$ must exactly match $1/Q_u$,
equivalently $Q_r=Q_u$ and $Q_c=Q_u/2$.
More broadly,
by comparing a cavity with and without a
coupling device,
$$
\beta = \frac{Q_r}{Q_u} = \frac{Q_{u}}{Q_{c}} - 1
$$
quantifies the degree of coupling
between the resonator and its transmission
line.
(Where the middle equations points out that
conceptually $\beta$ gives
<!-- moved up from below, and worked in with
paragraph above-->
the ratio of the resonator's radiative
and uncoupled $Q$-factors.)
For the critically coupled case,
$\beta=1$.
As $\beta$ strays from 1,
the resonator will then be more and more over
or undercoupled $\beta<1$ or overcoupled
$\beta>1$.

The term 'coupling' here is being used to
describe how well or poorly energy is being
stored in the device through the transmission
line.
In the bright/dark terminology
we have borrowed from optics
[@Zhang2008PlaIndTra],
$\beta$ specifically quantifies
the brightness of a mode:
from "dark" ($\beta \approx 0$),
through critically coupled ($\beta = 1$),
to severely overcoupled modes
($\beta \gg 1$).
While both of the latter can be considered
bright modes,
overcoupling also degrades power delivery.
Specifically,
the fraction of the incident power
delivered to the resonator
[@Rinard1994RelBenOve],
$$
T_{\beta} =
\frac{2Q_{c}}{Q_{u}}
\left(2 - \frac{2Q_{c}}{Q_{u}}\right)
= \frac{4\beta}{(1+\beta)^{2}},
$$
reaches 100% only at $\beta = 1$.
(With the remaining $1-T_\beta$ fraction
reflected from the coupling device.)
For overcoupled modes,
power fails to enter the cavity from a
transmission line for the same reason that a
low-resistance load <!-- $Q_r \gg Q_u$ equiv to $Q_u\ll Q_r$-->
reflects rather than accepting power from a
transmission line [@Rinard1994RelBenOve].
At $\beta \approx 38$,
90% of the power is rejected,
and at higher $\beta$, the fraction of
power that makes it into the resonator
goes as $T_\beta \approx 4/\beta$.

### Isolating and Understanding Evanescent Fields

While waveport simulations necessarily
include fields from waves traveling from the
waveport to the coupling device,
as well as fields reflected from the coupling
device,
eigenmode simulations directly report
on the evanescent field that couples
the cavity to the transmission line.
This permits optimization of the evanescent
fields involved in coupling.

The results will show that eigenmode
simulations including the coupling element
offer an opportunity to directly investigate
and optimize the evanescent fields involved
in coupling.
In particular,
the design demands an adjustable coupling
device that can achieve critical coupling
even for samples with different shapes
and different dielectric losses
(and therefore different effects on $Q_u$ and
therefore demands on the $Q_r$ provided by
the coupling device).

The concept of generalized current
proves useful here.
Specifically
the *total generalized electric current density* as the sum of displacement,
conduction, and impressed currents [@Harrington1961GeneralizedCurrent]:
$$
\mathbf{J}^t =
\frac{\partial\mathbf{D}}{\partial t}
+\mathbf{J}^c+\mathbf{J}^i.
$${#eq:totalCurrent}
<!-- Harrington Eq. (1-17), p. 7 -->
provides
Ampere-Maxwell's Law in a compact format:
$$
\nabla\times\mathbf{H}
=\mathbf{J}^t.
$${#eq:ampereMaxwell}
For harmonic fields, the time derivative becomes $i\omega$,
which togeter with
$\mathbf{D}=\epsilon\mathbf{E}$ and
$\mathbf{J}^c=\sigma\mathbf{E}$ (Ohm's law)
yields
$$
\mathbf{J}^t =
(\sigma+i\omega\epsilon)\mathbf{E}
+\mathbf{J}^i
$${#eq:totalCurrentHarmonic}
<!-- Harrington Eqs. (1-15), p. 6;
     (1-17), p. 7; (1-44), p. 17;
     (1-46), p. 18; (1-47) and (1-48), p. 19.
     Explicit expansion for simple matter. -->

The generalized current flux $\mathbf{J}^t$
forms closed loops in space
(it is divergenceless because it can be expressed as a curl
*via*  @eq:ampereMaxwell).
A major design question asks whether it
should flow through space (or a dielectric)
or through a conductor.

Maxwell's equations explain the fundamentals
of how electric and magnetic fields form,
whether in a resonator or waveguide and how
they are affected by the incorporation of
coupling devices or other perturbations to
the resonator device.
Perturbation theorem outlines the prediction
of how the frequencies and field patterns of
a cavity's eigenmodes will shift when the
cavity's geometry has been altered or deformed.
Perturbations are a change in the cavity's
overall physical structure;
most commonly through the introduction,
substitution,
or subtraction of a metallic or dielectric
material.

A good conductor ($\sigma\gg\omega\epsilon$)
has a complex propagation
constant [@Pozar2012ConductorFields]:
$$
\gamma=\frac{1+i}{\delta}
$$
where
$\delta=\sqrt{2/\omega\mu\sigma}$ is the skin depth.
This, together with its intrinsic impedance [@Pozar2012ConductorFields]:
$$
Z_s=(1+i)\sqrt{\frac{\omega\mu}{2\sigma}},
$${#eq:surfaceImpedance}
<!-- Pozar Eqs. (1.113)--(1.114), p. 31;
     skin depth from Eq. (1.60), p. 19 -->
determine the relationship between the tangential electric field
$$
E_\parallel(x)=Z_s H_0 e^{-\gamma x}.
$${#eq:conductorElectricField}
and the magnetic field $H_0$ tangential to the surface
(though perpendicular to the electric field).
<!-- Derived from Pozar Eqs. (1.113)--(1.114), p. 31,
     using the field relation stated with Eq. (1.96),
     p. 28. Coordinates chosen so E_y/H_z = Z_s. -->
At the surface, $E_y(0)=Z_sH_0$,
has equal in-phase and quadrature components,
with both inversely proportional to
$\sqrt{\sigma}$, and therefore vanishing for a perfect conductor.


As can be seen below in the selection of

current runs through the volume of the resonator
and must form closed loops.
Displacement current passes through gaps,
like the iris for the waveguide's insertion
or openings for a sample's insertion,
as well as resistor elements or other areas
of displacement current between the conductive
walls of the cavity resonator to form these
closed loops.
Of course,
the other half of this generalized current
described in Ampere-Maxwell's law is the actual
current running along the walls of the resonator.

Ampere-Maxwell's Law:
$$
\nabla \times H = -j\omega\epsilon E + \sigma E + J_{ext}
$$


### Predicting Resonator Efficiency from Eigenmode Simulations

A resonator parameter relevant through the
design process even before the transition to
incorporate a coupling device is the resonator
efficiency parameter,
($\Lambda$)[@Mett2008DieMicRes].

$$
\displaystyle \Lambda = \frac{B_{1}}{2\sqrt{P_{loss}}} \approx
\frac{\mu_{0}\sqrt{Q}}{V_s\sqrt{4\pi\nu_{0}}}
\iiint_{sample}{H_{1,y}(\mathbf{r})dV}
$$
  

The efficiency parameter explicitly displays
the average magnetic field generated over a
particular space (in this case the volume of
an ODNP sample capillary)
relative to how efficiently power was delivered
to the resonator to excite such a field.
The initial purpose of the efficiency parameter
in our investigation ensured that any additional
material (solenoid, transmission line, etc)
didn't greatly upset the projected fields
achievable across the sample's location in
the device.

The efficiency parameter is experimentally
meaningful when put into the context of the
resonator's degree of coupling while investigating
coupled designs.
Because we initially start with a poorly
coupled design through the appraisal of various
coupling schemes,
a controlled comparison was desired to
effectively judge a design's ability to generate
an effective magnetic field along the sample
region in the cavity design regardless of the
design's degree of coupling with the experimentally
incorporated coupling devices.
The resonator's efficiency parameter can then
be projected accounting for how power is
coupled to the excitation field in the volume
of the cavity by incorporating the design's
degree of coupling ($\beta$) with the
approximation of
$\Lambda$.

$$
{\Lambda_{critical} = \Lambda\sqrt{\frac{Q_{u}}{{2Q}_{c}}} =
\Lambda\sqrt{\frac{\beta + 1}{2}}}
$$

By reciprocity, the resonator's $\Lambda$
and effective coupled $B_{1}$
efficiency gives sensitivity as a detector
for identifying coupling schemes that generate
nearby resonant modes which intrude or impede
the desired mode and fields of an investigated
design.
While we want to highlight the benefits of
viewing the fields and the bridge HFSS eigenmode
provides for navigating the incorporation of
a coupling device with a particular resonator
design,
parameters that serve as a quick reference
for a design's potential capabilities are
useful.

$$
H_{1,y,mag avg} = \frac{\iiint_{sample}{|H_{1,y}|}dV}{V_{sample}}
$$

$$
<H_{1,y,mag avg}> =
\frac{\iiint_{sample}{{\left||H_{1,y}|\,-\,\frac{\iiint_{sample}{|H_{1,y}|}dV}{V_{sample}}\right|}^{2}}dV}{V_{sample}}
$$

Determining the variance of the magnitude of
the magnetic field's strength in the volume
of the sample capillary alongside the resonator's
efficiency over the same sample volume
supplements our abilities to track and monitor
the desired and nearby in frequency resonator
field patterns.
These parameters alongside the $B_1$ efficiency,
degree of coupling,
and reflection coefficient projections enable
the relative rating of resonator designs
against each other,
useful for comparing all designs within and
between the two subgroups of uncoupled and
coupled designs.
Tracking the changes across different designs
in both the variance of the field strengths
and the projections when critically coupled
is useful for determining the perturbations
like coupling device additions which generate
undesired field patterns capable of hybridizing
with the desired resonator cavity mode.
Being able to reference these parameters has
helped highlight in-effective resonator designs
which may have undesired solenoid incorporation,
a coupling device inclusion disruptive to the
TE$_{102}$ mode particularly near the sample,
and/or a design incapable of adjustment or
improvement.

### Generalized Current Aids in Describing Coupling Devices

Maxwell's equations explain the fundamentals
of how electric and magnetic fields form,
whether in a resonator or waveguide and how
they are affected by the incorporation of
coupling devices or other perturbations to
the resonator device.
Perturbation theorem outlines the prediction
of how the frequencies and field patterns of
a cavity's eigenmodes will shift when the
cavity's geometry has been altered or deformed.
Perturbations are a change in the cavity's
overall physical structure;
most commonly through the introduction,
substitution,
or subtraction of a metallic or dielectric
material.

### Nearby Modes Determine How Design Changes Affect Field Profiles

FEM simulations serve as useful tools for designing microwave
resonant structures.
However, design of novel practical resonators calls for
(1) an intuitive understanding of how alterations to a design
will change the shape of the electromagnetic fields
(*i.e.* the field profiles)
and (2) an understanding of which designs are more susceptible
to imperfections in machining.
Perturbation theory teaches that the field profiles
of neighboring modes contain vital information
that can answer both questions.

In particular,
eigenmode simulations can calculate
the various modes of an original design.
One then wishes to understand how the resonator
responds to changes --
which can be either (1) deliberate changes
introduced to the design or (2) accidental changes
arising from machining imperfections.
Perturbation theory points out that
the field profiles can be represented to first order
as mixing in other modes of the original design.
Specifically,
$$
\tilde{\mathbf{E}}_i=\mathbf{E}_i +
\mathbf{\sum_{j{\neq}i}}a_j\mathbf{E}_j
$${#eq:fullEset}
where the set
$\mathbf{E}_i$
gives the fields of the original
eigenmodes and
$\tilde{\mathbf{E}}_i$
gives the fields of the design after alteration
(whether deliberate or accidental).
Note that @eq:fullEset is equally true for magnetic ($\mathbf{B}$) fields,
as well as electric ($\mathbf{B}$) fields,
and relies only on the general fact that the eigenmodes
($\mathbf{E}_i$ or $\mathbf{B}_i$) form a complete orthonormal set.

Assuming one has designed a particular mode of interest
to have an important set of properties
(*e.g.* a strong magnetic field at the sample,
for the purpose of ESR)
one then seeks to (1) introduce alterations
(*e.g.* to introduce wires for an NMR probe's inductor)
that minimize the values of the $a_{j}$ and/or
(2) choose a design where the forseeable
alterations (*e.g.* due to low machining tolerances)
are expected to result in minimal $a_{j}$.

To first order in the changes to the fields,
established theory gives
$$
a_{j} = \frac{\alpha_{ij}}{(\omega_{i}^{2} - \omega_{j}^{2})}
.
$${#eq:alpha}
where $\alpha_{ij}$ generally comprises the dot products
between the fields of the $i^{th}$ and $j^{th}$ modes,
integrated over the region where the design is altered.

By way of [@eq:fullEset;@eq:alpha],
perturbation theory thus points out
two important principles:
(1) small design alterations tend to blend in the field
profiles of nearby (close in frequency) modes; and
(2) the strength of this blending also depends on
whether or not the fields of the two modes are aligned
over the region where the design is altered.

Meidlinger points this out through the example
of the time evolution of each expansion
coefficient (electric and magnetic)
which for the unperturbed examples appears
trivial but, with a perturbation introduced,
the expansion coefficients present the added
difficulty of handling a perturbation as the
expansion coefficients for the set of cavity
eigenmodes are now all governed by
coupled linear equations.
$$
\tilde{e}_i=e_i + \sum_{j{\neq}i}{a_j}{e_j}
$$
$$
\tilde{h}_i=h_i + \sum_{j{\neq}i}{b_j}{h_j}
$$
Similar to their expansion coefficients,
the fields patterns with the perturbation
introduced for any given eigenmode are also
linearly mixed with each other.
This leads to the similar expression under
which the field pattern in the perturbed state
equals the field pattern in the unperturbed
state combined with the vector field sum of
the mixing contributions between the fields
of each mode with the desired mode in the
complete set that arise from the perturbation's
introduction.
This vector field sum component consists of
the complete set of field patterns (minus the
mode of interest)
scaled by that mode's degree of linear mixing
(brought about by the perturbation)
with the mode of evaluation.
(Meidlinger [@Meidlinger2009GenPerThe] doesn't give a name for 'a'
specifically and I'm trying to differentiate
from 'e'/'h' which are also expansion
coefficients,
Brackebusch [@Brackebusch2011CalHigFre; @Brackebusch2012ImpAspEig] calls these
'weighting factors').

$$
\mathbf{\tilde{E}_i}=\mathbf{E_i} +
\mathbf{\sum_{j{\neq}i}}{a_j}\mathbf{E_j}
$$

$$
\mathbf{\tilde{H}_i}=\mathbf{H_i} +
\mathbf{\sum_{j{\neq}i}}{a_j}\mathbf{E_j}
$$

After a perturbation is introduced,
the effect on that field pattern for any given
perturbed mode can then be determine based on
the field pattern of the eigenmode prior to
perturbation combined with the vector field
of the mixing between all the other
eigenmodes
of the complete set of unperturbed eigenmode
field patterns with the unperturbed mode of
interest.

As holds true for the unperturbed system,
the time dependence of the perturbed expansion
coefficients exhibits harmonic motion.
By reformulating Maxwell's equations in terms
of the expansion coefficients,
the general differential equation for their
time evolution can be determined.
This enables solving the perturbed expansion
coefficient's time evolution but Meidlinger
avoids this as this would require numerical
calculation of the field patterns and we have
no need for this as we can already view these
perturbed field patterns in the HFSS software.

$$
\omega_{i}e_{i} + \frac{1}{2U_{i}}\oint{(E \times H_{i})} \cdot d\tilde{a} =
- \frac{dh_{i}}{dt}
$$

$$
\omega_{i}h_{i} - \frac{1}{2U_{i}}\oint{(E_{i} \times H)} \cdot d\tilde{a} =
\frac{de_{i}}{dt}
$$

As Meidlinger shows, prior to the instance of
a perturbation,
the first-order differential equations for
the expansion coefficients $e_{i}$ and $h_{i}$
are dependent on each other,
the two expressions can be decoupled into
their second-order differential equations for
each coefficient's independent determination.
Under a perturbed system,
the first-order differential equation can be
written out under the same principles over
the volume of the perturbed geometry.

Surface integrals are investigated only in
the geometry of the perturbation because the
perturbed area is the only space where the
field patterns for the set of eigenmodes will
be different than their unperturbed counterparts.
E and H field relations from Maxwell's curls
enables the evaluation of the surface integrals
towards a matrix-equivalence of the
coupled linear equations for the perturbed
eigenmode field patterns.
$$
M_{ij} \equiv \int_{\delta\tilde{MW}}{(\omega_{j}\mu\mathbf{H_{i}} \cdot
\mathbf{H_{j}} - \omega_{i}\epsilon\mathbf{E_{j}} \cdot
\mathbf{E_{i}})}d\tilde{\tau}
$$
$$
E_{ij} \equiv \int_{\delta\tilde{EW}}{(\omega_{i}\mu\mathbf{H_{j}} \cdot
\mathbf{H_{i}} - \omega_{j}\epsilon\mathbf{E_{i}} \cdot
\mathbf{E_{j}})}d\tilde{\tau}
$$
The nature and location of the perturbation
inside the resonator affect the characteristics
of the perturbation's effects on the eigenmode's
field patterns.
Walls of the resonator can be perceived as
purely magnetic, purely electric, or some
combination,
influencing the nature of the walls' effects
on the localized field patterns after the
instance of a perturbation.

With a perturbation introduced,
the first order differential equations above
are no longer valid as the field patterns of
the eigenmode's generated in the unperturbed
resonator now obey
coupled linear equations in the
perturbed design.

$$
\frac{d^{2}e_{i}}{dt^{2}} = -
\mathbf{\sum_{j}}{\omega_{i}}^{2}e_{j}\delta_{ij}, \frac{d^{2}h_{i}}{dt^{2}} =
- \mathbf{\sum_{j}}{\omega_{i}}^{2}h_{j}\delta_{ij}
$$

The differential equations for the expansion
coefficients in the unperturbed state (above)
can be rewritten for the perturbed state
geometry (below) through with the matrix
$A_{ij}$
introduced.
$A_{ij}$
represents the field perturbation of the new
eigenvalues with respect to the resonance
frequency of the desired unperturbed mode as
those field perturbations develop in the
perturbed cavity state.

$$
\frac{d^{2}e_{i}}{dt^{2}} = \mathbf{\sum_{j}}A_{ij}e_{j},
\frac{d^{2}h_{i}}{dt^{2}} = \mathbf{\sum_{j}}B_{ij}h_{j}
$$

Through this matrix of the perturbed field
pattern's eigenvalues and -vectors the correction
to the electric and magnetic field patterns
can be determined as well as the correction
to the resonance frequency for the desired
cavity mode.
This relationship between the first-order
weighting factors of the field perturbation
matrix and the change in the resonance frequency
of the desired mode before and after the
perturbation can be used to determine the
perturbed field pattern's expansion coefficients
as shown below.

$$
A_{ij} = -{\omega_{i}}^{2}\delta_{ij} + \alpha_{ij}
$$

$$
a_{j} = \frac{\alpha_{ij}}{(\omega_{i}^{2} - \omega_{j}^{2})}
$$

$$
b_{j} = \frac{\beta_{ij}}{(\omega_{i}^{2} - \omega_{j}^{2})}
$$

## Methods

This study was performed using the ANSYS
Electronics Desktop 2021 R1 (ANSYS EDT)
platform and its 3-dimensional high frequency
structure simulation (HFSS)
software.
The procedure for our approach to coupling
design relies on using an eigenmode solution
type available within an HFSS simulation.
Each design requires a simulation setup such
that once the design is solved,
a check is performed to ensure that each design
is converged on a set maximum delta frequency
per pass,
validating the resonance frequencies of the
determined modes and their solved fields.

As was desired,
HFSS enables the expansion of a design along
multiple design dimensions independently,
allowing for better understanding of the
mechanisms and effects of each physical
adjustment to the overall resonator design.
This includes solving for a design across
multiple frequency ranges with the ability of
being able to join these results together.
The effects of variation on a design parameter
(in this case the pitch of the solenoidal NMR
probe) was also studied,
taking advantage of a script developed for
modifying the value of the specified design
variable.
The processes above of producing and interpreting
the selection of design variants can be repeated
with models incorporating the necessary
additions to a realistic design,
including a coupling device and joined waveguide.

This procedure of generating a base design
with its different avenues of variants is
enabled by the eigenmode solution setup.
For example,
the ability to use a python script to modify
the 'pitch' design parameter and generate a
range of otherwise identical designs with
different pitch values was rapid and automated.
While there are processing limits on the number
of simulation jobs capable of being submitted
at one time,
this process was also enabled to be automated.
A 'best design' can then be arrived at once
each design iteration has been processed and
analyzed,
a procedure also capable of being automated
as described below.

Automating using python scripts was also taken
advantage of to generate and acquire each
design's simulation results.
With each valid solved design,
scripts were developed to export the fields
as well as the complex frequencies and relevant
vector field values for each of the design's
solved modes.
Inherent to the eigenmode solution setup,
a limited number of total modes may be solved
for in any particular solution setup for a
design.
Thus using the same base design,
setups can be made with different starting
frequencies to expand the number of determined
modes across a broader range of investigated
frequencies.

Inner dimensions of 21.65 mm x 30 mm x 43.3
mm were used for the rectangular resonator
based on the standing wave propagation function
that define a rectangular resonator of the
TE$_{102}$
mode at a resonance frequency of 9.8
GHz.[@Poole1996EleSpiRes] A thickness of 2 mm
is used for copper objects (cavity and waveguide)
to well exceed copper's skin depth of ~0.7
$\mu$m.
Wall thicknesses are also defined to generate
more realistic external conditions for the
design as opposed to using a perfect electric
conductor (PEC)
boundary.
Enabled within the eigenmode simulation setup,
a Perfectly Matched Layer (PML)
boundary is used to model the radiative losses
that arise from opening a design for the
incorporation of a coupling device.

## Results & Discussion
#### eigenmode lets resonator & coupling design be done separately [Red.? method-overview]

The methodology introduced here allows separation
of resonator design and coupling design into
two parts.
Therefore we begin by focusing individual
steps of the resonator's design from it's
initial efficiency through further additions
of solenoid and coupling devices for more
complex designs.
We are able to compartmentalize the addition
of a solenoidal NMR device and its effects on
the resonator's capabilities separate from
the incorporated probe's NMR capabilities.

#### eigenmode shows solenoid's disruption of desired & nearby modes

The ability to simulate isolated individual
design changes enabled the investigation of
the solenoid's incorporation into the resonator
cavity.
HFSS's eigenmode design setup provides a
platform for this modeling,
as we can constantly solve the fields and
modes present for any give solenoid-incorporated
design.
This is really useful for designs which the
solenoid's incorporation has deleterious
effects on the fields of the desired resonant
mode,
as we can visualize these disturbances in the
field patterns of the desired and nearby modes.

#### conventional: switch to Driven Modal + iris/waveguide to add coupling [Red.? conv-driven-modal]

All resonators require some method of supplying
power for the excitation of their modes.
Once a realistic active design is reached,
the necessary next steps include the incorporation
of a coupling device.
Traditional methods are done through transferring
the active design to a Driven Modal design
setup,
where often a conventional coupling approach
such as an iris port with waveguide approach
is employed.
This is done in the Driven Modal setup to
enable the easy interpretation of the active
coupled mode,
including its resonator efficiency and reflection
coefficient parameters.

#### PML keeps coupling inside eigenmode, catches weakly coupled modes [Red.? PML]

When power is supplied to a resonator,
the radiative losses that arise due to coupling
halves the Q of the resonator once critically
coupled.
We can stay within the eigenmode setup as the
PML boundary available through ANSYS HFSS can
be used to model these eternal radiative loses
quite well.
Doing so,
we can examine multiple coupling schemes
including some unconventional waveguide
incorporations with our DNP resonator design.
By remaining within eigenmode,
we can both detect multiple modes,
including the dark modes,
which are only weakly coupled
with whichever coupling scheme that is being
used.

#### optimize pitch (DNP) & coupling (crit.) independently [Red.? method-overview]

This methodology enables a new avenue of
resonator design,
as we can independently optimize the resonator's
important attributes for DNP purposes (such
as by adjusting the solenoid's pitch to deter
undesired mixing between the main mode of the
rectangular resonator cavity and the degenerative
modes surrounding the helix within the cavity)
as well as for practical purposes of achieving
a critically coupled design.
This is very useful as the typical purpose of
the waveport simulation is to collect a
simulated frequency-dependent reflection
coefficient ($S_{1,1}(\nu)$)
that predicts the results that would be seen
for a physical device using a vector network
analyzer measurement.

### Orthogonality Requirements for Multiple Excitation Fields {#sec:orthoReqs}

#### low-field ODNP std: cyl. ESR cavity + hairpin/saddle → too little signal

It is relatively common for labs with low-field
ODNP capabilities to use an instrumentation
setup that includes a cylindrical ESR cavity
and a small saddle or hairpin NMR probe for
RT measurements of samples at liquid state.
Under these conditions,
the confounding factors of both low volume
samples and a low field magnet make for cases
where noise is not only difficult to mitigate
but simply having inadequate sample for
generating sufficient signal can make measurements
difficult [@Guinness2025SepDetCha].

![ Schematic sketch of hairpin and solenoidal NMR probes Increased magnetic field strength illustrates motivation for desiring a higher sensitivity probe.](./media/BothProbes_Bfields.png){#fig:ProbeMagFieldsDrawing height="3.89375in"}

#### hairpin spares TE011 but wastes rf; solenoid wrecks TE011

This includes our current setup in the
acquisition of an ODNP experiment which uses
a common cylindrical ESR cavity with a hairpin
loop NMR probe.
Labs who currently implement ODNP experiments
tend to use these or small saddle coil designs
as these probes minimally perturb the TE~011~
cylindrical mode employed in most X-band ESR
instrumentation[@Doty2007].
For most cases of study in our lab,
this is adequate althought as reported
previously, suffers from very inefficient use
(and detection)
of rf magnetic fields[@Guinness2025SepDetCha].
The cylindrical TE~011~ resonator cavity is
drastically perturbed upon incorporation of
a solenoid, generating areas of heating
(significant E field) and imhomogenous
$\mu\omega$
magnetic fields at the sample's location.

![Sideview slices of the currently utilized cylindrical cavity design without and with the currently used hairpin NMR probe as well as the proposed solenoidal probe. The top row displays the electrical fields while the bottom row displays the magnetic fields. As can be seen in both the electric and magnetic field projections, the solenoidal probe's introduction greatly perturbs the resonant μw mode of the cavity, especially at and near the sample's location inside the probe.](./media/cyl_cav_uncoupled_all_EandHfields.png){#fig:EandHfieldsfor_3probes_cylcav width="6in"}

#### solenoid in TE011 → hybridization; fix = make μw & rf fields literally orthogonal

The addition of the solenoidal coil along the
main axis of a cylindrical TE~011~ cavity
generates a mixed system,
with the resulting mode pattern a hybrid
(linear)
combination of the TE~011~ resonant mode and
the self-resonant helical mode of the solenoid
[@Mett2008DieMicRes].
Borrowing terminology from quantum mechanics
in handling wavefunction interactions,
we refer to this linear mixing as "hybridization"
to help distinguish it from "coupling" to the
transmission line.
Notably,
hybridization allows a dark mode
to influence a bright mode,
even though the dark mode does not itself
couple to the transmission line
[@Mett2008DieMicRes].
The design criteria for constructing a
high-sensitivity ESR resonator *vs.* for
incorporating a high-sensitivity NMR resonator
are somewhat orthogonal,
and this paper will demonstrate how the two
modes of operation can be optimized by making
the fields for the μw (ESR) and NMR
(rf)
literally orthogonal.

#### precedent: dual-mode & TM110 ENDOR resonators w/ solenoid

As part of our investigations,
we are inspired by other complex resonator
designs [@folliNovelDualMode2020;
@Avdievich2001MulProEPR;
@He2021].
A dual-mode TM~110~/TM~010~ resonator illustrates
a design capable of generating 2 orthogonal
modes nearby in resonance frequency,
while a modified TM~110~ resonator using a
solenoidal rf probe enabling ENDOR capabilities
supports the feasibility of the similar ODNP
design we seek out studying [@Zweygart1994TM110ENDOR].

#### rect. TE102: '0' axis is free → solenoid along it allows longer sample

We are interested in using a rectangular cavity
to generate a TE102 mode which,
similar to the TE~011~ mode generated using
the cylindrical resonator cavity,
has a B field maximum aligned along a central
axis of the resonator.
A rectangular prism allows 2 sensible orientations
along which to introduce the solenoid probe
within the rectangular cavity resonator that
maintain field orthogonality between the
excited fields of the rectangular resonator
and solenoid probe.
The Basal conditions defining the TE~102~ mode
of the cavity dictate the '0' dimensional axis
of the resonator is adjustable without affecting
the fields of the resonant mode.
This axis is the preferred dimension for the
solenoid probe's placement as it allows
flexibility for increased probe and sample
length (see Figure 3).

#### solenoid in cyl. cavity → low Q, no ODNP [Red.? cyl-problem]

Two phenomenological observations illustrate
the design problem that we seek to overcome
and the design solution for a different type
of TM mode using dual-mode resonator that
inspired our hypothesized ODNP resonator design
[@Zweygart1994TM110ENDOR].
The problem is shown above for current ODNP
instrumentation setups such that attempts to
support a solenoid NMR probe inside a cylindrical
cavity results in a very low Q factor and the
inability to perform ODNP.

#### B alignment causes hybridization; parallel solenoid in rect. cavity hybridizes too [join w/ next?]

This linear mixing of modes supports the
hypothesis that the alignment between the
electromagnetic fields of the resonant TE~011~
and the active helical mode leads to the
hybridization observed in the relevant field
results.
The solenoid placed parallel to the B field
of the rectangular cavity in a similar field
alignment as tested in the cylindrical cavity
also shows significant hybridization between
the two resonant modes.
We owe some credit for the inspiration to
investigate a solenoid in a rectangular cavity
for the purposes of ODNP to a TM~110~ resonant
mode ENDOR resonator which takes advantage of
reorienting the solenoid perpendicular to the
magnetic field of the TM~110~ mode which
happened to present minimal mode mixing between
the resonant modes of the helix and rectangular
cavity [@Zweygart1994TM110ENDOR].

#### test ⊥ orientation, cue from TM110 ENDOR [join w/ prev?]

Operating under the hypothesis that the
alignment between the magnetic fields of the
helical mode and the desired resonator mode
is what leads to this hybridization,
a rectangular cavity system with solenoid
oriented in such a way appears to support this
hybridization that arises from the H field
alignment.
(@fig:solenoidDirection).
The addition of the solenoidal coil parallel
to the magnetic field of the TE102 cavity
introduces a helical mode.
However,
taking a cue of from orthogonal orientation
of the solenoidal axis and the magnetic field
of the TM110 mode of many ENDOR,
resonators (Zweygart/Thanner/Lubitz 1993),
a second simulation explores a field perpendicular
to the desired mode's magnetic field direction,

![Fields plotted along the center plane of the cavity,
composite electrc field (red) and magnetic field (blue).
The sample sits in the middle of the solenoid seen in the center.
When the solenoid is oriented with its axis along the direction of the magnetic
field of the cavity,
helical mode hybridizes significantly with the cavity resonance
(top).
As a result, regions of low magnetic field
intensity (dark blue),
as well as electric field drawing very close to the sample region
(red areas spanning between) the rungs of the helix result.
In contrast,
when oriented perpendicular to the magnet field (bottom)
such hybridization is generally avoided;
while the helix slightly perturbs the magnetic field,
pushing it away from the sample somewhat,
a significant field still remains flowing through the sample volume.
](./media/H_E_composite_example.png){#fig:solenoidDirection height="5in"}

#### ⊥ orientation: minimal mixing → solenoid/sample length free

In the non-agreeable potential orientation,
areas of perturbation at the B field maxima
arise along the sample's location due to the
helical modes generated through the solenoid's
incorporation.
These perturbations can also be seen in the
TE102's E field minima at the solenoid's and
sample's location as the generated helical
mode produces areas of dielectric loss thermally
heating any potential sample.
With the solenoid in the more agreeable
orientation,
the minimal mixing of the generated helical
modes with the TE102 mode enables the desired
capability of designing a solenoid-incorporated
ODNP resonator with varying heights (and
thereby)
enabling the optimization of the solenoid's
and sample's length within the cavity.

### Avoiding Undesired Hybridization of the ODNP Resonant Mode {#sec:avoidHybr}

#### mode map vs pitch → pick pitch w/ helix modes off TE102

Resonator cavities produce other transverse
electric/magnetic mode(s)
beyond the modes they are designed for that
appear at their own respective resonance
frequencies.
Periodically-lobed helical resonant modes can
appear standalone within the cavity as a
function of the helix's dimensions,
in particular its pitch.
Hybridized modes between interactions of the
helix within the resonator also appear to
develop as the helix itself behaves as a
resonator whose helical modes can interact
with the modes of the resonator,
often in undesirable ways.
This introduces multiple sets of potential
modes nearby in frequency to the desired
resonator's TE102 mode,
adding to the desire for a method to isolate
the location of the desired mode from any
other resonant modes that begin to appear
nearby.
By changing the helix's pitch inside of the
resonator,
the resonance location of both helix and
helix-resonator hybridized modes significantly
shift in their respective resonance frequencies.
Using the eigenmode solution setup,
we can determine the location of multiple
modes in one solution,
mapping all modes relative to helix pitch.
By finding helix pitch values where the
resonance frequencies of these undesired modes
are shifted away from the desired TE~102~
resonator mode,
we can control and minimize the degree of
hybridization between the TE~102~ mode and
these other undesired modes.
Changing the helix's pitch does effect the
achievable magnetic field strength of the
probe,
with a trend decreasing with increasing pitch.
Because we can view the fields of the solved
modes using the eigenmode setup,
a selection of unperturbed/less-perturbed
TE102 modes can be made visually while still
locating a model with a helix pitch such that
the achievable magnetic field strength and
NMR sensitivity are still acceptable.

![Map of resonant modes by relative $\Lambda$ amplitude solved across a 9 to 11 GHz frequency range for the solenoid-incorporated uncoupled TE~102~ resonator design. Plots are stacked by increasing heix pitch values associated with the value set for each model's solenoid probe](./media/UncoupledModeMap_250801.png){#fig:MappingModesByFreqvPitchUncoupled width="6in"}

#### helix modes (lobed E) disrupt cavity modes where freqs cross

The self-resonant helical modes that appear
as a function of the helix's pitch are lobes
of E field around the helix,
with oscillating lobes and nodes of H field
inside of the solenoid probe.
These number of lobes for these helix modes
appear with increasing order at smaller solenoid
pitches in the μw frequency range of
interest for the desired X band ODNP resonator.
These modes do appear to significantly disrupt
the fields of any of the cavity resonator's
modes where they overlap in resonance frequency.

![Sideviews of electric and magnetic field spectra for the TE~102~ mode of the symmetrical inductively coupled resonant cavity for the model with a 0.8 mm helix pitch. At this solenoid pitch, hybridization occurs between the TE~102~ mode and the 7 lobed helix mode due to the close proximity of their resonance frequencies.](./media/TE102mode_0p8mmpitch_EandH_7lobedhelixperturbed.png){#fig:BadPitch0p8mmCoupled width="6in"}

![Sideviews of electric and magnetic field spectra for the TE~102~ mode of the
symmetrical inductively coupled resonant cavity model with a 1.7 mm helix
pitch.
At this solenoid pitch, hybridization is deterred through a lack of
proximity with the resonance frequencies of the nearby helix modes
(3 and 4
lobed helix
modes).](./media/TE102mode_1p7mmpitch_EandH_goodpitch.png){#fig:GoodPitch1p7mmCoupled width="6in"}

#### at crossings TE102 loses homogeneous H / low E at sample

The figures above illustrate two such pitches.
In one case (@fig:BadPitch0p8mmCoupled),
a perturbation that admixes the nearby helix mode
significantly changes the field patterns of
the TE~102~ mode.
In another case,
where the resonance frequency of the helix mode
is further from the resonance frequency of the TE~102~ mode,
the TE~102~ mode fields change much less
(@fig:GoodPitch1p7mmCoupled).

Choice of helix pitch thus proves critical to ODNP applications.
ODNP applications
require a homogeneous $B$ field and minimal $E$ field
at the center of the resonator.
The design that shows greater admixture of the helical mode
(@fig:BadPitch0p8mmCoupled)
includes lobes of field along the central axis
(where the ODNP sample lies),
resulting in less $B$ field homogeneity and more
$E$ field interaction with dielectrically lossy samples.
Thus, the design in @fig:GoodPitch1p7mmCoupled supports the ODNP
application much better.

![Map of resonant modes by relative $\Lambda$ amplitude solved across a 9 to 11 GHz frequency range for the solenoid-incorporated symmetrical inductively coupled TE~102~ resonator design. Plots are stacked by increasing heix pitch values associated with the value set for each model's solenoid probe](./media/CoupledModeMap_250801.png){#fig:MappingModesByFreqvPitchCoupled width="6in"}

#### coupled map: opening cavity → stronger, wider hybridization (TM111)

By looking at the effect of changing the
solenoid's pitch for the coupled designs,
most modes are minimally affected at pitches
where their resonance frequencies are separated
from other nearby modes.
However,
with the addition of opening the cavity
resonator for the transmission of power,
perturbations where modes appear to overlap
appear more hybridized in their interactions.
These can be seen by the TM111 mode's interactions
with the TE111 mode and 3 lobed helix mode as
the solenoid's pitch increases to a 2.0 mm
height and larger.
The TM111 mode's occurrence appears to be
shifted at lower frequencies with the addition
of a coupling device,
relative to the uncoupled investigation.
The hybridization of the TE~102~ mode and 3
lobed helix mode cross each other over a short
range of solenoid pitches while the TM~111~
mode does not appear to separate from the
TE~102~ mode once they cross paths,
elucidating each of these two perturbing modes
interactions with the TE~102~ mode independently.
The helix modes in general appear to most
strongly affect the TE102 mode directly where
they overlap but this doesn't extend out much
further as long in there is notable difference
in their resonance frequencies.
The same cannot be said for the helix modes
(at least the 3 lobed helix mode)
and the TM111 mode which shows an area of
perturbation both in terms of varying the
helix's pitch and causing noticable variation
in each of their resonance frequencies.
Its also noteworthy that between the uncoupled
and coupled investigations, the TE111,
TE102 and TE112 modes do not appear to have
a significant change in their resonance
frequencies while the TE021 mode appears at
a lower resonance frequency in the coupled
designs vs the uncoupled.
None of the TE modes show any dependence on
their resonance frequencies relative to the
solenoid's pitch.

### Calculations of Resonator Efficiency {#sec:calcResEff}

#### compute Λ in eigenmode via field calculator over sample vol.

The resonator efficiency parameter, $\Lambda$,
serves as a useful indicator of a resonator's
magnetic field strength (over a specified
volume)
relative to the resonator's power loss.
Because this is relative to power loss,
its extremely useful to determine this parameter
for a loaded/coupled design.
Using (the lambda equation in the theory
section),
we take advantage of the field expression
calculator tool within the HFSS eigenmode
simulation setup to determine this parameter
over the intended volume of the sample cylinder,
determining the resonator's relative magnetic
field strength that aligns within the region
of the solenoid probe.

#### driven modal loses mode overview & needs prior coupling know-how [Red.? conv-driven-modal]

The conventional resonator design strategy
within HFSS initially uses the eigenmode
simulation setup for the investigation of an
unloaded design but then transfers that design
to a driven modal simulation setup for the
design's modification to accommodate the
supplying of power.
While the driven modal simulation setup enables
the investigation of a loaded resonator design,
it does relinquish the ability to view all
resonant modes solved along the simulation's
frequency range and easily view the fields of
all those modes.
The driven modal simulation setup also requires
some knowledge of acceptable coupling designs
to utilize to acquire any meaningful results
from the simulated frequency sweep of the
designed device.
This can restrict the designer to fallback
into using more traditional investigation
methods of supplying power to a resonator.

### Exploring Coupling in Power in an Eigenmode Simulation Setup {#sec:couplingPower}

#### PML lets eigenmode model loaded resonator [Red.? PML]

Here we provide an alternative strategy allowing
one to stay within the eigenmode simulation
setup through the important transition in the
design process from investigating an unloaded
resonator to a loaded resonator.
Included within the HFSS software is the
Perfectly Matched Layer (PML)
boundary condition for the simulation of an
open model face that allows for the uninhibited
radiation of waves from the relevant design
face.
The PML boundary is used to model the radiative
losses that arise from a open dissipative
model with an attached transmission line.

#### magnet gap forbids conv. waveguide → PML enables unconv. orientations [Red.? magnet-gap]

We must preserve the orthogonality between
the magnetic field direction of the static
$B_0$ field, the radio frequency NMR excitation,
and the μw frequency ESR excitation
used in the performance of DNP experiments.
Because of our instrumentation setup,
the spacing of the magnet gap between the two
Helmholtz coils that generates the static
$B_0$
field we use cannot accommodate the conventional
waveguide coupling scheme used with rectangular
cavity resonator.
The PML boundary can quite easily be placed
at the end of the waveguide for an open model,
no matter the relative design scheme.
This enables the investigations of unconventional
waveguide orientation schemes that still couple
in power to the rectangular ODNP resonator
while preserving the necessary field
orthogonalities.

#### PML advantages: all modes, all fields, loaded Λ [Red.? PML]

This method using the PML boundary for the
supplying of power to a resonator within the
eigenmode simulation type has multiple
advantages;
particularly the abilities to determine all
resonant modes including the dark modes
(those poorly coupled in),
view the resonant fields for all/multiple
solved resonant modes,
and calculate useful parameters that characterize
the fields and coupling capabilities of each
loaded design.
Through the use of the PML boundary simulating
the radiative loses that arise from a resonator
with power coupled in,
this ability to simulate the application of
this load enables a more accurate estimation
of the resonator design's efficiency parameter,
$\Lambda$.

#### eigenmode less restrictive than driven modal [Red.? magnet-gap]

Investigating a loaded design within the
eigenmode simulation setup offers reduced
restrictions on what can be simulated compared
to within the driven modal setup.
As mentioned above,
the investigation of a variety of non-traditional
coupling schemes is also enabled.
We can evaluate many alternative coupling
schemes such that they maintain the required
field orthogonalities and still design a loaded
resonator that fits within the physical
restrictions of our current instrumentation's
magnet gap.

![Sideviews of electric (left column) and magnetic (right column) field spectra of the TE~011~ mode for a cylindrical cavity design with coupling device incorporated. The evanescent fields brought about by the iris port and waveguide's introduction can be clearly seen. The difference between the unperturbed TE~011~ mode fields without a probe included (top row) and the areas perturbed by the helical probe's insertion (bottom row) can be detected.](./media/CoupledCylCav_labels_red-blue.png){#fig:CylCavWithSolenoid width="6in"}

### A Coupling Device for Modulating $\beta$ {#sec:couplingBeta}

In other words, the third problem is solved
by introducing a reciprocal approach to
resonator design.
To explain by analogy,
the classical trope of the opera singer
shattering the wine glass using solely their
voice resembles a waveport simulation.
The opera singer relies on their extraordinary
vocal capabilities to modulate their pitch,
direction,
an internal resonances to match an intrinsic
resonances of the wine glass.
In contrast,
the strategy employed here would be analogous
to ringing the glass with a fork,
and employing a device that monitored pickup
of that vibration in the vocal folds of the
singer.
Though more technically involved,
this would enable the singer to optimize their
vocal resonance before they produced any sound.
Important here,
it allows identification of the intrinsic
resonance of the glass before the singer even
interacts with it.
Furthermore, as we shall see,
such an eigenmode-based strategy provides more
useful information for situations that start
with a sub-optimal coupling to the power
source.

![Alternative symmetrical capacitive coupling scheme for the rectangular resonator design with solenoidal probe inserted. Differences in the H field x, y, z components near the region of the solenoidal probe's insertion as shown with the complex vector magnitude of these residual field differences below and the top-down view of the capacitive coupling scheme design provided in the right adjacent image.](./media/Symm_capacitive.png){#fig:diffFigSymCap width="6in"}

![Alternative resonant coupling scheme for the rectangular resonator design with solenoidal probe inserted. Differences in the H field x, y, z components near the region of the solenoidal probe's insertion as shown with the complex vector magnitude of these residual field differences below and the top-down view of the resonant coupling scheme design provided in the right adjacent image.](./media/Resonant_capa.png){#fig:diffFigResonant width="6in"}

![Alternative grated symmetrical inductive coupling scheme for the rectangular resonator design with solenoidal probe inserted. Differences in the H field x, y, z components near the region of the solenoidal probe's insertion as shown with the complex vector magnitude of these residual field differences below and the top-down view of the grated inductive coupling scheme design provided in the right adjacent image.](./media/Symm_inductive_grated.png){#fig:diffFigGratSymInd width="6in"}

![Alternative symmetrical inductive coupling scheme for the rectangular resonator design with solenoidal probe inserted. Differences in the H field x, y, z components near the region of the solenoidal probe's insertion as shown with the complex vector magnitude of these residual field differences below and the top-down view of the symmetrical inductive coupling scheme design provided in the right adjacent image.](./media/Symm_inductive.png){#fig:diffFigSymInd width="6in"}


#### field views reveal coupling-induced E hot spots near sample

The ability to view the evanescent fields
inside of the waveguide for any loaded design
has shown to be incredibly useful for determining
the effects of individual coupling changes.
Being able to zoom in and view the fields
within the resonator near the sample is also
important for visualizing how perturbations
like the solenoid, coupling scheme,
or an adjustable coupling device can potentially
introduce areas of high electric field at or
near the sample that we want to avoid as they
lead to potential sample heating and dielectric
losses.

![By solving a set of parametric simulations for the symmetrically inductive coupling solenoid-incorporated designs with an iris screw added and position in the waveguide modified, optimal iris screw positions for maximizing coupling variance can be determined $\DeltaBeta$. This can be very useful to more easily achieve a critically coupled model.](./media/Cu_Beta_vs_IrisScrewHeight.png){#fig:needsname1 width="6in"}

![Schematic of iris screw incorporated model based on relative fractional guide wavelength distance from the coupling port](./media/IrisScrewHeight_Diagram.png){#fig:needsname2 width="6in"}

![Sideview of electric and magnetic field projections for overall proposed ODNP resonator design. Solenoid probe along with symmetric inductive coupling scheme and iris screw incorporated.](./media/TE102mode_0p49LambdaG_IrisScrewHeight.png){width="6.5in"}

## Conclusion

Eigenmode simulations offer a wealth of information during early stages of μw
resonators
design.
<WKcom>
Bring into conclusion, incorp
</WKcom>
They easily focus on a mode of interest,
with no need for the designer to consider
coupling to the transmission line or to know
the precise frequency before simulating.
They also surveil
all modes of each design,
thus offering insight into how a design will
respond to imperfections in construction and
to modifications[@Mattar2017ModFieTwo].
In particular,
a qualitative understanding of cavity perturbation theory
can draw on
eigenmode simulations to understand and minimize the
disturbances introduced by perturbations.
However,
most existing protocols require closed structures
and avoid the crucial design problem of coupling
the resonator to a transmission line that
supplies power -- *i.e.* a coaxial cable or
(here)
a waveguide[@Mett2008DieMicRes].
This results in a bottleneck in the design
process when eigenmode simulations are converted
to waveport simulations (where the waveport
represents the transmission line);
this step requires not only a change of
simulation type,
but the simultaneous addition of physical
design elements (the "coupling device")
that efficiently couple to the
waveport[@Neudert2014AldGraRes].
Furthermore,
while popular simulation software (*e.g.*
Ansys Electronics desktop, née HFSS)
offers automated methods for tracking the
response of a waveport simulation to variations
of design parameters,
these techniques have the practical drawback
that they do not extend to eigenmode simulations
that track multiple eigenmodes.


- Why present a protocol/strategy for the
  simulation of a μw resonator?

We are currently unaware of any systematic
protocols for the simulation and design of
resonant objects for magnetic resonance studies
using ANSYS HFSS.
We particularly want to highlight the use and
benefits from the PML boundary available
through ANSYS HFSS's eigenmode simulation
setup for its capabilities in representing
the radiative losses that arise through the
incorporation of a tranmission line to a
modified opened resonator design to supply
power to a resonator.

- Why is this protocol/strategy important?

We believe this method of use of the PML
boundary is underutilized (or at least deserves
greater recognition).
This general strategy has potentially broad
applications to any instigator designing a rf
and/or uw resonant device (including those
for ESR and/or NMR applications),
especially those who cannot resort to the
conventional/traditional design tropes used
throughout the existing literature pertaining
to which ever kind of device they are actively
investigating.

## Supporting Information

![Early version of Uncoupled Parametric on helix pitch](./media/image3.png){#fig:needsname3 width="7in"}

### RLC models

An RLC equivalent resonant circuit is often
used as the model for a basic μw
resonator.
Although we will not delve extensively into
this analogy, the total input power delivered
to the resonator, $P_{input}$,
can be defined in terms of the power loss,
resonance frequency, and average magnetic
($W_{m}$) and average electric ($W_{e}$)
energies stored in the analogous circuit's
respective inductor and capacitor as shown
below.

$$
P_{input} = P_{loss} + 4 j \pi \nu_{0} (W_{m} -
W_{e})
$$
[@Pozar2012MicEng]

While the energies stored in the μw
cavity oscillate between inductive and
capacitive,
the fields of the transverse mode generated
at the respective resonance frequency being
studied also depends on how those energies
are stored (including at what phase).
The magnetic and electric energies each
conversely alternate between maximums equal
to twice their average energies and nulls in
quadrature with each other.
At resonance, where $W_{m}$ and $W_{e}$
are equivalent,
the resonator's input impedance is purely
resistive and real.
This helps illustrate Q's ability to serve as
a measure of the resonator's dissipative losses
as these losses are represented through the
cumulative resistance of the equivalent resonant
circuit.

$$
Q_{u} = 2 \pi \nu_{0} (\frac{W_{m} + W_{e}}{P_{loss}}) = \frac{1}{2 \pi
\nu_{0} R C}
$$

During traditional investigations in cavity
resonator design,
major attention when designing a closed cavity
resonator gets paid to maintaining a maximum
of the resonator's quality factor.
When incorporating the inclusion of a coupling
device,
sustaining a maximum Q is imperative along
with minimally perturbing that design (and
minimally disrupting said achievable Q).
A method for supplying power to a resonator
includes the incorporation of a transmission
line with a coaxial line or waveguide in some
form into the resonator's design,
electromagnetically "opening" the model and
allowing the entrance and emanation of
electromagnetic energy.

Returning to the series RLC circuit analogy,
this device modification for the supply of
power into a cavity resonator serves to behave
the same as an externally applied resistive
load.
This external load represents the energy lost
by the now electromagnetically "opened" cavity
resonator through the coupling holes used to
incorporate the supplying of power to the
designed device.



# Rapid Spin Labeling of Surface Sites
## Introduction

ODNP spectroscopy in the liquid state requires less volume than a traditional
NMR experiment, even when performed in conjunction with quantitative ESR.
Although this is an advantage, sample preparation itself still has its
disadvantages, especially when investigating biological samples such as
proteins and other macromolecules.

One particular desire while developing a biological ODNP study is to have a
catalog of single cysteine mutants for site-directed spin labeling and
spectroscopic analysis.
Being able to investigate multiple locations along a
proteins' surface or embedded within their structure is essential for the scope
of an ODNP study to develop an understanding of the variability in hydration
dynamics at various sites.

Prediction softwares provide some insight as to good sequences for generating
these mutants using PCR-based mutagenesis alongside their required melting
temperatures but are not perfect and can require further troubleshooting.
Initial ODNP measurements were deployed using mutants generated using
QuickChange and related mutagenesis technologies.
These use high-fidelity
polymerases for amplification which relies more on the original plasmid
template rather than using whole-plasmid doubling capable of exponential
amplification of the mutant plasmid.

## Experimental Methods

## Results and Discussion
<WKcom>
[Incorporate] Using modern low-error, high amplification polymerases for
rapidly generating mutants
[Incorporate] - Using gradient PCR alongside gel chromatography analysis
</WKcom>

<WKcom>
Add Mutagenesis protocol figure here
</WKcom>



# Precision Quantitative ESR and Lineshape Comparison that does not rely on Lineshape Simulation
## Introduction

An accurate determination of the concentration of spin-label in a sample is essential in the process of performing and interpreting an ODNP experiment and its collected data. There is a standard protocol for quantifying free-electron concentration in the analysis of QESR spectra [Weber ELEXSYS Manual], but there are two problems that lead to relatively low precision: 1) The Q value recorded in XEPR isn't to high precision and 2) QESR processing requires double integration, which serves as one source of uncertainty, alongside the issue that the standard software provided in XEPR doesn't show the baseline being used.

There are further complications during the performance of a QESR experiment that must also be considered. Slight changes in cavity tuning (ie. the microwave resonance frequency of the resonator cavity), changes in cavity position which affects the Hall sensor's calibration, and even changes in room temperature between experiments can alter locations of the ESR spectra along the $B_0$ axis making comparing different spectra difficult. This can even include different spectra of the same sample between experiments performed on different days. There are solutions to overcome these challenges but they require either additional calibration steps or additional hardware.

Including for ODNP, it is very important to have precise quantitative ESR measurements. During the process of performing an ODNP experiment, the determined spin label concentration is used to have a properly determined list of delayed measurement times across the timespan of the sample's relativity at multiple powers. An accurately determined concentration is also needed for the interpretation of the collected ODNP data for determining $k_{\sigma}$ from the cross-relaxation rate for differentiating the contribution of cross-relaxation form each individual protein.

One solution to this overall problem would be to perform simulation or wavelet analysis, but these each introduce their own new sets of assumptions. We instead explore the solutions of using a home-built script to illustrate the individual steps of spin quantization and a method using correlation alignment for the comparison of similar spectra.

## Experimental Methods 

<WKcom>
- Describe process of capturing EPR spectra and XEPR
- Include single EPR spectra here and layout basic processing methodology
</WKcom>

## Results and Discussion





<WKcom>
Add figures of:
- Tuning curve to normalized enhancements (make horizontal)
- Scaled overlay of ESR spectra for the same mutant, diff samples/concentrations
</WKcom>

# Methods for more Reproducible and Precise ODNP Measurements
## Introduction

<WKcom>
Focus on hardware and airflow improvements, assisting probe support design
- Hardware improvements - improved probe supports, sample changer, airflow reconfigure
- Software improvement - Capturing NMR signal, ODNP processing procedure (kRas as example)
- assisting in noise measurements (cite AG paper)
</WKcom>

## Experimental Methods

<WKcom>
Process of probe support design
process of airflow improvements
</WKcom>

## Results and Discussion







# Utilizing the IRI activities of PVA with co-solute incorporation to inform controlled hydrogel production
## Introduction

Polyvinyl alcohol (PVA) is the most widely studied synthetic polymer that
exhibits ice recrystallization inhibition (IRI), a key mechanism for preventing
ice crystal growth during the thawing process of cryopreservation. The findings
above show that PVA does not strongly bind to ice itself but is still extremely
efficient in its ability to effectively inhibit ice recrystallization through
the influence it has on restructuring interfacial water. Also shown above, we
can use added cosolutes including glycerol, sucrose, and trehalose in solution
who are capable of suppressing the freezing point of an aqueous solution for
additional improvements on the effectiveness of cryopreservation. Taking from
the morphological and spectroscopic analysis of PVA's IRI mechanism, a current
investigation of PVA-based hydrogels has been undertaken investigating the
tunability of these hydrogels' mechanical properties through the mechanism of
PVA's IRI effectiveness by tuning the annealing of the hydrogels at their
particular ice-water coexistence temperatures.  



## Results and Discussion



<WKcom>
Include for figures:
- Overview of IRI mechanism to tune hydrogels, use currently used figure in presentation
- Light microscope images of cryo-ultramicrotome slices, visualizing mesh and pores as well as overall gel structure
- Gd-labeling PVA 
</WKcom>
 



# Methods and Procedures
## Protocol for ImageJ processing of Microscope images
### Important to know:
You will need the image series for a microscope freeze-thaw experiment saved as
.TIF images.
It will most benefit you to use ones saved with available scale
bars imprinted on them.
ImageJ doesn’t not seem to have an event history/logged
actions to go back to previous points.
“Undo” will only go back 1 action so
make sure each click/action you make is precise.
I also recommend saving after
each step generally (beyond where indicated in the protocol below)
and in the
middle of steps if necessary.
Two python scripts automating this ImageJ
processing analysis were developed to be run from the command line outside of
ImageJ allowing for more efficient and uniform processing of the modified splat
assay results.
The first script automates the processing up to the threshold
method selection and watershed application while the second script takes the
resulting grey-filled Tiff image files for the chosen threshold method and
watershed application for the actual particle analysis.
Both scripts save at
each step in the image processing procedure as well as all resulting output
files.

### In ImageJ;
<WKcom>
This needs to be slightly updated to match the automated procedures specified above
</WKcom>

		#. Go to <span style="color:red">`File -> Open`</span> to open a file manager where the desire .tiff file can be selected.
		#. Go to <span style="color:red">`Image -> Duplicate`</span> which will create a second copy of the selected image.
		#. Save either the original or copy (I typically save the original)
		to the side/minimize to come back to later and use as a reference.
		#. With the duplicate selected, go to <span style="color:red">`Image -> Color -> Split Channels`</span>. This will split the duplicated image into 3 B&W images of the 3 wavelength/color contributions in  the full RGB colored original TIF image.
		#. Review the 3 channeled images for which one appears with the most contrast
		with defined crystal edges, most typically this is the '(red)' channeled
		images.
		Save all three outputs to come back to if you're unsure.
		#. Select <span style="color:red">`Process -> Noise -> Despeckle\le/span>.
		#. Select <span style="color:red">`Process -> Enhance Contrast`</span>. In the gui that appears, choose the default saturated pixels (for me this is 35%), and check Normalize and Equalize histogram.
		#. Select <span style="color:red">`Process -> Binary -> Convert to Mask`</span>. There is no way to select a light background or which method is used to determine the mask. Because of this, the software will sometimes choose a dark background with the ice crystal boundaries in white. If this happens, select <span style="color:red">`Edit -> Invert`</span> to flip the dark and light colors that make up the image.
		#. Select <span style="color:red">`Process -> Binary -> Close`</span>, which connects any pixels that are 1 pixel away from one another. If the backgrounds were flipped and the image is inverted like mentioned above, this can do the opposite of desired and open some boundaries between ice crystal. Keep an eye out for this.
		#. This is a good point to save, prior to selecting an area for the actual
		touching up and analysis.
		#. Go to <span style="color:red">`Edit -> Options -> Colors`</span> and for 'Selection:' pick 'Red'. This is for the rectangle/ellipse/text box/etc tools in the lower command panel. Click and draw a circle over the image, you will select dimensions for the circle next. If you find it is needed, you can also make a reference circle on the original image you have minimized by refollowing this and the following step for the upcoming ice crystal selection step.
		#. Select <span style="color:red">`Edit -> Selection -> Specify`</span> and in the Specify gui that pops up choose the following dimensions for the circle:

				Width: 800
				Height: 800
				X coordinate: 800
				Y coordinate: 600
				[x] Oval
				[ ] Constrain square/circle
				[x] Centered

		#. If you are performing this analysis on a sample which has many
		bubbles/speckles or has reflections/shadows, you will need to clean up the
		image as best you can.
		You want each ice crystal to be fully enclosed with a black border as best as
		possible.
		Using the original colored duplicated image as a reference,
		you can use the color picker and paintbrush tools to select white and black
		colors as needed to enclose each crystal (black) and color in each crystal
		(white) at least near the boundaries to be able to fill that crystal with gray
		color in the next step.
		Make these modifications within the circle you have defined first.
		It is best to do as minimal manual changes to the image at this step as possible.
		An automated protocol has been implemented avoiding this step
		#. Save and again generate a duplicated image selecting <span style="color:red">`Image -> Duplicate`</span>. This duplicated image will now be a square defined by the specified circular selection above.
		#. Go again to <span style="color:red">`Edit -> Options -> Colors`</span> and for 'foreground' select 'gray'. Also confirm background is selected as 'black'. Fill in the white space with grey of each ice crystal using the Flood fill tool in the ImageJ tool bar. Do this slowly at first, and be prepared to click `[CTRL] + [Z]` to undo any last move if a crystal is not actually enclosed. You can go back to using the color picker and paintbrush tools to fix crystals as you go.
		#. Once you have each crystal filled in with gray as you desired,
		save the file again as "...\_gray-filled.tif" or something similar/recognizable
		to you.
		#. Select <span style="color:red">`Image -> Adjust -> Threshold`</span>, a gui window will pop up with 2 slider bars adjusting the contribution of white and black to the image based on the images hues already assigned (this is why the ice crystals were filled with grey). Ideally, you can adjust the two bars such that the background (liquid) and the ice crystal outlines are white leaving the previously grey-filled crystals in black. This does not always work and a second best option is to leave just the outlines in whit and to go back in with the Flood fill tool to turn the background from black to white. This can be time consuming and thus a 3rd option is to adjust the threshold slides such that the outlines and background are in black leaving the crystals white and then inverting the image. This can lead to the watershed function at the next step not working as intended because of the specified threshold being flipped after the image's inversion. No matter which method you choose be sure to save the file before and after this step.
		#. Select <span style="color:red">`Process -> Binary -> Convert to Mask`</span> on the now threshold applied image.
		#. ImageJ's built-in watershed algorithm may work for you to determine and separate a cluster of crystals into individuals but this does not always work as expected, especially for crystals of smaller size or irregular shape such as those in trehalose-containing solution. You can apply this algorithm by selecting <span style="color:red">`Process -> Binary -> Watershed`</span> just be prepared to use `[CTRL] + [Z]` if this does not do as you intend.
		#.

## Protocol for Eigenmode Design (Using HFSS, general design principles)

This study was performed using the ANSYS Electronics Desktop 2021 R1
(ANSYS
EDT) platform and its 3-dimensional high frequency structure simulation (HFSS)
software.
The procedure for our approach to coupling design relies on using an
eigenmode solution type available within an HFSS simulation.
Each design
requires a simulation setup such that once the design is solved,
a check is
performed to ensure that each design is converged on a set maximum delta
frequency per pass, validating the resonance frequencies of the determined
modes and their solved fields.

As was desired, HFSS enables the expansion of a design along multiple design
dimensions independently, allowing for better understanding of the mechanisms
and effects of each physical adjustment to the overall resonator design.
This
includes solving for a design across multiple frequency ranges with the ability
to be able to join these results together.
The effects of variation on a design
parameter (in this case the pitch of the solenoidal NMR probe)
was also
studied, taking advantage of a script developed for modifying the value of the
specified design variable.
The processes above of producing and interpreting
the selection of design variants can be repeated with models incorporating the
necessary additions to a realistic design, including a coupling device and
joined waveguide.

This procedure of generating a base design with its different avenues of
variants is enabled by the eigenmode solution setup.
For example, the ability
to use a python script to modify the ‘pitch’ design parameter and generate a
range of otherwise identical designs with different pitch values was rapid and
automated.
While there are processing limits on the number of simulation jobs
capable of being submitted at one time, this process was also enabled to be
automated.
A ‘best design’ can then be arrived at once each design iteration
has been processed and analyzed, a procedure also capable of being automated as
described below.

Automating using python scripts was also taken advantage of to generate and
acquire each design’s simulation results.
With each valid solved design,
scripts were developed to export the fields as well as the complex frequencies
and relevant vector field values for each of the design’s solved modes.
Inherent to the eigenmode solution setup, a limited number of total modes may
be solved for in any particular solution setup for a design.
Thus using the
same base design, setups can be made with different starting frequencies to
expand the number of determined modes across a broader range of investigated
frequencies.

Inner dimensions of 21.65 mm x 30 mm x 43.3 mm were used for the rectangular
resonator based on the standing wave propagation function that define a
rectangular resonator of the TE102 mode at a resonance frequency of 9.8 GHz.
A
thickness of 2 mm is used for copper objects (cavity and waveguide)
to well
exceed copper’s skin depth of ~0.7 μm.
Wall thicknesses are also defined to
generate more realistic external conditions for the design as opposed to using
a perfect electric conductor (PEC) boundary.
Enabled within the eigenmode
simulation setup, a Perfectly Matched Layer (PML) boundary is used to model the
radiative losses that arise from opening a design for the incorporation of a
coupling device.

## Protocol for  single-cysteine mutant generation for SDSL - Applied for Proteorhodopsin protein

To prepare pR stocks of SDSL (site-directed spin label) mutants not already
available, mutagenesis of the template pR plasmid needs to be performed. We had
an issue of some mutant sequences not matching expected or not matching their
intended mutant label. To then make these mutants we desire, the protocol takes
4-5 days. Initially, primers need to be designed such to change the template pR
sequence to a cysteine residue at the desired amino acid position. Given
technology available today, this is very easy as nearly every genomics company
has an available primer design tool, typically to be used with their polymerase
chain reaction (PCR) products. Thus, we use NEBaseChanger, which is New England
Biolab’s (NEB’s) primer design tool. Now given that we used to have the mutants
that we wanted back, our primers for these mutants were still good and correct,
which I used NEBaseChanger to verify. Synthetically made primer sequences can
be ordered from Integrated DNA Technologies (IDT) if new primers had been
needed. Once new primers are received, they do need to be diluted to a 10 μM
concentration for use in future experiments. The pR template sequence plasmid
also needs to be prepared for experimental use. This is done by growing up a
template pR small culture, and miniprepping the pelleted culture to elute the
template plasmid at a high concentration and use to make a stock of the
concentration (typically ~12 ng/μL) that you desire.

The primers we use are designed for a back-to-back	 orientation, which
correlates with NEB’s Q5 Master Mix, that contains DNA polymerase, Mg2+, and
dNTPs for DNA amplification using PCR. NEBaseChanger provides a predicted
annealing temperature for the desired mutation of the primer you’re interested
in. This is just a prediction and is not always the optimal annealing
temperature for that specific desired mutation, although it does provide a
starting position to use when looking to optimize a mutant’s PCR mutagenesis
protocol. The extension step in all of the experiments I performed was
consistent, 146.25 s for the pR plasmid. LB/Amp petri dishes, made to 100 μg/mL
ampicillin in LB/Agar gelatin plates are prepared for future transformation and
transfection use. A DNA electrophoresis agarose gel was also used to detect and
look at potential amplification in the PCR products collected. PCR products
that were detected by the DNA gel were then given kinase, ligase, Dpn1 (KLD)
treatment, to digest the mutated plasmid made during PCR and degrade any
leftover template plasmid. Digested DNA after KLD treatment is then transformed
into z-competent DH5α cells, plated on the previously mentioned LB/Amp petri
dishes to incubate overnight.

Single colonies of the transformed DH5α cells from the LB/Amp plates were
picked and used to inoculate LB/Amp small cultures and grown overnight. The
presumed mutant cultures were pelleted and then miniprepped to pull out the
presumed mutant DNA plasmid. A Nanodrop was then used to determine the DNA
concentration and a portion of the plasmid was prepared and sent for sequencing
using Azenta’s Genewiz tool. If/Once sequencing comes back as the mutant
plasmid desired, the saved mutant DNA is transfected into z-competent BL21
cells, plated on LB/Amp petri dishes and incubated overnight at 37 ℃. These
colonies can then be picked directly for small cultures in the pR expression
and purification protocol below.










