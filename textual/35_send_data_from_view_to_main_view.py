from textual.app import App
from textual.widgets import Button, Static

class ChildView(Static):
    def __init__(self, send_callback):
        super().__init__()
        self.send_callback = send_callback
        self.button = Button(label="Click me")

    def on_mount(self):
        self.mount(self.button)

    def on_button_pressed(self, event: Button.Pressed) -> None:
        self.send_callback({"clicked": True})

class MainView(Static):
    def __init__(self):
        super().__init__()
        self.child = ChildView(self.receive_data)

    def on_mount(self):
        self.mount(self.child)

    def receive_data(self, data):
        print("Received from child:", data)

class MyApp(App):
    def compose(self):
        yield MainView()

if __name__ == "__main__":
    MyApp().run()
