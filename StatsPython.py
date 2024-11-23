import tkinter as tk
from tkinter import Label, Canvas
from PIL import Image, ImageTk, ImageSequence
from datetime import datetime
import psutil  # For system stats
import random  # For quotes
import time  # For precise timing
import requests  # For API calls

# Global variables
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 600  # Adjusted for a compact layout

# Inspirational quotes
quotes = [
    "Believe in yourself and all that you are.",
    "Success is not final, failure is not fatal: It is the courage to continue that counts.",
    "The only way to do great work is to love what you do.",
    "Your limitation—it's only your imagination.",
    "Push yourself, because no one else is going to do it for you.",
    "Great things never come from comfort zones.",
    "Dream it. Wish it. Do it.",
    "Success doesn’t just find you. You have to go out and get it."
]

# Track network stats for dynamic usage calculation
previous_network_stats = psutil.net_io_counters()
previous_time = time.time()

def get_weather_by_city(city_name):
    """Fetch weather information for a given city using OpenWeatherMap API."""
    try:
        api_key = "3da43ca6dbf76cadf18fbe657b1a8936"  # Your API key
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            # Extract actual temperature, feels like temperature, and description
            temperature = round(data["main"]["temp"], 1)
            feels_like = round(data["main"]["feels_like"], 1)
            description = data["weather"][0]["description"].capitalize()

            # Add relevant emoji based on description
            if "clear" in description.lower():
                emoji = "☀️"
            elif "cloud" in description.lower():
                emoji = "☁️"
            elif "rain" in description.lower():
                emoji = "🌧️"
            elif "smoke" in description.lower() or "haze" in description.lower():
                emoji = "🌫️"
            elif "snow" in description.lower():
                emoji = "❄️"
            else:
                emoji = "🌍"

            # Return formatted string
            return f"{emoji} {description}\n🌡️ Temp: {temperature}°C | Feels Like: {feels_like}°C"
        else:
            print(f"Failed to fetch weather data: {response.status_code}")
            return "Weather data not available."
    except Exception as e:
        print(f"Error fetching weather data: {e}")
        return "Weather data not available."



def update_stats():
    """Update all stats dynamically."""
    global previous_network_stats, previous_time
    try:
        # CPU Stats
        cpu_usage = psutil.cpu_percent(interval=0)
        cpu_freq = psutil.cpu_freq()
        cpu_label.config(text=f"CPU Usage: {cpu_usage:.1f}% | Freq: {cpu_freq.current:.0f} MHz")
        cpu_bar.coords(cpu_fill, 0, 0, cpu_usage * 3, 10)

        # RAM Stats
        mem = psutil.virtual_memory()
        ram_label.config(
            text=f"RAM Usage: {mem.percent:.1f}% | {mem.used // (1024 ** 2)} MB / {mem.total // (1024 ** 2)} MB"
        )
        ram_bar.coords(ram_fill, 0, 0, mem.percent * 3, 10)

        # Network Stats (Send/Receive in KBps)
        current_time = time.time()
        elapsed_time = current_time - previous_time
        current_network_stats = psutil.net_io_counters()
        sent_kbps = (current_network_stats.bytes_sent - previous_network_stats.bytes_sent) / elapsed_time / 1024
        received_kbps = (current_network_stats.bytes_recv - previous_network_stats.bytes_recv) / elapsed_time / 1024

        network_label.config(
            text=f"▲ Sent: {sent_kbps:.2f} KBps\n▼ Received: {received_kbps:.2f} KBps",
            fg="orange"
        )

        # Update previous stats for next calculation
        previous_network_stats = current_network_stats
        previous_time = current_time

        # Battery Stats
        battery = psutil.sensors_battery()
        if battery:
            battery_label.config(
                text=f"Battery: {battery.percent}% {'(Charging)' if battery.power_plugged else '(Discharging)'}"
            )
        else:
            battery_label.config(text="Battery: Not Available")

        # Time and Date
        current_time = datetime.now().strftime("%I:%M:%S %p")
        current_date = datetime.now().strftime("%Y-%m-%d")
        time_label.config(text=f"Time: {current_time}")
        date_label.config(text=f"Date: {current_date}")

        # Update Weather
        weather_info = get_weather_by_city("London")  # Replace "London" with your desired city
        weather_label.config(text=f"Weather: {weather_info}")

    except Exception as e:
        print(f"Error updating stats: {e}")

    root.after(1000, update_stats)

def update_quote():
    """Update the quote every 5 minutes."""
    quote = random.choice(quotes)
    quote_label.config(text=quote)
    root.after(300000, update_quote)

def adjust_transparency(value):
    """Adjust the transparency of the window."""
    root.attributes("-alpha", float(value) / 100)

