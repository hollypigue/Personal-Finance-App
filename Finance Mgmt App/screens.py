from common import Screen, FloatLayout, Label, TextInput, DropDown, Button, ScrollView, GridLayout, Popup, BoxLayout, CheckBox, ToggleButton
from widgets import RoundedButton
from user_data import UserData
from common import Window, Color, Rectangle

Window.size = (360, 640)

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


class FinanceScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = FloatLayout()

        with layout.canvas.before:
            Color(0.85, 1, 0.85, 1)  # Background color (light green for finance theme)
            self.rect = Rectangle(size=Window.size)
            
        self.transactions = []

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

        if amount and transaction_type:
            try:
                amount = float(amount)
                # Append to transactions list
                self.transactions.append({'amount': amount, 'type': transaction_type})
                self.transaction_amount.text = ''  # Clear input field

                # Optionally navigate to Account Summary
                self.manager.get_screen('account_summary').update_summary(self.transactions)
                self.manager.current = 'account_summary'
            except ValueError:
                self.show_error("Please enter a valid amount.")
        

class AccountSummaryScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = FloatLayout()

        with layout.canvas.before:
            Color(0.85, 1, 0.85, 1)  # Background color (light green for finance theme)
            self.rect = Rectangle(size=Window.size)

        # Title Label
        title_label = Label(text="Account Summary", font_size='20sp', color=(0, 0, 0, 1),
        size_hint=(None, None), size=(300, 50), pos_hint={'center_x': 0.5, 'center_y': 0.9})
        layout.add_widget(title_label)

        # Display summary information
        self.summary_label = Label(text="", font_size='16sp', color=(0, 0, 0, 1),
        size_hint=(None, None), size=(300, 200), pos_hint={'center_x': 0.5, 'center_y': 0.5})
        layout.add_widget(self.summary_label)

        # Back Button
        btn_back = RoundedButton(text="Back", pos_hint={'center_x': 0.5, 'center_y': 0.3})
        btn_back.bind(on_press=self.go_to_finance)
        layout.add_widget(btn_back)

        self.add_widget(layout)

    def update_summary(self, transactions):
        total_income = sum(t['amount'] for t in transactions if t['type'] == 'Income')
        total_expenses = sum(t['amount'] for t in transactions if t['type'] == 'Expense')
        net_balance = total_income - total_expenses

        self.summary_label.text = f"Total Income: ${total_income}\nTotal Expenses: ${total_expenses}\nNet Balance: ${net_balance}"

    def go_to_finance(self, instance):
        self.manager.current = 'finance'


class SettingsScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = FloatLayout()

        with layout.canvas.before:
            Color(0.85, 1, 0.85, 1)  # Background color (light green for finance theme)
            self.rect = Rectangle(size=Window.size)
        
        # Add a label for the settings screen title
        label = Label(text="Settings", font_size='24sp', color=(0, 0, 0, 1),
        size_hint=(None, None), size=(200, 50),
        pos_hint={'center_x': 0.5, 'center_y': 0.85})
        layout.add_widget(label)

        # Button: Change Password
        btn_change_password = RoundedButton(text="Change Password", size_hint=(None, None), size=(200, 50), pos_hint={'center_x': 0.5, 'center_y': 0.65})
        btn_change_password.bind(on_press=self.go_to_change_password)
        layout.add_widget(btn_change_password)

        # Button: Notification Preferences
        btn_notification_preferences = RoundedButton(text="Notification Preferences", size_hint=(None, None), size=(200, 50), pos_hint={'center_x': 0.5, 'center_y': 0.55})
        btn_notification_preferences.bind(on_press=self.go_to_notification_preferences)
        layout.add_widget(btn_notification_preferences)

        # Button: Privacy Settings
        btn_privacy_settings = RoundedButton(text="Privacy Settings", size_hint=(None, None), size=(200, 50), pos_hint={'center_x': 0.5, 'center_y': 0.45})
        btn_privacy_settings.bind(on_press=self.go_to_privacy_settings)
        layout.add_widget(btn_privacy_settings)

        # Button: Account Management
        btn_account_management = RoundedButton(text="Account Management", size_hint=(None, None), size=(200, 50), pos_hint={'center_x': 0.5, 'center_y': 0.35})
        btn_account_management.bind(on_press=self.go_to_account_management)
        layout.add_widget(btn_account_management)

        # Button: About
        btn_about = RoundedButton(text="About", size_hint=(None, None), size=(200, 50), pos_hint={'center_x': 0.5, 'center_y': 0.25})
        btn_about.bind(on_press=self.go_to_about)
        layout.add_widget(btn_about)

        # Back Button
        btn_back = RoundedButton(text="Back", pos_hint={'center_x': 0.5, 'center_y': 0.1})
        btn_back.bind(on_press=self.go_to_finance)
        layout.add_widget(btn_back)

        # Add the layout to the screen
        self.add_widget(layout)

    # Functions to switch to different screens
    def go_to_change_password(self, instance):
        self.manager.current = "Change_Password"
        
    def go_to_notification_preferences(self, instance):
        self.manager.current = "Notification_Preferences"
        
    def go_to_privacy_settings(self, instance):
        self.manager.current = "Privacy_Settings"
        
    def go_to_account_management(self, instance):
        self.manager.current = "Account_Management"
        
    def go_to_about(self, instance):
        self.manager.current = "About"

    def go_to_finance(self, instance):
        self.manager.current = "finance"


class ChangePassword(Screen):
    def __init__(self, **kwargs):
        super(ChangePassword, self).__init__(**kwargs)
        layout = FloatLayout()

        with layout.canvas.before:
            Color(0.85, 1, 0.85, 1)  # Background color
            self.rect = Rectangle(size=Window.size)

        label = Label(text="Change Password Page", size_hint=(0.2, 0.1), color=(0,0,0,1), pos_hint={'center_x': 0.5, 'top': 0.9})
        layout.add_widget(label)

        # Define a consistent size for all text inputs
        text_input_size = (200, 30)

        # Old Password
        old_password_label = Label(text="Old Password:", color=(0, 0, 0, 1), size_hint=(0.2, 0.1), pos_hint={'x': 0.1, 'top': 0.75})
        layout.add_widget(old_password_label)
        old_password_input = TextInput(size_hint=(None, None), size=text_input_size, pos_hint={'center_x': 0.7, 'center_y': 0.65}, password=True)
        layout.add_widget(old_password_input)

        # New Password
        new_password_label = Label(text="New Password:", color=(0, 0, 0, 1), size_hint=(0.2, 0.1), pos_hint={'x': 0.1, 'top': 0.6})
        layout.add_widget(new_password_label)
        new_password_input = TextInput(size_hint=(None, None), size=text_input_size, pos_hint={'center_x': 0.7, 'center_y': 0.5}, password=True)
        layout.add_widget(new_password_input)

        # Confirm New Password
        confirm_password_label = Label(text="Confirm Password:", color=(0, 0, 0, 1), size_hint=(0.2, 0.1), pos_hint={'x': 0.1, 'top': 0.45})
        layout.add_widget(confirm_password_label)
        confirm_password_input = TextInput(size_hint=(None, None), size=text_input_size, pos_hint={'center_x': 0.7, 'center_y': 0.35}, password=True)
        layout.add_widget(confirm_password_input)

        # Change Password Button
        change_password_button = RoundedButton(text="Change Password", size_hint=(0.3, 0.1), pos_hint={'center_x': 0.5, 'center_y': 0.2})
        layout.add_widget(change_password_button)

        # Feedback Label
        feedback_label = Label(text="", size_hint=(0.5, 0.1), pos_hint={'center_x': 0.5, 'top': 0.15})
        layout.add_widget(feedback_label)

        btn_back = RoundedButton(text="Back", size_hint=(0.3, 0.1), pos_hint={'center_x': 0.5, 'center_y': 0.1})  # Ensure size_hint is consistent
        btn_back.bind(on_press=self.go_to_settings)
        layout.add_widget(btn_back)

        self.add_widget(layout)

    def go_to_settings(self, instance):
        self.manager.current = 'settings'


