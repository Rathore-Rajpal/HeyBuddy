import sys
sys.path.insert(0, 'assist/Engine')
from features import listen_for_wake_word

print('🎤 Testing Porcupine wake word detection...')
print('Say "Hey Buddy" to test')
print('Press Ctrl+C to stop\n')

try:
    result = listen_for_wake_word()
    if result:
        print('✅ Wake word detection successful!')
    else:
        print('❌ Wake word not detected')
except KeyboardInterrupt:
    print('\n\n⏹ Test stopped by user')
except Exception as e:
    print(f'❌ Error: {e}')
