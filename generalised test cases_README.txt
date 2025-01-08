The test cases have been updated to allow users to provide parameters for testing directions and movements dynamically. Here's an overview of the changes:

1. Generalized Rotation Tests:
   - Accepts 'initial_direction, 'expected_direction', and 'rotation_type' ('L' for left, 'R' for right) as parameters.

2. Generalized Movement Tests:
   - Accepts 'x', 'y', 'direction', 'expected_position', and 'command' ('F' for forward) as parameters.

3. Generalized Command Execution Tests:
   - Accepts 'x', 'y', 'direction', 'commands', 'expected_position', and 'expected_direction' as parameters.

You can now reuse these generalized methods for flexible testing scenarios. Let me know if further refinements are needed!