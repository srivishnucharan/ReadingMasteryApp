[app]
title = Reading Mastery
package.name = readingmastery
package.domain = org.reading.mastery
source.dir = .
# CRITICAL: Include 'pdf' so your books are bundled!
source.include_exts = py,png,jpg,kv,atlas,pdf
version = 0.1

# Ensure these match your app's dependencies
requirements = python3, kivy==2.3.0, kivymd==1.2.0, pillow

orientation = portrait
fullscreen = 0
android.archs = arm64-v8a, armeabi-v7a
android.accept_sdk_license = True

[buildozer]
log_level = 2
warn_on_root = 1
