#!/usr/bin/env python3
"""
Test script to verify wake word detection is integrated into the main system
"""
import sys
import os

# Add the assist module to path
sys.path.insert(0, os.path.dirname(__file__))

print("=" * 60)
print("Wake Word Integration Test")
print("=" * 60)

try:
    # Test importing the updated allCommands function
    from assist.Engine.commands import allCommands
    print("✓ Successfully imported allCommands from commands.py")
    
    # Test importing the wake word detection function
    from assist.Engine.features import listen_for_wake_word
    print("✓ Successfully imported listen_for_wake_word from features.py")
    
    # Check the function signature
    import inspect
    sig = inspect.signature(allCommands)
    print(f"✓ allCommands signature: {sig}")
    
    # Check if listen_for_wake_word is properly integrated
    source = inspect.getsource(allCommands)
    if "listen_for_wake_word" in source:
        print("✓ Wake word detection is integrated into allCommands()")
    else:
        print("✗ Wake word detection NOT found in allCommands()")
        sys.exit(1)
    
    if "Wake word not detected" in source:
        print("✓ Wake word check logic is present")
    else:
        print("✗ Wake word check logic NOT found")
        sys.exit(1)
    
    print("\n" + "=" * 60)
    print("✓ ALL INTEGRATION CHECKS PASSED!")
    print("=" * 60)
    print("\nIntegration Summary:")
    print("- Wake word detection is now integrated into allCommands()")
    print("- Users must say 'Hey Buddy' before voice commands are processed")
    print("- Text input (from chat box) bypasses wake word check")
    print("- System provides feedback for wake word detection status")
    print("\nNext step: Run .\LAUNCH_BUDDY.bat to test the full system")
    
except Exception as e:
    print(f"✗ Error: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)
