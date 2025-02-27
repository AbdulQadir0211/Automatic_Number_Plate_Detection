import easyocr

# Initialize EasyOCR
reader = easyocr.Reader(['en'])

def extract_text_from_plate(plate_crop):
    """Extract text from the cropped plate image using EasyOCR."""
    plate_text = reader.readtext(plate_crop, detail=0)
    return " ".join(plate_text) if plate_text else "Not Detected"
