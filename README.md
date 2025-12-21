# Virtual Assistant "Buddy" - Complete AI System

A comprehensive AI assistant combining gesture-based controls and voice commands.

## Author
Rajpal Singh

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

## 🔧 Development

### Adding new voice commands
Edit `assist/Engine/commands.py` and add to `allCommands()` function

### Adding new contacts
Use the web UI contact form or edit database directly

### Training face recognition
1. Run `assist/Engine/auth/sample.py` to capture face samples
2. Run `assist/Engine/auth/trainer.py` to train the model

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


