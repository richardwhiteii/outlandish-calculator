# outlandish-calc - Sprint 1: MVP Sprint

The Outlandish Calculator is a theatrical CLI Python application that performs math with dramatic narration, ASCII art, and existential commentary. It features a core math engine, a dramatic narrator, calculation history, and hidden easter eggs, all wrapped in a robust REPL interface.

```json
{
  "project": "outlandish-calc",
  "sprint_slug": "mvp",
  "repo": "test/outlandish-calc",
  "ticket_prefix": "CALC",
  "total_tickets": 14,
  "estimated_hours": 30,
  "milestone": "Sprint 1: MVP",
  "stub_policy": "none_required",
  "stub_contracts": [],
  "categories": {
    "CORE": {
      "priority": "P0",
      "tickets": "001",
      "description": "Foundational math engine and error handling logic."
    },
    "TESTS": {
      "priority": "P0",
      "tickets": "002-009",
      "description": "Comprehensive test suites for all modules to ensure reliability without mocking."
    },
    "UI": {
      "priority": "P1",
      "tickets": "003-004",
      "description": "Visual and narrative components including ASCII art and dramatic text generation."
    },
    "FEATURES": {
      "priority": "P1",
      "tickets": "005-006",
      "description": "Extended functionality such as calculation history and easter egg triggers."
    },
    "CLI": {
      "priority": "P2",
      "tickets": "008",
      "description": "The interactive REPL loop and command-line interface."
    },
    "SEC": {
      "priority": "P0",
      "tickets": "010-014",
      "description": "Security scan gates \u2014 one per category"
    }
  },
  "parallel_tickets": [
    "002",
    "003",
    "004",
    "005",
    "006"
  ]
}
```

## Sprint Summary

| # | Title | Priority | Category | Estimate | Depends |
|---|-------|----------|----------|----------|---------|
| CALC-001 | Implement Core Math Engine and Exceptions | P0 | CORE | 4h | None |
| CALC-002 | Develop Math Engine Unit Tests | P0 | TESTS | 2h | 001 |
| CALC-003 | Implement Dramatic Narrator | P1 | UI | 3h | 001 |
| CALC-004 | Create ASCII Art Assets | P1 | UI | 2h | None |
| CALC-005 | Implement Calculation History | P1 | FEATURES | 3h | 001 |
| CALC-006 | Implement Easter Egg Logic | P1 | FEATURES | 2h | 001 |
| CALC-007 | Implement UI and Feature Unit Tests | P1 | TESTS | 3h | 005 |
| CALC-008 | Implement CLI REPL Interface | P2 | CLI | 4h | 001 |
| CALC-009 | Implement REPL Integration Tests | P2 | TESTS | 2h | 008 |

## CORE

### CALC-001: Implement Core Math Engine and Exceptions
**Priority:** P0 | **Category:** CORE | **Estimate:** 4h
**File:** `outlandish_calc/engine.py`
**Depends:** None

Develop the primary calculation logic and custom exception classes. This includes the CalcResult dataclass and the drama_level calculation logic based on result magnitude.

**Acceptance Criteria:**
- [ ] The calculate() function MUST support all 8 operations: +, -, *, /, **, %, sqrt, and !.
- [ ] The CalcResult dataclass MUST include value, operation, operands, and drama_level.
- [ ] OutlandishError MUST be raised for division by zero, negative square roots, and negative factorials.
- [ ] The drama_level MUST be correctly assigned from 1 to 5 based on the result magnitude thresholds defined in the PRD.

### CALC-011: [SEC] Security Scan - CORE
**Priority:** P0 | **Category:** SEC | **Estimate:** 1h
**Depends:** CALC-001

Run automated security scan on all files modified in the CORE category.

**Acceptance Criteria:**
- [ ] Security scan completes on all category files
- [ ] No CRITICAL or HIGH severity findings remain
- [ ] Verification report generated

## TESTS

### CALC-002: Develop Math Engine Unit Tests
**Priority:** P0 | **Category:** TESTS | **Estimate:** 2h
**File:** `tests/test_engine.py`
**Depends:** 001

Create a comprehensive test suite for the engine module using pytest. Tests must use real function calls and cover all edge cases and error conditions.

**Acceptance Criteria:**
- [ ] Tests MUST verify all 8 math operations with both integer and float inputs.
- [ ] Tests MUST assert that OutlandishError is raised with the correct dramatic message for invalid operations.
- [ ] Tests MUST verify that drama_level is correctly calculated for values across all five magnitude brackets.

### CALC-007: Implement UI and Feature Unit Tests
**Priority:** P1 | **Category:** TESTS | **Estimate:** 3h
**File:** `tests/test_history.py`
**Depends:** 005

Write unit tests for the narrator, ASCII art, history, and easter egg modules. Ensure all logic paths are covered without using mocks.

**Acceptance Criteria:**
- [ ] Tests MUST verify that History evicts the oldest record when the 101st calculation is added.
- [ ] Tests MUST verify that all 8 easter eggs trigger correctly with their respective values.
- [ ] Tests MUST verify that get_result_banner returns the correct ASCII string for each drama_level bracket.

### CALC-009: Implement REPL Integration Tests
**Priority:** P2 | **Category:** TESTS | **Estimate:** 2h
**File:** `tests/test_repl.py`
**Depends:** 008

