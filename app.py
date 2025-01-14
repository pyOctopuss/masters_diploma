from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button


class WeatherApp(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 10
        self.spacing = 10
        self.create_layout()

    def create_layout(self):
        # Header Section
        header = BoxLayout(size_hint=(1, 0.1), padding=5)
        header.add_widget(Label(text="Weather Forecast", font_size='20sp', bold=True))
        self.add_widget(header)

        # Day/Night Section
        day_night_box = BoxLayout(orientation='horizontal', size_hint=(1, 0.2), spacing=10)
        day_night_box.add_widget(self.create_box("Day Temp", "23°C", bg_color=[0.8, 0.8, 1, 1]))
        day_night_box.add_widget(self.create_box("Night Temp", "17°C", bg_color=[0.6, 0.6, 0.9, 1]))
        self.add_widget(day_night_box)

        # Hourly Forecast Section
        hourly_forecast = BoxLayout(orientation='horizontal', size_hint=(1, 0.3), spacing=10)
        for i in range(3):
            hourly_forecast.add_widget(self.create_hourly_box(f"{3 * i + 1}:00", "Icon", "20°C"))
        self.add_widget(hourly_forecast)

        # Footer with Refresh Button
        footer = BoxLayout(size_hint=(1, 0.1), padding=10)
        footer.add_widget(Button(text="Refresh", size_hint=(0.3, 1)))
        self.add_widget(footer)

    def create_box(self, title, value, bg_color):
        """Creates a labeled box with background color"""
        box = BoxLayout(orientation='vertical', padding=5, spacing=5, size_hint=(0.5, 1))
        label = Label(text=title, bold=True, font_size='14sp', size_hint=(1, 0.4))
        value_label = Label(text=value, font_size='16sp', color=bg_color, size_hint=(1, 0.6))
        box.add_widget(label)
        box.add_widget(value_label)
        return box

    def create_hourly_box(self, time, icon, temp):
        """Creates a box for hourly forecast"""
        box = BoxLayout(orientation='vertical', spacing=5, padding=5, size_hint=(0.3, 1))
        time_label = Label(text=time, size_hint=(1, 0.3))
        icon_label = Label(text=icon, size_hint=(1, 0.4))  # Placeholder for icons
        temp_label = Label(text=temp, size_hint=(1, 0.3))
        box.add_widget(time_label)
        box.add_widget(icon_label)
        box.add_widget(temp_label)
        return box


class WeatherForecastApp(App):
    def build(self):
        return WeatherApp()


if __name__ == '__main__':
    WeatherForecastApp().run()


