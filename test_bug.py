from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto('http://localhost:8080/?mode=overlay')

    # Wait for the page to load
    page.wait_for_selector('#notes-canvas')

    # Double click to open popup
    page.click('#canvas-note-note-1')
    page.wait_for_timeout(500)

    # Switch to tasks mode
    page.click('#popup-mode-tasks')

    # Set task title
    page.fill('#popup-task-title-input', 'My Popup Title')

    page.wait_for_timeout(500)

    html = page.evaluate('document.getElementById("notes-canvas").innerHTML')
    print("Overlay HTML:")
    print(html)

    browser.close()
