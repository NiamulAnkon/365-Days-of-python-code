from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

class MainApp(App):
    def build(self):
        # Create a BoxLayout to hold the label and button
        layout = BoxLayout(orientation='vertical', spacing=10, padding=10)
        
        # Create a label with centered text
        self.label = Label(text="Welcome to the app", halign="center")
        
        # Create a button and bind it to a function
        button = Button(text="Change Text")
        button.bind(on_press=self.change_text)
        
        # Add the label and button to the layout
        layout.add_widget(self.label)
        layout.add_widget(button)
        
        return layout

    def change_text(self, instance):
        self.label.text = "Hi my name is Ankon!"

if __name__ == "__main__":
    MainApp().run()