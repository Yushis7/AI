import pyautogui as pag
import mss,cv2
import numpy as np

#클릭 후 텀 두는 시간 지정
pag.PAUSE = 0.08

#pip install pyautogui   (오토기능)
#pip install mss (스크린샷 패키치 설치)
#pip install pyobjc-framework-Quartz(좌표 추적)
#pip install numpy(행렬연산 해주는 패키지)
#pip install opencv-python(이미지 처리를 위한 opencv 패키지)

#원하는 형태의 아이콘 위치에 좌표 놓기 icon_position
left_icon_pos = {'left':100,'top':540,'width':70,'height':70}
right_icon_pos = {'left':250,'top':540,'width':70,'height':70}

#button_position
left_button = [70,680]
right_button = [355,680]

def compute_icon_type(img):
    mean =np.mean(img ,axis=(0,1))
    result = None

    if mean[0] >50 and mean[0] <55 and mean[1] > 50 and mean[1]< 55 and mean[2]>50 and mean[2] <55:
        result ='BOMB'
    elif mean[0] >250 and mean[1] <85 and mean[1] < 110  and mean[2]>250 :
        result ='SWORD'
    elif mean[0] >100 and mean[0] <130 and mean[1] > 150 and mean[1]< 200 and mean[2]>90 and mean[2] <110:
        result ='POISON'
    elif mean[0] >210 and mean[0] <230 and mean[1] > 200 and mean[1]< 225 and mean[2]>120 and mean[2] <135:
        result ='JEWEL'
    
    return result

#duration 동안 마우스 커서를 x,y좌표로 이동
def click(coords):
    pag.moveTo(x=coords[0],y=coords[1],duration=0.0)
    pag.mouseDown()
    pag.mouseUp()

#x,y = pag.position() 실시간 마우스 좌표 받기
# while True:
#     x,y = pag.position()
#     position_str ='X:'+str(x)+'Y:'+str(y)
#     print(position_str)

#이러면 위치에 있는 아이콘 알아서 긁어옴
with mss.mss() as sct:
    left_img =np.array(sct.grab(left_icon_pos))[:,:,:3]
    right_img = np.array(sct.grab(right_icon_pos))[:,:,:3]

    cv2.imshow('left_img',left_img)
    cv2.imshow('right_img',right_img)
    cv2.waitKey(0)

left_icon = compute_icon_type(left_img)
right_icon = compute_icon_type(right_img)

if left_icon == 'SWORD' and (right_icon == 'BOMB' or right_icon =='POISON') :
    print('TAP LEFT!')
    click(left_button)
elif right_icon =='SWORD' and (left_icon == 'BOMB' or left_icon =='POISON'):
    print('TAP RIGHT!')
    click(right_button)
elif left_icon == 'JEWEL' and right_icon == 'JEWEL':
    print('FEVER!')
    click(left_button)
    click(right_button)
else:
    print('FAIL')
    