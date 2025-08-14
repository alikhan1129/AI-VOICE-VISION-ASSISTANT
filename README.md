# AI Voice & Vision Assistant

An advanced **voice-controlled AI assistant** with **Gemini-powered conversational abilities**, **secure commands**, **short-term memory**, and **computer vision capabilities** such as OCR, object detection (YOLOv8), and scene description (BLIP).

---

## 📌 Table of Contents
1. [Overview](#overview)
2. [Features](#features)
3. [Architecture](#architecture)
4. [Project Structure](#project-structure)
5. [Installation](#installation)
6. [Configuration](#configuration)
7. [Usage](#usage)
8. [Example Commands](#example-commands)
9. [Security](#security)
10. [Computer Vision Models](#computer-vision-models)
11. [Troubleshooting](#troubleshooting)
12. [License](#license)

---

## 📖 Overview

This assistant can:
- Listen for a **wake word** ("yo").
- Understand and execute **voice commands**.
- Answer questions using **Google's Gemini AI API**.
- Perform **computer vision** tasks like reading text from images, detecting objects, and describing scenes.
- Remember and recall **facts** during the session.
- Open applications, search the web, find files, and read schedules.
- Secure sensitive commands with **password authentication**.

---

## 🚀 Features

- **Wake Word Detection** – "yo" triggers listening mode.
- **Conversational AI** – Gemini API for natural responses.
- **Voice Command Execution** – Runs utilities and vision tasks.
- **Secure Commands** – Protects sensitive actions with passwords.
- **Memory System** – Stores and recalls short-term facts.
- **Computer Vision** – OCR, YOLOv8 object detection, BLIP scene description.
- **Utilities** – Open apps, search the web, search local files, tell date/schedule.
- **Fallback Chatbot** – Default to Gemini for unmatched commands.
- **Graceful Exit** – "good bye", "exit", or `Ctrl+C`.

---

## 🏗 Architecture

```
main.py
│
├── Wait for wake word → wakeword.py
│
├── Listen to voice → voice.py
│     ├── Secure commands → security.py
│     ├── Utility commands → utils.py
│     ├── Vision commands → vision.py
│     ├── Chat fallback → chat.py
│
├── Speak output → shared.py
```

---

## 📂 Project Structure

```
project/
│── core/
│   ├── chat.py          # Gemini API integration
│   ├── security.py      # Password-protected commands
│   ├── shared.py        # Shared TTS engine & memory
│   ├── utils.py         # Utility functions
│   ├── vision.py        # OCR, object detection, scene description
│   ├── voice.py         # Speech recognition & command handling
│   ├── wakeword.py      # Wake word detection
│── main.py              # Entry point
│── .env                 # Environment variables
│── requirements.txt     # Dependencies
│── yolov8n.pt           # YOLOv8 object detection model
│── screenshot.png       # Sample image for OCR
```

---

## 💻 Installation

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/ai-voice-assistant.git
cd ai-voice-assistant
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Set up environment variables**
Create `.env` file:
```env
GEMINI_API_KEY=your_gemini_api_key_here
```

4. **Download YOLOv8 model**  
Ensure `yolov8n.pt` is in the root directory.

5. **Install Tesseract OCR**
- Download: https://github.com/tesseract-ocr/tesseract
- Update path in `vision.py` if needed.

---

## ⚙ Configuration

- **Wake Word** – Change in `wakeword.py`:
```python
WAKE_WORD = "yo"
```
- **Password** – Change in `security.py`:
```python
PASSWORD = "1234"
```

---

## ▶️ Usage

Run the assistant:
```bash
python main.py
```

---

## 🎙 Example Commands

| Command | Action |
|---------|--------|
| "Hello" | Greets the user |
| "Open notepad" | Opens Notepad |
| "Search in browser artificial intelligence" | Google search |
| "Search file report" | Search local files |
| "Tell me the date" | Speaks today's date |
| "Tell me my schedule" | Reads `schedule.txt` |
| "Remember I have a meeting at 4 PM" | Stores memory |
| "Recall my memories" | Reads back memories |
| "Capture screen" | Saves a screenshot |
| "Screenshot and explain" | OCR + Gemini explanation |
| "Read text" | Reads text live from camera |
| "Identify objects" | YOLOv8 object detection |
| "Describe scene" | BLIP scene captioning |
| "Goodbye" / "Exit" | Exit program |

---

## 🔐 Security

- Certain commands ("open", "delete", "shut down") require a password.
- Default password: `1234`.

---

## 🖼 Computer Vision Models

- **YOLOv8** (`yolov8n.pt`) – Object detection.
- **BLIP** – Scene description.
- **Tesseract OCR** – Text recognition.

---

## 🛠 Troubleshooting

- **Speech not detected** → Check microphone & `speechrecognition` installation.
- **Gemini API errors** → Verify `GEMINI_API_KEY` in `.env`.
- **OCR not working** → Ensure Tesseract is installed & path is set.
- **Object detection slow** → Use smaller YOLO model (`yolov8n.pt`).

---

## 📜 License
This project is open-source. Modify and use freely.
