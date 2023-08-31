#
# from selenium import webdriver
# import time
#
# driver = webdriver.Chrome()
# import csv
#
# driver.get("https://www.douyu.com/directory/all")
# i = 1
# while True:
#     driver.execute_script(
#         "window.scrollTo(0, document.body.scrollHeight); var lenOfPage=document.body.scrollHeight; return lenOfPage;")
#     time.sleep(3)
#     r_list = driver.find_elements_by_xpath('//li[@class="layout-Cover-item"]')
#
#     for r in r_list:
#         m = r.text.split('\n')
#
#         if m == ['']:
#             pass
#         else:
#             name = m[0]
#             type = m[1]
#         # L=[name,type]
#         # print(m)
#             with open("斗鱼.csv", "a", newline="", encoding="gb18030") as f:
#                 writer = csv.writer(f)
#                 L = [name.strip(), type.strip()]
#                 writer.writerow(L)
#     print("第%d页数据获取成功" % i)
#     i += 1
#     if driver.page_source.find('dy-Pagination-item') != -1:
#         name = driver.find_element_by_class_name("dy-Pagination-item-custom")
#         name.click()
#     else:
#         print("数据获取结束!!!")
#
import tkinter as tk
import pyautogui
import cv2
from PIL import Image, ImageTk

# 创建主窗口对象
root = tk.Tk()

# 设置窗口标题和大小
root.title("透视")
root.geometry("960x540")

# 创建标签
label = tk.Label(root)
label.pack()

# 获取屏幕大小
screen_width, screen_height = pyautogui.size()
intq=0
# 循环更新截图
while True:
    # 获取屏幕截图
    screenshot = pyautogui.screenshot()
    # 转换为PIL图像对象
    image = Image.frombytes('RGB', screenshot.size, screenshot.tobytes())

    # intq +=1
    # screenshot.save('img\screenshot'+str(intq)+'.jpg')
    # 缩放图片
    image = image.resize((int(screen_width / 2), int(screen_height / 2)))

    # 转换为Tkinter的PhotoImage对象
    photo = ImageTk.PhotoImage(image)

    # 更新标签的图片
    label.config(image=photo)
    label.image = photo

    # 更新窗口
    root.update()

