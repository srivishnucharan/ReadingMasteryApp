[app]
title = Reading Mastery
package.name = readingmastery
package.domain = org.test

# Include .pdf extension
source.include_exts = py,png,jpg,kv,atlas,pdf
source.include_patterns = assets/*

# Requirements for KivyMD
requirements = python3,kivy==2.3.0,kivymd==1.2.0,pillow

# Necessary for Android file access
android.permissions = READ_EXTERNAL_STORAGE, WRITE_EXTERNAL_STORAGE

# Android API levels
android.api = 33
android.minapi = 21