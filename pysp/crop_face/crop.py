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

    timestamp = datetime.now().strftime("%Y-%m-%d-%H-%M-%S-%f")[:-3]
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

# if __name__ == "__main__":
#     tmpPath = "a.png"
#     if os.path.exists(tmpPath):
#         crop_with_yunet_padded(tmpPath)
#     tmpPath = "a.jpg"
#     if os.path.exists(tmpPath):
#         crop_with_yunet_padded(tmpPath)


import os
import glob



if __name__ == "__main__":
    # 1. 定义想要匹配的图片后缀名
    extensions = ('*.jpg', '*.jpeg', '*.png', '*.bmp', '*.webp')
    
    # 2. 获取当前目录下所有的图片路径并存入 list
    image_list = []
    for ext in extensions:
        # glob.glob 会自动处理路径匹配
        image_list.extend(glob.glob(ext))

    image_list.sort(key=str.lower)
    
    # 打印一下找到的文件，方便调试
    print(f"共找到 {len(image_list)} 张图片: {image_list}")

    # 3. 遍历 list 并执行操作
    for img_path in image_list:
        try:
            crop_with_yunet_padded(img_path)
        except Exception as e:
            print(f"处理 {img_path} 时出错: {e}")