class NotificationPreferences(Screen):
    def __init__(self, **kwargs):
        super(NotificationPreferences, self).__init__(**kwargs)
        layout = FloatLayout()

        with layout.canvas.before:
            Color(0.85, 1, 0.85, 1)  # Background color
            self.rect = Rectangle(size=Window.size)

        label = Label(text="Notification Preferences Page", size_hint=(0.2, 0.1), color=(0,0,0,1), pos_hint={'center_x': 0.5, 'top': 0.9})
        layout.add_widget(label)

        # Email Alerts
        email_alert_label = Label(text="Email Alerts:", size_hint=(0.3, 0.1), color=(0,0,0,1), pos_hint={'x': 0.1, 'top': 0.75})
        layout.add_widget(email_alert_label)
        email_alert_checkbox = CheckBox(size_hint=(0.1, 0.1), color=(0,0,0,1), pos_hint={'x': 0.5, 'top': 0.75})
        layout.add_widget(email_alert_checkbox)

        # Push Notifications
        push_alert_label = Label(text="Push Notifications:", size_hint=(0.3, 0.1), color=(0,0,0,1), pos_hint={'x': 0.1, 'top': 0.65})
        layout.add_widget(push_alert_label)
        push_alert_checkbox = CheckBox(size_hint=(0.1, 0.1), color=(0,0,0,1), pos_hint={'x': 0.5, 'top': 0.65})
        layout.add_widget(push_alert_checkbox)

        # SMS Alerts
        sms_alert_label = Label(text="SMS Alerts:", size_hint=(0.3, 0.1), color=(0,0,0,1), pos_hint={'x': 0.1, 'top': 0.55})
        layout.add_widget(sms_alert_label)
        sms_alert_checkbox = CheckBox(size_hint=(0.1, 0.1), color=(0,0,0,1), pos_hint={'x': 0.5, 'top': 0.55})
        layout.add_widget(sms_alert_checkbox)

        # Save Preferences Button
        save_button = RoundedButton(text="Save Preferences", size_hint=(0.3, 0.1), pos_hint={'center_x': 0.5, 'center_y': 0.2})
        layout.add_widget(save_button)

        # Feedback Label
        feedback_label = Label(text="", size_hint=(0.5, 0.1), color=(0,0,0,1), pos_hint={'center_x': 0.4, 'top': 0.35})
        layout.add_widget(feedback_label)

        btn_back = RoundedButton(text="Back", pos_hint={'center_x': 0.5, 'center_y': 0.1})
        btn_back.bind(on_press=self.go_to_settings)
        layout.add_widget(btn_back)

        self.add_widget(layout)

    def go_to_settings(self, instance):
        self.manager.current = 'settings'


class PrivacySettings(Screen):
    def __init__(self, **kwargs):
        super(PrivacySettings, self).__init__(**kwargs)
        layout = FloatLayout()

        with layout.canvas.before:
            Color(0.85, 1, 0.85, 1)  # Background color
            self.rect = Rectangle(size=Window.size)

        label = Label(text="Privacy Settings Page", size_hint=(0.2, 0.1), color=(0,0,0,1), pos_hint={'center_x': 0.5, 'top': 0.9})
        layout.add_widget(label)

        public_toggle = ToggleButton(text="Public", group='visibility', size_hint=(0.3, 0.1), pos_hint={'x': 0.33, 'top': 0.75})
        layout.add_widget(public_toggle)

        friends_toggle = ToggleButton(text="Friends Only", group='visibility', size_hint=(0.3, 0.1), pos_hint={'x': 0.33, 'top': 0.65})
        layout.add_widget(friends_toggle)

        private_toggle = ToggleButton(text="Private", group='visibility', size_hint=(0.3, 0.1), pos_hint={'x': 0.33, 'top': 0.55})
        layout.add_widget(private_toggle)

        # Save Changes Button
        save_button = RoundedButton(text="Save Changes", size_hint=(0.3, 0.1), pos_hint={'center_x': 0.5, 'center_y': 0.2})
        layout.add_widget(save_button)

        # Feedback Label
        feedback_label = Label(text="", size_hint=(0.5, 0.1), pos_hint={'center_x': 0.5, 'top': 0.35})
        layout.add_widget(feedback_label)

        btn_back = RoundedButton(text="Back", pos_hint={'center_x': 0.5, 'center_y': 0.1})
        btn_back.bind(on_press=self.go_to_settings)
        layout.add_widget(btn_back)

        self.add_widget(layout)

    def go_to_settings(self, instance):
        self.manager.current = 'settings'


