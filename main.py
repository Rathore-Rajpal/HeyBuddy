import os
import eel
import time
from assist.Engine.features import *
from assist.Engine.commands import *
from assist.Engine.auth import recoganize

def start():
    # Initialize eel with the correct path to the 'www' folder
    eel.init("assist/www")
    playAssistantSound()
    @eel.expose
    def init():
         #subprocess.call([r'device.bat'])
         
         # ============================================
         # FACE AUTHENTICATION CONFIGURATION
         # ============================================
         # Set to True to enable face authentication on startup
         # Set to False to skip face auth (for deployment/sharing)
         # Note: Users must run setup_face_auth.bat to register their face
         enable_face_auth = True
         # ============================================
         
         import os
         # Use absolute path since multiprocessing may change working directory
         trainer_path = os.path.join(os.path.dirname(__file__), 'assist', 'Engine', 'auth', 'trainer', 'trainer.yml')
         trainer_exists = os.path.exists(trainer_path)
         
         print(f"DEBUG: enable_face_auth={enable_face_auth}, trainer_exists={trainer_exists}")
         print(f"DEBUG: Looking for trainer at: {trainer_path}")
         
         if enable_face_auth and trainer_exists:
             print("Starting face authentication...")
             speak("Ready for face Authentication")
             flag = recoganize.AuthenticateFace()
         else:
             if not trainer_exists:
                 print(f"Face authentication model not found at {trainer_path}. Skipping...")
             else:
                 print("Face authentication disabled in code")
             flag = 0
         
         if(flag == 1):
             eel.hideFaceAuth()
             speak("Face authentication successful")
             eel.hideFaceAuthSuccess()
             speak("Welcome to AI Assistant. I am your buddy, ready to help")
             eel.hideStart()
             playAssistantSound()
         else:
             # Skip face auth and proceed
             speak("Welcome to AI Assistant. I am your buddy, ready to help")
             eel.hideFaceAuth()
             eel.hideFaceAuthSuccess()
             eel.hideStart()
             playAssistantSound()
        
   

    # Launch Microsoft Edge in app mode
    os.system('start msedge.exe --app="http://localhost:8000/index.html"')

    # Start the Eel server and ensure block is passed as a boolean
    eel.start('index.html', mode=None, host='localhost', port=8000, block=True)

if __name__ == '__main__':
    start()
