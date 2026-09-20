#!/usr/bin/env python3
"""Kn Gym Assistant - Local Network Server for Mobile & Other Devices
Enables accessing Kn Fitness Pro 2 from any device on your local WiFi (iPhone, Android, iPad, PC, Mac).
Zero extra dependencies required (uses standard library http.server).
"""

import http.server
import socket
import socketserver
import os
import sys

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
WEB_DIR = os.path.join(ROOT_DIR, "web")
VIDEOS_DIR = os.path.join(ROOT_DIR, "src", "videos")
PORT = 5000


def get_local_ip():
    """Finds the local network IP address of this machine."""
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    except Exception:
        ip = '127.0.0.1'
    finally:
        s.close()
    return ip



class CustomHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=WEB_DIR, **kwargs)

    def translate_path(self, path):
        # Route video requests to src/videos folder
        clean_path = path.split('?', 1)[0].split('#', 1)[0]
        if clean_path.startswith("/src/videos/"):
            rel_path = clean_path[len("/src/videos/"):]
            return os.path.join(VIDEOS_DIR, rel_path)
        elif clean_path.startswith("/videos/"):
            rel_path = clean_path[len("/videos/"):]
            return os.path.join(VIDEOS_DIR, rel_path)
        return super().translate_path(path)

    def log_message(self, format, *args):
        # Clean terminal logging
        sys.stderr.write(f"[{self.log_date_time_string()}] {args[0]} - {args[1]}\n")


def run_server():
    local_ip = get_local_ip()

    # Allow address reuse
    socketserver.TCPServer.allow_reuse_address = True

    try:
        with socketserver.TCPServer(("0.0.0.0", PORT), CustomHandler) as httpd:
            print("=" * 65)
            print("  ⚡ KN GYM ASSISTANT - UNIVERSAL DEVICE SERVER")
            print("=" * 65)
            print(f"  🖥️  On this computer:       http://localhost:{PORT}")
            print(f"  📱 On your Phone / Tablet:   http://{local_ip}:{PORT}")
            print("=" * 65)
            print("  💡 Instructions for Mobile Devices (iPhone / Android / iPad):")
            print("     1. Make sure your phone is connected to the same WiFi.")
            print(f"     2. Open your phone's browser (Safari/Chrome) and go to:")
            print(f"        👉  http://{local_ip}:{PORT}")
            print("     3. (Optional) Tap 'Share' -> 'Add to Home Screen' to use it")
            print("        just like an installed mobile app at the gym!")
            print("=" * 65)
            print("  Press Ctrl+C to stop the server.\n")

            httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nStopping server. Goodbye!")
    except OSError as e:
        print(f"\n[Error] Port {PORT} might already be in use: {e}")
        print(f"Try running with another port: python server.py <port>")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        try:
            PORT = int(sys.argv[1])
        except ValueError:
            pass
    run_server()

