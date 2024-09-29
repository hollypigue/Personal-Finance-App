from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window
from kivy.graphics import Color, Rectangle, RoundedRectangle
from kivy.uix.button import ButtonBehavior
from kivy.uix.screenmanager import FadeTransition
from kivy.uix.dropdown import DropDown
import json

Window.size = (360, 640)

class UserData:
    @staticmethod
    def load_data():
        try:
            with open("users.json", "r") as f:
                return json.load(f)
        except FileNotFoundError:
            return {}

    @staticmethod
    def save_data(data):
        with open("users.json", "w") as f:
            json.dump(data, f)

class RoundedButton(ButtonBehavior, Label):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.size_hint = (None, None)
        self.size = (200, 50)
        self.bind(pos=self.update_rect, size=self.update_rect)
        with self.canvas.before:
            Color(0.2, 0.6, 0.2, 0.6)  # Button color
            self.rect = RoundedRectangle(size=self.size, pos=self.pos, radius=[30])  # Adjust radius to make it more rounded

    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size

# Define the home screen
class HomeScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = FloatLayout()
        
        with layout.canvas.before:
            Color(0.85, 1, 0.85, 1)  # Background color
            self.rect = Rectangle(size=Window.size)

        # Application Name
        app_name = Label(text="My Finance Manager", font_size='20sp', color=(0, 0, 0, 1), size_hint=(None, None), size=(300, 50), pos_hint={'center_x': 0.5, 'center_y': 0.7})
        layout.add_widget(app_name)

        # Login Button
        btn_login = RoundedButton(text="Login", pos_hint={'center_x': 0.5, 'center_y': 0.5})
        btn_login.bind(on_press=self.go_to_login)
        layout.add_widget(btn_login)

        # Create Account Button
        btn_create_account = RoundedButton(text="Create Account", pos_hint={'center_x': 0.5, 'center_y': 0.4})
        btn_create_account.bind(on_press=self.go_to_create_account)
        layout.add_widget(btn_create_account)

        self.add_widget(layout)

    def go_to_login(self, instance):
        self.manager.current = 'login'

    def go_to_create_account(self, instance):
        self.manager.current = 'create_account_step_1'

