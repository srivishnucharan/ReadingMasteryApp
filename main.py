import webbrowser
import time
import json
import os
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.properties import StringProperty, ListProperty, NumericProperty
from kivymd.uix.list import TwoLineAvatarIconListItem, IRightBodyTouch, OneLineIconListItem, IconLeftWidget
from kivymd.uix.selectioncontrol import MDCheckbox
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton, MDRaisedButton
from kivymd.uix.label import MDLabel
from kivy.clock import Clock 
from kivy.uix.boxlayout import BoxLayout
import backend 

# --- CUSTOM WIDGETS ---

class RightCheckbox(IRightBodyTouch, MDCheckbox):
    pass

class LoginScreen(Screen):
    def process_login(self):
        name = self.ids.user_name.text
        if name.strip():
            app = MDApp.get_running_app()
            app.first_name = name.split()[0]
            self.manager.current = 'welcome'

class WelcomeScreen(Screen):
    pass

class ChildrenBooksScreen(Screen):
    pass

class AgeSelectionScreen(Screen):
    pass

class LevelSelectionScreen(Screen):
    pass

class GenreSelection(Screen):
    pass

class BookListScreen(Screen):
    category_title = StringProperty("")

class Dashboard(Screen):
    points = NumericProperty(0)
    earned_certificates = ListProperty([])
    
    def show_content(self, section, cert_data=None):
        content = self.ids.content_pane
        content.clear_widgets()
        app = MDApp.get_running_app()
        
        if section == "test":
            test_box = Builder.load_string('''
MDBoxLayout:
    orientation: 'vertical'
    spacing: "20dp"
    padding: "20dp"
    MDLabel:
        id: timer_display
        text: app.timer_text
        halign: "center"
        font_style: "H4"
        theme_text_color: "Primary"
        size_hint_y: None
        height: self.texture_size[1]
    MDLabel:
        id: passage_label
        text: "Reading books is one of the most beneficial and enriching habits one can cultivate, acting as a gateway to knowledge, imagination, and personal growth. Beyond just providing entertainment, diving into a book stimulates the brain, strengthens memory, and improves focus while offering a healthy mental escape that reduces stress."
        halign: "center"
        valign: "center"
        italic: True
        theme_text_color: "Secondary"
        adaptive_height: True
        pos_hint: {"center_x": .5}
    MDBoxLayout:
        orientation: 'horizontal'
        spacing: "15dp"
        size_hint: None, None
        width: self.minimum_width
        pos_hint: {"center_x": .5}
        MDRaisedButton:
            text: "TAKE TEST"
            md_bg_color: 0.15, 0.18, 0.45, 1
            on_release: app.start_speed_test(passage_label.text)
        MDRaisedButton:
            id: done_btn
            text: "I AM FINISHED"
            disabled: True
            md_bg_color: 0.85, 0.65, 0.13, 1
            on_release: app.stop_speed_test()
''')
            content.add_widget(test_box)
            
        elif section == "points":
            content.add_widget(MDLabel(
                text="Total Points: " + str(self.points),
                halign="center",
                font_style="H4",
                theme_text_color="Custom",
                text_color=(0.15, 0.18, 0.45, 1)
            ))
            
        elif section == "certificate":
            # UPDATED CERTIFICATE LAYOUT: Centered Header & Larger Font
            cert_layout = Builder.load_string(f'''
MDBoxLayout:
    orientation: 'vertical'
    padding: "30dp"
    md_bg_color: 1, 1, 1, 1
    line_color: 0.15, 0.18, 0.45, 1
    line_width: 2
    radius: [20,]
    spacing: "15dp"
    
    MDBoxLayout:
        orientation: 'horizontal'
        adaptive_size: True
        spacing: "15dp"
        pos_hint: {{"center_x": .5}}
        MDIcon:
            icon: "school"
            font_size: "48sp"
            theme_text_color: "Custom"
            text_color: 0.85, 0.65, 0.13, 1
            size_hint: None, None
            size: "48dp", "48dp"
            pos_hint: {{"center_y": .5}}
        MDLabel:
            text: "CERTIFICATE OF MASTERY"
            font_style: "H5"
            bold: True
            theme_text_color: "Custom"
            text_color: 0.15, 0.18, 0.45, 1
            adaptive_size: True
            pos_hint: {{"center_y": .5}}

    MDLabel:
        text: "This is to certify that"
        halign: "center"
        font_style: "Caption"
        theme_text_color: "Secondary"
        
    MDLabel:
        text: "{app.first_name}"
        halign: "center"
        font_style: "H4"
        bold: True
        theme_text_color: "Primary"
        
    MDLabel:
        text: "has successfully graduated the {app.user_level} level"
        halign: "center"
        font_style: "Body1"
        
    MDLabel:
        text: "We congratulate you for your dedication and consistency!"
        halign: "center"
        italic: True
        font_style: "Caption"
        theme_text_color: "Secondary"
        
    Widget:
        size_hint_y: None
        height: "30dp"
        
    MDBoxLayout:
        orientation: 'vertical'
        size_hint_y: None
        height: "80dp"
        spacing: "5dp"
        canvas.before:
            Color:
                rgba: 0.15, 0.18, 0.45, 1
            Line:
                points: self.x + 40, self.y + 65, self.right - 40, self.y + 65
                width: 1
        MDLabel:
            text: "Certified By"
            halign: "center"
            font_style: "Caption"
            theme_text_color: "Secondary"
        MDLabel:
            text: "Reading Mastery"
            halign: "center"
            bold: True
            theme_text_color: "Custom"
            text_color: 0.15, 0.18, 0.45, 1
''')
            content.add_widget(cert_layout)

