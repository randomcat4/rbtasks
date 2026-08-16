# F3CRC1 — CRC-32 bit order: reflected LFSR versus normal polynomial division

## Frozen source claim

Compute zlib CRC-32 for the frozen byte string with reflected polynomial EDB88320, init/xorout FFFFFFFF, and reconcile it exactly with the normal polynomial 04C11DB7 by reversing each input byte and the final register.

The exact input bytes and all bit-order conventions are frozen in `input.json`. The eight hexadecimal output digits are checked exactly; alternate reflection, initialization, xorout, or byte-order conventions are rejected.

## Submission contract

Return uppercase eight-digit `crc32` and kind `reflected_lfsr` or `normal_polynomial_bitreverse`.
