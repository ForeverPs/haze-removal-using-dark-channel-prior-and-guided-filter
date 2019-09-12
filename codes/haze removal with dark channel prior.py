import heapq
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from histogram_equalization import color_equal


def get_pos(img_shape, center, patch_size):
    x_start = max(center[0] - patch_size // 2, 0)
    x_end = min(center[0] + 1 + patch_size // 2, img_shape[0])
    y_start = max(center[1] - patch_size // 2, 0)
    y_end = min(center[1] + 1 + patch_size // 2, img_shape[1])
    return x_start, x_end, y_start, y_end


def get_dark_channel(img, eta, refined=True, radius=20):
    patch_size = 2 * radius + 1
    m, n, _ = img.shape
    dark_channel_img = np.zeros((m, n))
    for row in range(m):
        for col in range(n):
            x_start, x_end, y_start, y_end = get_pos([m, n], [row, col], patch_size)
            dark_channel_img[row, col] = np.min(img[x_start: x_end, y_start: y_end, :])
    if refined:
        dark_channel_img = guided_filter(input_img=dark_channel_img, guidance=img, radius=radius, eta=eta)
    return dark_channel_img


def atmospheric_light(img, dark_channel):
    A = np.zeros((1, 1, 3))

    atmospheric_list = []
    for row in range(dark_channel.shape[0]):
        for col in range(dark_channel.shape[1]):
            atmospheric_list.append((dark_channel[row, col], row, col))

    count = int(0.001 * len(atmospheric_list))
    atmospheric_list = heapq.nlargest(count, atmospheric_list)

    for ele in atmospheric_list:
        row = ele[1]
        col = ele[2]
        index = img[row, col, :] > A
        A[index] = img[row, col, :].reshape(A.shape)[index]
    return A


def histogram(dark_channel):
    a = np.zeros((1, 256))
    for row in range(dark_channel.shape[0]):
        for col in range(dark_channel.shape[1]):
            a[0, int(dark_channel[row, col])] += 1 / dark_channel.size
    plt.figure('haze removal with dark channel prior')
    plt.subplot(121)
    plt.title('Dark Channel')
    plt.xlabel('pixels')
    plt.ylabel('pixels')
    plt.imshow(dark_channel, cmap='gray')
    plt.subplot(122)
    plt.title('Histogram of Dark Channel')
    plt.xlabel('intensity')
    plt.ylabel('probability')
    plt.bar(range(256), list(a[0, :]))
    plt.show()


def get_t(orig, a, w=0.95, t0=0.1, eta=1e-4, radius=20, refined=True):
    dark_channel = get_dark_channel(img=orig / a, eta=eta, refined=refined, radius=radius)
    t = 1.0 - w * dark_channel
    t[t < t0] = t0
    return t


def get_ak(input_img, guidance, uk, eta=1e-4):
    size = input_img.size
    pk = np.mean(input_img)
    vec = np.matrix(sum(sum(guidance * input_img[:, :, None]))).T
    inter = guidance.reshape((size, 3)).T
    sigma = np.cov(inter)
    ak = np.matrix(sigma + eta * np.eye(sigma.shape[0])).I * (vec / size - uk * pk)
    return ak


def guided_filter(input_img, guidance, radius=20, eta=1e-4):
    shape = 2 * radius + 1
    a = np.zeros(guidance.shape)
    b = np.zeros(input_img.shape)
    count = np.zeros(input_img.shape)

    for row in range(input_img.shape[0]):
        for col in range(input_img.shape[1]):
            x_start, x_end, y_start, y_end = get_pos(input_img.shape, [row, col], shape)
            uk = np.matrix([np.mean(guidance[x_start: x_end, y_start: y_end, i]) for i in range(3)]).T
            ak = get_ak(input_img[x_start: x_end, y_start: y_end], guidance[x_start: x_end, y_start: y_end, :], uk, eta)
            bk = np.mean(input_img[x_start: x_end, y_start: y_end]) - ak.T * uk
            a[x_start: x_end, y_start: y_end] += ak.reshape((1, 1, 3))
            b[x_start: x_end, y_start: y_end] += bk
            count[x_start: x_end, y_start: y_end] += 1

    return np.sum(a * guidance / count[:, :, None], 2) + b / count


def haze_removal(img, w=0.95, t0=0.1, eta=1e-4, refined=True, radius=20):

    dark_channel = get_dark_channel(img=img, eta=eta, refined=False, radius=radius)

    A = atmospheric_light(img, dark_channel)

    t = get_t(orig=img, a=A, w=w, t0=t0, refined=refined)

    J = np.zeros(img.shape)
    for channel in range(img.shape[-1]):
        J[:, :, channel] = (img - A)[:, :, channel] / t + A[:, :, channel]
        maximum = np.max(J[:, :, channel])
        minimum = np.min(J[:, :, channel])
        J[:, :, channel] = (J[:, :, channel] - minimum) / (maximum - minimum)

    # improve brightness
    J_ = color_equal(J.copy())

    plt.figure('haze removal with dark channel prior')

    plt.subplot(121)
    plt.title('Original')
    plt.imshow(img)

    plt.subplot(122)
    plt.title('De-haze with Guided Filter')
    plt.imshow(J_)

    plt.show()


if __name__ == '__main__':
    image = mpimg.imread('./image/tiananmen1.jpg')
    haze_removal(image, w=0.7, radius=10, eta=1e-3, refined=True)
