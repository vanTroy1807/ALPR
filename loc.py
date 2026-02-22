from skimage.io import imread
from skimage.filters import threshold_otsu
import matplotlib.pyplot as mplt

cimg = imread("car.jpg", as_gray=True)
print(cimg.shape)

graycimg = cimg * 255
fig, (ax1, ax2) = mplt.subplots(1, 2)
ax1.imshow(graycimg, cmap="gray")
thrs = threshold_otsu(graycimg)
binarycimg = graycimg > thrs
ax2.imshow(binarycimg, cmap="gray")
mplt.show()
