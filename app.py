from flask import Flask, jsonify
import subprocess
import os

app = Flask(__name__)

@app.route('/launch-mouse', methods=['POST'])
def launch_virtual_mouse():
    try:
        # Launch the virtualMouse.py script
        script_path = os.path.join(os.path.dirname(__file__), 'virtualMouse.py')
        subprocess.Popen(['python', script_path])
        return jsonify({'message': 'Virtual Mouse Launched!'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
@app.route('/launch-keyboard', methods=['POST'])
def launch_virtual_keyboard():
    try:
        # Launch the virtual_keyboard.py script
        script_path = os.path.join(os.path.dirname(__file__), 'virtual_ketboard.py')
        subprocess.Popen(['python', script_path])
        return jsonify({'message': 'Virtual Keyboard Launched!'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