def start_drag(event):
    """Record the initial position of the mouse relative to the window."""
    root.start_x = event.x
    root.start_y = event.y

def drag_motion(event):
    """Move the window while dragging."""
    x = root.winfo_pointerx() - root.start_x
    y = root.winfo_pointery() - root.start_y
    root.geometry(f"+{x}+{y}")

# Tkinter setup
root = tk.Tk()
root.title("System Stats")
root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
root.attributes("-topmost", True)
root.overrideredirect(True)

def load_gif(path, width=None, height=None):
    """Load an animated GIF, resize it, and extract frame durations."""
    try:
        gif = Image.open(path)
        frames = []
        durations = []
        for frame in ImageSequence.Iterator(gif):
            if width and height:
                frame = frame.resize((width, height), Image.LANCZOS)
            frames.append(ImageTk.PhotoImage(frame.copy()))
            duration = frame.info.get("duration", 100)  # Default to 100ms if not provided
            durations.append(duration)
        print(f"Loaded {len(frames)} frames from the GIF.")
        return frames, durations
    except Exception as e:
        print(f"Error loading GIF: {e}")
        return [], []

# Load the GIF as background
background_frames, frame_durations = load_gif("C:/Users/Kakashi Uchiha/Downloads/200w.gif", WINDOW_WIDTH, WINDOW_HEIGHT)

if not background_frames:
    print("No frames loaded. Exiting...")
    exit()

# Ensure all frames have valid durations
default_duration = 100  # Default duration in milliseconds
frame_durations = [duration if duration > 0 else default_duration for duration in frame_durations]

# Canvas setup for displaying the GIF
canvas = tk.Canvas(root, width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
canvas.pack(fill="both", expand=True)

background_label = Label(canvas)
background_label.place(x=0, y=0)

def update_background():
    """Animate the GIF smoothly using precise timing."""
    current_time = time.time()
    # Check if enough time has passed for the next frame
    if current_time >= update_background.next_frame_time:
        # Display the current frame
        frame = background_frames[update_background.current_frame]
        background_label.config(image=frame)

        # Schedule the next frame
        duration = frame_durations[update_background.current_frame] / 1000.0  # Convert ms to seconds
        update_background.next_frame_time = current_time + duration
        update_background.current_frame = (update_background.current_frame + 1) % len(background_frames)

    # Call this function again very soon to ensure precise timing
    root.after(1, update_background)

# Initialize frame update variables
update_background.current_frame = 0
update_background.next_frame_time = time.time()
update_background()

# Widgets
font_name = "Consolas"
font_size = 12
font_color = "white"

cpu_label = Label(canvas, text="CPU Usage: ", font=(font_name, font_size), fg=font_color, bg="black")
cpu_label.place(x=10, y=20)

cpu_bar = Canvas(canvas, width=300, height=10, bg="black", highlightthickness=0)
cpu_bar.place(x=10, y=50)
cpu_fill = cpu_bar.create_rectangle(0, 0, 0, 10, fill="orange")

ram_label = Label(canvas, text="RAM Usage: ", font=(font_name, font_size), fg=font_color, bg="black")
ram_label.place(x=10, y=80)

ram_bar = Canvas(canvas, width=300, height=10, bg="black", highlightthickness=0)
ram_bar.place(x=10, y=110)
ram_fill = ram_bar.create_rectangle(0, 0, 0, 10, fill="orange")

network_label = Label(canvas, text="", font=(font_name, font_size), fg="orange", bg="black", justify="left")
network_label.place(x=10, y=140)

battery_label = Label(canvas, text="Battery: ", font=(font_name, font_size), fg=font_color, bg="black")
battery_label.place(x=10, y=200)

time_label = Label(canvas, text="Time: ", font=(font_name, font_size), fg=font_color, bg="black")
time_label.place(x=10, y=230)

date_label = Label(canvas, text="Date: ", font=(font_name, font_size), fg=font_color, bg="black")
date_label.place(x=10, y=260)

weather_info = get_weather_by_city("Lahore")  # Replace "Lahore" with your city

weather_label = Label(canvas, text=f"Weather:\n{weather_info}", font=(font_name, font_size), fg="white", bg="black", justify="left")
weather_label.place(x=10, y=300)



quote_label = Label(canvas, text="", font=(font_name, font_size), fg="white", bg="black", wraplength=WINDOW_WIDTH - 20)
quote_label.place(x=10, y=350)

transparency_slider = tk.Scale(canvas, from_=0, to=100, orient="horizontal", label="Transparency", command=adjust_transparency)
transparency_slider.set(80)
transparency_slider.place(x=50, y=500)

root.bind("<ButtonPress-1>", start_drag)
root.bind("<B1-Motion>", drag_motion)

update_stats()
update_quote()
root.mainloop()
