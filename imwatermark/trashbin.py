# class WatermarkEncoder(object):
#     def __init__(self, watermark=''):
#         content = watermark.encode('utf-8')
#         seq = np.array([n for n in content], dtype=np.uint8)
#         self._watermarks = list(np.unpackbits(seq))
#         self._wmLen = len(self._watermarks)
#         self._wmType = 'bytes'
#
#     def encode(self, cv2_image, **configs):
#         (r, c, channels) = cv2_image.shape
#         if r*c < 256*256:
#             raise RuntimeError('image too small, should be larger than 256x256')
#
#         embed = EmbedDwtDctSvd(self._watermarks, wmLen=self._wmLen, **configs)
#         return embed.encode(cv2_image)


# class WatermarkDecoder(object):
#     def __init__(self, length=0):
#         self._wmType = 'bytes'
#         self._wmLen = length*8
#
#     def decode(self, cv2_image, **configs):
#         (r, c, channels) = cv2_image.shape
#         if r*c < 256*256:
#             raise RuntimeError('image too small, should be larger than 256x256')
#
#         embed = EmbedDwtDctSvd(watermarks=[], wmLen=self._wmLen, **configs)
#         bits = embed.decode(cv2_image)
#
#         if len(bits) != self._wmLen:
#             raise RuntimeError('bits are not matched with watermark length')
#
#         nums = np.packbits(bits)
#         b_str = b''
#         for i in range(self._wmLen // 8):
#             b_str += struct.pack('>B', nums[i])
#         return b_str.decode('utf-8')
