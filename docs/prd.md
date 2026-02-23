# Outlandish Python Calculator - Product Requirements Document

## Overview

The Outlandish Calculator is a CLI Python application that performs math in absurdly dramatic fashion. Every calculation is narrated with theatrical flair, sound effects (ASCII art), and existential commentary. It's a fully functional calculator wrapped in comedic performance art.

## Technical Stack

- **Language:** Python 3.10+
- **Framework:** Pure Python, no external dependencies
- **Entry point:** `python -m outlandish_calc`
- **Package:** `outlandish_calc/`
- **Tests:** `tests/` using pytest

## Package Structure

```
outlandish_calc/
├── __init__.py          # Package init, version
├── __main__.py          # CLI entry point (REPL loop)
├── engine.py            # Core math engine (all operations)
├── narrator.py          # Dramatic narration generator
├── ascii_art.py         # ASCII art for operations and results
├── history.py           # Calculation history with dramatic replays
└── easter_eggs.py       # Hidden behaviors for special numbers
tests/
├── test_engine.py       # Math engine tests
├── test_narrator.py     # Narration tests
├── test_ascii_art.py    # ASCII art tests
├── test_history.py      # History tests
├── test_easter_eggs.py  # Easter egg tests
├── test_repl.py         # REPL integration tests
```

## Feature Specifications

### 1. Core Math Engine (`engine.py`)

The engine MUST support these operations:

| Operation | Syntax | Example |
|-----------|--------|---------|
| Addition | `X + Y` | `2 + 3` → 5 |
| Subtraction | `X - Y` | `10 - 4` → 6 |
| Multiplication | `X * Y` | `3 * 7` → 21 |
| Division | `X / Y` | `15 / 3` → 5.0 |
| Exponentiation | `X ** Y` | `2 ** 8` → 256 |
| Modulo | `X % Y` | `17 % 5` → 2 |
| Square root | `sqrt(X)` | `sqrt(144)` → 12.0 |
| Factorial | `X!` | `5!` → 120 |

**Implementation:**
- `calculate(expression: str) -> CalcResult` — parses and evaluates
- `CalcResult` dataclass: `value: float, operation: str, operands: list[float], drama_level: int`
- `drama_level` is 1-5 based on result magnitude: <10=1, <100=2, <1000=3, <1M=4, >=1M=5
- Division by zero MUST raise `OutlandishError("THE VOID DIVIDES BY NOTHING!")`
- Negative square root MUST raise `OutlandishError("IMAGINARY NUMBERS HAVE LEFT THE CHAT!")`
- Factorial of negative MUST raise `OutlandishError("NEGATIVE FACTORIAL?! THE TIMELINE COLLAPSES!")`
- The parser MUST handle integers and floats
- The parser MUST strip whitespace

### 2. Dramatic Narrator (`narrator.py`)

Every calculation gets narrated based on the operation and drama_level.

**Implementation:**
- `narrate(result: CalcResult) -> str` — returns dramatic narration string
- Each operation has a pool of 3+ narration templates
- Drama level controls intensity (1=mild, 5=apocalyptic)

**Narration pools (minimum 3 per operation):**

**Addition (drama_level examples):**
- Level 1: `"Two numbers join hands in peaceful union. {a} + {b} = {result}. How quaint."`
- Level 3: `"THE NUMBERS COLLIDE IN A THUNDEROUS EMBRACE! {a} + {b} = {result}! THE EARTH TREMBLES!"`
- Level 5: `"⚡ ADDITION OF COSMIC PROPORTIONS ⚡ {a} + {b} = {result}! GALAXIES WEEP AT THIS MAGNIFICENCE!"`

**Subtraction:**
- Level 1: `"{a} reluctantly parts with {b}. The remainder, {result}, sighs quietly."`
- Level 3: `"A DRAMATIC SEPARATION! {a} LOSES {b} AND IS LEFT WITH {result}! THE CROWD GASPS!"`
- Level 5: `"🔥 SUBTRACTION OF APOCALYPTIC SCALE! {a} MINUS {b} YIELDS {result}! DIMENSIONS SHATTER!"`

**Multiplication:**
- Level 1: `"{a} and {b} reproduce. Their offspring: {result}. Nature finds a way."`
- Level 3: `"MULTIPLICATION MAYHEM! {a} × {b} = {result}! THE CALCULATOR NEEDS A MOMENT!"`
- Level 5: `"💥 {a} × {b} = {result}!!! THE NUMBERS HAVE ACHIEVED CRITICAL MASS!"`

**Division:**
- Level 1: `"{a} is carefully sliced into {b} pieces. Each piece: {result}."`
- Level 3: `"THE GREAT DIVISION! {a} ÷ {b} = {result}! SOLOMON HIMSELF COULD NOT DO BETTER!"`
- Level 5: `"🌋 DIVISION BEYOND MORTAL COMPREHENSION! {a} ÷ {b} = {result}!"`

**Exponentiation:**
- Any level: `"{a} RAISES ITSELF {b} TIMES! THE POWER... IT'S OVER {result}!"`

**Factorial:**
- Any level: `"{a}! = {result}. That's {a} multiplied by ALL ITS PREDECESSORS. Every. Single. One."`

**Error narrations:**
- `narrate_error(error: OutlandishError) -> str` — dramatic error messages
- Pool of 3+ error wrappers: `"CATASTROPHE! {msg}"`, `"THE CALCULATOR HAS ENCOUNTERED... {msg}"`, `"*dramatic pause* ...{msg}"`

### 3. ASCII Art (`ascii_art.py`)

