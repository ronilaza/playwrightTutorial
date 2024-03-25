class MyHomepage:

    def __init__(self, page):
        self.celebrate_header = page.locator("text=Celebrating Beauty and Style")
        self.celebrate_body = page.locator('text=playwright-practice was founded by a group of like-minded fashion')
        self.celebrate_name = page.get_by_text("Shop Women Winter")
        self.myname =  page.get_by_text("Shop Women Winter")


    