KV = '''
<NavigationToolbar@MDTopAppBar>:
    title: "READING MASTERY \\n[size=10sp]Your Personal Reading Coach[/size]"
    left_action_items: [["arrow-left", lambda x: app.go_back()]]
    right_action_items: [["home", lambda x: app.go_home()], ["view-dashboard", lambda x: app.go_dashboard()], ["logout", lambda x: app.logout()]]
    md_bg_color: 0.15, 0.18, 0.45, 1

<Screen>:
    canvas.before:
        Color:
            rgba: 0.96, 0.97, 1, 1
        Rectangle:
            pos: self.pos
            size: self.size

ScreenManager:
    LoginScreen:
    WelcomeScreen:
    ChildrenBooksScreen:
    AgeSelectionScreen:
    LevelSelectionScreen:
    GenreSelection:
    BookListScreen:
    Dashboard:

<LoginScreen>:
    name: 'login'
    MDBoxLayout:
        orientation: 'vertical'
        padding: "40dp"
        spacing: "20dp"
        MDBoxLayout:
            orientation: 'vertical'
            adaptive_height: True
            pos_hint: {"center_x": .5}
            spacing: "12dp"
            MDGridLayout:
                cols: 2
                adaptive_size: True
                pos_hint: {"center_x": .5}
                spacing: "20dp"
                MDIcon:
                    icon: "book-open-page-variant"
                    font_size: "96sp"
                    theme_text_color: "Custom"
                    text_color: 0.15, 0.18, 0.45, 1
                    size_hint: None, None
                    size: "96dp", "96dp"
                    pos_hint: {"center_y": .5}
                MDBoxLayout:
                    orientation: 'vertical'
                    adaptive_size: True
                    pos_hint: {"center_y": .5}
                    spacing: "-8dp"
                    MDLabel:
                        text: "READING"
                        font_style: "H4"
                        bold: True
                        theme_text_color: "Custom"
                        text_color: 0.15, 0.18, 0.45, 1
                        adaptive_size: True
                    MDLabel:
                        text: "MASTERY"
                        font_style: "H4"
                        bold: True
                        theme_text_color: "Custom"
                        text_color: 0.15, 0.18, 0.45, 1
                        adaptive_size: True
            MDLabel:
                text: "Your Personal Reading Coach"
                halign: "center"
                font_style: "Subtitle2"
                theme_text_color: "Custom"
                text_color: 0.85, 0.65, 0.13, 1 
                adaptive_height: True
                bold: True
        Widget:
            size_hint_y: None
            height: "40dp"
        MDTextField:
            id: user_name
            hint_text: "Enter your name"
            mode: "rectangle"
            size_hint_x: 0.85
            pos_hint: {"center_x": .5}
            line_color_focus: 0.15, 0.18, 0.45, 1
        MDRaisedButton:
            text: "LOG IN"
            size_hint_x: 0.85
            pos_hint: {"center_x": .5}
            on_release: root.process_login()
            md_bg_color: 0.15, 0.18, 0.45, 1
        Widget:

<WelcomeScreen>:
    name: 'welcome'
    MDBoxLayout:
        orientation: 'vertical'
        NavigationToolbar:
            left_action_items: []
        MDBoxLayout:
            orientation: 'vertical'
            padding: "40dp"
            spacing: "20dp"
            MDLabel:
                text: "Welcome back, " + app.first_name + "!"
                font_style: "H4"
                halign: "center"
                theme_text_color: "Custom"
                text_color: 0.15, 0.18, 0.45, 1
            MDBoxLayout:
                orientation: 'horizontal'
                spacing: "15dp"
                size_hint_y: None
                height: "60dp"
                MDRaisedButton:
                    text: "CONTINUE JOURNEY"
                    size_hint_x: 0.5
                    md_bg_color: 0.15, 0.18, 0.45, 1
                    on_release: root.manager.current = 'age_selection'
                MDRaisedButton:
                    text: "CHILDREN'S BOOKS"
                    size_hint_x: 0.5
                    md_bg_color: 0.85, 0.65, 0.13, 1
                    on_release: root.manager.current = 'children_books'
            Widget:

<ChildrenBooksScreen>:
    name: 'children_books'
    MDBoxLayout:
        orientation: 'vertical'
        NavigationToolbar:
            title: "Children's Library"
        ScrollView:
            MDList:
                OneLineIconListItem:
                    text: "Hide & Seek (Click to Open)"
                    on_release: app.open_local_pdf("001-HIDE-AND-SEEK.pdf")
                    IconLeftWidget:
                        icon: "file-pdf-box"
                        theme_text_color: "Custom"
                        text_color: 0.85, 0.65, 0.13, 1
                OneLineIconListItem:
                    text: "Sunny Medows Woodland School (Click to Open)"
                    on_release: app.open_local_pdf("002-SUNNY-MEADOWS-WOODLAND-SCHOOL.pdf")
                    IconLeftWidget:
                        icon: "file-pdf-box"
                        theme_text_color: "Custom"
                        text_color: 0.85, 0.65, 0.13, 1
                OneLineIconListItem:
                    text: "Hammy the Hamster (Click to Open)"
                    on_release: app.open_local_pdf("003-HAMMY-THE-HAMSTER.pdf")
                    IconLeftWidget:
                        icon: "file-pdf-box"
                        theme_text_color: "Custom"
                        text_color: 0.85, 0.65, 0.13, 1       
                OneLineIconListItem:
                    text: "The Class of the Missing Smile (Click to Open)"
                    on_release: app.open_local_pdf("004-THE-CASE-OF-THE-MISSING-SMILE.pdf")
                    IconLeftWidget:
                        icon: "file-pdf-box"
                        theme_text_color: "Custom"
                        text_color: 0.85, 0.65, 0.13, 1       
                OneLineIconListItem:
                    text: "Captain Fantastic (Click to Open)"
                    on_release: app.open_local_pdf("005-CAPTAIN-FANTASTIC.pdf")
                    IconLeftWidget:
                        icon: "file-pdf-box"
                        theme_text_color: "Custom"
                        text_color: 0.85, 0.65, 0.13, 1                  

<AgeSelectionScreen>:
    name: 'age_selection'
    MDBoxLayout:
        orientation: 'vertical'
        NavigationToolbar:
        MDBoxLayout:
            orientation: 'vertical'
            padding: "20dp"
            spacing: "15dp"
            MDLabel:
                text: "Step 1: Choose Age Group"
                halign: "center"
                font_style: "H6"
                theme_text_color: "Custom"
                text_color: 0.15, 0.18, 0.45, 1
            MDRaisedButton:
                text: "8-10 Years"
                size_hint_x: 0.8
                pos_hint: {"center_x": .5}
                md_bg_color: 0.15, 0.18, 0.45, 1
                on_release: app.set_age("8-10")
            MDRaisedButton:
                text: "11-14 Years"
                size_hint_x: 0.8
                pos_hint: {"center_x": .5}
                md_bg_color: 0.15, 0.18, 0.45, 1
                on_release: app.set_age("11-14")
            MDRaisedButton:
                text: "15-21 Years"
                size_hint_x: 0.8
                pos_hint: {"center_x": .5}
                md_bg_color: 0.15, 0.18, 0.45, 1
                on_release: app.set_age("15-21")
            MDRaisedButton:
                text: "Above 21"
                size_hint_x: 0.8
                pos_hint: {"center_x": .5}
                md_bg_color: 0.15, 0.18, 0.45, 1
                on_release: app.set_age("Above 21")

<LevelSelectionScreen>:
    name: 'level_selection'
    MDBoxLayout:
        orientation: 'vertical'
        NavigationToolbar:
        MDBoxLayout:
            orientation: 'vertical'
            padding: "20dp"
            spacing: "15dp"
            MDLabel:
                text: "Step 2: Choose Proficiency"
                halign: "center"
                font_style: "H6"
                theme_text_color: "Custom"
                text_color: 0.15, 0.18, 0.45, 1
            MDRaisedButton:
                text: "Novice"
                size_hint_x: 0.8
                pos_hint: {"center_x": .5}
                md_bg_color: 0.15, 0.18, 0.45, 1
                on_release: app.set_level("Novice")
            MDRaisedButton:
                text: "Intermediate"
                size_hint_x: 0.8
                pos_hint: {"center_x": .5}
                md_bg_color: 0.15, 0.18, 0.45, 1
                on_release: app.set_level("Intermediate")
            MDRaisedButton:
                text: "Advanced"
                size_hint_x: 0.8
                pos_hint: {"center_x": .5}
                md_bg_color: 0.15, 0.18, 0.45, 1
                on_release: app.set_level("Advanced")

<GenreSelection>:
    name: 'genre_selection'
    MDBoxLayout:
        orientation: 'vertical'
        NavigationToolbar:
        ScrollView:
            MDGridLayout:
                id: genre_grid
                cols: 2
                padding: "20dp"
                spacing: "20dp"
                adaptive_height: True

<BookListScreen>:
    name: 'book_list'
    MDBoxLayout:
        orientation: 'vertical'
        NavigationToolbar:
            title: root.category_title
        ScrollView:
            MDList:
                id: book_list
        MDBoxLayout:
            size_hint_y: None
            height: "80dp"
            padding: "10dp"
            MDRaisedButton:
                id: submit_btn
                text: "COMPLETE LEVEL"
                pos_hint: {"center_x": .5}
                disabled: True
                md_bg_color: 0.85, 0.65, 0.13, 1
                on_release: app.graduation_popup()

<Dashboard>:
    name: 'dashboard'
    MDBoxLayout:
        orientation: 'vertical'
        NavigationToolbar:
        MDBoxLayout:
            orientation: 'horizontal'
            MDCard:
                size_hint_x: 0.4
                elevation: 2
                MDBoxLayout:
                    orientation: 'vertical'
                    MDLabel:
                        text: "PROGRESS"
                        halign: "center"
                        size_hint_y: None
                        height: "40dp"
                        bold: True
                        theme_text_color: "Custom"
                        text_color: 0.15, 0.18, 0.45, 1
                    MDList:
                        OneLineIconListItem:
                            text: "Speed Test"
                            on_release: root.show_content("test")
                            IconLeftWidget:
                                icon: "timer"
                                theme_text_color: "Custom"
                                text_color: 0.85, 0.65, 0.13, 1
                        OneLineIconListItem:
                            text: "Points"
                            on_release: root.show_content("points")
                            IconLeftWidget:
                                icon: "numeric"
                                theme_text_color: "Custom"
                                text_color: 0.85, 0.65, 0.13, 1
                    MDSeparator:
                    MDLabel:
                        text: "MY BADGES"
                        halign: "center"
                        size_hint_y: None
                        height: "40dp"
                        bold: True
                    ScrollView:
                        MDList:
                            id: badge_list
                            OneLineIconListItem:
                                text: "Novice Shield"
                                IconLeftWidget:
                                    icon: "shield-star"
                                    theme_text_color: "Custom"
                                    text_color: 0.85, 0.65, 0.13, 1
                            OneLineIconListItem:
                                text: "Master Reader"
                                IconLeftWidget:
                                    icon: "trophy-variant"
                                    theme_text_color: "Custom"
                                    text_color: 0.85, 0.65, 0.13, 1
                    MDSeparator:
                    MDLabel:
                        text: "CERTIFICATES"
                        halign: "center"
                        size_hint_y: None
                        height: "40dp"
                        bold: True
                    ScrollView:
                        MDList:
                            id: cert_gallery
            MDBoxLayout:
                id: content_pane
                orientation: 'vertical'
                padding: "20dp"
                spacing: "10dp"
                MDBoxLayout:
                    orientation: 'vertical'
                    size_hint_y: None
                    height: "60dp"
                    MDLabel:
                        text: "Overall Reading Progress"
                        theme_text_color: "Secondary"
                        font_style: "Caption"
                    MDProgressBar:
                        value: (root.points / 500) * 100 if root.points <= 500 else 100
                        color: 0.85, 0.65, 0.13, 1
                MDLabel:
                    text: "Select a module to view progress"
                    halign: "center"
                    theme_text_color: "Secondary"
'''

