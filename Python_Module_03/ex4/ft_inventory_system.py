#!/usr/bin/env python3


def item_line(name: str, data: dict) -> str:
    itype = data.get("type")
    rarity = data.get("rarity")
    qty = data.get("quantity")
    price = data.get("value")
    total = qty * price
    return (f"{name} ({itype}, {rarity}): {qty}x @ {price} gold each "
            f"= {total} gold")


def total_value(inv: dict[str, dict]) -> int:
    return sum(d["quantity"] * d["value"] for d in inv.values())


def total_items(inv: dict[str, dict]) -> int:
    return sum(d["quantity"] for d in inv.values())


def category_counts(inv: dict[str, dict]) -> dict[str, int]:
    counts: dict[str, int] = {}
    for data in inv.values():
        itype = data.get("type")
        qty = data.get("quantity")
        counts[itype] = counts.get(itype, 0) + qty
    return counts


def transfer(
    from_inv: dict[str, dict],
    to_inv: dict[str, dict],
    item: str,
    qty: int,
) -> bool:
    if item not in from_inv:
        return False
    if from_inv[item]["quantity"] < qty:
        return False

    from_inv[item]["quantity"] -= qty

    if item not in to_inv:
        to_inv[item] = {
            "type": from_inv[item]["type"],
            "rarity": from_inv[item]["rarity"],
            "value": from_inv[item]["value"],
            "quantity": 0,
        }
    to_inv[item]["quantity"] += qty
    return True


def main() -> None:
    print("=== Player Inventory System ===")

    alice_items = {
        "sword": {
            "type": "weapon",
            "rarity": "rare",
            "value": 500,
            "quantity": 1
        },
        "potion": {
            "type": "consumable",
            "rarity": "common",
            "value": 50,
            "quantity": 5,
        },
        "shield": {
            "type": "armor",
            "rarity": "uncommon",
            "value": 200,
            "quantity": 1
        },
        "boots": {
            "type": "armor",
            "rarity": "common",
            "value": 75,
            "quantity": 1,
        },

        "magic_ring": {
            "type": "accessory",
            "rarity": "epic",
            "value": 300,
            "quantity": 1,
        },
    }

    bob_items = {
        "potion": {
            "type": "consumable",
            "rarity": "common",
            "value": 50,
            "quantity": 0
            },
        "dagger": {
            "type": "weapon",
            "rarity": "common",
            "value": 90,
            "quantity": 1
            },
    }

    inventories = {
        "Alice": alice_items,
        "Bob": bob_items,
    }

    print("=== Alice's Inventory ===")
    for name, data in inventories["Alice"].items():
        print(item_line(name, data))

    a_value = total_value(inventories["Alice"])
    a_count = total_items(inventories["Alice"])
    cats = category_counts(inventories["Alice"])

    print(f"Inventory value: {a_value} gold")
    print(f"Item count: {a_count} items")

    cats_str = ", ".join(f"{k}({v})" for k, v in cats.items())
    print(f"Categories: {cats_str}")

    print("=== Transaction: Alice gives Bob 2 potions ===")
    ok = transfer(inventories["Alice"], inventories["Bob"], "potion", 2)
    if ok:
        print("Transaction successful!")
    else:
        print("Transaction failed!")

    print("=== Updated Inventories ===")
    print(f"Alice potions: {inventories['Alice']['potion']['quantity']}")
    print(f"Bob potions: {inventories['Bob']['potion']['quantity']}")

    print("=== Inventory Analytics ===")
    values = {p: total_value(inv) for p, inv in inventories.items()}
    most_valuable = max(values, key=lambda k: values[k])

    uniques = {p: len(inv.keys()) for p, inv in inventories.items()}
    most_items = max(uniques, key=lambda k: uniques[k])

    rarest = []
    for inv in inventories.values():
        for name, data in inv.items():
            if data.get("rarity") in ("rare", "epic", "legendary"):
                if name not in rarest:
                    rarest.append(name)

    print(
        f"Most valuable player: {most_valuable} "
        f"({values[most_valuable]} gold)"
    )

    print(f"Most items: {most_items} ({uniques[most_items]} items)")
    print(f"Rarest items: {', '.join(rarest)}")


if __name__ == "__main__":
    main()
