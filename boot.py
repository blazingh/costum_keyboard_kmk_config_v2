import board

from kmk.bootcfg import bootcfg

bootcfg(
    sense=board.GP14,  # column
    source=board.GP0, # row
    storage=False,
    usb_id=('KMK Keyboards', 'Custom 60% Ergo'),
)
