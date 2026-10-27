
from lab2_model import ClassroomAgent


def run_tests():
    agent = ClassroomAgent()

    tests = [
        {
            "name": "Initial cooling",
            "temp": 29,
            "occupied": True,
            "expected_target": "COOL",
            "expected_command": True,
        },
        {
            "name": "Repeated cooling",
            "temp": 29,
            "occupied": True,
            "expected_target": "COOL",
            "expected_command": False,
        },
        {
            "name": "Lower boundary: 20 C",
            "temp": 20,
            "occupied": True,
            "expected_target": "IDLE",
            "expected_command": True,
        },
        {
            "name": "Upper boundary: 26 C",
            "temp": 26,
            "occupied": True,
            "expected_target": "IDLE",
            "expected_command": False,
        },
        {
            "name": "Transition to warming",
            "temp": 19,
            "occupied": True,
            "expected_target": "WARM",
            "expected_command": True,
        },
        {
            "name": "Empty room priority",
            "temp": 29,
            "occupied": False,
            "expected_target": "ECO",
            "expected_command": True,
        },
        {
            "name": "Repeated empty-room percept",
            "temp": 29,
            "occupied": False,
            "expected_target": "ECO",
            "expected_command": False,
        },
    ]

    passed = 0

    print("LAB 2 TEST RESULTS")
    print("=" * 65)

    for number, test in enumerate(tests, 1):
        previous, target, command = agent.act(
            test["temp"], test["occupied"]
        )

        success = (
            target == test["expected_target"]
            and command == test["expected_command"]
        )

        if success:
            passed += 1

        print(f"\nTest {number}: {test['name']}")
        print(f"Previous mode: {previous}")
        print(
            f"Percept: ({test['temp']}, "
            f"{test['occupied']})"
        )
        print(f"Expected target: {test['expected_target']}")
        print(f"Actual target: {target}")
        print(f"Expected command: {test['expected_command']}")
        print(f"Actual command: {command}")
        print("Result:", "PASS" if success else "FAIL")

    print("\n" + "=" * 65)
    print(f"Summary: {passed}/{len(tests)} tests passed")


if __name__ == "__main__":
    run_tests()

