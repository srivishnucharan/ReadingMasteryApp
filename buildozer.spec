[app]

title = Reading Mastery
package.name = readingmastery
package.domain = org.reading
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json,db,pdf
version = 0.1

# Fixed requirements - Kivy 2.3.0 and kivymd without version
requirements = python3,kivy==2.3.0,android,pillow,pyjnius,kivymd

# CRITICAL: Use master branch which has libffi fixes for newer systems
p4a.branch = master

orientation = portrait
fullscreen = 0

android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE
android.api = 31
android.minapi = 21

# CRITICAL FIX: Force NDK r25b (not r28c which has libffi issues)
android.ndk = 25b

android.archs = arm64-v8a,armeabi-v7a
android.accept_sdk_license = True

[buildozer]

log_level = 2
warn_on_root = 1
