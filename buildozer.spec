
[app]

# اسم التطبيق
title = النظام المحاسبي لمحل الملابس

# معرّف التطبيق
package.name = clothingaccounting
package.domain = org.sevenfullmoon

# مجلد ملفات المشروع
source.dir = .

# أنواع الملفات التي يجب تضمينها
source.include_exts = py,kv,png,jpg,jpeg,ttf,atlas,json

# إصدار التطبيق
version = 0.1.0

# مكتبات التطبيق
requirements = python3,kivy,arabic-reshaper,python-bidi

# اتجاه الشاشة
orientation = portrait

# عدم تشغيل التطبيق بملء الشاشة
fullscreen = 0

# إعدادات Android
android.minapi = 23
android.archs = arm64-v8a, armeabi-v7a

# استخدام SDL2 لتشغيل Kivy
p4a.bootstrap = sdl2
p4a.branch = develop

# إعدادات Buildozer
[buildozer]
log_level = 2
warn_on_root = 1
