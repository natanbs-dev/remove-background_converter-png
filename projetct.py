from rembg import remove
from PIL import Image
import io
import os

input_path = os.path.join('images', 'webp-logo.webp')
output_path = os.path.join('result', 'test5-back.png')

print("escolha uma das opções: ")
print("1. converter a imagem para PNG")
print("2. remover o background")
opcao = input("digite: ")

try:

    with open(input_path, 'rb') as img_file:
        img_data = img_file.read()


    if opcao == '1':
        img = Image.open(io.BytesIO(img_data))
        img.save(output_path, 'PNG')
        print("imagem convertida")

    elif opcao == '2':
        result_data = remove(img_data)
        img_no_bg = Image.open(io.BytesIO(result_data))
        img_no_bg.save(output_path, 'PNG')
        print("Imagem com fundo removido e salva como PNG com sucesso.")

    else:
        print("Opção inválida. Escolha 1 ou 2.")

except Exception as e:

    print(f"Ocorreu um erro ao processar a imagem: {e}")