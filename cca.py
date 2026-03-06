from skimage import measure
from skimage.measure import regionprops
import matplotlib.pyplot as mplt
import matplotlib.patches as pat
import loc

# groups all connected portions and groups them together
labimg = measure.label(loc.binarycimg)
# setting the maximum width , height, that a license plate can be
platedim = (0.08*labimg.shape[0], 0.2*labimg.shape[0], 0.15*labimg.shape[1], 0.4*labimg.shape[1])
minh, maxh, minw, maxw = platedim
plateobjcoor = []
platelike = []
fig, (ax1) = mplt.subplots(1)
ax1.imshow(loc.graycimg, cmap="gray")

# regionprops is used to create a group of properties of all the labelled regions
for r in regionprops(labimg):
    # handling really small area- can't possibly be a number plate
    if r.area < 50:
        continue

    # the bounding box
    minR, minC, maxR, maxC = r.bbox
    regionh = maxR - minR
    regionw = maxC - minC
    # now ensuring that the identified region actually satisfies the condition
    if regionh >= minh and regionh <= maxh and regionw >= minw and regionw <= maxw and regionw > regionh:
        platelike.append(loc.binarycimg[minR:maxR, minC:maxC])
        plateobjcoor.append((minR, minC, maxR, maxC))
        rborder = pat.Rectangle((minC, minR), maxC - minC, maxR - minR, edgecolor="red", linewidth=1, fill=False)
        ax1.add_patch(rborder)
        # this will draw a rec rectangle over the identified regions

mplt.show()
