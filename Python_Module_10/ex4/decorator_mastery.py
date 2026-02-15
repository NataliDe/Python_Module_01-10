
from functools import wraps
import time


def spell_timer(func: callable) -> callable:
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Casting {func.__name__}...")
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        elapsed = end - start
        print(f"Spell completed in {elapsed:.3f} seconds")
        return result

    return wrapper


def power_validator(min_power: int) -> callable:
    def decorator(func: callable) -> callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Prefer keyword argument
            if "power" in kwargs:
                power = kwargs.get("power", 0)
            else:
                # Try to locate power in common positions:
                # (power, ...) OR (self, power, ...) OR (self, name, power,)
                power = 0
                for idx in (0, 1, 2):
                    if len(args) > idx and isinstance(args[idx], int):
                        power = args[idx]
                        break

            if isinstance(power, int) and power >= min_power:
                return func(*args, **kwargs)
            return "Insufficient power for this spell"

        return wrapper

    return decorator


def retry_spell(max_attempts: int) -> callable:
    def decorator(func: callable) -> callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            attempt = 1
            while attempt <= max_attempts:
                try:
                    return func(*args, **kwargs)
                except Exception:
                    if attempt < max_attempts:
                        print(
                            f"Spell failed, retrying... "
                            f"(attempt {attempt}/{max_attempts})"
                        )
                        attempt += 1
                        continue
                    return (
                        f"Spell casting failed after :{max_attempts} attempts"
                        )
            return f"Spell casting failed after {max_attempts} attempts"
        return wrapper
    return decorator


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        cleaned = name.strip()
        if len(cleaned) < 3:
            return False
        if not any(ch.isalpha() for ch in cleaned):
            return False
        return all(ch.isalpha() or ch == " " for ch in cleaned)

    @power_validator(min_power=10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        """Return success message if power is sufficient."""
        return f"Successfully cast {spell_name} with {power} power"


@retry_spell(max_attempts=3)
@spell_timer       # знизу вгору
def fireball() -> str:
    time.sleep(0.101)
    return "Fireball cast!"


def main() -> None:
    print("\nTesting spell timer...")
    result = fireball()
    print(f"Result: {result}")

    print("\nTesting MageGuild...")
    print(MageGuild.validate_mage_name("Ariana"))
    print(MageGuild.validate_mage_name("X1"))

    guild = MageGuild()
    print(guild.cast_spell("Lightning", 15))
    print(guild.cast_spell("Lightning", 5))


if __name__ == "__main__":
    main()
