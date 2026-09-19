# Kn Fitness Pro 2 — Universal Device Guide 🚀

This guide explains how to run and use **Kn Fitness Pro 2** on **any device**:
- 📱 **Mobile Phones & Tablets** (iPhone, iPad, Android)
- 🪟 **Windows PCs & Laptops** (Standalone `.exe` or Python)
- 🍎 **Apple Mac Computers** (macOS `.app` or Python)
- 🌐 **Any Web Browser** (Zero installation required)

---

## 1. 📱 Use on Mobile Phones & Tablets (iPhone / iPad / Android)

Desktop Qt applications (PySide6) cannot run natively on smartphones. We provided two zero-installation solutions:

### Option A: Local WiFi Access (Gym / Home)
1. On your Mac or PC, open Terminal in this folder and start the local server:
   ```bash
   python server.py
   ```
2. Terminal will display your network address, for example:
   ```text
   📱 On your Phone / Tablet: http://192.168.1.50:5000
   ```
3. Connect your phone or tablet to the same WiFi network and open that URL in **Safari** or **Chrome**.
4. **Pro Tip**: Tap **Share** (iOS) or **Menu (⋮)** (Android) → **"Add to Home Screen"**. It will install and look like a native app on your phone!

### Option B: Free Cloud Hosting (Use Anywhere in the World)
You can deploy the files inside the `web/` folder to free static hosting services like:
- **GitHub Pages** (Free 100% forever)
- **Vercel** or **Netlify** (Drag and drop the `web/` folder to deploy in 10 seconds)
Once deployed, anyone on any device can access it from anywhere using a public link!

---

## 2. 🪟 Use on Windows Computers

### Why the Mac version didn't work on Windows:
macOS `.app` files are Mach-O Unix bundles and do not run on Windows. Windows requires a `.exe` executable.

### How to Build `Kn Fitness Pro.exe` on Windows:
1. Copy this folder to your Windows computer (via USB drive, cloud, or zip).
2. Double-click the included script:
   ```text
   build_windows.bat
   ```
3. It will automatically:
   - Create a Python virtual environment.
   - Install `PySide6` and `PyInstaller`.
   - Compile a standalone single-file `Kn Fitness Pro.exe` with the fitness app icon!
4. You will find your ready-to-use application in:
   ```text
   dist\Kn Fitness Pro.exe
   ```
   You can send this `.exe` to any Windows computer and it will run without needing Python installed!

---

## 3. 🍎 Use on macOS Computers

### Running via Python:
```bash
source .venv/bin/activate
python app.py
```

### Building the macOS `.app`:
```bash
pyinstaller "Kn Health Check.spec" --clean --noconfirm
```
The resulting `.app` is located in `dist/Kn Health Check.app`.

> **Note for other Macs**: If you transfer the `.app` to another Mac and macOS Gatekeeper displays *"App is damaged and can't be opened"*, open Terminal on that Mac and run:
> ```bash
> xattr -cr "/path/to/Kn Health Check.app"
> ```

---

## 4. 💻 Screen Scaling & Resolution Fixes

The desktop app (`app.py`) has been upgraded with:
- **Universal Scrolling (`QScrollArea`)**: Window elements will never be pushed off-screen or cut off on small laptop displays (1366×768 or 720p).
- **Adaptive 2-Column Layout**: Input parameters on the left, instant results and workout tables on the right.
- **High-DPI Scaling Support**: Crisp text and sharp borders on Retina displays and Windows laptops with 125% or 150% scaling.

---

## 5. 🏋️ Complete Workout Database

All goals now include full 4-Day structured workout routines:
- **Build Muscle**: Hypertrophy splits (Chest & Triceps, Back & Biceps, Legs, Shoulders & Abs).
- **Lose Weight**: High-energy circuits (Cardio + HIIT intervals, bodyweight circuits, core, metabolic conditioning).
- **Maintain Weight**: Functional strength and aerobic balance (Full body, functional mobility, upper/lower tone).

