<div align="center">

# 🤖 Buddy - AI Virtual Assistant

### *Your Intelligent Desktop Companion with Gesture Control & Voice Commands*

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![OpenCV](https://img.shields.io/badge/OpenCV-4.11-green.svg)](https://opencv.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/Platform-Windows-lightgrey.svg)](https://www.microsoft.com/windows)
[![Stars](https://img.shields.io/github/stars/Rathore-Rajpal/HeyBuddy?style=social)](https://github.com/Rathore-Rajpal/HeyBuddy)

**[Features](#-features)** • **[Quick Start](#-quick-start)** • **[Demo](#-demo)** • **[Documentation](#-documentation)** • **[Contributing](#-contributing)**

---

</div>

## 📖 About

**Buddy** is an all-in-one AI virtual assistant that revolutionizes how you interact with your computer. Control your mouse and keyboard with hand gestures, execute commands with your voice, and automate tasks with AI-powered features.

**Author:** Rajpal Singh Rathore

## Features

### 🎯 Core Components
1. **Virtual Mouse** - Hand gesture-based mouse control
2. **Virtual Keyboard** - On-screen keyboard with gesture typing
3. **Voice Assistant "Buddy"** - AI-powered voice commands

### 🤖 Assistant Capabilities
- ✅ Face authentication
- ✅ Voice command recognition
- ✅ Spotify integration (play music, search artists)
- ✅ YouTube control (play videos, search)
- ✅ WhatsApp automation (messages, calls)
- ✅ Phone integration (calls, SMS via Phone Link)
- ✅ Email composition (Gmail)
- ✅ Web search (Google, product search on 20+ sites)
- ✅ Note taking (Sticky Notes, file-based)
- ✅ Reminders (Windows Task Scheduler)
- ✅ Screenshots
- ✅ AI chatbot (HuggingChat)
- ✅ Code generation
- ✅ Image generation (Stable Diffusion)
- ✅ Google Maps routes

### 🖱️ Virtual Mouse Gestures
| Gesture | Action |
|---------|--------|
| Index finger movement | Move cursor |
| Index finger bent + middle straight | Left click |
| Middle finger bent + index straight | Right click |
| Both fingers bent (thumb far) | Double click |
| Both fingers bent (thumb close) | Screenshot |
| Thumb + index touching + move up/down | Scroll |
| Thumb + pinky touching | Drawing mode |
| Thumb + ring finger (1 sec) | Close window |
| Thumb + middle finger (1 sec) | Minimize window |

## 🚀 Quick Start

### Prerequisites
- Windows 10/11
- Python 3.8 or higher
- Webcam
- Microphone
- Internet connection

### Installation

1. **Clone or download this repository**
   ```
   cd C:\VirtualMouseProject
   ```

2. **Run setup script**
   ```
   setup.bat
   ```
   This will:
   - Create virtual environment
   - Install all dependencies
   - Verify installation

3. **Configure API keys (Optional)**
   Create a `.env` file in the project root:
   ```
   CLIENT_ID=your_spotify_client_id
   CLIENT_SECRET=your_spotify_client_secret
   HuggingFaceApiKey=your_huggingface_api_key
   ```

4. **Test components**
   ```
   python test_components.py
   ```

5. **Launch the assistant**
   ```
   start.bat
   ```
   Or directly:
   ```
   python run.py
   ```

## 📖 Usage

### Starting the Assistant
1. Run `start.bat`
2. Complete face authentication when prompted
3. Wait for "Ready to help" confirmation
4. Use voice commands or click the mic button
5. Press `Alt + J` for quick voice activation

### Voice Command Examples
- "Open YouTube"
- "Play Despacito on YouTube"
- "Search for laptop on Amazon"
- "Send a message to [contact name] on WhatsApp"
- "Set a reminder for tomorrow at 3 PM to call mom"
- "Take a screenshot"
- "Generate an image of a sunset over mountains"
- "Write a code to sort a list in Python"
- "What's the weather like?"

### Launching Virtual Mouse/Keyboard
- Voice: "Start virtual mouse" / "Start virtual keyboard"
- Or use Flask API endpoints (if running app.py)

## 🛠️ Troubleshooting

### Camera not working
- Check if camera is being used by another application
- Grant camera permissions to Python

### Voice recognition not responding
- Check microphone permissions
- Ensure internet connection (uses Google Speech API)
- Adjust `r.pause_threshold` in commands.py if needed

### Face authentication fails
- Ensure good lighting
- Train your face using `assist/Engine/auth/sample.py`
- Run `assist/Engine/auth/trainer.py` to generate trainer.yml

### Module not found errors
- Activate virtual environment: `envjarvis\Scripts\activate`
- Reinstall: `pip install -r requirements.txt`

### Spotify not working
- Get API credentials from https://developer.spotify.com
- Add to .env file

## 📁 Project Structure
```
VirtualMouseProject/
├── run.py              # Main launcher (multiprocessing)
├── main.py             # Assistant initialization
├── app.py              # Flask API server
├── virtualMouse.py     # Gesture-based mouse
├── virtual_ketboard.py # Gesture-based keyboard
├── requirements.txt    # Dependencies
├── setup.bat           # Installation script
├── start.bat           # Launch script
├── test_components.py  # Component testing
├── assist/
│   ├── Engine/
│   │   ├── commands.py      # Command handler
│   │   ├── features.py      # Feature implementations
│   │   ├── config.py        # Configuration
│   │   ├── db.py            # Database operations
│   │   ├── spotify.py       # Spotify integration
│   │   ├── auth/            # Face authentication
│   │   ├── ImageBot/        # Image generation UI
│   │   └── CodingBuddy/     # Code assistant UI
│   └── www/                 # Web interface
│       ├── index.html
│       ├── main.js
│       └── style.css
└── envjarvis/          # Virtual environment
```

## 🎥 Demo

> **Coming Soon:** Full demo video showcasing all features

### Screenshots

<div align="center">

#### 🎭 Face Authentication
*Secure login with facial recognition*

#### 🖱️ Virtual Mouse Control
*Control cursor with hand gestures*

#### 🗣️ Voice Assistant Interface
*Beautiful web-based UI with voice commands*

#### 🎨 AI Image Generation
*Create images from text prompts*

</div>

### Quick Feature Preview

```
🎵 "Play [song name] on Spotify"
📧 "Send email to [contact]"
🌐 "Search Google for [query]"
🎨 "Generate image of [description]"
💻 "Write code to [task]"
```

---

## 🔧 Development

### Adding New Voice Commands
Edit [assist/Engine/commands.py](assist/Engine/commands.py) and add to `allCommands()` function

### Adding New Contacts
Use the web UI contact form or edit database directly

### Training Face Recognition
Run the easy setup script:
```bash
.\setup_face_auth.bat
```

Or manually:
1. Run `python assist/Engine/auth/sample.py` to capture face samples
2. Run `python assist/Engine/auth/trainer.py` to train the model

---

## 🤝 Contributing

Contributions are welcome! Here's how:

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Development Setup
See [DEPLOYMENT.md](DEPLOYMENT.md) for complete deployment guide.

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- OpenCV for computer vision capabilities
- MediaPipe for hand tracking
- Eel for Python-JavaScript bridge
- HuggingFace for AI models
- All open-source contributors

---

## 📧 Contact

**Rajpal Singh Rathore**
- GitHub: [@Rathore-Rajpal](https://github.com/Rathore-Rajpal)
- Project Link: [https://heybuddy.rathorerajpal.live](https://heybuddy.rathorerajpal.live)

---

<div align="center">

### ⭐ Star this repo if you find it useful!

**Made with ❤️ by Rajpal Singh Rathore**

</div>

## 📝 License
This project is open source and available for educational purposes.

## 🤝 Contributing
Contributions, issues, and feature requests are welcome!

## ⚠️ Important Notes
- Some features require API keys (Spotify, HuggingFace)
- WhatsApp automation may require WhatsApp Desktop app
- Phone features require Windows Phone Link app
- Face authentication model needs to be trained with your face

## 📞 Support
For issues or questions, please create an issue in the repository.


