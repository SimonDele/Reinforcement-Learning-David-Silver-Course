from skimage.color import rgb2gray
from skimage.util import crop
from skimage.transform import resize
from scipy import misc

import numpy as np

def preprocessed_img(img):
    #plt.imshow(img)

    gray_scaled = rgb2gray(img)
    #plt.imshow(gray_scaled, cmap=plt.cm.gray)

    cropped = gray_scaled[34:160+34]
    #plt.imshow(cropped, cmap=plt.cm.gray)

    rescaled = resize(cropped, (84,84))
    #plt.imshow(rescaled, cmap=plt.cm.gray)

    return rescaled


def preprocessed_img_pong(observation):
    """Transforms the specified observation into a 47x47x1 grayscale image.
    Returns:
        A 47x47x1 tensor with float32 values between 0 and 1.
    """

    # Transform the observation into a grayscale image with values between 0 and 1. Use the simple
    # np.mean method instead of sophisticated luminance extraction techniques since they do not seem
    # to improve training.
    grayscale_observation = observation.mean(2)

    # Resize grayscale frame to a 47x47 matrix of 32-bit floats.
    resized_observation = misc.imresize(grayscale_observation, (47, 47)).astype(np.float32)

    return resized_observation