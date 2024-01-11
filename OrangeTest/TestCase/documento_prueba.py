from reportlab.pdfgen import canvas
from PIL import Image

def create_pdf_with_images(file_path, image_folder):
    # Crear un objeto PDF
    pdf = canvas.Canvas(file_path)

    # Agregar contenido de texto al PDF
    pdf.drawString(100, 800, "¡Hola, este es mi primer PDF!")

    # Obtener la lista de archivos en la carpeta de imágenes
    image_files = ["captura_20231124154948.png", "captura_20231128174830.png"]  # Lista de nombres de archivos, ajusta según tus archivos reales

    # Coordenadas iniciales para las imágenes
    x, y = 100, 700

    # Agregar imágenes al PDF
    for image_file in image_files:
        # Ruta completa de la imagen
        image_path = f"{image_folder}\\{image_file}"

        # Abrir la imagen con Pillow
        img = Image.open(image_path)

        # Obtener las dimensiones originales de la imagen
        width, height = img.size

        # Agregar la imagen al PDF sin escalar
        pdf.drawInlineImage(img, x, y, width=width, height=height)

        # Ajustar las coordenadas para la siguiente imagen
        y -= height + 20  # Espaciado entre las imágenes

    # Guardar el PDF
    pdf.save()

# Especifica la ruta completa del archivo PDF que deseas crear
pdf_file_path = r"C:\Users\ttoledoa\Desktop\PROYECTOS\mi_primer_pdf_con_imagenes.pdf"

# Especifica la carpeta de imágenes
image_folder_path = r"C:\Users\ttoledoa\Desktop\PROYECTOS\ATO\OrangeTest\screenshots"

# Llama a la función para crear el PDF con imágenes
create_pdf_with_images(pdf_file_path, image_folder_path)

print(f"Se ha creado el PDF con imágenes en: {pdf_file_path}")
