from tethys_sdk.base import TethysAppBase, url_map_maker


class SnowpackViewer(TethysAppBase):
    """
    Tethys app class for Snowpack Viewer.
    """

    name = 'Snowpack Viewer'
    index = 'snowpack_viewer:home'
    icon = 'snowpack_viewer/images/snowpack1.gif'
    package = 'snowpack_viewer'
    root_url = 'snowpack-viewer'
    color = '#8e44ad'
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
                url='snowpack-viewer',
                controller='snowpack_viewer.controllers.home'
            ),
            UrlMap(
                name='about',
                url='snowpack-viewer/about',
                controller='snowpack_viewer.controllers.about'
            ),
            UrlMap(
                name='data_services',
                url='snowpack-viewer/data_services',
                controller='snowpack_viewer.controllers.data_services'
            ),
            UrlMap(
                name='mapview',
                url='snowpack-viewer/mapview',
                controller='snowpack_viewer.controllers.mapview'
            ),
            UrlMap(
                name='proposal',
                url='snowpack-viewer/proposal',
                controller='snowpack_viewer.controllers.proposal'
            ),
            UrlMap(
                name='mockup',
                url='snowpack-viewer/mockup',
                controller='snowpack_viewer.controllers.mockup'
            ),
            UrlMap(
                name='animation',
                url='snowpack-viewer/animation',
                controller='snowpack_viewer.controllers.animation'
            ),
        )

        return url_maps
