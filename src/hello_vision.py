import numpy as np
import cv2
import os
import matplotlib.pyplot as plt

def main():
    # Crear una imagen negra de 200x200 con 3 canales (RGB)
    image = np.zeros((200, 200, 3), dtype=np.uint8)

    # Dibujar un círculo rojo en el centro
    center = (100, 100)
    radius = 50
    color = (0, 0, 255)  # OpenCV usa BGR, así que esto es rojo
    thickness = -1       # Relleno completo
    cv2.circle(image, center, radius, color, thickness)

    # Crear carpeta de salida
    output_dir = "output"
    os.makedirs(output_dir, exist_ok=True)

    # Guardar la imagen original (BGR) como archivo
    output_path = os.path.join(output_dir, "hello_circle.png")
    cv2.imwrite(output_path, image)
    print(f"Imagen guardada en: {output_path}")

    # Convertir la imagen de BGR a RGB para mostrar con matplotlib
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Mostrar y guardar la imagen como gráfico matplotlib
    plt.imshow(image_rgb)
    plt.axis('off')
    plt.title("Hola Visión Artificial")

    output_plot_path = os.path.join(output_dir, "hello_circle_plot.png")
    plt.savefig(output_plot_path)
    print(f"Gráfico guardado en: {output_plot_path}")

if __name__ == "__main__":
    main()
