from playwright.sync_api import sync_playwright

def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("https://www.google.com")
        title = page.title()
        print(f"Page title: {title}")
        browser.close()

if __name__ == "__main__":
    main()
