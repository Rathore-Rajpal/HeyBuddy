#!/usr/bin/env python3
"""
Test improved wake word detection with timeout
"""
import sys
import os

sys.path.insert(0, os.path.dirname(__file__))

print("=" * 70)
print("IMPROVED WAKE WORD DETECTION TEST")
print("=" * 70)
print()
print("Instructions:")
print("1. When you see '🎤 Listening...' speak clearly")
print("2. Say 'Hey Buddy' naturally (like you're greeting someone)")
print("3. You have 5 seconds to say the wake word")
print("4. If not detected, it will retry automatically")
print()
print("-" * 70)

from assist.Engine.features import listen_for_wake_word

try:
    for attempt in range(3):
        print(f"\n📍 Attempt {attempt + 1} of 3:")
        result = listen_for_wake_word(timeout=5)
        
        if result:
            print("\n✅ SUCCESS! Wake word detected!")
            print("The integration is working correctly.")
            break
        else:
            print(f"\n❌ Attempt {attempt + 1} failed - Wake word not detected")
            if attempt < 2:
                print("   Try again with a clearer voice...")
    
    if not result:
        print("\n" + "=" * 70)
        print("⚠ TROUBLESHOOTING:")
        print("=" * 70)
        print("If wake word is not being detected:")
        print("1. Check microphone is connected and working")
        print("2. Try speaking louder and clearer")
        print("3. Ensure 'Hey Buddy' is spoken as two distinct words")
        print("4. Check that microphone level is not too low")
        print("5. Try the test_wakeword.py script instead for longer timeout")
        
except Exception as e:
    print(f"\n❌ Error: {e}")
    import traceback
    traceback.print_exc()

print("\n" + "=" * 70)
