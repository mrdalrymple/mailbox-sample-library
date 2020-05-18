from yapsy.IPlugin import IPlugin


class PluginOne(IPlugin):
    def print_name(self):
        print("This is plugin one")

    def on_init(self, default_api):
        self.default = default_api
        self.print_name()


def main():
    print("HELLO WORLD FROM MY MODULE")
