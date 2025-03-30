

---

# Buddy: Virtual Mouse, Keyboard, and Assistant

![Buddy Logo](link-to-your-logo-image)

### **Version:** 1.0.0  
**Author:** Rajpal Singh Rathore

## Project Overview

**Buddy** is an all-in-one virtual assistant that revolutionizes user interaction with computers. It combines gesture-based mouse and keyboard control with a smart virtual assistant to perform tasks through voice commands. Buddy is designed to enhance user productivity by automating routine tasks and providing AI-powered support.

## Features

### 1. **Virtual Mouse & Keyboard**
- **Gesture-Based Control:** Control mouse and keyboard with hand gestures using OpenCV and a hand detection algorithm.
- **No Physical Devices Required:** Perform common tasks like clicking, typing, and dragging with simple hand movements.

### 2. **Face Authentication**
Buddy includes a **Face Authentication** feature, adding an extra layer of security to the system. This feature uses facial recognition technology to authenticate the user before allowing access to certain functions of the assistant or system.

- **Easy Setup:** Configure face authentication with a simple registration process.
- **Seamless Experience:** Once set up, the system will automatically verify the user’s identity during activation.

### 3. **Buddy Virtual Assistant**
Buddy is a voice-controlled assistant that understands user queries and performs a variety of tasks, including:
- **Application Management:** Open and close local applications.
- **Web Automation:** Open web applications and perform searches on Google, YouTube, and specific e-commerce websites.
- **WhatsApp Automation:** Send messages, make calls, and video calls.
- **Spotify Integration:** Play music, search for artists, and control playback on Spotify.
- **AI-Based Features:**
  - **Buddy CodeMaster:** Automatically write Python code based on user queries.
  - **Buddy ImageMaster:** Generate AI-powered images based on prompts.
- **Navigation and Location Services:** Find the shortest distance between two locations.
- **Email Automation:** Compose and send emails via Gmail with voice commands.
- **Reminder and Note Management:** Set reminders and take notes.
- **Voice Typing:** Type using voice commands with automatic speech-to-text conversion.

### 4. **Hotword Detection**
Buddy activates with a custom hotword, listening in the background for commands. It’s designed to respond immediately once triggered.

### 5. **Multiprocessing Support**
To ensure efficient performance, Buddy uses multiprocessing, allowing the virtual assistant and hotword detection to work simultaneously without interruptions.

## Technologies Used

- **Programming Language:** Python
- **Libraries:**
  - **OpenCV:** For gesture detection and face authentication.
  - **SpeechRecognition:** For converting voice commands into text.
  - **Eel:** For building the web interface.
  - **Multiprocessing:** For handling multiple processes.
  - **SMTP Library:** For email automation.
  - **Spotify API:** For music integration.
  - **Google Maps API:** For navigation and route management.
- **Web Technologies:** HTML, CSS, JavaScript (for the web interface).

## Installation

### Prerequisites:
- Python 3.x
- OpenCV
- Eel
- SpeechRecognition
- PyAudio
- Spotify API key
- Gmail API setup

### Steps to Install:
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/buddy-virtual-assistant.git
   ```
2. Install the required Python libraries:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the project:
   ```bash
   python run.py
   ```

## How to Use

1. **Virtual Mouse & Keyboard:** Start the hand detection system and control your PC with gestures.
2. **Buddy Assistant:** Trigger Buddy with the hotword or by running the assistant script. Give voice commands to perform tasks like opening applications, sending messages, or generating AI-based images.
3. **Buddy CodeMaster & ImageMaster:** Ask Buddy to write Python code or generate images using a simple voice command like, “Write a Python code to sort an array” or “Generate an image of a sunset.”
4. **Face Authentication:** Ensure the face authentication is enabled for secure access. Buddy will prompt for facial recognition during activation.

## Upcoming Features

- **Enhanced Language Support:** Adding support for multiple languages.
- **AI Chat Integration:** Advanced conversation handling with GPT-based models.
- **Deeper App Integrations:** Expanding automation for additional applications like Zoom, Slack, and others.

## Contributing

If you'd like to contribute to Buddy, please submit a pull request with a detailed description of your changes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

