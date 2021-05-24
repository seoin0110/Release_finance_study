#2.8 파일 처리 및 외부 라이브러리 활용

#2.8.1 리퀘스트로 인터넷에서 이미지 파일 가져오기

import requests
url = 'http://bit.ly/2JnsHnT'
r = requests.get(url, stream=True).raw

#2.8.2 필로로 이미지 보여주기

from PIL import Image
img = Image.open(r)
img.show()
img.save('src.png')
print(img.get_format_mimetype)

#2.8.3 'with~as 파일 객체:'로 이미지 파일 복사

BUF_SIZE = 1024
with open('src.png', 'rb') as sf, open('dst.png', 'wb') as df:
    while True:
        data = sf.read(BUF_SIZE)
        if not data:
            break
        df.write(data)

#2.8.4 SHA-256으로 파일 복사 검증하기

import hashlib
sha_src = hashlib.sha256()
sha_dst = hashlib.sha256()
with open('src.png', 'rb') as sf, open ('dst.png', 'rb') as df:
    sha_src.update(sf.read())
    sha_dst.update(df.read())
print("src.png's hash : {}".format(sha_src.hexdigest()))
print("dst.png's hash : {}".format(sha_dst.hexdigest()))

#2.8.5 맷플롯립으로 이미지 가공하기

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
dst_img = mpimg.imread('dst.png')
print(dst_img)

pseudo_img = dst_img [:, :, 0]
print(pseudo_img)

plt.suptitle('Image Processing', fontsize=18)
plt.subplot(1, 2, 1)
plt.title('Original Image')
plt.imshow(mpimg.imread('src.png'))
plt.subplot(122)
plt.title('Pseudocolor Image')
dst_img = mpimg.imread('dst.png')
pseudo_img = dst_img [:, :, 0]
plt.imshow(pseudo_img)
plt.show()
