from skimage.color import rgb2gray
from skimage.util import crop
from skimage.transform import resize


def preprocessed_img(img):
    #plt.imshow(img)

    gray_scaled = rgb2gray(img)
    #plt.imshow(gray_scaled, cmap=plt.cm.gray)

    cropped = gray_scaled[34:160+34]
    #plt.imshow(cropped, cmap=plt.cm.gray)

    rescaled = resize(cropped, (84,84))
    #plt.imshow(rescaled, cmap=plt.cm.gray)

    return rescaled
