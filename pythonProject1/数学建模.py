import cv2
from keras.models import load_model

model = load_model('path/to/model.h5')  # Kerasģ�ͼ���ʾ��

# video = cv2.VideoCapture('path/to/video.mp4')  # ���ļ���ȡ��Ƶ
video = cv2.VideoCapture(0)  # ����ʵʱ��Ƶ

while True:
    ret, frame = video.read()  # ��ȡ��֡
    if not ret:
        break
    resized_frame = cv2.resize(frame, (200, 400))
    normalized_frame = frame / 255.0  # ������ֵ��һ���� [0, 1]
    BGR_frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
    batched_frame = np.expand_dims(frame, axis=0)
    # ��֡����Ԥ�����������š���һ����
    processed_frame = preprocess_frame(frame)

    # ʹ��ģ�ͽ�������ʶ��
    predictions = model.predict(processed_frame)

    # ����Ԥ����������Ʊ߽���
    draw_predictions(frame, predictions)

    # ��ʾ������֡
    cv2.imshow('Video', frame)

    # ���� 'q' ���˳�ѭ��
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()