class AccountManagement(Screen):
    def __init__(self, **kwargs):
        super(AccountManagement, self).__init__(**kwargs)
        layout = FloatLayout()

        with layout.canvas.before:
            Color(0.85, 1, 0.85, 1)  # Background color
            self.rect = Rectangle(size=Window.size)

        label = Label(text="Account Management Page", size_hint=(0.2, 0.1), color=(0,0,0,1), pos_hint={'center_x': 0.5, 'top': 0.9})
        layout.add_widget(label)

        # Update Email
        email_label = Label(text="New Email:", size_hint=(0.2, 0.1), color=(0,0,0,1), pos_hint={'x': 0.1, 'top': 0.75})
        layout.add_widget(email_label)
        email_input = TextInput(size_hint=(None, None), size=(200, 30), pos_hint={'center_x': 0.5, 'center_y': 0.6})
        layout.add_widget(email_input)

        # Delete Account Button
        delete_button = RoundedButton(text="Delete Account", size_hint=(0.3, 0.1), pos_hint={'center_x': 0.5, 'center_y': 0.2})
        layout.add_widget(delete_button)

        # Feedback Label
        feedback_label = Label(text="", size_hint=(0.5, 0.1), pos_hint={'center_x': 0.5, 'top': 0.35})
        layout.add_widget(feedback_label)

        btn_back = RoundedButton(text="Back", pos_hint={'center_x': 0.5, 'center_y': 0.1})
        btn_back.bind(on_press=self.go_to_settings)
        layout.add_widget(btn_back)

        self.add_widget(layout)

    def go_to_settings(self, instance):
        self.manager.current = 'settings'


class About(Screen):
    def __init__(self, **kwargs):
        super(About, self).__init__(**kwargs)
        layout = FloatLayout()

        with layout.canvas.before:
            Color(0.85, 1, 0.85, 1)  # Background color
            self.rect = Rectangle(size=Window.size)

        label = Label(text="About Page", size_hint=(0.2, 0.1), color=(0,0,0,1), pos_hint={'center_x': 0.5, 'top': 0.9})
        layout.add_widget(label)

        # Application Information
        info_label = Label(text="This app helps you manage your finances effectively.\nVersion: 1.0.0", size_hint=(0.5, 0.2), color=(0,0,0,1), pos_hint={'center_x': 0.5, 'top': 0.75})
        layout.add_widget(info_label)

        # Contact Information
        contact_label = Label(text="Contact Support: support@example.com", size_hint=(0.5, 0.1), color=(0,0,0,1), pos_hint={'center_x': 0.5, 'top': 0.6})
        layout.add_widget(contact_label)

        # Feedback Button
        feedback_button = RoundedButton(text="Give Feedback", size_hint=(0.3, 0.1), pos_hint={'center_x': 0.5, 'center_y': 0.2})
        layout.add_widget(feedback_button)

        btn_back = RoundedButton(text="Back", pos_hint={'center_x': 0.5, 'center_y': 0.1})
        btn_back.bind(on_press=self.go_to_settings)
        layout.add_widget(btn_back)

        self.add_widget(layout)

    def go_to_settings(self, instance):
        self.manager.current = 'settings'