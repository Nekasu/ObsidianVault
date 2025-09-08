'''
以图像 rgb 通道为横坐标, 生成直方图
'''
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import io

def generate_rgb_histogram_image(img: Image.Image) -> Image.Image:
    """生成RGB直方图图像并转换为PIL.Image"""
    r, g, b = img.split()

    plt.figure(figsize=(5, 4))
    plt.hist(r.getdata(), bins=256, range=(0, 255), color='red', alpha=0.5, label='Red')
    plt.hist(g.getdata(), bins=256, range=(0, 255), color='green', alpha=0.5, label='Green')
    plt.hist(b.getdata(), bins=256, range=(0, 255), color='blue', alpha=0.5, label='Blue')
    plt.xlabel("Pixel Value")
    plt.ylabel("Frequency")
    plt.title("RGB Histogram")
    plt.legend()
    plt.tight_layout()

    # 将 Matplotlib 图像保存到内存
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    plt.close()
    buf.seek(0)

    hist_img = Image.open(buf).convert("RGB")
    return hist_img

def concatenate_image_with_histogram(image_path, output_path):
    # 加载原图像并转为RGB
    original_img = Image.open(image_path).convert("RGB")
    hist_img = generate_rgb_histogram_image(original_img)

    # 调整 histogram 图像尺寸为与原图高度一致
    h1 = original_img.height
    h2 = hist_img.height
    scale = h1 / h2
    new_width = int(hist_img.width * scale)
    hist_img = hist_img.resize((new_width, h1))

    # 拼接图像（水平）
    combined = Image.new("RGB", (original_img.width + hist_img.width, h1))
    combined.paste(original_img, (0, 0))
    combined.paste(hist_img, (original_img.width, 0))

    # 保存结果
    combined.save(output_path)
    print(f"拼接图像已保存为: {output_path}")

# 示例用法
concatenate_image_with_histogram(r'C:\Users\Nekasu\Pictures\double_seele_05.jpg', 'combined_output.jpg')