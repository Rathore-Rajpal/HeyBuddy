import os
import eel
import time
import json
from assist.Engine.features import *
from assist.Engine.commands import *
from assist.Engine.auth import recoganize

def check_first_run():
    """Check if this is the first time running the app"""
    return not os.path.exists("config.json")

def run_setup_wizard():
    """Run the first-time setup wizard"""
    import setup_wizard
    wizard = setup_wizard.SetupWizard()
    wizard.run()
    
def load_user_config():
    """Load user configuration"""
    if os.path.exists("config.json"):
        with open("config.json", 'r') as f:
            return json.load(f)
    return None

def start():
    # Initialize eel with the correct path to the 'www' folder
    eel.init("assist/www")
    playAssistantSound()
    
    @eel.expose
    def getFaceAuthStatus():
        """Get current face auth status from config"""
        config = load_user_config()
        if config:
            return config.get('face_auth_enabled', True)
        return True
    
    @eel.expose
    def setFaceAuthStatus(enabled):
        """Save face auth status to config"""
        config = load_user_config()
        if not config:
            config = {}
        config['face_auth_enabled'] = enabled
        with open('config.json', 'w') as f:
            json.dump(config, f, indent=4)
        return True
    
    @eel.expose
    def launchFaceSetup():
        """Launch face authentication setup"""
        import subprocess
        import os
        bat_path = os.path.join(os.path.dirname(__file__), 'setup_face_auth.bat')
        subprocess.Popen([bat_path], shell=True, creationflags=subprocess.CREATE_NEW_CONSOLE)
    
    @eel.expose
    def testFaceAuth():
        """Test face authentication"""
        try:
            flag = recoganize.AuthenticateFace()
            if flag == 1:
                return "✓ Face authentication successful!"
            else:
                return "✗ Face not recognized. Please setup your face first."
        except Exception as e:
            return f"✗ Error: {str(e)}"
    
    @eel.expose
    def resetSettings():
        """Reset all settings to default"""
        config = {
            'face_auth_enabled': True,
            'setup_completed': True
        }
        if os.path.exists('config.json'):
            existing = load_user_config()
            if existing and 'user_name' in existing:
                config['user_name'] = existing['user_name']
        
        with open('config.json', 'w') as f:
            json.dump(config, f, indent=4)
        return True
    
    @eel.expose
    def init():
         #subprocess.call([r'device.bat'])
         
         # ============================================
         # FACE AUTHENTICATION CONFIGURATION
         # ============================================
         # Load face auth setting from config
         config = load_user_config()
         enable_face_auth = True  # Default to enabled
         
         if config and 'face_auth_enabled' in config:
             enable_face_auth = config['face_auth_enabled']
         # ============================================
         
         import os
         # Use absolute path since multiprocessing may change working directory
         trainer_path = os.path.join(os.path.dirname(__file__), 'assist', 'Engine', 'auth', 'trainer', 'trainer.yml')
         trainer_exists = os.path.exists(trainer_path)
         
         print(f"DEBUG: enable_face_auth={enable_face_auth}, trainer_exists={trainer_exists}")
         print(f"DEBUG: Looking for trainer at: {trainer_path}")
         
         if enable_face_auth:
             if trainer_exists:
                 print("Starting face authentication...")
                 speak("Ready for face Authentication")
                 flag = recoganize.AuthenticateFace()
             else:
                 # Show message that model needs to be set up
                 print(f"⚠ Face recognition model not found at {trainer_path}. Skipping authentication.")
                 print("  To enable: Run setup_face_auth.bat or click 'Setup Face Recognition' in Settings")
                 speak("Face recognition not configured. Please setup your face first.")
                 flag = 0
         else:
             print("Face authentication disabled in settings")
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
    # Check if this is the first run
    if check_first_run():
        print("First time setup detected. Running setup wizard...")
        run_setup_wizard()
        
        # After setup, check if we should continue
        config = load_user_config()
        if not config or not config.get('setup_completed'):
            print("Setup was cancelled. Exiting...")
            exit()
        
        print(f"Welcome, {config.get('user_name', 'User')}!")
    
    # Start the main application
    start()
