import ckan.plugins as p
import ckan.plugins.toolkit as tk

class MyLandingPagePlugin(p.SingletonPlugin):
    p.implements(p.IConfigurer)
    p.implements(p.IRoutes, inherit=True)

    def update_config(self, config):
        tk.add_template_directory(config, 'templates')
        tk.add_public_directory(config, 'public')
        tk.add_resource('fanstatic', 'my_landing_page')

    def after_map(self, map):
        map.connect('home', '/', controller='ckanext.my_landing_page.controller:LandingPageController', action='index')
        return map