# Define the create account screen (Step 1)
class CreateAccountScreen1(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = FloatLayout()
        
        with layout.canvas.before:
            Color(0.8, 1, 0.8, 1)  # Background color (light green for finance theme)
            self.rect = Rectangle(size=Window.size)

        # First Name
        first_name = Label(text="First Name", font_size='14sp', color=(0, 0, 0, 1), size_hint=(None, None), size=(100, 30), pos_hint={'center_x': 0.2, 'center_y': 0.8})
        layout.add_widget(first_name)
        self.entry_first_name = TextInput(size_hint=(None, None), size=(200, 30), pos_hint={'center_x': 0.7, 'center_y': 0.8})
        layout.add_widget(self.entry_first_name)

        # Last Name
        last_name = Label(text="Last Name", font_size='14sp', color=(0, 0, 0, 1), size_hint=(None, None), size=(100, 30), pos_hint={'center_x': 0.2, 'center_y': 0.7})
        layout.add_widget(last_name)
        self.entry_last_name = TextInput(size_hint=(None, None), size=(200, 30), pos_hint={'center_x': 0.7, 'center_y': 0.7})
        layout.add_widget(self.entry_last_name)

        # Email
        email = Label(text="Email", font_size='14sp', color=(0, 0, 0, 1), size_hint=(None, None), size=(100, 30), pos_hint={'center_x': 0.2, 'center_y': 0.6})
        layout.add_widget(email)
        self.entry_email = TextInput(size_hint=(None, None), size=(200, 30), pos_hint={'center_x': 0.7, 'center_y': 0.6})
        layout.add_widget(self.entry_email)

        # Phone Number
        phone_number = Label(text="Phone Number", font_size='14sp', color=(0, 0, 0, 1), size_hint=(None, None), size=(100, 30), pos_hint={'center_x': 0.2, 'center_y': 0.5})
        layout.add_widget(phone_number)
        self.entry_phone_number = TextInput(size_hint=(None, None), size=(200, 30), pos_hint={'center_x': 0.7, 'center_y': 0.5})
        layout.add_widget(self.entry_phone_number)

        # Next Button
        btn_next = RoundedButton(text="Next", pos_hint={'center_x': 0.5, 'center_y': 0.3})
        btn_next.bind(on_press=self.go_to_next_step)
        layout.add_widget(btn_next)

        self.add_widget(layout)

    def go_to_next_step(self, instance):
        first_name = self.entry_first_name.text.strip()
        last_name = self.entry_last_name.text.strip()
        email = self.entry_email.text.strip()
        phone_number = self.entry_phone_number.text.strip()

        # Perform validation checks
        if not first_name or not last_name:
            self.show_error("First and Last Name are required!")
        elif not self.validate_email(email):
            self.show_error("Invalid email address!")
        elif not phone_number.isdigit() or len(phone_number) != 10:
            self.show_error("Phone number must be 10 digits!")
        else:
            self.manager.current = 'create_account_step_2'  # Navigate to the next step

    def validate_email(self, email):
        # Simple email validation (checking for '@' and '.' symbols)
        return '@' in email and '.' in email

    def show_error(self, message):
        # Display a popup with an error message
        popup = Popup(title='Error', content=Label(text=message), size_hint=(None, None), size=(300, 200))
        popup.open()


# Define the create account screen (Step 2) with password validation
class CreateAccountScreen2(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = FloatLayout()
        
        with layout.canvas.before:
            Color(0.85, 1, 0.85, 1)  # Background color (light green for finance theme)
            self.rect = Rectangle(size=Window.size)

        # Username
        username = Label(text="Username", font_size='14sp', color=(0, 0, 0, 1), size_hint=(None, None), size=(100, 30), pos_hint={'center_x': 0.2, 'center_y': 0.6})
        layout.add_widget(username)
        self.entry_username = TextInput(size_hint=(None, None), size=(200, 30), pos_hint={'center_x': 0.7, 'center_y': 0.6})
        layout.add_widget(self.entry_username)

        # Password
        password = Label(text="Password", font_size='14sp', color=(0, 0, 0, 1), size_hint=(None, None), size=(100, 30), pos_hint={'center_x': 0.2, 'center_y': 0.5})
        layout.add_widget(password)
        self.entry_password = TextInput(size_hint=(None, None), size=(200, 30), pos_hint={'center_x': 0.7, 'center_y': 0.5}, password=True)
        layout.add_widget(self.entry_password)

        # Confirm Password
        confirm_password = Label(text="Confirm Password", font_size='14sp', color=(0, 0, 0, 1), size_hint=(None, None), size=(100, 30), pos_hint={'center_x': 0.2, 'center_y': 0.4})
        layout.add_widget(confirm_password)
        self.entry_confirm_password = TextInput(size_hint=(None, None), size=(200, 30), pos_hint={'center_x': 0.7, 'center_y': 0.4}, password=True)
        layout.add_widget(self.entry_confirm_password)

        # Create Account Button
        btn_create_account = RoundedButton(text="Create Account", pos_hint={'center_x': 0.5, 'center_y': 0.3})
        btn_create_account.bind(on_press=self.create_account)
        layout.add_widget(btn_create_account)

        self.add_widget(layout)

    def create_account(self, instance):
        username = self.entry_username.text.strip()
        password = self.entry_password.text.strip()
        confirm_password = self.entry_confirm_password.text.strip()

        # Validate password
        if password != confirm_password:
            self.show_error("Passwords do not match!")
            return

        if len(password) < 8:
            self.show_error("Password must be at least 8 characters long!")
            return

        # Load user data
        users = UserData.load_data()

        # Check if username already exists
        if username in users:
            self.show_error("Username already exists!")
            return

        # Save new user data
        users[username] = {
            "password": password,
            "first_name": self.manager.get_screen('create_account_step_1').entry_first_name.text,
            "last_name": self.manager.get_screen('create_account_step_1').entry_last_name.text,
            "email": self.manager.get_screen('create_account_step_1').entry_email.text,
            "phone_number": self.manager.get_screen('create_account_step_1').entry_phone_number.text
        }
        UserData.save_data(users)

        self.manager.current = 'home'

    def show_error(self, message):
        popup = Popup(title='Error', content=Label(text=message), size_hint=(None, None), size=(300, 200))
        popup.open()


# Define the login screen
class LoginScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = FloatLayout()
        
        with layout.canvas.before:
            Color(0.85, 1, 0.85, 1)  # Background color (light green for finance theme)
            self.rect = Rectangle(size=Window.size)

        # Username
        username = Label(text="Username", font_size='14sp', color=(0, 0, 0, 1), size_hint=(None, None), size=(100, 30), pos_hint={'center_x': 0.2, 'center_y': 0.6})
        layout.add_widget(username)
        self.entry_username = TextInput(size_hint=(None, None), size=(200, 30), pos_hint={'center_x': 0.7, 'center_y': 0.6})
        layout.add_widget(self.entry_username)

        # Password
        password = Label(text="Password", font_size='14sp', color=(0, 0, 0, 1), size_hint=(None, None), size=(100, 30), pos_hint={'center_x': 0.2, 'center_y': 0.5})
        layout.add_widget(password)
        self.entry_password = TextInput(size_hint=(None, None), size=(200, 30), pos_hint={'center_x': 0.7, 'center_y': 0.5}, password=True)
        layout.add_widget(self.entry_password)

        # Login Button
        btn_login = RoundedButton(text="Login", pos_hint={'center_x': 0.5, 'center_y': 0.3})
        btn_login.bind(on_press=self.login)
        layout.add_widget(btn_login)

        self.add_widget(layout)

    def login(self, instance):
        username = self.entry_username.text.strip()
        password = self.entry_password.text.strip()

        # Load user data
        users = UserData.load_data()

        if username in users and users[username]['password'] == password:
            self.manager.current = 'finance'
        else:
            self.show_error("Invalid username or password!")

    def show_error(self, message):
        popup = Popup(title='Error', content=Label(text=message), size_hint=(None, None), size=(300, 200))
        popup.open()


# Define the finance screen
class FinanceScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = FloatLayout()

        with layout.canvas.before:
            Color(0.85, 1, 0.85, 1)  # Background color (light green for finance theme)
            self.rect = Rectangle(size=Window.size)

        # Transactions label
        label = Label(text="Transactions", font_size='20sp', color=(0, 0, 0, 1), size_hint=(None, None), size=(300, 50), pos_hint={'center_x': 0.5, 'center_y': 0.9})
        layout.add_widget(label)

        # Transaction input fields
        self.transaction_amount = TextInput(hint_text="Transaction Amount", size_hint=(None, None), size=(200, 30), pos_hint={'center_x': 0.5, 'center_y': 0.75})
        layout.add_widget(self.transaction_amount)

        # Dropdown for transaction type
        self.dropdown = DropDown()
        self.dropdown.add_widget(Button(text='Income', size_hint_y=None, height=44, on_release=lambda btn: self.dropdown.select(btn.text)))
        self.dropdown.add_widget(Button(text='Expense', size_hint_y=None, height=44, on_release=lambda btn: self.dropdown.select(btn.text)))

        self.mainbutton = Button(text='Select Transaction Type', size_hint=(None, None), size=(200, 30), pos_hint={'center_x': 0.5, 'center_y': 0.65})
        self.mainbutton.bind(on_release=self.dropdown.open)
        self.dropdown.bind(on_select=lambda instance, x: setattr(self.mainbutton, 'text', x))
        layout.add_widget(self.mainbutton)

        # Add Transaction Button
        btn_add_transaction = RoundedButton(text="Add Transaction", pos_hint={'center_x': 0.5, 'center_y': 0.55})
        btn_add_transaction.bind(on_press=self.add_transaction)
        layout.add_widget(btn_add_transaction)

        # Navigate to Account Summary Button
        btn_account_summary = RoundedButton(text="View Account Summary", pos_hint={'center_x': 0.5, 'center_y': 0.45})
        btn_account_summary.bind(on_press=self.go_to_account_summary)
        layout.add_widget(btn_account_summary)

        # Navigate to Settings Button
        btn_settings = RoundedButton(text="Settings", pos_hint={'center_x': 0.5, 'center_y': 0.35})
        btn_settings.bind(on_press=self.go_to_settings)
        layout.add_widget(btn_settings)

        self.add_widget(layout)

    def go_to_account_summary(self, instance):
        self.manager.current = 'account_summary'

    def go_to_settings(self, instance):
        self.manager.current = 'settings'  # Navigate to Settings Screen

    def add_transaction(self, instance):
        amount = self.transaction_amount.text.strip()
        transaction_type = self.mainbutton.text

        if not amount or transaction_type == 'Select Transaction Type':
            self.show_error("Please enter a valid amount!")
            return

        # Here you can save the transaction data
        # For now, just show a success message
        self.show_error(f"Added {transaction_type}: ${amount}")

        # Clear the input fields
        self.transaction_amount.text = ''
        self.mainbutton.text = 'Select Transaction Type'

    def show_error(self, message):
        popup = Popup(title='Message', content=Label(text=message), size_hint=(None, None), size=(300, 200))
        popup.open()

class AccountSummaryScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = FloatLayout()
        
        with layout.canvas.before:
            Color(0.85, 1, 0.85, 1)  # Background color
            self.rect = Rectangle(size=Window.size)

        # Add content for account summary
        label = Label(text="Account Summary", font_size='20sp', color=(0, 0, 0, 1), size_hint=(None, None), size=(300, 50), pos_hint={'center_x': 0.5, 'center_y': 0.9})
        layout.add_widget(label)

        # Example content for account summary
        account_balance = Label(text="Account Balance: $20,000", font_size='16sp', color=(0, 0, 0, 1), size_hint=(None, None), size=(300, 50), pos_hint={'center_x': 0.5, 'center_y': 0.7})
        layout.add_widget(account_balance)

        # Back Button
        btn_back = RoundedButton(text="Back", pos_hint={'center_x': 0.5, 'center_y': 0.3})
        btn_back.bind(on_press=self.go_to_finance)
        layout.add_widget(btn_back)

        self.add_widget(layout)

    def go_to_finance(self, instance):
        self.manager.current = 'finance'


# Define the settings screen
class SettingsScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = FloatLayout()

        # Background color
        with layout.canvas.before:
            Color(0.85, 1, 0.85, 1)  # Light green background
            self.rect = Rectangle(size=Window.size)

        # Settings title
        label = Label(text="Settings", font_size='24sp', color=(0, 0, 0, 1), size_hint=(None, None), size=(300, 50), pos_hint={'center_x': 0.5, 'center_y': 0.9})
        layout.add_widget(label)

        # Example settings options
        settings_options = [
            "Change Password",
            "Notification Preferences",
            "Privacy Settings",
            "Account Management",
            "About"
        ]
        
        # Create buttons for each setting option
        for index, option in enumerate(settings_options):
            btn = RoundedButton(text=option, size_hint=(0.5, None), height=40, pos_hint={'center_x': 0.5, 'center_y': 0.8 - index * 0.1})
            btn.bind(on_press=self.on_setting_selected)
            layout.add_widget(btn)

        # Back to Finance Button
        btn_back = RoundedButton(text="Back to Finance", pos_hint={'center_x': 0.5, 'center_y': 0.3})
        btn_back.bind(on_press=self.go_back)
        layout.add_widget(btn_back)

        self.add_widget(layout)

    def on_setting_selected(self, instance):
        print(f"Selected setting: {instance.text}")  # Placeholder for handling settings

    def go_back(self, instance):
        self.manager.current = 'finance'  # Navigate back to the Finance Screen


# Update the ScreenManager to include the new screens
class MyFinanceApp(App):
    def build(self):
        sm = ScreenManager(transition=FadeTransition())
        sm.add_widget(HomeScreen(name='home'))
        sm.add_widget(CreateAccountScreen1(name='create_account_step_1'))
        sm.add_widget(CreateAccountScreen2(name='create_account_step_2'))
        sm.add_widget(LoginScreen(name='login'))
        sm.add_widget(FinanceScreen(name='finance'))
        sm.add_widget(AccountSummaryScreen(name='account_summary'))
        sm.add_widget(SettingsScreen(name='settings'))
        return sm

# Run the app
if __name__ == '__main__':
    MyFinanceApp().run()
