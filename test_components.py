"""
Component Test Script
Tests each component of the Virtual Assistant individually
"""

import sys
import os

def test_imports():
    """Test if all required modules can be imported"""
    print("\n=== Testing Imports ===")
    modules = [
        'eel', 'pyttsx3', 'speech_recognition', 'cv2', 'mediapipe',
        'cvzone', 'pyautogui', 'pynput', 'pywhatkit', 'keyboard',
        'playsound', 'dateparser', 'plyer', 'flask', 'requests',
        'PIL', 'dotenv', 'psutil'
    ]
    
    failed = []
    for module in modules:
        try:
            __import__(module)
            print(f"✓ {module}")
        except ImportError as e:
            print(f"✗ {module}: {e}")
            failed.append(module)
    
    if failed:
        print(f"\n❌ Failed to import: {', '.join(failed)}")
        print("Run: pip install -r requirements.txt")
        return False
    else:
        print("\n✅ All imports successful!")
        return True

def test_paths():
    """Test if required directories exist"""
    print("\n=== Testing Directory Structure ===")
    required_dirs = [
        'assist',
        'assist/Engine',
        'assist/www',
        'assist/Engine/auth',
        'assist/Engine/ImageBot',
        'assist/Engine/CodingBuddy'
    ]
    
    missing = []
    for dir_path in required_dirs:
        if os.path.exists(dir_path):
            print(f"✓ {dir_path}")
        else:
            print(f"✗ {dir_path} - MISSING")
            missing.append(dir_path)
    
    if missing:
        print(f"\n❌ Missing directories: {', '.join(missing)}")
        return False
    else:
        print("\n✅ All required directories exist!")
        return True

def test_database():
    """Test if database exists and has tables"""
    print("\n=== Testing Database ===")
    try:
        import sqlite3
        if os.path.exists('buddy.db'):
            conn = sqlite3.connect('buddy.db')
            cursor = conn.cursor()
            
            # Check tables
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
            tables = cursor.fetchall()
            print(f"✓ Database exists with tables: {[t[0] for t in tables]}")
            conn.close()
            return True
        else:
            print("⚠ Database file 'buddy.db' not found")
            print("  Database will be created on first run")
            return True
    except Exception as e:
        print(f"✗ Database error: {e}")
        return False

def test_audio():
    """Test text-to-speech"""
    print("\n=== Testing Text-to-Speech ===")
    try:
        import pyttsx3
        engine = pyttsx3.init()
        print("✓ TTS engine initialized")
        engine.say("Testing")
        engine.runAndWait()
        print("✓ TTS working")
        return True
    except Exception as e:
        print(f"✗ TTS error: {e}")
        return False

def test_camera():
    """Test camera access"""
    print("\n=== Testing Camera ===")
    try:
        import cv2
        cap = cv2.VideoCapture(0)
        if cap.isOpened():
            ret, frame = cap.read()
            if ret:
                print(f"✓ Camera accessible (Resolution: {frame.shape[1]}x{frame.shape[0]})")
                cap.release()
                return True
            else:
                print("✗ Camera opened but cannot read frames")
                cap.release()
                return False
        else:
            print("✗ Cannot open camera")
            return False
    except Exception as e:
        print(f"✗ Camera error: {e}")
        return False

def main():
    print("=" * 60)
    print("  VIRTUAL ASSISTANT BUDDY - COMPONENT TEST")
    print("=" * 60)
    
    results = []
    results.append(("Imports", test_imports()))
    results.append(("Paths", test_paths()))
    results.append(("Database", test_database()))
    results.append(("Audio (TTS)", test_audio()))
    results.append(("Camera", test_camera()))
    
    print("\n" + "=" * 60)
    print("  TEST SUMMARY")
    print("=" * 60)
    
    for name, passed in results:
        status = "✅ PASS" if passed else "❌ FAIL"
        print(f"{name:20} {status}")
    
    all_passed = all(result[1] for result in results)
    
    if all_passed:
        print("\n✅ All tests passed! System is ready to run.")
        print("\nTo start the assistant:")
        print("  1. Run: start.bat")
        print("  2. Or run: python run.py")
    else:
        print("\n❌ Some tests failed. Please fix the issues above.")
        return 1
    
    return 0

if __name__ == '__main__':
    sys.exit(main())
