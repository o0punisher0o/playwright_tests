# from playwright.sync_api import Page, expect
#
#
# class HomePage:
#     BASE = "https://effective-mobile.ru/"
#
#     def __init__(self, page: Page):
#         self.page = page
#
#     def open(self):
#         self.page.goto(self.BASE)
#         # ждем, пока навигация видна
#         expect(self.page.get_by_role("navigation"), "nav not found").to_be_visible()
#
#     def click_nav(self, name: str):
#         link = self.page.get_by_role("link", name=name)
#         expect(link, f"link '{name}' not visible").to_be_visible()
#         link.click()
#
#     def assert_url(self, expected: str):
#         expect(self.page).to_have_url(expected)
