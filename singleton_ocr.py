# singleton_ocr.py
from paddleocr import PaddleOCR

class OCRSingleton:
    _instance = None

    @staticmethod
    def get_instance():
        if OCRSingleton._instance is None:
            OCRSingleton._instance = PaddleOCR(use_angle_cls=False, lang='en')
        return OCRSingleton._instance
