from langchain_community.document_loaders import PyPDFLoader
from pdf2image import convert_from_path
import pytesseract
from PIL import Image
import os
import shutil

def extract_pdf_data(pdf_path, ocr_page_limit=20):
    print(" Extracting text from PDF...")
    loader = PyPDFLoader(pdf_path)
    pages = loader.load()
    text_content = " ".join([p.page_content for p in pages])

    # --- Check if Tesseract is installed ---
    tesseract_path = shutil.which("tesseract")
    if tesseract_path is None:
        print("  Tesseract not found. Skipping OCR on images.")
        return text_content

    print(f"  Tesseract found. Performing OCR on first {ocr_page_limit} pages only...")
    try:
        # Convert only the first few pages to save time
        images = convert_from_path(pdf_path, first_page=1, last_page=ocr_page_limit)
    except Exception as e:
        print(f"  Poppler or conversion issue: {e}")
        print(" Proceeding with text-only extraction.")
        return text_content

    ocr_text = ""
    temp_folder = "data/temp_images"
    os.makedirs(temp_folder, exist_ok=True)

    for i, img in enumerate(images):
        img_path = os.path.join(temp_folder, f"page_{i+1}.png")
        img.save(img_path, 'PNG')
        try:
            text_from_img = pytesseract.image_to_string(Image.open(img_path))
            ocr_text += f"\n--- OCR from Page {i+1} ---\n{text_from_img}\n"
        except Exception as e:
            print(f"  OCR failed for page {i+1}: {e}")

    combined_text = text_content + "\n" + ocr_text
    print(f" Text + Image OCR extraction complete for {ocr_page_limit} pages.")
    return combined_text
