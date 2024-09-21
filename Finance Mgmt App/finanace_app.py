from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window

Window.size = (360, 640)

# Define the home screen
class HomeScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = FloatLayout()
        
        with layout.canvas.before:
            from kivy.graphics import Color, Rectangle
            # Set background color (light green for finance theme)
            Color(0.85, 1, 0.85, 1)  # RGBA values for a soft green color
            self.rect = Rectangle(size=Window.size)

        # Application Name
        app_name = Label(text="My Finance Manager", font_size='20sp', color=(0, 0.3, 0, 1), size_hint=(None, None), size=(300, 50), pos_hint={'center_x': 0.5, 'center_y': 0.7})
        layout.add_widget(app_name)

        # Login Button
        btn_login = Button(text="Login", size_hint=(None, None), size=(200, 50), pos_hint={'center_x': 0.5, 'center_y': 0.5})
        btn_login.bind(on_press=self.go_to_login)
        layout.add_widget(btn_login)

        # Create Account Button
        btn_create_account = Button(text="Create Account", size_hint=(None, None), size=(200, 50), pos_hint={'center_x': 0.5, 'center_y': 0.4})
        btn_create_account.bind(on_press=self.go_to_create_account)
        layout.add_widget(btn_create_account)

        self.add_widget(layout)

    def go_to_login(self, instance):
        self.manager.current = 'login'

    def go_to_create_account(self, instance):
        self.manager.current = 'create_account_step_1'  # Corrected navigation


