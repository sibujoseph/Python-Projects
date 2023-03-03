import _plotly_utils.basevalidators


class TickvalsValidator(_plotly_utils.basevalidators.DataArrayValidator):

    def __init__(
        self,
        plotly_name='tickvals',
        parent_name='layout.scene.zaxis',
        **kwargs
    ):
        super(TickvalsValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type='plot',
            role='data',
            **kwargs
        )
