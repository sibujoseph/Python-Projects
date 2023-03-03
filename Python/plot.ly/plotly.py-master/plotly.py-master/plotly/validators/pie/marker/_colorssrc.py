import _plotly_utils.basevalidators


class ColorssrcValidator(_plotly_utils.basevalidators.SrcValidator):

    def __init__(
        self, plotly_name='colorssrc', parent_name='pie.marker', **kwargs
    ):
        super(ColorssrcValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type='none',
            role='info',
            **kwargs
        )
