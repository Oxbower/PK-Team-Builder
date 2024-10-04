import os
import platform
import sys

from app.Application import App


def main():
    """
    Main function to run app, checks if the app works on system,
    calls appropriate functions to start main loop and build UI
    """
    # OS check
    if os.name == "nt" or os.name == "posix":
        print(f"OS: {platform.system()}{platform.release()}-{platform.architecture()[0]}"
              f"-Version:{platform.version()}")
        print(f"Python Version: {platform.python_version()}")
    else:
        sys.exit(f"Unsupported OS, Running on {platform.system()} {platform.release()} {platform.architecture()}")

    # create window object
    run_app = App()
    run_app.run()


if __name__ == '__main__':
    main()
