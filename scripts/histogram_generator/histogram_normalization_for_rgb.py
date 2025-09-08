from PIL import Image
import numpy as np
import cv2  # 使用 OpenCV 实现均衡化

def equalize_histogram_rgb_preserve_color(image_path, output_path):
    img = cv2.imread(image_path)  # BGR 读入
    ycrcb = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)
    
    y, cr, cb = cv2.split(ycrcb)
    y_eq = cv2.equalizeHist(y)  # 对亮度通道均衡化
    ycrcb_eq = cv2.merge((y_eq, cr, cb))
    
    img_eq = cv2.cvtColor(ycrcb_eq, cv2.COLOR_YCrCb2BGR)
    cv2.imwrite(output_path, img_eq)
    print(f"亮度均衡后保留色彩的图像已保存：{output_path}")

# 示例用法
equalize_histogram_rgb_preserve_color(r'C:\Users\Nekasu\Pictures\double_seele_05.jpg', 'color_preserved_equalized.jpg')