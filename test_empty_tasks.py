from playwright.sync_api import sync_playwright
import time

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto('http://localhost:8080/?mode=dock')

    # Wait for the page to load
    page.wait_for_selector('#dock-notes-list')

    # Select the first note
    page.click('.p-3.rounded-xl.border.transition-all')

    # Switch to tasks mode
    page.click('#editor-mode-tasks')

    # Delete all tasks
    delete_btns = page.locator('.task-inner-del')
    for i in range(delete_btns.count()):
        delete_btns.nth(0).click() # always click the first one as they shift up

    # Set task title
    page.fill('#editor-task-title-input', 'My Awesome Checklist Title')

    time.sleep(1)

    # Take screenshot of overlay
    page.goto('http://localhost:8080/?mode=overlay')
    page.wait_for_selector('#notes-canvas')
    time.sleep(1)
    page.screenshot(path='empty_tasks_screenshot.png')

    html = page.evaluate('document.getElementById("notes-canvas").innerHTML')
    print("Overlay HTML:")
    print(html)

    browser.close()
