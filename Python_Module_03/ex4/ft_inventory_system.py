"""
ft_inventory_system.py

Exercise: Inventory Master (Data Quest)
Authorized: dict(), len(), print(), keys(), values(), items(), get(), update()

This script demonstrates how to manage RPG-like inventories using dictionaries:
- store item details (type, rarity, value, quantity)
- calculate total value and total item count
- group items by category
- transfer items between players
- print reports and simple analytics
"""


def item_line(name: str, data: dict) -> str:
    """
    Build a single printable line for one item.

    Args:
        name: Item name (dictionary key).
        data: Item details dictionary with keys:
              "type", "rarity", "value", "quantity".

    Returns:
        A formatted string describing the item and its total value.
    """
    itype = data.get("type")
    rarity = data.get("rarity")
    qty = data.get("quantity")
    value = data.get("value")
    total = qty * value

    return (
        f"{name} ({itype}, {rarity}): "
        f"{qty}x @ {value} gold each = {total} gold"
    )


def total_inventory_value(inv: dict) -> int:
    """
    Calculate total gold value of an inventory.

    Args:
        inv: Inventory dictionary (item_name -> item_details dict).

    Returns:
        Total value (sum of quantity * value for each item).
    """
    total = 0
    for data in inv.values():
        qty = data.get("quantity")
        value = data.get("value")
        total += qty * value
    return total


def total_item_count(inv: dict) -> int:
    """
    Calculate total number of items (sum of quantities) in inventory.

    Args:
        inv: Inventory dictionary.

    Returns:
        Total quantity of all items.
    """
    count = 0
    for data in inv.values():
        count += data.get("quantity")
    return count


def category_counts(inv: dict) -> dict:
    """
    Count quantities by category (type).

    Args:
        inv: Inventory dictionary.

    Returns:
        A dictionary mapping type -> total quantity.
    """
    counts = dict()

    for data in inv.values():
        itype = data.get("type")
        qty = data.get("quantity")
        counts[itype] = counts.get(itype, 0) + qty

    return counts


def format_categories(counts: dict) -> str:
    """
    Format category counts in a stable order like the example output.

    Args:
        counts: Dict type -> total quantity.

    Returns:
        A string like: "weapon(1), consumable(5), armor(1)"
    """
    result = ""
    first = True

    ordered = ("weapon", "consumable", "armor", "accessory")
    for itype in ordered:
        qty = counts.get(itype)
        if qty is None:
            continue
        part = f"{itype}({qty})"
        if first:
            result = part
            first = False
        else:
            result = result + ", " + part

    return result


def transfer_item(from_inv: dict, to_inv: dict, name: str, qty: int) -> bool:
    """
    Transfer qty of an item from one inventory to another.

    Args:
        from_inv: Source inventory.
        to_inv: Destination inventory.
        name: Item name to transfer.
        qty: Quantity to transfer (must be positive and available).

    Returns:
        True if transfer succeeded, False otherwise.
    """
    if qty <= 0:
        return False

    src_item = from_inv.get(name)
    if src_item is None:
        return False

    src_qty = src_item.get("quantity")
    if src_qty < qty:
        return False

    src_item["quantity"] = src_qty - qty

    dst_item = to_inv.get(name)
    if dst_item is None:
        to_inv[name] = dict()
        to_inv[name].update({"type": src_item.get("type")})
        to_inv[name].update({"rarity": src_item.get("rarity")})
        to_inv[name].update({"value": src_item.get("value")})
        to_inv[name].update({"quantity": 0})
        dst_item = to_inv.get(name)

    dst_item["quantity"] = dst_item.get("quantity") + qty
    return True


def most_valuable_player(values: dict) -> str:
    """
    Find the player with the highest total value.

    Args:
        values: Dict player_name -> total_value.

    Returns:
        Player name with maximum value.
    """
    best_name = ""
    best_value = -1

    for name, val in values.items():
        if val > best_value:
            best_value = val
            best_name = name

    return best_name


def most_items_player(counts: dict) -> str:
    """
    Find the player with the highest total item quantity.

    Args:
        counts: Dict player_name -> total_item_count.

    Returns:
        Player name with maximum item count.
    """
    best_name = ""
    best_count = -1

    for name, cnt in counts.items():
        if cnt > best_count:
            best_count = cnt
            best_name = name

    return best_name


def rare_items_report(inventories: dict) -> str:
    """
    Collect rare/epic/legendary item names across all inventories.

    Args:
        inventories: Dict player_name -> inventory dict.

    Returns:
        Comma-separated string of rare items (stable order of discovery).
    """
    seen = dict()
    result = ""
    first = True

    for inv in inventories.values():
        for name, data in inv.items():
            rarity = data.get("rarity")
            if rarity not in ("rare", "epic", "legendary"):
                continue
            if name in seen:
                continue
            seen[name] = 1

            if first:
                result = name
                first = False
            else:
                result = result + ", " + name

    return result


def main() -> None:
    """Run the inventory demo and print analytics."""
    print("=== Player Inventory System ===")

    alice_items = dict()
    alice_items.update(
        {
            "sword": {
                "type": "weapon",
                "rarity": "rare",
                "value": 500,
                "quantity": 1,
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
                "quantity": 1,
            },
        }
    )

    bob_items = dict()
    bob_items.update(
        {
            "potion": {
                "type": "consumable",
                "rarity": "common",
                "value": 50,
                "quantity": 0,
            },
            "magic_ring": {
                "type": "accessory",
                "rarity": "epic",
                "value": 300,
                "quantity": 1,
            },
        }
    )

    inventories = dict()
    inventories.update({"Alice": alice_items})
    inventories.update({"Bob": bob_items})

    print("=== Alice's Inventory ===")
    for name, data in inventories.get("Alice").items():
        print(item_line(name, data))

    a_inv = inventories.get("Alice")
    a_value = total_inventory_value(a_inv)
    a_count = total_item_count(a_inv)
    cats = category_counts(a_inv)

    print(f"Inventory value: {a_value} gold")
    print(f"Item count: {a_count} items")
    print(f"Categories: {format_categories(cats)}")

    print("=== Transaction: Alice gives Bob 2 potions ===")
    ok = transfer_item(
        inventories.get("Alice"),
        inventories.get("Bob"),
        "potion",
        2,
    )
    if ok:
        print("Transaction successful!")
    else:
        print("Transaction failed!")

    print("=== Updated Inventories ===")
    alice_potions = inventories.get("Alice").get("potion").get("quantity")
    bob_potions = inventories.get("Bob").get("potion").get("quantity")
    print(f"Alice potions: {alice_potions}")
    print(f"Bob potions: {bob_potions}")

    print("=== Inventory Analytics ===")

    values = dict()
    counts = dict()
    for player, inv in inventories.items():
        values[player] = total_inventory_value(inv)
        counts[player] = total_item_count(inv)

    best_value_player = most_valuable_player(values)
    best_items_player = most_items_player(counts)

    best_value_gold = values.get(best_value_player)
    best_items_qty = counts.get(best_items_player)

    print(
        f"Most valuable player: {best_value_player} "
        f"({best_value_gold} gold)"
    )
    print(
        f"Most items: {best_items_player} "
        f"({best_items_qty} items)"
    )
    print(f"Rarest items: {rare_items_report(inventories)}")


if __name__ == "__main__":
    main()
