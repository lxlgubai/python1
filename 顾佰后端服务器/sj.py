import mss
import numpy as np
import requests
import base64

def capture_screen():
    with mss.mss() as sct:
        # 获取主屏幕的尺寸
        monitor = sct.monitors[1]
        monitor["top"] = 0
        monitor["left"] = 0
        monitor["width"] = 1080
        monitor["height"] = 1920

        # 截取屏幕图像
        sct_img = sct.grab(monitor)

        # 将截图转换为numpy数组
        img = np.array(sct_img)

        return img

def send_screenshot(image):
    # 将图像编码为Base64字符串
    image_base64 = base64.b64encode(image).decode("utf-8")

    # 构建请求的URL
    url = "http:///Users/tu"

    # 构建请求的参数
    payload = {
        "image": image_base64
    }

    # 发送POST请求
    response = requests.post(url, json=payload)

    # 输出响应结果
    print(response.text)

# 调用函数捕获屏幕截图
screen_img = capture_screen()

# 发送截图到指定接口
send_screenshot(screen_img)