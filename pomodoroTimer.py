import tkinter as tk
from tkinter import ttk
import time
import threading

class PomodoroTimer:
    def __init__(self, root):
        self.root = root
        self.root.title("Pomodoro Timer")

        self.running = False
        self.paused = False

        # mins and secs for work and break
        self.work_minutes = tk.IntVar(value=25)
        self.break_minutes = tk.IntVar(value=5)

        # show timer
        self.label = tk.Label(root, text="25:00", font=("Arial", 40), fg="blue")
        self.label.pack(pady=10)

        self.status = tk.Label(root, text="Ready", font=("Arial", 14))
        self.status.pack()

        # bar for progress
        self.progress = ttk.Progressbar(root, length=300, mode='determinate')
        self.progress.pack(pady=10)

        # customize the input for work and break time
        frame = tk.Frame(root)
        frame.pack()

        tk.Label(frame, text="Work (min):").grid(row=0, column=0)
        tk.Entry(frame, textvariable=self.work_minutes, width=5).grid(row=0, column=1)

        tk.Label(frame, text="Break (min):").grid(row=0, column=2)
        tk.Entry(frame, textvariable=self.break_minutes, width=5).grid(row=0, column=3)

        # buttons for start, pause and reset
        self.start_btn = tk.Button(root, text="Start", command=self.start)
        self.start_btn.pack(side="left", padx=5)

        self.pause_btn = tk.Button(root, text="Pause", command=self.pause)
        self.pause_btn.pack(side="left", padx=5)

        self.reset_btn = tk.Button(root, text="Reset", command=self.reset)
        self.reset_btn.pack(side="right", padx=5)


    def run_timer(self, total_seconds, mode):
        self.running = True
        self.paused = False

        self.progress["maximum"] = total_seconds

        seconds = total_seconds

        while seconds >= 0 and self.running:
            if self.paused:
                time.sleep(0.1)
                continue

            mins = seconds // 60
            secs = seconds % 60
            self.label.config(text=f"{mins:02d}:{secs:02d}")

            # change color and sound when time is almost up
            if seconds <= 10:
                self.label.config(fg="red")
                self.root.bell()
            else:
                self.label.config(fg="blue")

            self.status.config(text=mode)

            self.progress["value"] = total_seconds - seconds

            time.sleep(1)
            seconds -= 1

        if self.running:
            if mode == "Work":
                self.run_timer(self.break_minutes.get() * 60, "Break")
            else:
                self.run_timer(self.work_minutes.get() * 60, "Work")

    def start(self):
        if not self.running:
            total = self.work_minutes.get() * 60
            thread = threading.Thread(target=self.run_timer, args=(total, "Work"))
            thread.start()

    def pause(self):
        self.paused = not self.paused
        if self.paused:
            self.status.config(text="Paused")
        else:
            self.status.config(text="Running")

    def reset(self):
        self.running = False
        self.paused = False
        self.label.config(text="25:00", fg="blue")
        self.status.config(text="Reset")
        self.progress["value"] = 0


if __name__ == "__main__":
    root = tk.Tk()
    app = PomodoroTimer(root)
    root.mainloop()