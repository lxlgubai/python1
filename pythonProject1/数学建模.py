import cv2
from keras.models import load_model

model = load_model('path/to/model.h5')  # Keras模型加载示例

# video = cv2.VideoCapture('path/to/video.mp4')  # 从文件读取视频
video = cv2.VideoCapture(0)  # 捕获实时视频

while True:
    ret, frame = video.read()  # 读取单帧
    if not ret:
        break
    resized_frame = cv2.resize(frame, (200, 400))
    normalized_frame = frame / 255.0  # 将像素值归一化到 [0, 1]
    BGR_frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
    batched_frame = np.expand_dims(frame, axis=0)
    # 对帧进行预处理，例如缩放、归一化等
    processed_frame = preprocess_frame(frame)

    # 使用模型进行人物识别
    predictions = model.predict(processed_frame)

    # 处理预测结果，如绘制边界框等
    draw_predictions(frame, predictions)

    # 显示处理后的帧
    cv2.imshow('Video', frame)

    # 按下 'q' 键退出循环
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()