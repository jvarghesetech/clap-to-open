# 👏 Clap to Open

> Clap twice and your day starts like magic ✨

Clap your hands twice and this script automatically opens:
- 🤖 **Claude** — desktop app
- 📚 **Google Classroom** — in Safari
- 💬 **ChatGPT** — in Safari

No clicking, no searching, no typing. Just two claps and you're ready to go.

Inspired by [two_claps_open](https://github.com/Yutarop/two_claps_open) — built for students who want a magical start to their day.

---

## 🖥️ Requirements

- Mac (macOS)
- Python 3
- Safari browser
- Claude desktop app installed

---

## ⚙️ Setup (do this once)

**Step 1 — Install Homebrew** (if you don't have it):
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```
When it finishes, run:
```bash
echo 'eval "$(/opt/homebrew/bin/brew shellenv zsh)"' >> /Users/$(whoami)/.zprofile && eval "$(/opt/homebrew/bin/brew shellenv zsh)"
```

**Step 2 — Install portaudio** (needed for microphone access):
```bash
brew install portaudio
```

**Step 3 — Install Python dependencies:**
```bash
pip3 install pyaudio numpy scipy
```

**Step 4 — Download the script:**

Download `clap_to_open.py` from this repo and save it to your Desktop.

---

## ▶️ How to run it

Open Terminal (`Cmd + Space` → type Terminal → Enter) and run:
```bash
python3 ~/Desktop/clap_to_open.py
```

You'll see:
```
🎤 Listening — clap TWICE loudly! (Ctrl+C to quit)
```

Now **clap twice** 👏👏 and watch the magic happen!

---

## 🛑 How to stop it

Press `Ctrl + C` in Terminal.

---

## 💡 Tips

- Clap **loud and sharp** — the mic needs to hear a real clap
- Two claps need to happen within **2 seconds** of each other
- First time running: Mac will ask for **microphone permission** — click Allow
- To run it again another day, just open Terminal and run the same command

---

## 🪄 What happens when you clap twice

1. Claude desktop app opens
2. Safari opens with Google Classroom
3. ChatGPT opens as a second tab in Safari

Perfect for students starting their school day! 🎒
