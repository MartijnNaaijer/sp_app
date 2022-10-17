from tf.advanced.app import App

class TfApp(App):
    def __init__(app, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def fmt_layoutRich(app, n, **kwargs):
        api = app.api
        F = api.F
        material = F.g_cons_utf8.v(n)
        
        return f"{material}"
