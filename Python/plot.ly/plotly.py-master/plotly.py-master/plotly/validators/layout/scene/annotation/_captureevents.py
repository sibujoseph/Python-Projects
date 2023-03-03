import _plotly_utils.basevalidators


class CaptureeventsValidator(_plotly_utils.basevalidators.BooleanValidator):

    def __init__(
        self,
        plotly_name='captureevents',
        parent_name='layout.scene.annotation',
        **kwargs
    ):
        super(CaptureeventsValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type='calc',
            role='info',
            **kwargs
        )