# Define the create account screen (Step 1)
class CreateAccountScreen1(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = FloatLayout()
        
        with layout.canvas.before:
            from kivy.graphics import Color, Rectangle
            # Set background color (light green for finance theme)
            Color(0.85, 1, 0.85, 1)  # RGBA values for a soft green color
            self.rect = Rectangle(size=Window.size)

        # First Name
        first_name = Label(text="First Name", font_size='12sp', color=(0, 0.3, 0, 1), size_hint=(None, None), size=(100, 30), pos_hint={'center_x': 0.2, 'center_y': 0.8})
        layout.add_widget(first_name)
        self.entry_first_name = TextInput(size_hint=(None, None), size=(200, 30), pos_hint={'center_x': 0.7, 'center_y': 0.8})
        layout.add_widget(self.entry_first_name)

        # Last Name
        last_name = Label(text="Last Name", font_size='12sp', color=(0, 0.3, 0, 1), size_hint=(None, None), size=(100, 30), pos_hint={'center_x': 0.2, 'center_y': 0.7})
        layout.add_widget(last_name)
        self.entry_last_name = TextInput(size_hint=(None, None), size=(200, 30), pos_hint={'center_x': 0.7, 'center_y': 0.7})
        layout.add_widget(self.entry_last_name)

        # Email
        email = Label(text="Email", font_size='12sp', color=(0, 0.3, 0, 1), size_hint=(None, None), size=(100, 30), pos_hint={'center_x': 0.2, 'center_y': 0.6})
        layout.add_widget(email)
        self.entry_email = TextInput(size_hint=(None, None), size=(200, 30), pos_hint={'center_x': 0.7, 'center_y': 0.6})
        layout.add_widget(self.entry_email)

        # Phone Number
        phone_number = Label(text="Phone Number", font_size='12sp', color=(0, 0.3, 0, 1), size_hint=(None, None), size=(100, 30), pos_hint={'center_x': 0.2, 'center_y': 0.5})
        layout.add_widget(phone_number)
        self.entry_phone_number = TextInput(size_hint=(None, None), size=(200, 30), pos_hint={'center_x': 0.7, 'center_y': 0.5})
        layout.add_widget(self.entry_phone_number)

        # Next Button
        btn_next = Button(text="Next", size_hint=(None, None), size=(150, 50), pos_hint={'center_x': 0.5, 'center_y': 0.3})
        btn_next.bind(on_press=self.go_to_next_step)
        layout.add_widget(btn_next)

        self.add_widget(layout)

    def go_to_next_step(self, instance):
        self.manager.current = 'create_account_step_2'  # Navigate to step 2: 'create_account_step_2'


# Define the create account screen (Step 2)
class CreateAccountScreen2(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = FloatLayout()
        
        with layout.canvas.before:
            from kivy.graphics import Color, Rectangle
            # Set background color (light green for finance theme)
            Color(0.85, 1, 0.85, 1)  # RGBA values for a soft green color
            self.rect = Rectangle(size=Window.size)

        # Username
        username = Label(text="Username", font_size='12sp', color=(0, 0.3, 0, 1), size_hint=(None, None), size=(100, 30), pos_hint={'center_x': 0.2, 'center_y': 0.6})
        layout.add_widget(username)
        self.entry_username = TextInput(size_hint=(None, None), size=(200, 30), pos_hint={'center_x': 0.7, 'center_y': 0.6})
        layout.add_widget(self.entry_username)

        # Password
        password = Label(text="Password", font_size='12sp', color=(0, 0.3, 0, 1), size_hint=(None, None), size=(100, 30), pos_hint={'center_x': 0.2, 'center_y': 0.5})
        layout.add_widget(password)
        self.entry_password = TextInput(size_hint=(None, None), size=(200, 30), pos_hint={'center_x': 0.7, 'center_y': 0.5}, password=True)
        layout.add_widget(self.entry_password)

        # Confirm Password
        confirm_password = Label(text="Confirm Password", font_size='12sp', color=(0, 0.3, 0, 1), size_hint=(None, None), size=(150, 30), pos_hint={'center_x': 0.2, 'center_y': 0.4})
        layout.add_widget(confirm_password)
        self.entry_confirm_password = TextInput(size_hint=(None, None), size=(200, 30), pos_hint={'center_x': 0.7, 'center_y': 0.4}, password=True)
        layout.add_widget(self.entry_confirm_password)

        # Create Account Button
        btn_create_account = Button(text="Create Account", size_hint=(None, None), size=(150, 50), pos_hint={'center_x': 0.5, 'center_y': 0.2})
        btn_create_account.bind(on_press=self.create_account)
        layout.add_widget(btn_create_account)

        self.add_widget(layout)

    def create_account(self, instance):
        username = self.entry_username.text
        password = self.entry_password.text
        confirm_password = self.entry_confirm_password.text

        if password == confirm_password:
            # Proceed to create the account (you can add logic to store the data)
            print(f"Account created with Username: {username}")
            self.manager.current = 'home'  # After account creation, go back to the home screen
        else:
            # Handle password mismatch
            popup = Popup(title='Error', content=Label(text='Passwords do not match!'), size_hint=(None, None), size=(300, 200))
            popup.open()


# Define the login screen
class LoginScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = FloatLayout()
        
        with layout.canvas.before:
            from kivy.graphics import Color, Rectangle
            # Set background color (light green for finance theme)
            Color(0.85, 1, 0.85, 1)  # RGBA values for a soft green color
            self.rect = Rectangle(size=Window.size)

        # Username Label and Entry
        lbl_username = Label(text="Username", font_size='12sp', color=(0, 0.3, 0, 1), size_hint=(None, None), size=(100, 30), pos_hint={'center_x': 0.5, 'center_y': 0.6})
        layout.add_widget(lbl_username)
        self.entry_username = TextInput(size_hint=(None, None), size=(200, 30), pos_hint={'center_x': 0.5, 'center_y': 0.55})
        layout.add_widget(self.entry_username)

        # Password Label and Entry
        lbl_password = Label(text="Password", font_size='12sp', color=(0, 0.3, 0, 1), size_hint=(None, None), size=(100, 30), pos_hint={'center_x': 0.5, 'center_y': 0.4})
        layout.add_widget(lbl_password)
        self.entry_password = TextInput(size_hint=(None, None), size=(200, 30), pos_hint={'center_x': 0.5, 'center_y': 0.35}, password=True)
        layout.add_widget(self.entry_password)

        # Login Button
        btn_login = Button(text="Login", size_hint=(None, None), size=(150, 50), pos_hint={'center_x': 0.5, 'center_y': 0.2})
        btn_login.bind(on_press=self.login)
        layout.add_widget(btn_login)

        # Cancel Button
        btn_cancel = Button(text="Cancel", size_hint=(None, None), size=(150, 50), pos_hint={'center_x': 0.5, 'center_y': 0.1})
        btn_cancel.bind(on_press=self.cancel)
        layout.add_widget(btn_cancel)

        self.add_widget(layout)

    def login(self, instance):
        username = self.entry_username.text
        password = self.entry_password.text
        if username == "admin" and password == "password":
            popup = Popup(title='Login Success', content=Label(text='Welcome!'), size_hint=(None, None), size=(300, 200))
            popup.open()
        else:
            popup = Popup(title='Login Failed', content=Label(text='Invalid credentials!'), size_hint=(None, None), size=(300, 200))
            popup.open()

    def cancel(self, instance):
        self.manager.current = 'home'


# Define the screen manager
class MyScreenManager(ScreenManager):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(HomeScreen(name='home'))
        self.add_widget(CreateAccountScreen1(name='create_account_step_1'))
        self.add_widget(CreateAccountScreen2(name='create_account_step_2'))
        self.add_widget(LoginScreen(name='login'))


class MyApp(App):
    def build(self):
        sm = MyScreenManager()
        return sm


if __name__ == '__main__':
    MyApp().run()
