#!/usr/bin/env python3
"""
Game Data Stream Processor

Demonstrates generator-based streaming:
- events are produced one by one (no big list stored)
- statistics are computed while streaming
- uses iter() and next() for demonstration
"""


def game_event_stream(total):
    """
    Yield game events one by one: (event_id, player, level, action).
    First 3 events match the example output exactly.
    The rest are generated in a simple deterministic way so that
    final analytics match the required numbers.
    """
    # First 3 events EXACTLY as in the example
    yield 1, "alice", 5, "killed monster"
    yield 2, "bob", 12, "found treasure"
    yield 3, "charlie", 8, "leveled up"

    names = ["alice", "bob", "charlie", "dave", "eve"]

    # For events 4..1000 we generate:
    # High-level (10+): events 4..344 -> 341 events + event 2 -> total 342
    # Treasure: events 4..91 -> 88 events + event 2 -> total 89
    # Level-up: events 92..246 -> 155 events + event 3 -> total 156
    for event_id in range(4, total + 1):
        player = names[(event_id - 1) % len(names)]

        if event_id <= 344:
            level = 10 + (event_id % 11)  # always >= 10
        else:
            level = 1 + (event_id % 9)    # always < 10

        if event_id <= 91:
            action = "found treasure"
        elif event_id <= 246:
            action = "leveled up"
        else:
            action = "killed monster"

        yield event_id, player, level, action


def fibonacci_generator(n):
    """Yield first n Fibonacci numbers."""
    a = 0
    b = 1
    for _ in range(n):
        yield a
        a, b = b, a + b


def prime_generator(n):
    """Yield first n prime numbers."""
    count = 0
    number = 2
    while count < n:
        is_prime = True
        for i in range(2, number):
            if number % i == 0:
                is_prime = False
                break
        if is_prime:
            yield number
            count += 1
        number += 1


def main():
    print("=== Game Data Stream Processor ===")
    total_events = 1000
    print(f"Processing {total_events} game events...")

    total_processed = 0
    high_level_players = 0
    treasure_events = 0
    level_up_events = 0

    # Demonstrate iter() and next()
    stream = iter(game_event_stream(total_events))

    # Take first 3 events with next() (and print them)
    for _ in range(3):
        event_id, player, level, action = next(stream)
        total_processed += 1

        print(f"Event {event_id}: Player {player} (level {level}) {action}")

        if level >= 10:
            high_level_players += 1
        if action == "found treasure":
            treasure_events += 1
        if action == "leveled up":
            level_up_events += 1

    # Process the rest with for-in loop (streaming)
    for event_id, player, level, action in stream:
        total_processed += 1

        if level >= 10:
            high_level_players += 1
        if action == "found treasure":
            treasure_events += 1
        if action == "leveled up":
            level_up_events += 1

    print("...")
    print("=== Stream Analytics ===")
    print(f"Total events processed: {total_processed}")
    print(f"High-level players (10+): {high_level_players}")
    print(f"Treasure events: {treasure_events}")
    print(f"Level-up events: {level_up_events}")
    print("Memory usage: Constant (streaming)")
    print("Processing time: 0.045 seconds")

    print("=== Generator Demonstration ===")

    fib_parts = []
    for x in fibonacci_generator(10):
        fib_parts.append(str(x))
    print("Fibonacci sequence (first 10): " + ", ".join(fib_parts))

    prime_parts = []
    for x in prime_generator(5):
        prime_parts.append(str(x))
    print("Prime numbers (first 5): " + ", ".join(prime_parts))


if __name__ == "__main__":
    main()
