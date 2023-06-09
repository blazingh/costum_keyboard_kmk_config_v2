import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.mouse_keys import MouseKeys
from kmk.modules.layers import Layers
from kmk.extensions.media_keys import MediaKeys
from kmk.modules.tapdance import TapDance

from kmk.modules.holdtap import HoldTap

keyboard = KMKKeyboard()

holdtap = HoldTap()

tapdance = TapDance()

holdtap.tap_time = 200

keyboard.col_pins = (board.GP0,board.GP1,board.GP2,board.GP3, board.GP4,board.GP15,board.GP14,board.GP13)

keyboard.row_pins = (board.GP18,board.GP19,board.GP20,board.GP21)

keyboard.diode_orientation = DiodeOrientation.COL2ROW

keyboard.modules.append(MouseKeys())

keyboard.modules.append(Layers())

keyboard.modules.append(holdtap)

keyboard.modules.append(tapdance)

keyboard.extensions.append(MediaKeys())

A_LCTL = KC.HT(KC.A, KC.LCTRL, prefer_hold=False, tap_interrupted=False)
R_LSFT = KC.HT(KC.R, KC.LSFT, prefer_hold=False, tap_interrupted=False)
S_LGUI = KC.HT(KC.S, KC.LGUI, prefer_hold=False, tap_interrupted=False)
T_LALT = KC.HT(KC.T, KC.LALT, prefer_hold=False, tap_interrupted=False)

N_RALT = KC.HT(KC.N, KC.RALT, prefer_hold=False, tap_interrupted=False)
E_RGUI = KC.HT(KC.E, KC.RGUI, prefer_hold=False, tap_interrupted=False)
I_RSFT = KC.HT(KC.I, KC.RSFT, prefer_hold=False, tap_interrupted=False)
O_RCTL = KC.HT(KC.O, KC.RCTRL, prefer_hold=False, tap_interrupted=False)

HOME_LCTL = KC.HT(KC.HOME, KC.LCTRL, prefer_hold=False, tap_interrupted=False)
PGDN_LSFT = KC.HT(KC.PAGEDOWN, KC.LSFT, prefer_hold=False, tap_interrupted=False)
PGUP_LGUI = KC.HT(KC.PAGEUP, KC.LGUI, prefer_hold=False, tap_interrupted=False)
END_LALT = KC.HT(KC.END, KC.LALT, prefer_hold=False, tap_interrupted=False)

L1_TAB = KC.HT(KC.TAB, KC.MO(1))
L2_SPC = KC.HT(KC.SPC, KC.MO(2))
L3_BSP = KC.HT(KC.BSPC, KC.MO(3))
L4_DEL = KC.HT(KC.DEL, KC.MO(4))

M_ENT = KC.TD(KC.M, KC.ENT, tap_time=170)
G_ENT = KC.TD(KC.G, KC.ESC, tap_time=170)

CNTRL_Z = KC.LCTL(KC.Z)
CNTRL_Y = KC.LCTL(KC.Y)
CNTRL_C = KC.LCTL(KC.C)
CNTRL_V = KC.LCTL(KC.V)

X = KC.NO

'''
layer0 = [
    X        ,  X        ,  X        ,  X        ,  X        ,  X        ,  X        ,  X        ,
    X        ,  X        ,  X        ,  X        ,  X        ,  X        ,  X        ,  X        ,
    X        ,  X        ,  X        ,  X        ,  X        ,  X        ,  X        ,  X        ,
    X        ,  L3_BSP   ,  L1_TAB   ,  X        ,  X        ,  L2_SPC   ,  L4_DEL   ,  X        ,
    ]
'''

layer0 = [
    KC.Q     ,  KC.W      ,  KC.F     ,  KC.P     ,  KC.L     ,  KC.U     ,  KC.Y    ,  KC.J     ,
    A_LCTL   ,  R_LSFT    ,  S_LGUI   ,  T_LALT   ,  N_RALT   ,  E_RGUI   ,  I_RSFT  ,  O_RCTL   ,
    KC.X     ,  KC.C      ,  KC.D     ,  KC.V     ,  KC.H     ,  KC.B     ,  KC.K    ,  KC.Z     ,
    X        ,  L3_BSP    ,  L1_TAB   ,  G_ENT    ,  M_ENT    ,  L2_SPC   ,  L4_DEL  ,  X        ,
    ]

layer1 = [
    KC.DQT   ,  KC.QUOT   ,  KC.LPRN  ,  KC.LABK  ,  KC.RABK  ,  KC.RPRN  ,  KC.SCLN  ,  KC.COLN  ,
    KC.N1    ,  KC.N2     ,  KC.N3    ,  KC.N4    ,  KC.N7    ,  KC.N8    ,  KC.N9    ,  KC.N0    ,
    KC.TILD  ,  KC.GRV    ,  KC.LCBR  ,  KC.LBRC  ,  KC.RBRC  ,  KC.RCBR  ,  KC.COMM  ,  KC.DOT   ,
    X        ,  L3_BSP    ,  L1_TAB   ,  KC.N5    ,  M_ENT    ,  KC.N6    ,  L4_DEL   ,  X        ,
    ]

layer2 = [
    KC.EXLM  ,  KC.AT     ,  KC.HASH  ,  KC.DLR   ,  KC.PERC  ,  KC.CIRC  ,  KC.AMPR ,  KC.ASTR  ,
    HOME_LCTL,  PGDN_LSFT ,  PGUP_LGUI,  END_LALT ,  KC.LEFT  ,  KC.DOWN  ,  KC.UP   ,  KC.RIGHT ,
    KC.QUES  ,  KC.PIPE   ,  KC.BSLS  ,  KC.SLSH  ,  KC.UNDS  ,  KC.MINS  ,  KC.PLUS ,  KC.EQL   ,
    X        ,  L3_BSP    ,  L1_TAB   ,  KC.ESC   ,  KC.ENT   ,  L2_SPC   ,  L4_DEL  ,  X        ,
    ]

layer3 = [
    KC.F1    ,  KC.F2     ,  KC.F3    ,  KC.F4    ,  KC.MW_UP ,  X        ,  X       ,  X        ,
    KC.MS_LT ,  KC.MS_DN  ,  KC.MS_UP ,  KC.MS_RT ,  KC.MB_LMB,  KC.MB_RMB,  X       ,  X        ,
    CNTRL_Z  ,  CNTRL_C   ,  CNTRL_V  ,  CNTRL_Y  ,  KC.MW_DN ,  X        ,  X       ,  X        ,
    X        ,  L3_BSP    ,  L1_TAB   ,  X        ,  KC.PSCR  ,  L2_SPC   ,  L4_DEL  ,  X        ,
    ]

layer4 = [
    X        ,  X         ,  X        ,  X        ,  X        ,  X        ,  X       ,  X        ,
    X        ,  KC.BRID   ,  KC.BRIU  ,  X        ,  KC.MPLY  ,  KC.VOLD  ,  KC.VOLU ,  X        ,  
    X        ,  X         ,  X        ,  X        ,  X        ,  X        ,  X       ,  X        ,
    X        ,  L3_BSP    ,  L1_TAB   ,  X        ,  KC.MUTE  ,  L2_SPC   ,  L4_DEL  ,  X        ,
    ]    

keyboard.keymap = [
    layer0, layer1, layer2, layer3, layer4
    ]
if __name__ == '__main__':
    keyboard.go()