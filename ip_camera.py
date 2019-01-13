import cv2
import pygame
from pygame.locals import *
import sys

# OpenCV用の画像をPygame用に変換する
def cv2pygame(cv_img):
    opencv_image = cv_img[:,:,::-1]  # OpenCVはBGR、pygameはRGBなので変換してやる必要がある
    shape = opencv_image.shape[1::-1]  # OpenCVは(高さ, 幅, 色数)、pygameは(幅, 高さ)なのでこれも変換
    return pygame.image.frombuffer(opencv_image.tostring(), shape, 'RGB')

camera_ip = "111.111.11.1"
user_name = "name"
password = "pass"
stream_mode = "11"  # ストリーミングモード（第一設定）。機種により異なる
capture = cv2.VideoCapture("rtsp://"+camera_ip+"/"+stream_mode+":"+user_name+":"+password)
ret, frame = capture.read()
print(ret)

pygame.init()
pygame.display.set_caption("IP camera stream on Pygame")
screen = pygame.display.set_mode([1920,1080])
while True:
    ret, frame = capture.read()
    screen.fill([0,0,0])
    if ret:
        frame = cv2pygame(frame)
        screen.blit(frame, (0,0))
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

# キャプチャ画像を保存
#cv2.imwrite('lena_opencv.jpg', frame)

# キャプチャを解放する
capture.release()
