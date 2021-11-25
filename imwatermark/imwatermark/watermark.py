import struct
import numpy as np
from .dwtDctSvd import EmbedDwtDctSvd


def encoder(cv2_image, watermark='', **configs):
    content = watermark.encode('utf-8')
    seq = np.array([n for n in content], dtype=np.uint8)
    watermarks = list(np.unpackbits(seq))
    length = len(watermarks)

    (r, c, channels) = cv2_image.shape
    if r * c < 256 * 256:
        raise RuntimeError('image too small, should be larger than 256x256')

    embed = EmbedDwtDctSvd(watermarks, wmLen=length, **configs)
    return embed.encode(cv2_image)


def decoder(cv2_image, length=0, **configs):
    length = length * 8
    (r, c, channels) = cv2_image.shape
    if r * c < 256 * 256:
        raise RuntimeError('image too small, should be larger than 256x256')

    embed = EmbedDwtDctSvd(watermarks=[], wmLen=length, **configs)
    bits = embed.decode(cv2_image)

    if len(bits) != length:
        raise RuntimeError('bits are not matched with watermark length')

    nums = np.packbits(bits)
    b_str = b''
    for i in range(length // 8):
        b_str += struct.pack('>B', nums[i])
    return b_str.decode('utf-8')
