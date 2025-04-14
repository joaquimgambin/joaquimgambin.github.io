import PyPDF2
import os

# Ruta al archivo PDF
pdf_path = '/home/ubuntu/upload/CV - Perfil JGC - 2024.pdf'
output_dir = '/home/ubuntu/cv_web'

# Crear archivo para guardar el texto extraído
extracted_text_path = os.path.join(output_dir, 'cv_content.txt')

# Abrir el archivo PDF
with open(pdf_path, 'rb') as file:
    # Crear un objeto lector de PDF
    pdf_reader = PyPDF2.PdfReader(file)
    
    # Obtener el número de páginas
    num_pages = len(pdf_reader.pages)
    print(f"El CV tiene {num_pages} páginas.")
    
    # Extraer texto de todas las páginas
    full_text = ""
    
    for page_num in range(num_pages):
        # Obtener página
        page = pdf_reader.pages[page_num]
        
        # Extraer texto de la página
        page_text = page.extract_text()
        
        # Añadir al texto completo
        full_text += f"\n\n--- PÁGINA {page_num + 1} ---\n\n"
        full_text += page_text
    
    # Guardar el texto extraído en un archivo
    with open(extracted_text_path, 'w', encoding='utf-8') as text_file:
        text_file.write(full_text)
    
    print(f"Contenido del CV extraído y guardado en: {extracted_text_path}")

# Extraer información de metadatos si está disponible
metadata_path = os.path.join(output_dir, 'cv_metadata.txt')
with open(pdf_path, 'rb') as file:
    pdf_reader = PyPDF2.PdfReader(file)
    metadata = pdf_reader.metadata
    
    with open(metadata_path, 'w', encoding='utf-8') as meta_file:
        if metadata:
            meta_file.write("METADATOS DEL CV:\n\n")
            for key, value in metadata.items():
                meta_file.write(f"{key}: {value}\n")
        else:
            meta_file.write("No se encontraron metadatos en el documento.")
    
    print(f"Metadatos guardados en: {metadata_path}")
