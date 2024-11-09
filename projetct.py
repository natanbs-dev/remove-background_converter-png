from rembg import remove
from PIL import Image
import io
import os

input_path = os.path.join('images', 'black-cat.jpg')
output_path = os.path.join('result', 'test2-back.png')

try:

    with open(input_path, 'rb') as img_file:
        img_data = img_file.read()

    result_data = remove(img_data)

    img_no_bg = Image.open(io.BytesIO(result_data))
    img_no_bg.save(output_path, 'PNG')

    print("Imagem processada e salva como png")

except Exception as e:

    print(f"Ocorreu um erro ao processar a imagem: {e}")