class ReadingMasteryApp(MDApp):
    user_age = StringProperty("")
    user_level = StringProperty("")
    first_name = StringProperty("Reader")
    timer_text = StringProperty("00:00")
    total_books = NumericProperty(0)
    checked_count = NumericProperty(0)
    start_time = 0
    timer_event = None
    dialog = None

    def build(self):
        self.theme_cls.primary_palette = "Indigo"
        return Builder.load_string(KV)

    def open_local_pdf(self, filename):
        # Use os.path.dirname(__file__) to find the folder regardless of OS
        base_path = os.path.dirname(__file__)
        # Use this for Android/Linux compatibility
        assets_path = os.path.join(os.path.dirname(__file__), "assets")
        
        filepath = os.path.join(assets_path, filename)
        if os.path.exists(filepath):
            webbrowser.open(filepath)
        else:
            self.dialog = MDDialog(
                title="File Not Found",
                text=f"Cannot find {filename} in assets folder.",
                buttons=[MDFlatButton(text="OK", on_release=lambda x: self.dialog.dismiss())]
            )
            self.dialog.open()

    def start_speed_test(self, passage):
        self.current_passage = passage
        self.start_time = time.time()
        content = self.root.get_screen('dashboard').ids.content_pane
        for child in content.children:
            if hasattr(child, 'ids') and 'done_btn' in child.ids:
                child.ids.done_btn.disabled = False
        if self.timer_event:
            Clock.unschedule(self.timer_event)
        self.timer_event = Clock.schedule_interval(self.update_timer, 0.1)

    def update_timer(self, dt):
        elapsed = time.time() - self.start_time
        mins, secs = divmod(int(elapsed), 60)
        self.timer_text = f"{mins:02}:{secs:02}"

    def stop_speed_test(self):
        if self.timer_event:
            Clock.unschedule(self.timer_event)
            self.timer_event = None
        word_count = len(self.current_passage.split())
        elapsed_mins = (time.time() - self.start_time) / 60
        wpm = round(word_count / elapsed_mins) if elapsed_mins > 0 else 0
        self.dialog = MDDialog(
            title="Results",
            text=f"Great job! You read at {wpm} Words Per Minute.",
            buttons=[MDFlatButton(text="OK", text_color=(0.15, 0.18, 0.45, 1), on_release=lambda x: self.dialog.dismiss())]
        )
        self.dialog.open()

    def on_checkbox_active(self, checkbox, value):
        if value:
            self.checked_count += 1
        else:
            self.checked_count -= 1
        btn = self.root.get_screen('book_list').ids.submit_btn
        btn.disabled = (self.checked_count < self.total_books)

    def graduation_popup(self):
        dash = self.root.get_screen('dashboard')
        dash.points += (self.total_books * 10)
        cert_text = (
            f"CERTIFICATE OF MASTERY\n\n"
            f"Awarded to: {self.first_name}\n"
            f"Level: {self.user_level}\n\n"
            f"We congratulate you for your dedication and consistency!\n"
            f"Total Points: {dash.points}"
        )
        dash.earned_certificates.append(cert_text)
        item = OneLineIconListItem(
            text=f"Graduated: {self.user_level}",
            on_release=lambda x: dash.show_content("certificate", cert_text)
        )
        item.add_widget(IconLeftWidget(icon="certificate", theme_text_color="Custom", text_color=(0.85, 0.65, 0.13, 1)))
        dash.ids.cert_gallery.add_widget(item)
        self.dialog = MDDialog(
            title="Level Complete!",
            text=f"Congratulations! You've graduated the {self.user_level} level.",
            buttons=[MDFlatButton(text="VIEW CERTIFICATE", text_color=(0.15, 0.18, 0.45, 1), on_release=self.go_to_cert)]
        )
        self.dialog.open()

    def go_to_cert(self, *args):
        self.dialog.dismiss()
        self.go_dashboard()
        self.root.get_screen('dashboard').show_content("certificate", self.root.get_screen('dashboard').earned_certificates[-1])

    def set_age(self, age):
        self.user_age = age
        self.root.current = 'level_selection'

    def set_level(self, level):
        self.user_level = level
        allowed = backend.get_allowed_genres(self.user_age)
        gs = self.root.get_screen('genre_selection')
        gs.ids.genre_grid.clear_widgets()
        for g in allowed:
            tile_kv = f'''
MDCard:
    orientation: "horizontal"
    size_hint: None, None
    size: "180dp", "80dp"
    padding: "10dp"
    spacing: "10dp"
    radius: 15
    elevation: 2
    on_release: app.show_books("{g}")
    MDIcon:
        icon: "book-open-variant"
        size_hint_x: None
        width: "40dp"
        theme_text_color: "Custom"
        text_color: 0.15, 0.18, 0.45, 1
        pos_hint: {{"center_y": .5}}
    MDLabel:
        text: "{g}"
        bold: True
        valign: "middle"
        halign: "left"
        theme_text_color: "Custom"
        text_color: 0.15, 0.18, 0.45, 1
'''
            gs.ids.genre_grid.add_widget(Builder.load_string(tile_kv))
        self.root.current = 'genre_selection'

    def show_books(self, genre):
        bs = self.root.get_screen('book_list')
        bs.category_title = f"{self.user_level} - {genre}"
        bs.ids.book_list.clear_widgets()
        bs.ids.submit_btn.disabled = True
        books = backend.get_books_for_selection(self.user_age, genre, self.user_level)
        self.total_books = len(books)
        self.checked_count = 0
        for b in books:
            item = TwoLineAvatarIconListItem(
                text=b['title'],
                secondary_text="Buy on Amazon.in",
                on_release=lambda x, url=b['link']: webbrowser.open(url)
            )
            check = RightCheckbox(selected_color=(0.15, 0.18, 0.45, 1))
            check.bind(active=self.on_checkbox_active)
            item.add_widget(check)
            bs.ids.book_list.add_widget(item)
        self.root.current = 'book_list'

    def logout(self): self.root.current = 'login'
    def go_home(self): self.root.current = 'welcome'
    def go_dashboard(self): self.root.current = 'dashboard'
    def go_back(self):
        curr = self.root.current
        if curr == 'book_list': self.root.current = 'genre_selection'
        elif curr == 'genre_selection': self.root.current = 'level_selection'
        elif curr == 'level_selection': self.root.current = 'age_selection'
        elif curr == 'children_books': self.root.current = 'welcome'
        else: self.root.current = 'welcome'

if __name__ == '__main__':

    ReadingMasteryApp().run()




