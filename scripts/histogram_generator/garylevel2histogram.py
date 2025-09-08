from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import io

def generate_grayscale_histogram_image(img: Image.Image) -> Image.Image:
    gray = img.convert("L")
    pixels = np.array(gray).flatten()

    plt.figure(figsize=(5, 4))
    plt.hist(pixels, bins=256, range=(0, 255), color='gray', alpha=0.7)
    plt.xlabel("Gray Value")
    plt.ylabel("Frequency")
    plt.title("Grayscale Histogram")
    plt.tight_layout()

    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    plt.close()
    buf.seek(0)
    hist_img = Image.open(buf).convert("RGB")
    return hist_img

def concatenate_grayscale_with_histogram(image_path, output_path):
    img = Image.open(image_path).convert("L")
    hist_img = generate_grayscale_histogram_image(img)

    # Resize histogram to match image height
    new_width = int(hist_img.width * (img.height / hist_img.height))
    hist_img = hist_img.resize((new_width, img.height))
    img_rgb = img.convert("RGB")

    combined = Image.new("RGB", (img.width + hist_img.width, img.height))
    combined.paste(img_rgb, (0, 0))
    combined.paste(hist_img, (img.width, 0))
    combined.save(output_path)
    print(f"灰度图拼接完成: {output_path}")

# 示例用法
concatenate_grayscale_with_histogram(r'C:\Users\Nekasu\Pictures\double_seele_05.jpg', 'grayscale_with_hist.jpg')
# 示例用法