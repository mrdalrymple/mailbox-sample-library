from yapsy.IPlugin import IPlugin


class PluginOne(IPlugin):
    def print_name(self):
        print("This is plugin one")


def main():
    print("HELLO WORLD FROM MY MODULE")
