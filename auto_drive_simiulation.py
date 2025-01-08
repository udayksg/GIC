# Author: Uday
# Date Modified: 2025-01-08

import sys
from typing import List, Tuple, Dict

# Class to represent a car in the simulation
class Car:
    DIRECTIONS = ['N', 'E', 'S', 'W']  # Order of directions for rotation

    CAR_IMAGES = {
        'N': "\u25B2",  # Triangle Up
        'E': "\u25B6",  # Triangle Right
        'S': "\u25BC",  # Triangle Down
        'W': "\u25C0"   # Triangle Left
    }

    def __init__(self, name: str, x: int, y: int, direction: str, commands: str):
        # Initialize car properties
        self.name = name
        self.x = x
        self.y = y
        self.direction = direction
        self.commands = commands
        self.active = True  # Status of the car (active/inactive)

    def rotate_left(self):
        # Rotate the car 90 degrees to the left
        current_idx = Car.DIRECTIONS.index(self.direction)
        self.direction = Car.DIRECTIONS[(current_idx - 1) % 4]

    def rotate_right(self):
        # Rotate the car 90 degrees to the right
        current_idx = Car.DIRECTIONS.index(self.direction)
        self.direction = Car.DIRECTIONS[(current_idx + 1) % 4]

    def move_forward(self, width: int, height: int):
        # Move the car one step forward, if within boundaries
        if self.direction == 'N' and self.y < height - 1:
            self.y += 1
        elif self.direction == 'E' and self.x < width - 1:
            self.x += 1
        elif self.direction == 'S' and self.y > 0:
            self.y -= 1
        elif self.direction == 'W' and self.x > 0:
            self.x -= 1

    def execute_command(self, command: str, width: int, height: int):
        # Execute a single command for the car
        if not self.active:
            return
        if command == 'L':
            self.rotate_left()
        elif command == 'R':
            self.rotate_right()
        elif command == 'F':
            self.move_forward(width, height)

    def display_image(self):
        # Return the car's visual representation based on direction
        return Car.CAR_IMAGES[self.direction]

    def __str__(self):
        # String representation of the car's state
        return f"{self.name}, ({self.x},{self.y}) {self.direction}"

# Function to print the simulation field
def print_field(width: int, height: int, cars: List[Car]):
    field = [["." for _ in range(width)] for _ in range(height)]
    for car in cars:
        if car.active:
            field[height - 1 - car.y][car.x] = car.display_image()

    print("\nSimulation Field:")
    for row in field:
        print(" ".join(row))

# Function to run the simulation for all cars
def run_simulation(width: int, height: int, cars: List[Car]):
    # Determine the maximum number of commands among all cars
    max_steps = max(len(car.commands) for car in cars)

    for step in range(max_steps):
        positions = {}  # Track car positions to detect collisions

        for car in cars:
            if car.active and step < len(car.commands):
                car.execute_command(car.commands[step], width, height)
                if (car.x, car.y) in positions:
                    # Handle collision scenario
                    other_car_name = positions[(car.x, car.y)]
                    other_car = next(c for c in cars if c.name == other_car_name)
                    if other_car.active:
                        print(f"Collision detected: {car.name} collides with {other_car_name} at ({car.x},{car.y}) at step {step + 1}")
                        other_car.active = False
                    print(f"Collision detected: {other_car_name} collides with {car.name} at ({car.x},{car.y}) at step {step + 1}")
                    car.active = False
                else:
                    positions[(car.x, car.y)] = car.name

        print_field(width, height, cars)  # Display the field after each step

    # Print final results after simulation
    print("After simulation, the result is:")
    for car in cars:
        print(f"- {car}")

# Main function to handle user interaction and run the program
def main():
    print("Welcome to Auto Driving Car Simulation!")

    # Get the field dimensions from the user
    width, height = map(int, input("Please enter the width and height of the simulation field in x y format: ").split())
    print(f"You have created a field of {width} x {height}.")

    cars = []  # List to store all cars in the simulation

    while True:
        # Display options to the user
        print("\nPlease choose from the following options:")
        print("[1] Add a car to field")
        print("[2] Run simulation")

        choice = input().strip()

        if choice == '1':
            # Add a new car to the simulation
            name = input("Please enter the name of the car: ").strip()
            x, y, direction = input(f"Please enter initial position of car {name} in x y Direction format: ").split()
            x, y = int(x), int(y)

            if direction not in ['N', 'E', 'S', 'W']:
                print("Invalid direction. Only N, E, S, W are allowed.")
                continue

            commands = input(f"Please enter the commands for car {name}: ").strip().upper()

            if not all(c in ['L', 'R', 'F'] for c in commands):
                print("Invalid commands. Only L, R, F are allowed.")
                continue

            cars.append(Car(name, x, y, direction, commands))

            # Display the updated list of cars
            print("\nYour current list of cars are:")
            for car in cars:
                print(f"- {car}, {car.commands}")

        elif choice == '2':
            # Run the simulation if cars have been added
            if not cars:
                print("No cars added to the simulation. Please add at least one car.")
                continue

            print("\nYour current list of cars are:")
            for car in cars:
                print(f"- {car}, {car.commands}")

            run_simulation(width, height, cars)

            # Post-simulation options
            print("\nPlease choose from the following options:")
            print("[1] Start over")
            print("[2] Exit")

            restart_choice = input().strip()
            if restart_choice == '1':
                main()
            elif restart_choice == '2':
                print("Thank you for running the simulation. Goodbye!")
                sys.exit()
        else:
            print("Invalid choice. Please try again.")

# Entry point of the program
if __name__ == "__main__":
    main()
