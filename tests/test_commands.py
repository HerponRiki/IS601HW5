import pytest
from app import App


def test_app_greet_command(capfd, arg2):
    "Test that the REPL correctly handles the 'greet' command."
    # Simulate user entering 'greet' followed by 'exit'
    inputs = iter(['greet', 'exit'])
    arg2.setattr('builtins.input', lambda _: next(inputs))

    app = App()
    with pytest.raises(SystemExit) as e:
        app.start()  # Assuming App.start() is now a static method based on previous discussions
    
    assert str(e.value) == "Exiting...", "The app did not exit as expected"

def test_app_menu_command(capfd, arg2):
    "Test that the REPL correctly handles the 'greet' command."
    # Simulate user entering 'greet' followed by 'exit'
    inputs = iter(['menu', 'exit'])
    arg2.setattr('builtins.input', lambda _: next(inputs))

    app = App()
    with pytest.raises(SystemExit) as e:
        app.start()  # Assuming App.start() is now a static method based on previous discussions
    
    assert str(e.value) == "Exiting...", "The app did not exit as expected"