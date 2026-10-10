import gi
gi.require_version("Gtk", "4.0")
from gi.repository import Gtk
from datetime import datetime
import calendar


class CalendarWindow(Gtk.Window):
    def __init__(self, app):
        super().__init__(
            application=app,
            title="Calendar",
            default_width=320,
            default_height=330,
            resizable=False
        )

        self.set_decorated(False)

        # Current month
        now = datetime.now()
        self.year = now.year
        self.month = now.month

        # Escape / arrow keys
        key_controller = Gtk.EventControllerKey()
        key_controller.connect("key-pressed", self.on_key_pressed)
        self.add_controller(key_controller)

        # CSS
        css = Gtk.CssProvider()
        css.load_from_data("""
        window {
            background: #0f0f0f;
            border-radius: 24px;
        }

        label {
            color: #ffffff;
            font-family: "JetBrainsMono Nerd Font";
            font-size: 14px;
        }

        .header {
            font-size: 18px;
            font-weight: bold;
        }

        .day {
            color: #888888;
        }

        .today {
            color: #ffffff;
            font-weight: bold;
            background: #252525;
            border-radius: 12px;
        }

        button {
            color: #aaaaaa;
            background: transparent;
            border: none;
            border-radius: 12px;
            padding: 5px 12px;
            font-size: 18px;
        }

        button:hover {
            color: #ffffff;
            background: #252525;
        }
        """.encode())

        Gtk.StyleContext.add_provider_for_display(
            self.get_display(),
            css,
            Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
        )

        self.build_calendar()

    def on_key_pressed(self, controller, keyval, keycode, state):
        # Escape
        if keyval == 65307:
            self.close()
            return True

        # Left arrow
        if keyval == 65361:
            self.previous_month()
            return True

        # Right arrow
        if keyval == 65363:
            self.next_month()
            return True

        return False

    def previous_month(self):
        self.month -= 1

        if self.month == 0:
            self.month = 12
            self.year -= 1

        self.build_calendar()

    def next_month(self):
        self.month += 1

        if self.month == 13:
            self.month = 1
            self.year += 1

        self.build_calendar()

    def build_calendar(self):
        # Remove old content
        old_child = self.get_child()

        if old_child:
            self.set_child(None)

        box = Gtk.Box(
            orientation=Gtk.Orientation.VERTICAL,
            spacing=10
        )

        box.set_margin_top(18)
        box.set_margin_bottom(18)
        box.set_margin_start(18)
        box.set_margin_end(18)

        # Header
        header_box = Gtk.Box(
            orientation=Gtk.Orientation.HORIZONTAL,
            spacing=10
        )

        previous = Gtk.Button(label="‹")
        previous.connect(
            "clicked",
            lambda button: self.previous_month()
        )

        next_button = Gtk.Button(label="›")
        next_button.connect(
            "clicked",
            lambda button: self.next_month()
        )

        header = Gtk.Label(
            label=f"{calendar.month_name[self.month]} {self.year}"
        )

        header.add_css_class("header")

        header_box.append(previous)
        header_box.append(header)
        header_box.append(next_button)

        box.append(header_box)

        # Calendar grid
        grid = Gtk.Grid()
        grid.set_row_spacing(5)
        grid.set_column_spacing(5)

        days = ["Mo", "Tu", "We", "Th", "Fr", "Sa", "Su"]

        for col, day in enumerate(days):
            label = Gtk.Label(label=day)
            label.add_css_class("day")
            grid.attach(label, col, 0, 1, 1)

        month_data = calendar.monthcalendar(
            self.year,
            self.month
        )

        now = datetime.now()

        for row, week in enumerate(month_data, start=1):
            for col, day in enumerate(week):

                if day == 0:
                    continue

                label = Gtk.Label(label=str(day))
                label.set_size_request(34, 30)

                # Highlight today's date only
                if (
                    day == now.day
                    and self.month == now.month
                    and self.year == now.year
                ):
                    label.add_css_class("today")

                grid.attach(label, col, row, 1, 1)

        box.append(grid)

        self.set_child(box)


app = Gtk.Application(
    application_id="com.anzi.calendar"
)


def on_activate(app):
    window = CalendarWindow(app)
    window.present()


app.connect("activate", on_activate)

app.run()
