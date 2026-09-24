from playwright.sync_api import sync_playwright

def test():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto('http://localhost:8000')

        # Wait for the note to appear
        note = page.locator('.note-container').first
        note.wait_for()

        # Get initial bounding box
        initial_box = note.bounding_box()
        print(f"Initial size: {initial_box['width']}x{initial_box['height']}")

        # Simulate wheel event (scroll up to zoom in)
        # Note: Playwright doesn't have a direct scroll on element, but we can use dispatch_event
        note.dispatch_event('wheel', {'deltaY': -100})

        # Give it a tiny bit of time
        page.wait_for_timeout(500)

        new_box = note.bounding_box()
        print(f"New size: {new_box['width']}x{new_box['height']}")

        if new_box['width'] > initial_box['width'] and new_box['height'] > initial_box['height']:
            print("Test passed: Element resized on scroll up")
        else:
            print("Test failed: Element did not resize")

        # Try shrinking
        note.dispatch_event('wheel', {'deltaY': 100})
        page.wait_for_timeout(500)
        final_box = note.bounding_box()
        print(f"Final size after shrinking: {final_box['width']}x{final_box['height']}")

        if final_box['width'] < new_box['width'] and final_box['height'] < new_box['height']:
            print("Test passed: Element resized on scroll down")
        else:
            print("Test failed: Element did not shrink")

        browser.close()

if __name__ == '__main__':
    test()
