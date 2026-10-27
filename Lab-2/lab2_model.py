
class ClassroomAgent:
    def __init__(self):
        self.previous_mode = None

    def act(self, temp, occupied):
        # Decide the target mode using the original rules
        if not occupied:
            target_mode = "ECO"
        elif temp > 26:
            target_mode = "COOL"
        elif temp < 20:
            target_mode = "WARM"
        else:
            target_mode = "IDLE"

        # Send a command only when the target changes
        if target_mode != self.previous_mode:
            send_command = True
        else:
            send_command = False

        # Remember the target mode for the next percept
        previous_mode = self.previous_mode
        self.previous_mode = target_mode

        return previous_mode, target_mode, send_command


if __name__ == "__main__":
    agent = ClassroomAgent()

    percepts = [
        (29, True),
        (29, True),
        (20, True),
        (26, True),
        (19, True),
        (29, False),
        (29, False)
    ]

    print("STATEFUL CLASSROOM AGENT")
    print("-" * 65)

    for step, (temp, occupied) in enumerate(percepts, 1):
        previous_mode, target_mode, send_command = agent.act(
            temp, occupied
        )

        command_status = (
            "SEND COMMAND" if send_command else "NO COMMAND"
        )

        print(
            f"Step {step}: "
            f"Previous={previous_mode}, "
            f"Percept=({temp}, {occupied}), "
            f"Target={target_mode}, "
            f"Action={command_status}"


        )