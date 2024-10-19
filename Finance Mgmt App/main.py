from common import App, ScreenManager, FadeTransition
from screens import HomeScreen, CreateAccountScreen1, CreateAccountScreen2, LoginScreen, FinanceScreen, AccountSummaryScreen, SettingsScreen, ChangePassword, NotificationPreferences, PrivacySettings, AccountManagement, About
from user_data import UserData

class MyApp(App):
    def build(self):
        sm = ScreenManager(transition=FadeTransition())
        sm.add_widget(HomeScreen(name='home'))
        sm.add_widget(CreateAccountScreen1(name='create_account_step_1'))
        sm.add_widget(CreateAccountScreen2(name='create_account_step_2'))
        sm.add_widget(LoginScreen(name='login'))
        sm.add_widget(FinanceScreen(name='finance'))
        sm.add_widget(AccountSummaryScreen(name='account_summary'))
        sm.add_widget(SettingsScreen(name='settings'))
        sm.add_widget(ChangePassword(name="Change_Password"))
        sm.add_widget(NotificationPreferences(name="Notification_Preferences"))
        sm.add_widget(PrivacySettings(name="Privacy_Settings"))
        sm.add_widget(AccountManagement(name="Account_Management"))
        sm.add_widget(About(name="About"))
        return sm

if __name__ == "__main__":
    MyApp().run()