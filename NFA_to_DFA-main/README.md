# NFA to DFA Web Server

A REST API that converts a Nondeterministic Finite Automaton (NFA) into its
equivalent Deterministic Finite Automaton (DFA) using the Subset Construction
Algorithm (Kozen, *Automata and Computability*, Lecture 6).

## Environment

- OS: Windows 11 Pro (build 10.0.26200.0)
- Python: 3.11.9
- Framework: Flask 3.0.3
- Testing: pytest 8.3.3

## Project structure

src/
├── controllers/ # HTTP layer: receives requests, validates input, returns responses
├── gateways/ # Orchestration layer: calls Functions, handles exceptions
├── functions/ # Pure automata algorithms, no HTTP-related code
└── app.py # Application entry point
tests/ # Automated tests (pytest)


## How to run

1. Create and activate a virtual environment:

python -m venv .venv
.venv\Scripts\activate

2. Install dependencies:

pip install -r requirements.txt

3. Start the server:

python src\app.py

   The server will run on `http://127.0.0.1:5000`.

## How to run the tests

pytest tests/


## Endpoints

### POST /convert

Converts an NFA into its equivalent DFA.

**Request body:**
```json
{
    "states": [0, 1, 2, 3],
    "alphabet": ["a", "b"],
    "initial": 0,
    "accepting": [3],
    "transitions": [
        {"from": 0, "symbol": "a", "to": 1}
    ]
}
```

Epsilon transitions are represented with `"symbol": null`.

**Response body:**
```json
{
    "dfaStates": ["0", "1", "dead"],
    "transitions": [...],
    "acceptingStates": ["1"]
}
```

### POST /simulate

Simulates a DFA against an input string.

**Request body:**
```json
{
    "initial": "0",
    "accepting": ["1"],
    "input": "ab",
    "transitions": [...]
}
```

**Response body:**
```json
{
    "path": ["0", "1"],
    "accepted": true
}
```

## Algorithm overview

The server implements the **Subset Construction Algorithm**: given an NFA,
each state of the resulting DFA represents a *set* of NFA states that could
be active simultaneously.

1. **Epsilon closure**: for any set of NFA states, compute every state
   reachable without consuming input (following epsilon transitions).
2. **Move**: for a set of NFA states and a symbol, compute every state
   reachable by consuming that symbol.
3. Starting from the epsilon closure of the initial state(s), repeatedly
   apply `move` + `epsilon closure` for every symbol in the alphabet,
   discovering new DFA states until no new states appear.
4. A DFA state is accepting if the NFA state set it represents contains
   at least one accepting NFA state.
5. To make the transition function total, any symbol with no reachable
   states leads to a special absorbing `dead` state (representing the
   empty set), which loops to itself for every symbol.

## Team

- Juan José Sierra Ocampo
- Miguel Muñoz Jiménez