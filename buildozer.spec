[app]
title = Reading Mastery
package.name = readingmastery
package.domain = org.reading.mastery
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,pdf,json,db
version = 0.1

# Fixed requirements - correct versions and added missing dependencies
requirements = python3,kivy==2.3.0,kivymd==1.1.1,pillow,pyjnius,sqlite3,certifi

# Android-specific settings
orientation = portrait
fullscreen = 0
android.archs = arm64-v8a,armeabi-v7a
android.accept_sdk_license = True

# CRITICAL: Add INTERNET permission for opening URLs
android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

# Specify Android API level
android.api = 31
android.minapi = 21
android.ndk = 25b

# Presplash settings
#presplash.filename = %(source.dir)s/data/presplash.png

# Icon settings
#icon.filename = %(source.dir)s/data/icon.png

[buildozer]
log_level = 2
warn_on_root = 1
