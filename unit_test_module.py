import unittest
from auto_driving_car_simulation import Car

class TestCar(unittest.TestCase):
    """
    Unit tests for the Car class.
    Verifies initialization, movements, rotations, and command executions.
    Allows user-provided parameters for testing directions and movements.
    """

    def test_initialization(self):
        """
        Test if the Car object is initialized correctly with given parameters.
        """
        car = Car(name="A", x=1, y=2, direction="N", commands="FFR")
        self.assertEqual(car.name, "A")
        self.assertEqual(car.x, 1)
        self.assertEqual(car.y, 2)
        self.assertEqual(car.direction, "N")
        self.assertEqual(car.commands, "FFR")
        self.assertTrue(car.active)

    def test_rotate(self, initial_direction, expected_direction, rotation_type):
        """
        Generalized test for rotating left or right based on user input.
        :param initial_direction: Starting direction of the car (e.g., "N").
        :param expected_direction: Expected direction after rotation.
        :param rotation_type: "L" for left, "R" for right.
        """
        car = Car(name="A", x=0, y=0, direction=initial_direction, commands="")
        if rotation_type == "L":
            car.rotate_left()
        elif rotation_type == "R":
            car.rotate_right()
        self.assertEqual(car.direction, expected_direction)

    def test_movement(self, x, y, direction, expected_position, command):
        """
        Generalized test for movement based on user-provided command.
        :param x: Initial x-coordinate of the car.
        :param y: Initial y-coordinate of the car.
        :param direction: Initial direction of the car (e.g., "N").
        :param expected_position: Expected position after movement.
        :param command: Command to be executed (e.g., "F" for forward).
        """
        car = Car(name="A", x=x, y=y, direction=direction, commands="")
        if command == "F":
            car.move_forward(width=5, height=5)
        self.assertEqual((car.x, car.y), expected_position)

    def test_commands(self, x, y, direction, commands, expected_position, expected_direction):
        """
        Generalized test for executing commands.
        :param x: Initial x-coordinate of the car.
        :param y: Initial y-coordinate of the car.
        :param direction: Initial direction of the car (e.g., "N").
        :param commands: Commands to be executed (e.g., "FFRL").
        :param expected_position: Final position after executing commands.
        :param expected_direction: Final direction after executing commands.
        """
        car = Car(name="A", x=x, y=y, direction=direction, commands=commands)
        for command in commands:
            car.execute_command(command, width=5, height=5)
        self.assertEqual((car.x, car.y), expected_position)
        self.assertEqual(car.direction, expected_direction)

if __name__ == "__main__":
    unittest.main()
