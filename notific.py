from win10toast import ToastNotifier

toaster = ToastNotifier()

toaster.show_toast(
    'Notificação',
    'Clee informa que esse algoritimo está funcionando bem',
    threaded=True,
    icon_path=None,
    duration=5
)

