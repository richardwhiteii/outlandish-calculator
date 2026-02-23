class DramaticNarrator:
    def narrate_calculation(self, expression, result):
        print("--- DRAMATIC CALCULATION ---")
        print(f"The numbers swirl in the void: {expression}")
        print(f"The truth is revealed: {result}")
        print("----------------------------")

    def narrate_error(self, message):
        print("!!! DRAMATIC ERROR !!!")
        print(f"The heavens cry out: {message}")
        print("!!!!!!!!!!!!!!!!!!!!!!")

    def show_history(self, history):
        print("=== CHRONICLES OF CALCULATION ===")
        if not history:
            print("The scrolls are empty.")
        else:
            for entry in history:
                print(f"Replay: {entry}")
        print("==================================")

def repl_loop():
    narrator = DramaticNarrator()
    history = []
    while True:
        try:
            line = input("calc> ")
            cmd = line.strip()
            if not cmd:
                continue
            if cmd.lower() in ("exit", "quit"):
                break
            if cmd.lower() == "history":
                narrator.show_history(history)
                continue
            
            # Basic math evaluation using a restricted environment
            result = eval(cmd, {"__builtins__": {}}, {})
            history.append(f"{cmd} = {result}")
            narrator.narrate_calculation(cmd, result)
        except EOFError:
            break
        except Exception as e:
            narrator.narrate_error(str(e))