[app]
title = XHunter Myanmar
package.name = xhunter
package.domain = org.ryan
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,ttf
version = 1.0.0
requirements = python3, kivy
orientation = portrait
fullscreen = 1
android.archs = arm64-v8a, armeabi-v7a
android.api = 31
android.minapi = 21
android.accept_sdk_license = True
android.permissions = INTERNET, ACCESS_WIFI_STATE, ACCESS_NETWORK_STATE

[buildozer]
log_level = 2
warn_on_root = 1
