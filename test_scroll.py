from playwright.sync_api import sync_playwright

def test():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto('http://localhost:8001')

        # Wait for the note to appear
        note = page.locator('.note-container').first
        note.wait_for()

        # Get initial bounding box
        initial_box = note.bounding_box()
        print(f"Initial size: {initial_box['width']}x{initial_box['height']}")

        # Get initial font size
        initial_font_size_str = note.locator('.z-10').evaluate("el => el.style.fontSize")
        initial_font_size = float(initial_font_size_str.replace('px', ''))
        print(f"Initial font size: {initial_font_size}")

        # Simulate wheel event (scroll up to zoom in)
        # Note: Playwright doesn't have a direct scroll on element, but we can use dispatch_event
        note.dispatch_event('wheel', {'deltaY': -100})

        # Give it a tiny bit of time
        page.wait_for_timeout(500)

        new_box = note.bounding_box()
        print(f"New size: {new_box['width']}x{new_box['height']}")

        new_font_size_str = note.locator('.z-10').evaluate("el => el.style.fontSize")
        new_font_size = float(new_font_size_str.replace('px', ''))
        print(f"New font size: {new_font_size}")

        if new_box['width'] > initial_box['width'] and new_box['height'] > initial_box['height']:
            print("Test passed: Element resized on scroll up")
        else:
            print("Test failed: Element did not resize")

        if new_font_size > initial_font_size:
            print("Test passed: Font size increased on scroll up")
        else:
            print("Test failed: Font size did not increase")

        # Try shrinking
        note.dispatch_event('wheel', {'deltaY': 100})
        page.wait_for_timeout(500)
        final_box = note.bounding_box()
        print(f"Final size after shrinking: {final_box['width']}x{final_box['height']}")

        final_font_size_str = note.locator('.z-10').evaluate("el => el.style.fontSize")
        final_font_size = float(final_font_size_str.replace('px', ''))
        print(f"Final font size: {final_font_size}")

        if final_box['width'] < new_box['width'] and final_box['height'] < new_box['height']:
            print("Test passed: Element resized on scroll down")
        else:
            print("Test failed: Element did not shrink")

        if final_font_size < new_font_size:
            print("Test passed: Font size decreased on scroll down")
        else:
            print("Test failed: Font size did not decrease")

        browser.close()

if __name__ == '__main__':
    test()
