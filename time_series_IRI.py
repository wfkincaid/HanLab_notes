import cv2
import numpy as np
from skimage import filters, morphology, measure, segmentation
from scipy.ndimage import distance_transform_edt
import matplotlib.pyplot as plt
plt.style.use('default')

gly = cv2.imread(r"Candice_Images/Sugars_only_control/Glycerol/1/Images_with_scale_bar/Process_322_T0001.tif", cv2.IMREAD_GRAYSCALE)
suc = cv2.imread(r"Candice_Images/Sugars_only_control/Sucrose/2/Images/Process_312_T0001.tif", cv2.IMREAD_GRAYSCALE)
tre = cv2.imread(r"Candice_Images/Sugars_only_control/Trehalose/1/Images/Process_314_T0001.tif", cv2.IMREAD_GRAYSCALE)


Glycerol_control = [cv2.imread(f"Candice_Images/Sugars_only_control/Glycerol/1/Images_with_scale_bar/Process_322_T00{i:02d}.tif", cv2.IMREAD_GRAYSCALE) for i in range(1, 25)]
Sucrose_control = [cv2.imread(f"Candice_Images/Sugars_only_control/Sucrose/2/Images/Process_312_T00{i:02d}.tif", cv2.IMREAD_GRAYSCALE) for i in range(1, 25)]
Trehalose_control = [cv2.imread(f"Candice_Images/Sugars_only_control/Trehalose/2/Images/Process_320_T00{i:02d}.tif", cv2.IMREAD_GRAYSCALE) for i in range(1, 25)]


Glycerol_IRI = [cv2.imread(f"Candice_Images/Sugar_PVA/Glycerol_PVA/1/Images_with_scale_bar/Process_408_T00{i:02d}.tif", cv2.IMREAD_GRAYSCALE) for i in range(1, 25)]
Sucrose_IRI = [cv2.imread(f"Candice_Images/Sugar_PVA/Sucrose_PVA/2/Images_with_scale_bar/Process_334_T00{i:02d}.tif", cv2.IMREAD_GRAYSCALE) for i in range(1, 25)]
Trehalose_IRI = [cv2.imread(f"Candice_Images/Sugar_PVA/Trehalose_PVA/2/Images_with_scale_bar/Process_337_T00{i:02d}.tif", cv2.IMREAD_GRAYSCALE) for i in range(1, 25)]

# Create 6x8 grid
fig, axs = plt.subplots(6, 8,dpi =300, figsize=(20, 12))
time = 5  # Initialize time variable
# Plot images
iri_index = 0
for row in range(6):
    for col in range(8):
        ax = axs[row, col]
        if row % 2 == 0:  # Rows 1, 3, 5 (0, 2, 4): Control image
            ax.imshow(Glycerol_control[iri_index], cmap='gray')
        else:  # Rows 2, 4, 6 (1, 3, 5): IRI images
            ax.imshow(Glycerol_IRI[iri_index], cmap='gray')
            iri_index += 1
        
        ax.axis('off')

# Apply cropping (right half and bottom half)
for ax in axs.flat:
    ax.set_xlim(left=ax.get_xlim()[0] + (ax.get_xlim()[1] - ax.get_xlim()[0]) / 1.3, 
                right=ax.get_xlim()[1])
    ax.set_ylim(bottom=ax.get_ylim()[0], 
                top=ax.get_ylim()[1] - (ax.get_ylim()[1] - ax.get_ylim()[0]) / 1.3)

# Add red borders and black rectangles
for ax in axs.flat:
    # Red border
    for spine in ax.spines.values():
        spine.set_edgecolor('red')
        spine.set_linewidth(5)
    
    # Black rectangle
    rect = plt.Rectangle((0, 0), 1, 1, transform=ax.transAxes, color='k', linewidth=2, fill=False)
    ax.add_patch(rect)
axs[0, 0].text(1150, 1150, 'Glycerol', fontsize=12, rotation=90)
axs[1, 0].text(1150, 1150, 'Glycerol+PVA', fontsize=12, rotation=90)
axs[2, 0].text(1150, 1150, 'Glycerol', fontsize=12, rotation=90)
axs[3, 0].text(1150, 1150, 'Glycerol+PVA', fontsize=12, rotation=90)
axs[4, 0].text(1150, 1150, 'Glycerol', fontsize=12, rotation=90)
axs[5, 0].text(1150, 1150, 'Glycerol+PVA', fontsize=12, rotation=90)
# Set titles only for odd rows (0, 2, 4), i.e., rows 1, 3, 5 (1-based)
time = 5
for row in range(6):
    if row % 2 == 0:  # Only for rows 0, 2, 4
        for col in range(8):
            axs[row, col].set_title(f'time={time} Min.', fontsize=10)
            time += 5

plt.savefig('Glycerol_IRI_Grid.pdf', dpi=300, bbox_inches='tight')
plt.show()
