import subprocess
import sys
import time
import webbrowser
import re
import dateparser
import keyboard
import pyttsx3
import speech_recognition as sr
import eel
import os
import assist.Engine.spotify as sp
import pyautogui as auto


def normalize_query(text):
    """Normalize speech/text input to improve intent detection."""
    if not text:
        return ""

    normalized = text.lower().strip()
    normalized = re.sub(r"[^a-z0-9\s]", " ", normalized)
    normalized = re.sub(r"\s+", " ", normalized).strip()

    replacements = {
        "you tube": "youtube",
        "whats app": "whatsapp",
        "what s app": "whatsapp",
        "watsapp": "whatsapp",
        "whatsup": "whatsapp",
        "spotfy": "spotify",
        "gogle": "google",
        "e mail": "email",
        "note down": "take a note",
        "remind me": "set a reminder",
        "launch": "start",
    }

    for wrong, right in replacements.items():
        normalized = normalized.replace(wrong, right)

    return normalized


def contains_any(text, keywords):
    return any(keyword in text for keyword in keywords)

@eel.expose
def speak(text):
    text = str(text)
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.setProperty('rate', 174)
    eel.DisplayMessage(text)
    engine.say(text)
    eel.receiverText(text)
    engine.runAndWait()


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        eel.DisplayMessage('Listening...')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)

        audio = r.listen(source, 10, 6)
    
    try:
        print("Recognizing...")
        eel.DisplayMessage('Recognizing...')
        query = r.recognize_google(audio, language='en-in')
        print(f"User Said: {query}")
        eel.DisplayMessage(query)
    
    except Exception as e:
        return ""
    
    return query.lower()

