import ckan.plugins.toolkit as tk
from ckan.plugins.toolkit import BaseController, render

class LandingPageController(BaseController):
    def index(self):
        context = {'model': tk.model, 'session': tk.session, 'user': tk.c.user}
        data_dict = {'all_fields': True, 'sort': 'name asc', 'limit': 20}
        groups = tk.get_action('group_list')(context, data_dict)
        return render('landing_page.html', extra_vars={'groups': groups})
