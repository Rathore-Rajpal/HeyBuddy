"""
First-Time Setup Wizard for Buddy
Runs on first launch to configure user settings
"""

import os
import json
import tkinter as tk
from tkinter import ttk, messagebox
import cv2
from PIL import Image, ImageTk
import sys

class SetupWizard:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Buddy - First Time Setup")
        self.window.geometry("700x550")
        self.window.resizable(False, False)
        
        # Configuration file path
        self.config_file = "config.json"
        
        # User data
        self.user_data = {
            "user_name": "",
            "face_trained": False,
            "spotify_configured": False,
            "huggingface_configured": False,
            "setup_completed": False
        }
        
        # Current step
        self.current_step = 0
        self.total_steps = 4
        
        # Face capture variables
        self.face_id = 0
        self.face_count = 0
        self.capturing = False
        self.cam = None
        
        self.setup_ui()
        
    def setup_ui(self):
        """Setup the main UI"""
        # Header
        header = tk.Frame(self.window, bg="#667eea", height=80)
        header.pack(fill=tk.X)
        
        title = tk.Label(header, text="🤖 Welcome to Buddy!", 
                        font=("Arial", 24, "bold"), 
                        bg="#667eea", fg="white")
        title.pack(pady=20)
        
        # Content area
        self.content_frame = tk.Frame(self.window, bg="white")
        self.content_frame.pack(fill=tk.BOTH, expand=True, padx=40, pady=30)
        
        # Progress bar
        self.progress_frame = tk.Frame(self.window, bg="#f7fafc", height=60)
        self.progress_frame.pack(fill=tk.X, side=tk.BOTTOM)
        
        self.progress = ttk.Progressbar(self.progress_frame, length=600, 
                                       mode='determinate')
        self.progress.pack(pady=15)
        
        # Navigation buttons
        nav_frame = tk.Frame(self.window, bg="white", height=60)
        nav_frame.pack(fill=tk.X, side=tk.BOTTOM)
        
        self.back_btn = tk.Button(nav_frame, text="← Back", 
                                  command=self.previous_step,
                                  font=("Arial", 11), 
                                  bg="#e2e8f0", fg="#1a202c",
                                  padx=20, pady=10, border=0,
                                  cursor="hand2")
        self.back_btn.pack(side=tk.LEFT, padx=20)
        
        self.next_btn = tk.Button(nav_frame, text="Next →", 
                                 command=self.next_step,
                                 font=("Arial", 11, "bold"), 
                                 bg="#667eea", fg="white",
                                 padx=20, pady=10, border=0,
                                 cursor="hand2")
        self.next_btn.pack(side=tk.RIGHT, padx=20)
        
        # Show first step
        self.show_step()
        
    def show_step(self):
        """Display current step"""
        # Clear content
        for widget in self.content_frame.winfo_children():
            widget.destroy()
        
        # Update progress
        self.progress['value'] = (self.current_step / self.total_steps) * 100
        
        # Update buttons
        self.back_btn['state'] = tk.NORMAL if self.current_step > 0 else tk.DISABLED
        
        if self.current_step == self.total_steps:
            self.next_btn['text'] = "Finish ✓"
        else:
            self.next_btn['text'] = "Next →"
        
        # Show appropriate step
        if self.current_step == 0:
            self.show_welcome()
        elif self.current_step == 1:
            self.show_name_input()
        elif self.current_step == 2:
            self.show_face_training()
        elif self.current_step == 3:
            self.show_api_setup()
        elif self.current_step == 4:
            self.show_completion()
    
    def show_welcome(self):
        """Welcome screen"""
        tk.Label(self.content_frame, text="Welcome to Buddy! 👋", 
                font=("Arial", 20, "bold"), bg="white").pack(pady=20)
        
        tk.Label(self.content_frame, 
                text="Your intelligent desktop companion is ready for setup.\n\n"
                     "This wizard will help you configure:\n",
                font=("Arial", 12), bg="white", justify=tk.LEFT).pack(pady=10)
        
        features = [
            "✓ Your personal profile",
            "✓ Face authentication (optional)",
            "✓ API keys for advanced features (optional)"
        ]
        
        for feature in features:
            tk.Label(self.content_frame, text=feature, 
                    font=("Arial", 11), bg="white", 
                    justify=tk.LEFT).pack(anchor=tk.W, pady=5)
        
        tk.Label(self.content_frame, 
                text="\nSetup takes about 2-3 minutes.\nLet's get started!",
                font=("Arial", 11), bg="white", fg="#718096").pack(pady=20)
    
    def show_name_input(self):
        """Name input screen"""
        tk.Label(self.content_frame, text="What's your name?", 
                font=("Arial", 18, "bold"), bg="white").pack(pady=20)
        
        tk.Label(self.content_frame, 
                text="Buddy will use this to greet you.",
                font=("Arial", 11), bg="white", fg="#718096").pack(pady=5)
        
        self.name_entry = tk.Entry(self.content_frame, 
                                   font=("Arial", 14), 
                                   width=30)
        self.name_entry.pack(pady=20)
        self.name_entry.focus()
        
        # Load existing name if available
        if self.user_data["user_name"]:
            self.name_entry.insert(0, self.user_data["user_name"])
    
    def show_face_training(self):
        """Face training screen"""
        tk.Label(self.content_frame, text="Face Authentication (Optional)", 
                font=("Arial", 18, "bold"), bg="white").pack(pady=10)
        
        tk.Label(self.content_frame, 
                text="Train Buddy to recognize your face for secure login.",
                font=("Arial", 11), bg="white", fg="#718096").pack(pady=5)
        
        # Video frame
        self.video_label = tk.Label(self.content_frame, bg="#1a202c")
        self.video_label.pack(pady=15)
        
        # Status label
        self.status_label = tk.Label(self.content_frame, 
                                     text="Click 'Start Training' to begin",
                                     font=("Arial", 11, "bold"), 
                                     bg="white", fg="#667eea")
        self.status_label.pack(pady=10)
        
        # Training button
        btn_frame = tk.Frame(self.content_frame, bg="white")
        btn_frame.pack(pady=10)
        
        self.train_btn = tk.Button(btn_frame, text="Start Training", 
                                   command=self.start_face_training,
                                   font=("Arial", 12, "bold"), 
                                   bg="#48bb78", fg="white",
                                   padx=30, pady=10, border=0,
                                   cursor="hand2")
        self.train_btn.pack(side=tk.LEFT, padx=5)
        
        self.skip_btn = tk.Button(btn_frame, text="Skip for Now", 
                                 command=self.skip_face_training,
                                 font=("Arial", 11), 
                                 bg="#e2e8f0", fg="#1a202c",
                                 padx=20, pady=10, border=0,
                                 cursor="hand2")
        self.skip_btn.pack(side=tk.LEFT, padx=5)
    
    def show_api_setup(self):
        """API keys setup screen"""
        tk.Label(self.content_frame, text="API Keys (Optional)", 
                font=("Arial", 18, "bold"), bg="white").pack(pady=10)
        
        tk.Label(self.content_frame, 
                text="Add API keys to unlock advanced features like Spotify control and AI image generation.",
                font=("Arial", 10), bg="white", fg="#718096",
                wraplength=600).pack(pady=5)
        
        # Spotify
        spotify_frame = tk.LabelFrame(self.content_frame, text="Spotify API", 
                                     font=("Arial", 12, "bold"),
                                     bg="white", padx=20, pady=15)
        spotify_frame.pack(fill=tk.X, pady=10)
        
        tk.Label(spotify_frame, text="Client ID:", font=("Arial", 10), 
                bg="white").grid(row=0, column=0, sticky=tk.W, pady=5)
        self.spotify_id = tk.Entry(spotify_frame, font=("Arial", 10), width=40)
        self.spotify_id.grid(row=0, column=1, padx=10, pady=5)
        
        tk.Label(spotify_frame, text="Client Secret:", font=("Arial", 10), 
                bg="white").grid(row=1, column=0, sticky=tk.W, pady=5)
        self.spotify_secret = tk.Entry(spotify_frame, font=("Arial", 10), 
                                       width=40, show="*")
        self.spotify_secret.grid(row=1, column=1, padx=10, pady=5)
        
        tk.Button(spotify_frame, text="Get API Keys →", 
                 command=lambda: self.open_url("https://developer.spotify.com/dashboard"),
                 font=("Arial", 9), bg="#1DB954", fg="white", 
                 border=0, cursor="hand2", padx=10, pady=5).grid(row=2, column=1, sticky=tk.E, pady=5)
        
        # HuggingFace
        hf_frame = tk.LabelFrame(self.content_frame, text="HuggingFace API", 
                                font=("Arial", 12, "bold"),
                                bg="white", padx=20, pady=15)
        hf_frame.pack(fill=tk.X, pady=10)
        
        tk.Label(hf_frame, text="API Token:", font=("Arial", 10), 
                bg="white").grid(row=0, column=0, sticky=tk.W, pady=5)
        self.hf_token = tk.Entry(hf_frame, font=("Arial", 10), 
                                width=40, show="*")
        self.hf_token.grid(row=0, column=1, padx=10, pady=5)
        
        tk.Button(hf_frame, text="Get API Token →", 
                 command=lambda: self.open_url("https://huggingface.co/settings/tokens"),
                 font=("Arial", 9), bg="#FF9D00", fg="white", 
                 border=0, cursor="hand2", padx=10, pady=5).grid(row=1, column=1, sticky=tk.E, pady=5)
        
        tk.Label(self.content_frame, 
                text="💡 You can add these later in the settings",
                font=("Arial", 9), bg="white", fg="#718096").pack(pady=10)
    
    def show_completion(self):
        """Completion screen"""
        tk.Label(self.content_frame, text="🎉 Setup Complete!", 
                font=("Arial", 22, "bold"), bg="white", 
                fg="#48bb78").pack(pady=30)
        
        summary = [
            f"👤 Name: {self.user_data['user_name']}",
            f"🎭 Face Auth: {'Enabled' if self.user_data['face_trained'] else 'Skipped'}",
            f"🎵 Spotify: {'Configured' if self.user_data['spotify_configured'] else 'Not configured'}",
            f"🤖 HuggingFace: {'Configured' if self.user_data['huggingface_configured'] else 'Not configured'}"
        ]
        
        for item in summary:
            tk.Label(self.content_frame, text=item, 
                    font=("Arial", 12), bg="white").pack(pady=5)
        
        tk.Label(self.content_frame, 
                text="\nYou're all set! Click 'Finish' to start using Buddy.",
                font=("Arial", 11, "bold"), bg="white", 
                fg="#667eea").pack(pady=20)
    
    def start_face_training(self):
        """Start face capture"""
        self.capturing = True
        self.face_count = 0
        self.train_btn['state'] = tk.DISABLED
        self.skip_btn['state'] = tk.DISABLED
        self.next_btn['state'] = tk.DISABLED
        
        self.cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        self.cam.set(3, 640)
        self.cam.set(4, 480)
        
        self.detector = cv2.CascadeClassifier(
            'assist/Engine/auth/haarcascade_frontalface_default.xml')
        
        self.update_face_capture()
    
    def update_face_capture(self):
        """Update face capture frame"""
        if not self.capturing:
            return
        
        ret, img = self.cam.read()
        if not ret:
            return
        
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        gray = cv2.equalizeHist(gray)
        faces = self.detector.detectMultiScale(gray, scaleFactor=1.2, 
                                               minNeighbors=5, minSize=(30, 30))
        
        for (x, y, w, h) in faces:
            self.face_count += 1
            cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
            
            # Save face sample
            os.makedirs("assist/Engine/auth/samples", exist_ok=True)
            cv2.imwrite(f"assist/Engine/auth/samples/face.{self.face_id}.{self.face_count}.jpg",
                       gray[y:y+h, x:x+w])
            
            # Update status
            self.status_label['text'] = f"Capturing... {self.face_count}/100"
        
        # Convert to PhotoImage
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img_pil = Image.fromarray(img_rgb)
        img_pil = img_pil.resize((500, 375))
        img_tk = ImageTk.PhotoImage(img_pil)
        
        self.video_label.config(image=img_tk)
        self.video_label.image = img_tk
        
        if self.face_count >= 100:
            self.finish_face_training()
        else:
            self.window.after(100, self.update_face_capture)
    
    def finish_face_training(self):
        """Finish face training"""
        self.capturing = False
        if self.cam:
            self.cam.release()
        
        self.status_label['text'] = "Training model... Please wait"
        self.window.update()
        
        # Train the model
        try:
            import sys
            sys.path.append('assist/Engine/auth')
            from trainer import train_model
            train_model()
            
            self.user_data['face_trained'] = True
            self.status_label['text'] = "✓ Face authentication configured!"
            self.status_label['fg'] = "#48bb78"
        except Exception as e:
            self.status_label['text'] = f"Error: {str(e)}"
            self.status_label['fg'] = "#e53e3e"
        
        self.next_btn['state'] = tk.NORMAL
    
    def skip_face_training(self):
        """Skip face training"""
        self.user_data['face_trained'] = False
        self.current_step += 1
        self.show_step()
    
    def next_step(self):
        """Go to next step"""
        # Validate current step
        if self.current_step == 1:
            name = self.name_entry.get().strip()
            if not name:
                messagebox.showwarning("Name Required", "Please enter your name")
                return
            self.user_data['user_name'] = name
        
        elif self.current_step == 3:
            # Save API keys
            self.save_api_keys()
        
        elif self.current_step == self.total_steps:
            # Finish setup
            self.finish_setup()
            return
        
        self.current_step += 1
        self.show_step()
    
    def previous_step(self):
        """Go to previous step"""
        if self.current_step > 0:
            self.current_step -= 1
            self.show_step()
    
    def save_api_keys(self):
        """Save API keys to .env file"""
        spotify_id = self.spotify_id.get().strip()
        spotify_secret = self.spotify_secret.get().strip()
        hf_token = self.hf_token.get().strip()
        
        if spotify_id and spotify_secret:
            self.user_data['spotify_configured'] = True
        if hf_token:
            self.user_data['huggingface_configured'] = True
        
        # Create .env file
        env_content = f"""# Spotify API
CLIENT_ID={spotify_id}
CLIENT_SECRET={spotify_secret}

# HuggingFace API
HuggingFaceApiKey={hf_token}
"""
        with open('.env', 'w') as f:
            f.write(env_content)
    
    def finish_setup(self):
        """Finish setup and save configuration"""
        self.user_data['setup_completed'] = True
        
        # Save configuration
        with open(self.config_file, 'w') as f:
            json.dump(self.user_data, f, indent=4)
        
        messagebox.showinfo("Setup Complete", 
                          f"Welcome aboard, {self.user_data['user_name']}!\n\n"
                          "Buddy is ready to use.")
        
        self.window.destroy()
    
    def open_url(self, url):
        """Open URL in browser"""
        import webbrowser
        webbrowser.open(url)
    
    def run(self):
        """Run the wizard"""
        self.window.mainloop()

def check_first_run():
    """Check if this is first run"""
    return not os.path.exists("config.json")

if __name__ == "__main__":
    if check_first_run():
        wizard = SetupWizard()
        wizard.run()
    else:
        print("Setup already completed. Delete config.json to run setup again.")
