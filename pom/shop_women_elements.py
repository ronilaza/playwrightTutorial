class ShopWomen:
    def __init__(self, page):
        self.celebrating_beauty_header = page.locator("text=Celebrating Beauty and Style")
        self.celebrating_beauty_body = page.locator('text=playwright-practice was founded by a group of like-minded fashion')
        self.celebrating_beauty_hdr = page.locator("text=Celebrating Beauty and Style")
        self.profile_arrow= page.locator("._1hHt1")
        self.profile_icon = page.locator("defaultAvatar-comp-kqx7o7qv")
        self.cart_icon = page.locator(".bqgup")
        self.my_orders = page.locator("text=My Orders")
        self.my_orders_profile_box = page.locator("text=Celebrating Beauty and Style")