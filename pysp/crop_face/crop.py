import cv2
import os
from datetime import datetime

# Download from https://github.com/opencv/opencv_zoo/blob/main/models/face_detection_yunet/face_detection_yunet_2023mar.onnx

def crop_with_yunet_padded(image_path, model_path="face_detection_yunet_2023mar.onnx"):
    img = cv2.imread(image_path)
    if img is None: return

    height, width, _ = img.shape

    detector = cv2.FaceDetectorYN.create(
        model=model_path,
        config="",
        input_size=(width, height),
        score_threshold=0.6
    )

    _, faces = detector.detect(img)
    if faces is None:
        print("No face detected.")
        return

    top_left_face = min(faces, key=lambda f: f[0] + f[1])
    x, y, w, h = map(int, top_left_face[:4])

    padding_rate = 0.6
    
    crop_x_end = int(x + w + (w * padding_rate))
    crop_y_end = int(y + h + (h * padding_rate))

    crop_x_end = min(width, crop_x_end)
    crop_y_end = min(height, crop_y_end)
    
    final_crop = img[0:crop_y_end, 0:crop_x_end]

    timestamp = datetime.now().strftime("%Y-%m-%d %H%M%S")
    original_copy_name = f"t{timestamp}.png"
    cropped_name = f"t{timestamp}s.png"

    if os.path.exists(original_copy_name):
        print(f"文件 {original_copy_name} 已存在，为了避免覆盖，本次操作已跳过。")
    else:
        cv2.imwrite(original_copy_name, img)

    if os.path.exists(cropped_name):
        print(f"文件 {cropped_name} 已存在，为了避免覆盖，本次操作已跳过。")
    else:
        cv2.imwrite(cropped_name, final_crop)
        
    print(f"Processing successful!")
    print(f"Original copy: {original_copy_name}")
    print(f"Cropped image: {cropped_name}")

if __name__ == "__main__":
    tmpPath = "a.png"
    if os.path.exists(tmpPath)
        crop_with_yunet_padded(tmpPath)
    tmpPath = "a.jpg"
    if os.path.exists(tmpPath)
        crop_with_yunet_padded(tmpPath)
