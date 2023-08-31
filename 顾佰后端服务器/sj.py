import mss
import numpy as np
import requests
import base64

def capture_screen():
    with mss.mss() as sct:
        # ��ȡ����Ļ�ĳߴ�
        monitor = sct.monitors[1]
        monitor["top"] = 0
        monitor["left"] = 0
        monitor["width"] = 1080
        monitor["height"] = 1920

        # ��ȡ��Ļͼ��
        sct_img = sct.grab(monitor)

        # ����ͼת��Ϊnumpy����
        img = np.array(sct_img)

        return img

def send_screenshot(image):
    # ��ͼ�����ΪBase64�ַ���
    image_base64 = base64.b64encode(image).decode("utf-8")

    # ���������URL
    url = "http:///Users/tu"

    # ��������Ĳ���
    payload = {
        "image": image_base64
    }

    # ����POST����
    response = requests.post(url, json=payload)

    # �����Ӧ���
    print(response.text)

# ���ú���������Ļ��ͼ
screen_img = capture_screen()

# ���ͽ�ͼ��ָ���ӿ�
send_screenshot(screen_img)