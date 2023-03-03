import _plotly_utils.basevalidators


class TickmodeValidator(_plotly_utils.basevalidators.EnumeratedValidator):

    def __init__(
        self, plotly_name='tickmode', parent_name='layout.yaxis', **kwargs
    ):
        super(TickmodeValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type='ticks+margins',
            implied_edits={},
            role='info',
            values=['auto', 'linear', 'array'],
            **kwargs
        )
