import numpy as np


def histogram(img):
    d = {}
    for i in range(np.max(img) + 1):
        d[i] = 0
    for ele in np.nditer(img):
        d[int(ele)] += 1
    return d


def equalization(img):
    s, add = [], 0
    d = histogram(img)
    for key in d.keys():
        add += 255 * d[key] / img.size
        s.append(round(add))
    processed = img.copy()
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            processed[i, j] = s[processed[i, j]]
    return processed


def color_equal(img):
    abs_img = get_add(img).astype(int)
    equ = equalization(abs_img)
    processed = np.zeros(img.shape)
    ratio = equ / (abs_img + 1e-7)
    for channel in range(img.shape[-1]):
        processed[:, :, channel] = np.sqrt(ratio + 0.5) * img[:, :, channel]
    processed[processed > 1.0] = 1.0
    processed = normalization(processed)
    return processed


def normalization(img):
    maximum = np.max(img)
    minimum = np.min(img)
    return (img - minimum) / (maximum - minimum)


def get_add(img):
    new = 255 * img
    abs_img = np.zeros((img.shape[0], img.shape[1]))
    for channel in range(img.shape[-1]):
        abs_img += new[:, :, channel] ** 2
    return np.sqrt(abs_img)
