
Built by https://www.blackbox.ai

---

```markdown
# Call Waiting and Voicemail System

## Project Overview
The Call Waiting and Voicemail System is a simple application built using Python's Tkinter library and HTML/CSS for the web interface. It simulates incoming calls, allows users to accept or reject calls, and facilitates leaving voicemails for missed calls. The application also logs missed calls and recorded voicemails for easy access.

## Installation

### Prerequisites
- Python 3.x
- Tkinter (usually included with Python installations)
- A web browser for the HTML interface

### Steps to Install
1. **Clone the Repository:**
   ```
   git clone https://github.com/yourusername/call_voicemail_app.git
   cd call_voicemail_app
   ```

2. **Run the Python Application:**
   ```
   python call_voicemail_app.py
   ```

3. **Open `index.html` in a web browser** to view the web interface.

## Usage
- **Incoming calls** will be simulated every 15 seconds.
- You can **accept** a call by clicking "Accept Call", or **reject** it by clicking "Reject Call".
- If a call is rejected, you'll be prompted to leave a voicemail message.
- All missed calls and voicemails are logged and can be viewed in the appropriate section of the interface.
- You can play the last voicemail recorded or clear the logs at any time.

## Features
- Simulated calls from a preset list of callers.
- Accept or reject incoming calls.
- Leave voicemail messages for missed calls.
- Scrollable logs of missed calls and recorded voicemails.
- Ability to clear all logged messages.

## Dependencies
The project does not have an explicit `package.json` file; however, it depends on the following:
- Python (with Tkinter for GUI)
- Basic HTML5 and CSS

To ensure all necessary libraries for running a Python program are available, simply confirm that Tkinter is installed with your Python distribution.

## Project Structure
```
call_voicemail_app/
│
├── call_voicemail_app.py        # Main Python application file
└── index.html                   # HTML file for the web interface
```

### Key Components
- **`call_voicemail_app.py`**: Contains the logic and UI for the voicemail system using Tkinter, simulating incoming calls and managing voicemails.
- **`index.html`**: Provides the structure and design of the web interface, enabling interaction with the voicemail system through a browser.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
```

Feel free to copy this README markdown and modify any sections as necessary to fit your specific project needs!