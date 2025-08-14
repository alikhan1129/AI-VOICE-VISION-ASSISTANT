import cv2
import pytesseract
from ultralytics import YOLO
from transformers import BlipProcessor, BlipForConditionalGeneration
import torch
from core.shared import engine
from core.chat import query

pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

yolo_model = YOLO("yolov8n.pt")
blip_processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
blip_model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")
import pyautogui  

def capture_screen():
    """Captures the screen (not webcam) and saves the screenshot."""
    screenshot = pyautogui.screenshot()
    filename = "screenshot.png"
    screenshot.save(filename)
    print("Screenshot saved as", filename)
    engine.say("Screenshot captured and saved.")
    engine.runAndWait()

def screenshot_and_explain():
    """Takes a screenshot of the screen, extracts text, and explains it."""
    capture_screen()
    image = cv2.imread("screenshot.png")
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    text = pytesseract.image_to_string(gray)
    if text.strip():
        print("Detected Text:", text)
        output = query(text)
        engine.say(f"The screen contains text: {output}")
    else:
        engine.say("No readable text detected in the screenshot.")
    engine.runAndWait()

def start_camera_processing(process_frame):
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        process_frame(frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

def read_text():
    def process_frame(frame):
        cv2.putText(frame, "Press 'c' to Capture Text", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
        cv2.imshow("Text Detection - Press 'c' to Capture", frame)
        key = cv2.waitKey(1) & 0xFF
        if key == ord('c'):
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
            blur = cv2.GaussianBlur(thresh, (3, 3), 0)
            text = pytesseract.image_to_string(blur, config=r'--oem 3 --psm 6')
            print("Detected Text:", text)
            engine.say(text if text.strip() else "No text detected.")
            engine.runAndWait()
    start_camera_processing(process_frame)

def identify_objects():
    def process_frame(frame):
        results = yolo_model.predict(frame)
        for result in results:
            frame = result.plot()
        cv2.imshow("Object Detection", frame)
    start_camera_processing(process_frame)

def describe_scene():
    def process_frame(frame):
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        inputs = blip_processor(images=image, return_tensors="pt")
        with torch.no_grad():
            outputs = blip_model.generate(**inputs)
        description = blip_processor.decode(outputs[0], skip_special_tokens=True)
        print("Scene Description:", description)
        engine.say(description)
        cv2.imshow("Scene Description", frame)
    start_camera_processing(process_frame)
