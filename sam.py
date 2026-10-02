import requests
from bs4 import BeautifulSoup


def print_grid_from_google_doc(url):
    response = requests.get(url)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    table = soup.find("table")

    if table is None:
        raise ValueError("No table found in the document.")

    points = []

    # Skip the header row
    for row in table.find_all("tr")[1:]:
        cells = row.find_all(["td", "th"])

        if len(cells) < 3:
            continue

        x = int(cells[0].get_text(strip=True))
        character = cells[1].get_text(strip=True)
        y = int(cells[2].get_text(strip=True))

        points.append((x, y, character))

    if not points:
        return

    # Determine grid dimensions
    max_x = max(x for x, y, char in points)
    max_y = max(y for x, y, char in points)

    # Create grid filled with spaces
    grid = [
        [" "] * (max_x + 1)
        for _ in range(max_y + 1)
    ]

    # Place characters
    for x, y, character in points:
        grid[y][x] = character

    # Print from highest y to lowest y
    for y in range(max_y, -1, -1):
        print("".join(grid[y]))