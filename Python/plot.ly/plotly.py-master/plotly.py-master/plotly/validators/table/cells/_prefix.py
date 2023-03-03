import _plotly_utils.basevalidators


class PrefixValidator(_plotly_utils.basevalidators.StringValidator):

    def __init__(
        self, plotly_name='prefix', parent_name='table.cells', **kwargs
    ):
        super(PrefixValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            array_ok=True,
            edit_type='calc',
            role='style',
            **kwargs
        )