Create integration tests for the REPL loop to ensure all components work together and commands are processed correctly.

**Acceptance Criteria:**
- [ ] Tests MUST verify that entering a math expression results in the full dramatic output sequence.
- [ ] Tests MUST verify that the 'history' command correctly displays the replay string.
- [ ] Tests MUST verify that invalid expressions are caught and displayed using the dramatic error narrator.

### CALC-013: [SEC] Security Scan - TESTS
**Priority:** P0 | **Category:** SEC | **Estimate:** 1h
**Depends:** CALC-009

Run automated security scan on all files modified in the TESTS category.

**Acceptance Criteria:**
- [ ] Security scan completes on all category files
- [ ] No CRITICAL or HIGH severity findings remain
- [ ] Verification report generated

## UI

### CALC-003: Implement Dramatic Narrator
**Priority:** P1 | **Category:** UI | **Estimate:** 3h
**File:** `outlandish_calc/narrator.py`
**Depends:** 001

Build the narration engine that generates theatrical descriptions of calculations. Each operation requires multiple templates that scale in intensity with the drama_level.

**Acceptance Criteria:**
- [ ] The narrate() function MUST return a string from a pool of at least 3 templates per operation.
- [ ] Narration intensity MUST increase as the drama_level moves from 1 to 5.
- [ ] The narrate_error() function MUST wrap OutlandishError messages in one of the 3+ dramatic error templates.

### CALC-004: Create ASCII Art Assets
**Priority:** P1 | **Category:** UI | **Estimate:** 2h
**File:** `outlandish_calc/ascii_art.py`
**Depends:** None

Implement the visual components of the calculator, including operation symbols and result banners. The banners must change based on the drama_level of the result.

**Acceptance Criteria:**
- [ ] The get_result_banner() function MUST return SMALL_RESULT for levels 1-2, MEDIUM_RESULT for 3-4, and BIG_RESULT for level 5.
- [ ] The EXPLOSION constant MUST be implemented exactly as specified in the PRD.
- [ ] The get_operation_art() function MUST return unique ASCII symbols for +, -, *, and /.

### CALC-014: [SEC] Security Scan - UI
**Priority:** P0 | **Category:** SEC | **Estimate:** 1h
**Depends:** CALC-004

Run automated security scan on all files modified in the UI category.

**Acceptance Criteria:**
- [ ] Security scan completes on all category files
- [ ] No CRITICAL or HIGH severity findings remain
- [ ] Verification report generated

## FEATURES

### CALC-005: Implement Calculation History
**Priority:** P1 | **Category:** FEATURES | **Estimate:** 3h
**File:** `outlandish_calc/history.py`
**Depends:** 001

Develop a history tracking system that stores past calculations and provides statistics. The system must handle dramatic replays and clear operations.

**Acceptance Criteria:**
- [ ] The History class MUST store a maximum of 100 entries using FIFO eviction.
- [ ] The stats() method MUST return a dictionary containing total_calculations, biggest_result, and most_dramatic.
- [ ] The clear() method MUST return the specific dramatic erasure message defined in the PRD.

### CALC-006: Implement Easter Egg Logic
**Priority:** P1 | **Category:** FEATURES | **Estimate:** 2h
**File:** `outlandish_calc/easter_eggs.py`
**Depends:** 001

Create a module to detect and respond to 'magic' numbers with special messages. This adds the comedic 'performance art' layer to the calculator.

**Acceptance Criteria:**
- [ ] The check_easter_egg() function MUST return the correct dramatic string for all 8 specified triggers (42, 69, 404, 666, pi, 0, negative, infinity).
- [ ] The pi trigger MUST use a tolerance of 0.001.
- [ ] The function MUST return None for any result that does not match an easter egg condition.

### CALC-012: [SEC] Security Scan - FEATURES
**Priority:** P0 | **Category:** SEC | **Estimate:** 1h
**Depends:** CALC-006

Run automated security scan on all files modified in the FEATURES category.

**Acceptance Criteria:**
- [ ] Security scan completes on all category files
- [ ] No CRITICAL or HIGH severity findings remain
- [ ] Verification report generated

## CLI

### CALC-008: Implement CLI REPL Interface
**Priority:** P2 | **Category:** CLI | **Estimate:** 4h
**File:** `outlandish_calc/__main__.py`
**Depends:** 001

Assemble all components into an interactive command-line loop. This includes handling user input, executing calculations, and displaying the dramatic output sequence.

**Acceptance Criteria:**
- [ ] The REPL MUST display the welcome banner on startup and the specific farewell message on 'quit' or 'exit'.
- [ ] The output sequence for a calculation MUST be: ASCII Art -> Narration -> Easter Egg (if applicable).
- [ ] The REPL MUST handle 'history', 'stats', 'clear', and 'help' as special commands.
- [ ] KeyboardInterrupt MUST be caught to display the dramatic 'cannot be silenced' message before exiting.

### CALC-010: [SEC] Security Scan - CLI
**Priority:** P0 | **Category:** SEC | **Estimate:** 1h
**Depends:** CALC-008

Run automated security scan on all files modified in the CLI category.

**Acceptance Criteria:**
- [ ] Security scan completes on all category files
- [ ] No CRITICAL or HIGH severity findings remain
- [ ] Verification report generated

## Spec Files Cross-Reference

| Spec | Purpose |
|------|---------|
