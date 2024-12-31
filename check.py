from singleton_ocr import OCRSingleton

# # Lấy đối tượng OCR đã khởi tạo
ocr = OCRSingleton.get_instance()
import easyocr
reader = easyocr.Reader(['en'])
print("EasyOCR loaded successfully!")