from typing import List, Dict
from datetime import datetime, time

from mcp.server.fastmcp import FastMCP

from restaurant_data import MENU, TABLES, OPERATING_HOURS

mcp = FastMCP("Restaurant", port=3900)


@mcp.tool(name="get_all_menu", description="Get all menu items from all categories")
def get_all_menu_items() -> List[Dict]:
    """Get all menu items from all categories"""
    all_items = []
    for category, items in MENU.items():
        for item in items:
            item_copy = item.copy()
            item_copy["category"] = category
            all_items.append(item_copy)
    return all_items


@mcp.tool(name="get_menu_by_category", description="Get menu items by category")
def get_menu_by_category(category: str) -> List[Dict]:
    """Get menu items by category"""
    return MENU.get(category.lower(), [])


@mcp.tool(name="get_vegetarian_menu", description="Get all vegetarian items")
def get_vegetarian_items() -> List[Dict]:
    """Get all vegetarian items"""
    all_items = get_all_menu_items()
    return [item for item in all_items if item["vegetarian"]]


@mcp.tool(name="get_non_vegetarian_menu", description="Get all non-vegetarian items")
def get_non_vegetarian_items() -> List[Dict]:
    """Get all non-vegetarian items"""
    all_items = get_all_menu_items()
    return [item for item in all_items if not item["vegetarian"]]


@mcp.tool(name="get_available_tables", description="Get all available tables")
def get_available_tables() -> Dict:
    """Get all available tables"""
    return {table_id: info for table_id, info in TABLES.items() if info["status"] == "available"}


@mcp.tool(name="is_restaurant_open", description="Check if restaurant is currently open")
def is_restaurant_open() -> bool:
    """Check if restaurant is currently open"""
    now = datetime.now()
    day = now.strftime("%A").lower()

    if day not in OPERATING_HOURS:
        return False

    current_time = now.time()
    open_time = datetime.strptime(OPERATING_HOURS[day]["open"], "%H:%M").time()
    close_time = datetime.strptime(OPERATING_HOURS[day]["close"], "%H:%M").time()

    return open_time <= current_time <= close_time


if __name__ == "__main__":
    mcp.run(transport="streamable-http")


