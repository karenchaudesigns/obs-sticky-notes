import subprocess
import time
from playwright.sync_api import sync_playwright

def test_popup_drag():
    server = subprocess.Popen(["python3", "-m", "http.server", "8080"])
    time.sleep(1)

    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()
            page.goto("http://localhost:8080/")

            # Click inside canvas to ensure it's loaded
            page.locator("#overlay-container").click()
            time.sleep(0.5)

            # First note
            note1 = page.locator("#canvas-note-note-1")
            note1.dispatch_event('pointerdown')

            # Click text to trigger popup
            note_content = note1.locator(".z-10").first
            note_content.click()
            time.sleep(0.5)

            # Verify popup is visible
            popup = page.locator("#popup-text-editor")
            assert not "hidden" in popup.get_attribute("class"), "Popup should be visible"

            # Get popup initial position
            box = popup.bounding_box()
            initial_x = box['x']
            initial_y = box['y']

            # Drag the header
            header = page.locator("#popup-header")
            header_box = header.bounding_box()

            # Mouse drag
            page.mouse.move(header_box['x'] + 10, header_box['y'] + 10)
            page.mouse.down()
            page.mouse.move(header_box['x'] + 110, header_box['y'] + 110, steps=10)
            page.mouse.up()

            time.sleep(0.5)
            new_box = popup.bounding_box()

            print(f"Initial: {initial_x}, {initial_y}")
            print(f"New: {new_box['x']}, {new_box['y']}")

            assert new_box['x'] > initial_x + 50, "Popup should have moved right"
            assert new_box['y'] > initial_y + 50, "Popup should have moved down"

            print("Popup drag test passed!")
    finally:
        server.terminate()

if __name__ == "__main__":
    test_popup_drag()
