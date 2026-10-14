from playwright.sync_api import sync_playwright

def test():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(record_video_dir="videos/", record_video_size={"width": 1280, "height": 720})
        # Note we use ?mode=dock for the dock view
        page.goto('http://localhost:8000/?mode=dock')

        # Test 1: Note Selection (Blue Ring)
        note = page.locator('#dock-note-note-1')
        note.wait_for()

        # We must trigger pointerdown to select the note
        # By using Playwright dispatch_event directly we bypass any collision checks
        note.dispatch_event("pointerdown")

        page.screenshot(path="dock-selection-debug.png")
        assert note.evaluate("el => el.classList.contains('is-selected-note')"), "Note was not selected"

        # Test 2: Text Selection (Dashed Outline)
        text_layer = note.locator('.z-10')
        text_layer.dispatch_event("pointerdown")

        assert text_layer.evaluate("el => el.classList.contains('is-selected-text')"), "Text was not selected"

        page.screenshot(path="dock-selection.png")
        print("UI tests passed!")

        browser.close()

if __name__ == '__main__':
    test()
