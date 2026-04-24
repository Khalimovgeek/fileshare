# 📁 Simple File Transfer (Phone ↔ PC)

A lightweight, **zero-dependency** file transfer tool to send files between your phone and computer over a local network.

## 🚀 Why this project?

Many existing solutions:

* Require installing multiple dependencies
* Are unreliable or bloated
* Raise privacy concerns

This project keeps things **simple, transparent, and local**.

---

## ✨ Features

* 🔌 **Zero dependencies** — no `pip install` required
* 🌐 Uses Python’s built-in `http.server` (no FastAPI, Django, etc.)
* 📲 **QR code connection** for easy mobile access
* 🔄 Send & receive files over the same network
* 🔒 Fully local (no external servers involved)

---

## ⚙️ How it works

* Starts a local HTTP server using Python’s built-in libraries
* Detects your system IP
* Generates a QR code to quickly connect from your phone
* Allows file upload/download via browser

---

## 🛠️ Usage

1. Run the project:

```bash
python settings.py
```

2. On startup:

   * The server will start
   * A QR code will be displayed

3. On your phone:

   * Scan the QR code
   * Open the link in your browser

4. Start sending or receiving files 🎉

---

## 📡 Don’t know your IP?

No problem.

Just click the **Send/Receive** button — the app generates a QR code that automatically connects your phone to your computer.

---

## 📦 Tech Stack

* Python (built-in libraries only)

  * `http.server`
  * standard networking utilities

---

## 🎯 Project Goals

* Keep it **minimal**
* Keep it **dependency-free**
* Keep it **reliable and local-first**

---

## ⚠️ Notes

* Works only when both devices are on the **same network**
* Not intended for internet-wide file sharing (local use only)

---
