from ckan.plugins.toolkit import BaseController, render

class LandingPageController(BaseController):
    def index(self):
        return render('landing_page.html')