@eel.expose
def allCommands(message=1):
    # Voice path: listen immediately when mic is clicked
    if message == 1:
        eel.DisplayMessage("🎤 Listening...")
        try:
            query = takecommand()
        except Exception as mic_err:
            err_msg = f"Microphone error: {mic_err}"
            print(err_msg)
            eel.DisplayMessage(err_msg)
            return err_msg
        print(f"Query received: {query}")  # Debugging statement
        eel.senderText(query)
    else:
        # Text path: direct message from chat box
        query = message
        eel.senderText(query)
        
    query = normalize_query(query)

    try:
        # Handle Spotify command first if it matches the format "open {artist_name} on Spotify"
        if "spotify" in query and contains_any(query, ["open", "start", "play"]):
            print("Handling 'open artist on Spotify' command")
            token = sp.get_token()
            sp.handle_query(token, query)
        
        elif contains_any(query, ["bye-bye", "bye bye", "goodbye"]):
            speak("Terminating the assistant...")
            auto.hotkey('alt','f4')

        # General "open" command
        elif contains_any(query, ["open", "run"]):
            print("Handling general 'open' command")
            from assist.Engine.features import openCommand
            openCommand(query)
        
        elif "youtube" in query:
            if contains_any(query, ["search", "find", "look up"]):
                from assist.Engine.features import SearchYoutube
                SearchYoutube(query)
            else:
                from assist.Engine.features import PlayYoutube
                PlayYoutube(query)
        
        elif contains_any(query, ["call", "make a call", "dial"]) and contains_any(query, ["on my phone", "on my iphone", "on phone", "on mobile"]):
            print("Handling phone call command")
            from assist.Engine.phone_connection import call_on_mobile
            call_on_mobile(query)

        elif contains_any(query, ["send a message", "text", "send message"]) and contains_any(query, ["on my phone", "on my iphone", "on phone", "on mobile"]):
            print("Handling phone message command")
            from assist.Engine.phone_connection import message_on_phone
            speak("What is the message ?")
            message = takecommand()
            message_on_phone(query,message)

        # Then handle WhatsApp commands (MOVED DOWN)
        elif contains_any(query, ["send message", "voice call", "video call", "send a message", "call"]):
            print("Handling WhatsApp command")
            from assist.Engine.features import findContact, whatsApp
            flag = ""
            contact_no, name = findContact(query)
            print(f"Contact number: {contact_no}, Name: {name}")
            
            if contact_no != 0:
                if "send message" in query or "send a message" in query:
                    flag = 'message'
                    speak("What message to send?")
                    query = takecommand()
                    print(f"Message to send: {query}")
                
                elif "video call" in query:
                    flag = 'video call'
                    
                elif "phone call" in query or "call" in query or "voice call" in query:
                    flag = 'call'
                
                
                print(f"Calling whatsApp() with number: {contact_no}, message: {query}, flag: {flag}, name: {name}")
                whatsApp(contact_no, query, flag, name)
            else:
                print("Contact not found!")
                
        elif contains_any(query, ["search", "find", "look up"]):
            if contains_any(query, ["on google", "on internet", "on web", "google"]):
                print("Handling 'search on Google' command")
                from assist.Engine.features import google_search
                google_search(query)
            else:
                print("Handling 'product search on website' command")
                from assist.Engine.searchingProduct import search_product
                search_product(query)
        
        elif "spotify" in query:
            print("Handling 'Spotify' command")
            token = sp.get_token()
            sp.handle_query(token, query)
        
        elif contains_any(query, ["take a note", "write a note", "make a note"]) and "in file" not in query:
            print("Handling 'take a note' command")
            speak("What would you like to note down?")
            note = takecommand()
            if note:
                from assist.Engine.features import take_note
                take_note(note)
                speak("Your note has been saved.")
            else:
                speak("I couldn't hear the note properly. Please try again.")
        
        elif contains_any(query, ["take a note in file", "write a note in file", "save a note in file"]):
            print("Handling 'take a note in file' command")
            speak("What would you like to note down?")
            note = takecommand()
            if note:
                with open("sticky_notes.txt", "a") as file:
                    file.write(note + "\n")
                speak("Your note has been saved to the file.")
            else:
                speak("I couldn't hear the note properly. Please try again.")
        
        elif contains_any(query, ["some music", "play music", "music"]):
            speak("Playing some music for you")
            print("Handling 'music play' command")
            sp.play_pause()
        
        elif "screenshot" in query.lower():
            from assist.Engine.features import caputure_screenshot
            speak("capturing screenshot")
            caputure_screenshot()
            speak("Screenshot captured sucessfully")
            
        elif contains_any(query, ["set a reminder", "set reminder", "reminder"]):
            from assist.Engine.features import set_reminder
            speak("Please tell me when you want to set the reminder.'.")
            reminder_input = takecommand()

            speak("What is the reminder about?")
            reminder_subject = takecommand()

            # Use dateparser to parse natural language input into a datetime object
            reminder_datetime = dateparser.parse(reminder_input)
            
            if reminder_datetime:
                set_reminder(reminder_datetime, reminder_subject)
                speak(f"Your reminder for {reminder_subject} is set for {reminder_datetime}.")
            else:
                speak("Sorry, I couldn't understand the date and time. Please try again.")
                
        elif contains_any(query, ["send a email", "send email", "send a mail", "send an email", "draft a mail", "write an emai", "write a mail", "send mail", "email"]):
            from assist.Engine.features import send_email
            send_email(query)
            
        elif contains_any(query, ["close", "terminate", "quit"]):
            from assist.Engine.features import close_app
            close_app(query)
            
        elif contains_any(query, ["generate image", "generate an image", "create image", "make image"]):
            from assist.Engine.image_generator import generate_image
            speak("What image you need to generate: ")
            prompt = takecommand()
            speak(f"Generating image:{prompt}")
            generate_image(prompt)
            speak("Image Generated Sucessfully")
            
        elif "search for " in query:
            from assist.Engine.searchingProduct import search_product
            search_product(query)
            
        elif contains_any(query, ["write a code", "generate a code", "write the code", "create code", "code for"]):
            from assist.Engine.features import codeBot
            codeBot(query)
            
        elif contains_any(query, ["shortest route", "shortest distance", "google maps", "maps", "distance", "directions", "route"]):
            from assist.Engine.features import open_shortest_route
            open_shortest_route(query)
        
        elif contains_any(query, ["start image master", "launch image master", "open image master"]):
            speak("Launching Image Master")
            eel.ShowHood()
            file_path = r'assist\Engine\ImageBot\index.html'
            webbrowser.open(file_path)
            python_interpreter = r'C:\VirtualMouseProject\envjarvis\Scripts\python.exe'
            subprocess.Popen([python_interpreter, r'assist\Engine\ImageBot\app.py'], creationflags=subprocess.CREATE_NEW_CONSOLE)
            
            
        elif contains_any(query, ["start code master", "launch code master", "open code master"]):
            speak("Launching Code Master")
            eel.ShowHood()
            file_path = r'assist\Engine\CodingBuddy\index.html'
            webbrowser.open(file_path)
            python_interpreter = r'C:\VirtualMouseProject\envjarvis\Scripts\python.exe'
            subprocess.Popen([python_interpreter, r'assist\Engine\CodingBuddy\app.py'], creationflags=subprocess.CREATE_NEW_CONSOLE)
            
        elif contains_any(query, ["start virtual mouse", "launch virtual mouse", "open virtual mouse"]):
            speak("Launching virtual mouse")
            eel.ShowHood()
            subprocess.run(['python','virtualMouse.py'])

            
        elif contains_any(query, ["start virtual keyboard", "launch virtual keyboard", "open virtual keyboard"]):
            speak("Starting virtual keyboard")
            eel.ShowHood()
            subprocess.run(['python','virtual_ketboard.html.py'])
            
            
        else:
            eel.DisplayMessage("Handling 'AI Bot' command")
            print("Handling 'AI Bot' command")
            try:
                from assist.Engine.features import chatBot
                # Unknown commands are now sent directly to AI bot.
                chatBot(query)
                return "ai_bot_handled"
            except Exception as bot_error:
                err_msg = f"AI Bot error: {bot_error}"
                print(err_msg)
                eel.DisplayMessage(err_msg)
                return "ai_bot_error"
    except Exception as e:
        print(f"Error in allCommands: {e}")  # Detailed error message for debugging

    # Always return a value so eel has something to send back
    return "handled"

    eel.ShowHood()  # Ensure this is called even if an error occurs
