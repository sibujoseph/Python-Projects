import _plotly_utils.basevalidators


class ColorValidator(_plotly_utils.basevalidators.ColorValidator):

    def __init__(
        self,
        plotly_name='color',
        parent_name='layout.xaxis.titlefont',
        **kwargs
    ):
        super(ColorValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type='ticks+margins',
            role='style',
            **kwargs
        )
