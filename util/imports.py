print("\t\n\033[93mImporting modules... 🚀\033[0m")
try:
    print("\t\n\033[93mImporting pygame 🐍\033[0m")
    from pygame import (
        init,
        display,
        quit,
        QUIT,
        Vector2,
        event,
        Rect
    )
except ImportError as Error:
    print(f"{Error}, please make sure you have pygame installed")
print("\033[92mPygame imported sucessfully 👍\033[0m\n")