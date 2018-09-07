from tethys_sdk.base import TethysAppBase, url_map_maker


class Ndvi(TethysAppBase):
    """
    Tethys app class for NDVI.
    """

    name = 'NDVI'
    index = 'ndvi:home'
    icon = 'ndvi/images/icon.gif'
    package = 'ndvi'
    root_url = 'ndvi'
    color = '#16a085'
    description = 'Place a brief description of your app here.'
    tags = ''
    enable_feedback = False
    feedback_emails = []

    def url_maps(self):
        """
        Add controllers
        """
        UrlMap = url_map_maker(self.root_url)

        url_maps = (
            UrlMap(
                name='home',
                url='ndvi',
                controller='ndvi.controllers.home'
            ),
            UrlMap(
                name='get-plot',
                url='ndvi/get-plot',
                controller='ndvi.controllers.get_plot'
            ),
        )

        return url_maps
