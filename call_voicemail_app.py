import tkinter as tk
from tkinter import messagebox, simpledialog, scrolledtext
import threading
import time
import datetime
import os

class CallVoicemailApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Call Waiting and Voicemail System")
        self.root.geometry("600x500")

        # State variables
        self.call_active = False
        self.current_caller = None
        self.missed_calls = []
        self.voicemails = []  # list of (caller, message, timestamp)

        # UI Setup
        self.setup_ui()

        # Start call simulation thread
        self.call_thread = threading.Thread(target=self.simulate_calls, daemon=True)
        self.call_thread.start()

    def setup_ui(self):
        # Incoming call frame
        self.call_frame = tk.LabelFrame(self.root, text="Incoming Call", padx=10, pady=10)
        self.call_frame.pack(fill="x", padx=10, pady=5)

        self.caller_label = tk.Label(self.call_frame, text="No incoming call", font=("Arial", 14))
        self.caller_label.pack()

        self.accept_button = tk.Button(self.call_frame, text="Accept Call", state="disabled", command=self.accept_call)
        self.accept_button.pack(side="left", padx=10, pady=5)

        self.reject_button = tk.Button(self.call_frame, text="Reject Call", state="disabled", command=self.reject_call)
        self.reject_button.pack(side="left", padx=10, pady=5)

        # Missed calls and voicemails frame
        self.log_frame = tk.LabelFrame(self.root, text="Missed Calls and Voicemails", padx=10, pady=10)
        self.log_frame.pack(fill="both", expand=True, padx=10, pady=5)

        self.log_text = scrolledtext.ScrolledText(self.log_frame, state="disabled", height=15)
        self.log_text.pack(fill="both", expand=True)

        # Playback controls
        self.playback_frame = tk.Frame(self.root)
        self.playback_frame.pack(fill="x", padx=10, pady=5)

        self.play_voicemail_button = tk.Button(self.playback_frame, text="Play Last Voicemail", state="disabled", command=self.play_last_voicemail)
        self.play_voicemail_button.pack(side="left", padx=10)

        self.clear_logs_button = tk.Button(self.playback_frame, text="Clear Logs", command=self.clear_logs)
        self.clear_logs_button.pack(side="right", padx=10)

    def simulate_calls(self):
        callers = ["Alice", "Bob", "Charlie", "Diana", "Eve"]
        while True:
            # Wait random time between calls
            time.sleep(10)
            if not self.call_active:
                self.current_caller = callers[int(time.time()) % len(callers)]
                self.call_active = True
                self.update_incoming_call_ui()
                # Wait for 20 seconds for user to respond
                for _ in range(20):
                    if not self.call_active:
                        break
                    time.sleep(1)
                if self.call_active:
                    # Call timed out, treat as missed call
                    self.missed_calls.append((self.current_caller, datetime.datetime.now()))
                    self.log_message(f"Missed call from {self.current_caller} at {self.missed_calls[-1][1].strftime('%Y-%m-%d %H:%M:%S')}")
                    self.call_active = False
                    self.current_caller = None
                    self.update_incoming_call_ui()

    def update_incoming_call_ui(self):
        if self.call_active and self.current_caller:
            self.caller_label.config(text=f"Incoming call from {self.current_caller}")
            self.accept_button.config(state="normal")
            self.reject_button.config(state="normal")
        else:
            self.caller_label.config(text="No incoming call")
            self.accept_button.config(state="disabled")
            self.reject_button.config(state="disabled")

    def accept_call(self):
        if self.call_active:
            messagebox.showinfo("Call Accepted", f"You accepted the call from {self.current_caller}.")
            self.call_active = False
            self.current_caller = None
            self.update_incoming_call_ui()

    def reject_call(self):
        if self.call_active:
            self.call_active = False
            caller = self.current_caller
            self.current_caller = None
            self.update_incoming_call_ui()
            self.missed_calls.append((caller, datetime.datetime.now()))
            self.log_message(f"Missed call from {caller} at {self.missed_calls[-1][1].strftime('%Y-%m-%d %H:%M:%S')}")
            # Ask user to record voicemail (text input)
            self.ask_record_voicemail(caller)

    def ask_record_voicemail(self, caller):
        answer = messagebox.askyesno("Voicemail", f"Do you want to leave a voicemail message for {caller}?")
        if answer:
            self.record_voicemail(caller)

    def record_voicemail(self, caller):
        message = simpledialog.askstring("Record Voicemail", f"Enter your voicemail message for {caller}:")
        if message:
            timestamp = datetime.datetime.now()
            self.voicemails.append((caller, message, timestamp))
            self.log_message(f"Voicemail recorded for {caller} at {timestamp.strftime('%Y-%m-%d %H:%M:%S')}")
            self.play_voicemail_button.config(state="normal")

    def play_last_voicemail(self):
        if not self.voicemails:
            messagebox.showinfo("No Voicemail", "No voicemails to play.")
            return
        caller, message, timestamp = self.voicemails[-1]
        self.log_message(f"Playing voicemail for {caller} recorded at {timestamp.strftime('%Y-%m-%d %H:%M:%S')}")
        messagebox.showinfo(f"Voicemail from {caller}", message)

    def log_message(self, message):
        self.log_text.config(state="normal")
        self.log_text.insert(tk.END, message + "\n")
        self.log_text.see(tk.END)
        self.log_text.config(state="disabled")

    def clear_logs(self):
        self.log_text.config(state="normal")
        self.log_text.delete(1.0, tk.END)
        self.log_text.config(state="disabled")

    def on_closing(self):
        self.root.destroy()

def main():
    root = tk.Tk()
    app = CallVoicemailApp(root)
    root.protocol("WM_DELETE_WINDOW", app.on_closing)
    root.mainloop()

if __name__ == "__main__":
    main()
