import numpy as np
import cv2
import os

def main():
    # Crear una imagen negra de 200x200 con 3 canales (RGB)
    image = np.zeros((200, 200, 3), dtype=np.uint8)

    # Dibujar un círculo rojo en el centro
    center = (100, 100)
    radius = 50
    color = (0, 0, 255)  # OpenCV usa BGR, así que esto es rojo
    thickness = -1       # Relleno completo
    cv2.circle(image, center, radius, color, thickness)

    # Mostrar la imagen en una ventana
    cv2.imshow("Hola Visión Artificial", image)
    print("Pulsa cualquier tecla para cerrar la imagen...")
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Guardar la imagen generada en disco
    output_dir = os.path.join("dataspace", "outputs")
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "hello_circle.png")
    cv2.imwrite(output_path, image)
    print(f"Imagen guardada en: {output_path}")

if __name__ == "__main__":
    main()
