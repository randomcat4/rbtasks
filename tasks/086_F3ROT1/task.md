# F3ROT1 — Ordered 3-D rotations: exact quaternion and matrix composition

## Frozen source claim

Apply the first frozen scalar-last unit quaternion and then the second to the frozen vector; return the canonical exact composite and rotated vector under SciPy active-rotation composition order.

All rationals use reduced `{"num": integer, "den": positive_integer}`. The quaternion component order, active-rotation convention, multiplication/composition order, and canonical sign are frozen in `input.json`; tolerance-based float equality is rejected.

## Submission contract

Return exact `composite_quaternion_xyzw`, exact `rotated_vector`, and kind `hamilton_sandwich` or `composed_rotation_matrices`.
