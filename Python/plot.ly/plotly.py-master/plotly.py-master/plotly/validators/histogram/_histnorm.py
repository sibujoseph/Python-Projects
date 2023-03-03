import _plotly_utils.basevalidators


class HistnormValidator(_plotly_utils.basevalidators.EnumeratedValidator):

    def __init__(
        self, plotly_name='histnorm', parent_name='histogram', **kwargs
    ):
        super(HistnormValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type='calc',
            role='style',
            values=[
                '', 'percent', 'probability', 'density', 'probability density'
            ],
            **kwargs
        )
