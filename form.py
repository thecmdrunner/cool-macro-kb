import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, GLib


class EntryWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title="Enter Password")
        self.set_size_request(300, 100)

        self.timeout_id = None

        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.add(vbox)

        self.entry = Gtk.Entry()
        # Set empty text box
        self.entry.set_text("")
        # Max length 100
        self.entry.set_max_length(100)
        # Set Visibility
        self.entry.set_visibility(False)

        hbox = Gtk.Box(spacing=6)
        vbox.pack_start(self.entry, True, True, 0)
        vbox.pack_start(hbox, True, True, 0)

        # Pulsing Effect
        self.pulse = Gtk.CheckButton(label="Pulse")
        self.pulse.connect("toggled", self.on_pulse_toggled)
        self.pulse.set_active(True)
        hbox.pack_start(self.pulse, True, True, 0)

        # Hide the password
        self.check_visible = Gtk.CheckButton(label="Hide Password")
        self.check_visible.connect("toggled", self.on_visible_toggled)
        self.check_visible.set_active(True)
        hbox.pack_start(self.check_visible, True, True, 0)


        def on_submit_clicked(self):
                print('"SUBMIT" button was clicked')
                value = self.entry.get_text()
                print("value is",value)
        
        self.button = Gtk.Button.new_with_label("SUBMIT")
        self.button.connect("clicked", on_submit_clicked)
        hbox.pack_start(self.button, True, True, 0)

       

    def on_editable_toggled(self, button):
        value = button.get_active()
        self.entry.set_editable(value)

    def on_visible_toggled(self, button):
        value = button.get_active()
        self.entry.set_visibility(not value)  # Opposite of true will be false

    def on_pulse_toggled(self, button):
        if button.get_active():
            self.entry.set_progress_pulse_step(0.2)
            # Call self.do_pulse every 100 ms
            self.timeout_id = GLib.timeout_add(100, self.do_pulse, None)
        else:
            # Don't call self.do_pulse anymore
            GLib.source_remove(self.timeout_id)
            self.timeout_id = None
            self.entry.set_progress_pulse_step(0)

    def do_pulse(self, user_data):
        self.entry.progress_pulse()
        return True

    def on_icon_toggled(self, button):
        if button.get_active():
            icon_name = "system-search-symbolic"
        else:
            icon_name = None
        self.entry.set_icon_from_icon_name(
            Gtk.EntryIconPosition.PRIMARY, icon_name)


win = EntryWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
