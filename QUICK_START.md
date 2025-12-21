# Quick Start Guide

## First Time Setup (5 minutes)

### Step 1: Install Dependencies
Double-click `setup.bat` and wait for installation to complete.

### Step 2: Train Face Recognition (Optional but Recommended)
```
cd assist\Engine\auth
python sample.py
```
- Look at the camera and let it capture 30 samples
- Press 'q' when done

Then train the model:
```
python trainer.py
```

### Step 3: Configure API Keys (Optional)
Create a file named `.env` in the project root with:
```
# Spotify (Get from https://developer.spotify.com)
CLIENT_ID=your_spotify_client_id
CLIENT_SECRET=your_spotify_client_secret

# HuggingFace (Get from https://huggingface.co/settings/tokens)
HuggingFaceApiKey=your_huggingface_token
```

### Step 4: Test Everything
```
python test_components.py
```

### Step 5: Launch!
Double-click `start.bat`

---

## Daily Usage

### Starting the Assistant
1. Run `start.bat`
2. Complete face auth (or press ESC to skip)
3. Browser window opens automatically
4. Say "Hey Buddy" or click the mic button
5. Give your command

### Quick Commands to Try
- "Open YouTube"
- "Play some music"
- "Take a screenshot"
- "Set a reminder for 5 PM to call John"
- "Search for laptop on Amazon"
- "Start virtual mouse"

### Using Virtual Mouse
1. Say "start virtual mouse" or run `python virtualMouse.py`
2. Show your hand to the camera
3. Move index finger to move cursor
4. Use gestures (see README for full list)
5. Press ESC to exit

### Using Virtual Keyboard
1. Say "start virtual keyboard" or run `python virtual_ketboard.py`
2. Show your hand to the camera
3. Pinch (thumb + index close) over a key to type
4. Press ESC to exit

---

## Troubleshooting

### "Module not found"
Solution: Run `setup.bat` again

### Voice not recognized
Solution: Check microphone, speak clearly, ensure internet connection

### Camera not working
Solution: Close other apps using camera, check permissions

### Face auth fails
Solution: Press ESC to skip, or retrain your face (see Step 2)

### Browser doesn't open
Solution: Check if Edge is installed, or modify main.py to use Chrome

---

## Keyboard Shortcuts
- `Alt + J` - Activate voice command (when web UI is open)
- `ESC` - Exit virtual mouse/keyboard

---

## Need Help?
Check the full README.md or create an issue on GitHub.
