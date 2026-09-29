import sys
from playwright.sync_api import sync_playwright

def main():
    url = sys.argv[1] if len(sys.argv) > 1 else 'http://localhost:8000'
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={"width": 1920, "height": 1080})
        page.goto(url)
        # Add mode=dock
        page.goto(url + '?mode=dock')
        page.wait_for_timeout(2000)
        page.screenshot(path='dock.png')
        print("Saved screenshot to dock.png")

        # Overlay mode
        page.goto(url)
        page.wait_for_timeout(2000)
        page.screenshot(path='overlay.png')
        print("Saved screenshot to overlay.png")

        browser.close()

if __name__ == '__main__':
    main()
