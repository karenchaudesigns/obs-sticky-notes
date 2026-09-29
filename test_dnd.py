from playwright.sync_api import sync_playwright

def test():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto('http://localhost:8000/?mode=dock')

        # Wait for the memo pads to load
        pad = page.locator('.memo-pad-option').first
        pad.wait_for()

        # Before adding, count notes
        initial_notes = page.evaluate('appState.notes.length')

        # Click test
        pad.click()
        page.wait_for_timeout(500)
        after_click_notes = page.evaluate('appState.notes.length')
        assert after_click_notes == initial_notes + 1, f"Expected {initial_notes + 1} notes after click, got {after_click_notes}"

        # Try drag and drop test via evaluating JS
        page.evaluate('''() => {
            const pad = document.querySelector('.memo-pad-option');
            const canvas = document.getElementById('dock-preview-canvas');

            const dataTransfer = new DataTransfer();
            dataTransfer.setData('text/plain', pad.getAttribute('data-preset'));

            const dropEvent = new DragEvent('drop', {
                bubbles: true,
                cancelable: true,
                clientX: 500,
                clientY: 500,
                dataTransfer: dataTransfer
            });
            canvas.dispatchEvent(dropEvent);
        }''')

        page.wait_for_timeout(500)
        after_drop_notes = page.evaluate('appState.notes.length')
        assert after_drop_notes == after_click_notes + 1, f"Expected {after_click_notes + 1} notes after drop, got {after_drop_notes}"

        print("DND and Click tests passed!")
        browser.close()

if __name__ == '__main__':
    test()
