# Mission 5 — Numbers and data

## 1. Task / objective
Convert numbers between decimal, binary and hexadecimal, verify with Python, build a converter, and explain text encoding.

## 2. Work completed
### 5.1 Manual conversions
- Decimal 13 to binary: 13 = 8 + 4 + 1 = `1101₂`.
- Decimal 25 to binary: 25 = 16 + 8 + 1 = `11001₂`.
- Binary `1010₂` to decimal: 1×8 + 0×4 + 1×2 + 0×1 = `10₁₀`.
- Binary `1101₂` to decimal: 1×8 + 1×4 + 0×2 + 1×1 = `13₁₀`.
- Hex `A₁₆` to decimal: A = 10, so the answer is `10₁₀`.
- Hex `1F₁₆` to decimal: 1×16 + 15 = `31₁₀`.
- Binary `1111₂` to hexadecimal: `1111₂` = 15 decimal = `F₁₆`.

### 5.2 Python verification
- `bin(13)` → `'0b1101'`
- `bin(25)` → `'0b11001'`
- `int('1010', 2)` → `10`
- `int('1101', 2)` → `13`
- `hex(10)` → `'0xa'`
- `int('1F', 16)` → `31`
- `hex(15)` → `'0xf'`

The `0b` and `0x` prefixes identify the base; the converted digits are written without those prefixes in the tables.

### 5.3 Number converter
`number_converter.py` asks for a positive decimal integer. `int()` parses the input, `bin()` converts it to binary and `hex()` converts it to hexadecimal.

| Input | Binary | Hexadecimal |
|---:|---:|---:|
| 13 | 1101 | D |
| 25 | 11001 | 19 |
| 42 | 101010 | 2A |

### 5.4 Text encoding
The ASCII decimal code for uppercase `A` is 65, and for lowercase `a` it is 97. An encoding maps characters to numeric values so computers can store and exchange text consistently. The snowman character `☃` is outside basic ASCII; UTF-8 can represent it.

## 3. Commands / tools used
`python3 number_converter.py` runs the program. Python functions used: `input()`, `int()`, `bin()`, `hex()`, and `print()`.

## 4. My understanding
Binary uses powers of 2, decimal uses powers of 10, and hexadecimal uses powers of 16. One hexadecimal digit represents four binary bits, so `1111₂` becomes `F₁₆`. Character encodings let computers agree on the numbers used for text.

## 5. Difficulties faced
Python includes base prefixes in the results from `bin()` and `hex()`, while conversion tables usually show only the digits.

## 6. How I resolved them
I kept the prefixes in the verification results and omitted them when writing the converted numeral.

## 7. Evidence / files
`number_converter.py` and this README with conversion working, Python verification, test values and encoding notes.

## 8. Commit details
- Commit message: `Build number converter and explain data representation`.
- The mission commit is pushed to GitHub.