Visual flair for operations and results.

**Implementation:**
- `get_operation_art(operation: str) -> str` — returns ASCII art for the operation
- `get_result_banner(value: float, drama_level: int) -> str` — returns result display

**Required art pieces:**

```python
EXPLOSION = r"""
    \         .  ./
  \      .:";'.:.."   /
      (M]d;:diffutils"/)
    \       'googol!'    ./
  \  .:. ;.:.." ;.  :.: /
      .:;  :;diffutils ;:
    (googol googol)
"""

SMALL_RESULT = r"""
  ┌─────────┐
  │ {result} │
  └─────────┘
"""

MEDIUM_RESULT = r"""
  ╔═══════════════╗
  ║   {result}    ║
  ║   ✨ nice ✨   ║
  ╚═══════════════╝
"""

BIG_RESULT = r"""
  ╔══════════════════════════╗
  ║  🔥🔥🔥🔥🔥🔥🔥🔥🔥  ║
  ║       {result}           ║
  ║  🔥🔥🔥🔥🔥🔥🔥🔥🔥  ║
  ╚══════════════════════════╝
"""
```

- drama_level 1-2: SMALL_RESULT
- drama_level 3-4: MEDIUM_RESULT
- drama_level 5: BIG_RESULT
- Operations (+, -, *, /) each have a small ASCII symbol art

### 4. Calculation History (`history.py`)

Track and replay past calculations with dramatic commentary.

**Implementation:**
- `History` class with:
  - `add(result: CalcResult) -> None` — stores calculation
  - `replay() -> str` — replays all calculations with "PREVIOUSLY ON OUTLANDISH CALCULATOR..."
  - `last() -> CalcResult | None` — returns most recent
  - `clear() -> str` — clears with dramatic message: "THE SLATE IS WIPED CLEAN! MEMORIES... ERASED!"
  - `stats() -> dict` — returns `{total_calculations: int, biggest_result: float, most_dramatic: CalcResult}`
  - Max 100 entries, FIFO eviction

### 5. Easter Eggs (`easter_eggs.py`)

Special behaviors for magic numbers.

**Implementation:**
- `check_easter_egg(result: CalcResult) -> str | None` — returns special message or None
- Required easter eggs:
  - Result is **42**: `"🌌 THE ANSWER TO LIFE, THE UNIVERSE, AND EVERYTHING! Douglas Adams smiles from beyond."`
  - Result is **69**: `"nice."`
  - Result is **404**: `"RESULT NOT FO-- wait, it's {result}. Never mind."`
  - Result is **666**: `"👹 THE CALCULATOR GROWS WARM TO THE TOUCH... 👹"`
  - Result is **π (3.14159...)**: `"Mmm... pie. 🥧"` (check within 0.001 tolerance)
  - Result is **0**: `"Nothing. The void stares back. 🕳️"`
  - Result is **negative**: `"The result has gone to the SHADOW REALM: {result}"`
  - Result is **infinity**: `"♾️ INFINITY! THE CALCULATOR HAS TRANSCENDED MORTAL BOUNDS! ♾️"`

### 6. REPL Interface (`__main__.py`)

Interactive command loop.

**Implementation:**
- Print welcome banner on start (dramatic ASCII art title)
- Prompt: `"🔮 Enter thy calculation: "`
- Parse input, calculate, narrate, show art, check easter eggs
- Special commands:
  - `history` — show replay
  - `stats` — show calculation stats
  - `clear` — clear history
  - `help` — show operations list
  - `quit` or `exit` — dramatic farewell: `"THE CALCULATOR BIDS YOU FAREWELL... UNTIL WE CALCULATE AGAIN! 🎭"`
- After each calculation, display in order: ASCII art → narration → easter egg (if any)
- Handle `KeyboardInterrupt` gracefully with `"THE CALCULATOR CANNOT BE SILENCED BY MERE CTRL+C!... okay fine, goodbye. 👋"`

**Welcome banner:**
```
╔══════════════════════════════════════════════╗
║   🎭 THE OUTLANDISH CALCULATOR 🎭            ║
║   Where every equation is an EXPERIENCE      ║
║                                              ║
║   Type 'help' for commands                   ║
║   Type 'quit' to leave (if you dare)         ║
╚══════════════════════════════════════════════╝
```

## Error Handling

All errors MUST be instances of `OutlandishError(Exception)` defined in `engine.py`.
- Invalid expression: `OutlandishError("THE CALCULATOR CANNOT COMPREHEND: '{expr}'")`
- Overflow: `OutlandishError("THE NUMBER IS TOO POWERFUL! IT HAS ESCAPED THE CALCULATOR!")`
- Any unexpected error: wrap in `OutlandishError("SOMETHING DEEPLY WRONG HAS OCCURRED: {e}")`

## Test Requirements

Every module MUST have corresponding tests in `tests/`:

- **test_engine.py**: Test all 8 operations with normal inputs, edge cases (0, negative, large numbers), and all 3 error conditions
- **test_narrator.py**: Test that narrate() returns non-empty strings for each operation and drama level, test error narrations
- **test_ascii_art.py**: Test that art functions return non-empty strings, test each drama level bracket
- **test_history.py**: Test add/replay/last/clear/stats, test FIFO eviction at 100 entries
- **test_easter_eggs.py**: Test all 8 easter eggs trigger correctly, test non-easter-egg numbers return None
- **test_repl.py**: Test REPL processes expressions correctly, test special commands (history, stats, clear, help, quit)

All tests MUST use real function calls — NO MOCKING.
