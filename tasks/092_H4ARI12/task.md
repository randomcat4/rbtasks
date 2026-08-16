# H4ARI12 — Exact arithmetic coding: rational interval and integer range traces

## Submission

Read `input.json` and return one JSON object satisfying `output_schema.json`. All arithmetic is exact. Arrays and nested objects follow the public contract below; extra fields are rejected.

## Complete public contract

- Indices are zero-based unless a mathematical exponent or degree is explicitly named. Matrices are row-major; nested tensor array order is stated per task.
- A rational scalar is a reduced JSON string "n" or "n/d" with positive denominator. JSON integers are used only where the field contract says integer. Floats, decimal approximations, NaN and infinity are invalid.
- The submission object has exactly required_fields, with no additional keys. Nested objects likewise use exactly the named keys.

### Task-specific definitions

- alphabet[j] has integer weight weights[j], total T=sum weights, and cumulative C_0=0, C_(j+1)=C_j+weights[j]. Start [l_0,h_0)=[0,1).
- For message symbol j at step t, l_(t+1)=l_t+(h_t-l_t)C_j/T and h_(t+1)=l_t(old)+(h_t-l_t)C_(j+1)/T. Integer trace starts L_0=0,H_0=1,D_0=1 and updates L,H by L*T+(H-L)C_j and L*T+(H-L)C_(j+1), with D*=T.
- tag_bits is the smallest positive b for which an integer k exists with final_low<=k/2^b<final_high; tag_numerator is the smallest such k. Decode that tag for exactly message length symbols using the same half-open intervals.

### Required output fields

- `interval_trace` — JSON type: array of objects; shape: [message length]. each {low:rational,high:rational} after that symbol. Canonicalization: chronological; half-open intervals.
- `integer_trace` — JSON type: array of objects; shape: [message length]. each {low_numerator:int,high_numerator:int,denominator:int} from integer recursion. Canonicalization: chronological, positive denominator.
- `tag_numerator` — JSON type: integer; shape: scalar. least k at the shortest dyadic precision. Canonicalization: paired with tag_bits.
- `tag_bits` — JSON type: integer; shape: scalar. smallest positive b with final_low<=k/2^b<final_high. Canonicalization: positive integer.
- `decoded_message` — JSON type: array of strings; shape: [message length]. decoding of the canonical dyadic tag. Canonicalization: must reproduce input message.
