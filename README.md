# StudyRing for Android

These files let GitHub build the StudyRing app (an APK) for you, free, in about 10 minutes. You can do every step from your phone's browser.

The app rings at the start of each study slot, even when it is closed.

## What you need
- A free GitHub account (github.com)
- The 5 files from this chat: index.html, package.json, capacitor.config.json, make_icons.py, build.yml

## Steps

1. **Create a repository.** On github.com tap the + button, then New repository. Name it `studyring`. Keep it Private if you like. Tap Create repository.

2. **Upload four files.** In the new repository tap Add file, then Upload files. Choose these four from your Downloads: `index.html`, `package.json`, `capacitor.config.json`, `make_icons.py`. Tap Commit changes.

3. **Add the build file.** Tap Add file, then Create new file. In the name box type exactly `.github/workflows/build.yml` (typing a slash makes the folders). Open `build.yml` from this chat, copy all of it, paste it into the big box, and tap Commit changes.

4. **Wait for the build.** Tap the Actions tab. A run called "Build StudyRing APK" starts by itself and takes about 10 minutes. A green tick means it worked. If it does not start, tap "Build StudyRing APK" on the left, then Run workflow.

5. **Download the app.** Tap the finished run. Scroll to Artifacts and tap `StudyRing-apk`. You get a zip. Open it with your Files app, extract it, and tap `StudyRing.apk`.

6. **Install.** Android asks to allow installs from your browser or Files app. Allow it once, then tap Install.

7. **Allow alarms.** Open StudyRing. When it asks to send notifications, tap Allow. In Settings, the Alarms card should say alarms are on.

## If an alarm comes late
Open the phone's Settings, then Apps, then StudyRing, then Battery, and choose Unrestricted. Some phone brands (Xiaomi, Realme, Oppo, Vivo) also have an "Autostart" setting that should be on.

## Notes
- Your timetable is saved inside the app on your phone. It does not sync with the Claude web version.
- The photo scan feature is only in the Claude web version.
- This is a debug build for your own use, not a Play Store release.
