[app]
title = Reading Mastery
package.name = readingmastery
package.domain = org.srivishnu

source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json,ttf

version = 0.1

requirements = python3,kivy==2.2.1,kivymd==1.1.1,pillow,pyjnius

orientation = portrait
fullscreen = 0

icon.filename = %(source.dir)s/icon.png
presplash.filename = %(source.dir)s/presplash.png

log_level = 2

[buildozer]
log_level = 2
warn_on_root = 1

[app:android]
bootstrap = sdl2

android.api = 33
android.minapi = 21
android.ndk = 25b

android.archs = arm64-v8a, armeabi-v7a

android.permissions = INTERNET

android.allow_backup = True
android.debuggable = True

android.gradle_dependencies =
android.enable_androidx = True

android.add_src =

android.copy_libs = True

android.accept_sdk_license = True

android.use_leakcanary = False

[app:android.gradle]
# Leave empty – buildozer handles this

[app:android.activity]
orientation = portrait

[app:android.meta_data]