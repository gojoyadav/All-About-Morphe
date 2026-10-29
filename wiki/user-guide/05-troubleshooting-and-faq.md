# Wiki: User Guide — Chapter 5: Troubleshooting & FAQ

## 🚨 Top Issues & Step-by-Step Fixes

---

### 1. YouTube Video Stops & Buffers Indefinitely at 1:00 or 1:30
- **The Cause:** YouTube's Botguard anti-bot system is challenging your client because it lacks a valid **Proof of Origin Token (PoToken)** or is using an obsolete client identifier.
- **The Solution:**
  1. Open your patched YouTube app $\rightarrow$ tap **Settings** $\rightarrow$ **Morphe Settings** $\rightarrow$ **Misc**.
  2. Ensure **Spoof Video Streams** (or **Client Spoof**) is enabled.
  3. Select client spoof target: **Android VR** or **iOS**.
  4. Ensure `PotHelper` / PoToken support is enabled.
  5. Restart the YouTube app. Playback will stream continuously without buffering.

---

### 2. "App not installed as package conflicts with an existing package"
- **The Cause:** You are trying to install a non-root patched app that has the same package name as the official Google app already installed on your device, or the signatures do not match.
- **The Solution:**
  - When patching non-root YouTube, **make sure the `MicroG Support` patch is checked**. This automatically changes the package name to `app.morphe.android.youtube`, allowing it to install side-by-side with stock YouTube.
  - If you previously uninstalled a previous Morphe build and see this error, ensure the old app is completely removed for **All Users** (Settings $\rightarrow$ Apps $\rightarrow$ YouTube $\rightarrow$ Uninstall for all users).

---

### 3. Push Notifications Not Arriving for Subscriptions / Comments
- **The Cause:** Android's OEM battery saver has placed MicroG-RE into deep sleep, terminating its persistent FCM (Firebase Cloud Messaging) heartbeat socket.
- **The Solution:**
  1. Open **MicroG Services** from your app drawer.
  2. Tap **Cloud Messaging**.
  3. Tap the three dots $\rightarrow$ **Advanced** $\rightarrow$ set **Heartbeat Interval** to **Automatic** or **Manual (60s)**.
  4. Ensure MicroG is exempted from OEM battery optimization (see [Chapter 2](02-microg-and-account-setup.md)).

---

### 4. YouTube Music Missing in Android Auto Car Dashboard
- **The Cause:** Android Auto rejects third-party media apps whose cryptographic certificates are not signed by Google or certified OEMs.
- **The Solution:**
  1. In Morphe Manager, ensure the **`Android Auto`** patch was selected when patching YouTube Music.
  2. On your phone, open **Settings** $\rightarrow$ **Apps** $\rightarrow$ **Android Auto**.
  3. Scroll down and tap **Version** 10 times until **Developer mode** is enabled.
  4. Tap the three dots (top right) $\rightarrow$ **Developer settings**.
  5. Check **Unknown sources** to allow modified media apps on your car's head unit.

---

### 5. Patching Crashes Midway with "OutOfMemoryError"
- **The Cause:** The target APK is massive (150MB+) and your device has 3GB or 4GB RAM, causing the Android OS to terminate Morphe Manager.
- **The Solution:**
  1. In Morphe Manager $\rightarrow$ **Settings** $\rightarrow$ **Patcher Engine**:
     - Ensure **Lazy Resource Decoding** is toggled **ON** (enabled by default in Morphe Patcher 2.0).
     - Reduce parallel worker threads to `1` or `2`.
  2. Close background apps before initiating the patch.
  3. Alternatively, use [**Morphe Desktop**](02-morphe-desktop.md) on your PC to patch the APK in 5 seconds and transfer it to your phone.
