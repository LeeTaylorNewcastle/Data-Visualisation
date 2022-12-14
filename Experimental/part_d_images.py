# Author: Lee Taylor, ST Number: 190211479
from imports import *
import matplotlib.image as mpimg


## Create figure of subplots 'r' = Row
fig, (r1, r2) = plt.subplots(2, 2, figsize=(19.2, 10.8))
fig.tight_layout(pad=0)
plt.subplots_adjust(wspace=0, hspace=0)
plts = [r1[0], r1[1], r2[0], r2[1]]
for plt_ in plts:
    plt_.set_xticks([])
    plt_.set_yticks([])
imgs_char = [c for c in 'dabc']
## Load and plot images
for plt_, ichar in zip(plts, imgs_char):
    plt_.imshow(mpimg.imread(f'../Images/part_{ichar}.png'))
## Render figure and save as image
fig.show()
plt.savefig('_images.png')
