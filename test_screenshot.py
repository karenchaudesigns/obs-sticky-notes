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

    # Set task title
    page.fill('#editor-task-title-input', 'My Awesome Checklist Title')

    time.sleep(1)

    # Take screenshot of overlay
    page.goto('http://localhost:8080/?mode=overlay')
    page.wait_for_selector('#notes-canvas')
    time.sleep(1)
    page.screenshot(path='overlay_screenshot.png')

    browser.close()
