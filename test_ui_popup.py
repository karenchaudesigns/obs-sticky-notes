import subprocess
import time
from playwright.sync_api import sync_playwright

def test_popup_close_on_deselect():
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

            # Click on background to deselect
            page.locator("#overlay-container").dispatch_event('pointerdown')
            time.sleep(0.5)

            # Verify popup is hidden
            assert "hidden" in popup.get_attribute("class"), "Popup should be hidden after deselection"

            print("Popup close on deselect test passed!")
    finally:
        server.terminate()

if __name__ == "__main__":
    test_popup_close_on_deselect()
