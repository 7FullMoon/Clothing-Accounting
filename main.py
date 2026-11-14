
# -*- coding: utf-8 -*-
"""
النظام المحاسبي لمحل بيع الملابس
المرحلة الأولى: واجهة عربية واختبار قاعدة SQLite.
"""

import os
import sqlite3

from kivy.app import App
from kivy.core.window import Window
from kivy.metrics import dp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.scrollview import ScrollView

# معالجة تشكيل الحروف العربية واتجاه الكتابة
try:
    import arabic_reshaper
    from bidi.algorithm import get_display

    def rtl(text):
        return get_display(arabic_reshaper.reshape(str(text)))

except ImportError:
    def rtl(text):
        return str(text)


APP_TITLE = "النظام المحاسبي لمحل الملابس"

FONT_PATH = os.path.join(
    os.path.dirname(__file__),
    "assets",
    "fonts",
    "NotoSansArabic-Regular.ttf"
)


def arabic_font():
    if os.path.isfile(FONT_PATH):
        return FONT_PATH
    return "Roboto"


class ClothingAccountingApp(App):

    title = APP_TITLE

    def build(self):
        Window.clearcolor = (0.95, 0.96, 0.98, 1)

        self.db_path = os.path.join(
            self.user_data_dir,
            "clothing_accounting.db"
        )

        database_ok = self.check_database()

        root = BoxLayout(
            orientation="vertical",
            padding=dp(14),
            spacing=dp(10)
        )

        scroll = ScrollView()
        content = BoxLayout(
            orientation="vertical",
            spacing=dp(12),
            size_hint_y=None
        )
        content.bind(
            minimum_height=content.setter("height")
        )

        header = Label(
            text=rtl(APP_TITLE),
            font_name=arabic_font(),
            font_size="22sp",
            bold=True,
            color=(0.10, 0.16, 0.25, 1),
            size_hint_y=None,
            height=dp(65),
            halign="right",
            valign="middle"
        )
        header.bind(
            size=lambda obj, value:
            setattr(obj, "text_size", value)
        )
        content.add_widget(header)

        subtitle = Label(
            text=rtl(
                "إدارة الحسابات والمبيعات والمشتريات والمخزون"
            ),
            font_name=arabic_font(),
            font_size="14sp",
            color=(0.30, 0.35, 0.42, 1),
            size_hint_y=None,
            height=dp(45),
            halign="right",
            valign="middle"
        )
        subtitle.bind(
            size=lambda obj, value:
            setattr(obj, "text_size", value)
        )
        content.add_widget(subtitle)

        sections = [
            "الحسابات",
            "المبيعات",
            "المشتريات",
            "المخزون والأصناف",
            "العملاء والموردون",
            "التقارير المالية",
            "الإعدادات"
        ]

        for section in sections:
            button = Button(
                text=rtl(section),
                font_name=arabic_font(),
                font_size="17sp",
                size_hint_y=None,
                height=dp(55),
                background_normal="",
                background_color=(0.12, 0.30, 0.52, 1),
                color=(1, 1, 1, 1)
            )

            button.bind(
                on_release=lambda instance, name=section:
                self.show_section(name)
            )

            content.add_widget(button)

        status_text = (
            "SQLite: متصل بنجاح"
            if database_ok
            else "تعذر الاتصال بقاعدة البيانات"
        )

        status = Label(
            text=rtl(status_text),
            font_name=arabic_font(),
            font_size="13sp",
            color=(0.10, 0.45, 0.25, 1),
            size_hint_y=None,
            height=dp(45),
            halign="right",
            valign="middle"
        )
        status.bind(
            size=lambda obj, value:
            setattr(obj, "text_size", value)
        )

        content.add_widget(status)

        scroll.add_widget(content)
        root.add_widget(scroll)

        return root

    def check_database(self):
        """اختبار اتصال SQLite دون إنشاء جداول محاسبية بعد."""

        try:
            connection = sqlite3.connect(self.db_path)
            connection.execute("SELECT sqlite_version()")
            connection.close()
            return True

        except sqlite3.Error:
            return False

    def show_section(self, section_name):

        message = (
            f"قسم {section_name}\n"
            "سيتم بناء وظائف هذا القسم "
            "وربطه بقاعدة البيانات لاحقاً."
        )

        popup = Popup(
            title=rtl("قيد التجهيز"),
            content=Label(
                text=rtl(message),
                font_name=arabic_font(),
                halign="center",
                valign="middle"
            ),
            size_hint=(0.88, 0.35)
        )

        popup.open()


if __name__ == "__main__":
    ClothingAccountingApp().run()

