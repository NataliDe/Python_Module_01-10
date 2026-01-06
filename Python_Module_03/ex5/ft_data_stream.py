#!/usr/bin/env python3


def game_event_stream(n: int):
    event_types = ["kill", "treasure", "level_up", "login", "logout"]
    players = ["alice", "bob", "charlie", "diana"]
    zones = ["pixel_zone_1", "pixel_zone_2", "pixel_zone_3"]

    for i in range(1, n + 1):
        player = players[i % len(players)]
        event_type = event_types[i % len(event_types)]
        level = (i % 25) + 1
        zone = zones[i % len(zones)]
        yield {
            "id": i,
            "player": player,
            "level": level,
            "event_type": event_type,
            "zone": zone,
        }


def fibonacci():
    a = 0
    b = 1
    while True:
        yield a
        a, b = b, a + b


def primes():
    n = 2
    while True:
        is_prime = True
        d = 2
        while d * d <= n:
            if n % d == 0:
                is_prime = False
                break
            d += 1
        if is_prime:
            yield n
        n += 1


def main() -> None:
    total = 1000
    print("=== Game Data Stream Processor ===")
    print(f"Processing {total} game events...")

    processed = 0
    high_level = 0
    treasure_events = 0
    level_up_events = 0

    for ev in game_event_stream(total):
        processed += 1

        if processed <= 3:
            et = ev["event_type"]
            p = ev["player"]
            lvl = ev["level"]
            if et == "kill":
                print(
                    f"Event {processed}: Player {p} "
                    f"(level {lvl}) killed monster"
                )
            elif et == "treasure":
                print(
                    f"Event {processed}: Player {p} "
                    f"(level {lvl}) found treasure"
                )
            elif et == "level_up":
                print(
                    f"Event {processed}: Player {p} "
                    f"(level {lvl}) leveled up"
                )
            else:
                print(f"Event {processed}: Player {p} (level {lvl}) {et}")

        if ev["level"] >= 10:
            high_level += 1
        if ev["event_type"] == "treasure":
            treasure_events += 1
        if ev["event_type"] == "level_up":
            level_up_events += 1

    print("=== Stream Analytics ===")
    print(f"Total events processed: {processed}")
    print(f"High-level players (10+): {high_level}")
    print(f"Treasure events: {treasure_events}")
    print(f"Level-up events: {level_up_events}")
    print("Memory usage: Constant (streaming)")

    print("=== Generator Demonstration ===")

    fib = fibonacci()
    fib_first_10 = []
    for _ in range(10):
        fib_first_10.append(next(fib))
    fib_str = ", ".join(str(x) for x in fib_first_10)
    print(f"Fibonacci sequence (first 10): {fib_str}")

    pr = primes()
    prime_first_5 = []
    for _ in range(5):
        prime_first_5.append(next(pr))
    prime_str = ", ".join(str(x) for x in prime_first_5)
    print(f"Prime numbers (first 5): {prime_str}")


if __name__ == "__main__":
    main()
