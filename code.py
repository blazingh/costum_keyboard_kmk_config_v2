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

keyboard.col_pins = (board.GP14,board.GP9,board.GP3,board.GP4, board.GP18,board.GP19,board.GP20,board.GP21)

keyboard.row_pins = (board.GP0,board.GP5,board.GP10,board.GP15)

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

L3_TAB = KC.HT(KC.TAB, KC.MO(3))
L2_SPC = KC.HT(KC.SPC, KC.MO(2))
L1_BSP = KC.HT(KC.BSPC, KC.MO(1))
L4_DEL = KC.HT(KC.DEL, KC.MO(4))
L5_G   = KC.HT(KC.G, KC.MO(5))

CNTRL_Z = KC.LCTL(KC.Z)
CNTRL_Y = KC.LCTL(KC.Y)
CNTRL_C = KC.LCTL(KC.C)
CNTRL_V = KC.LCTL(KC.V)
CNTRL_X = KC.LCTL(KC.X)
CNTRL_A = KC.LCTL(KC.A)


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
    X        ,  L5_G      ,  L1_BSP   ,  L3_TAB   ,  L4_DEL   ,  L2_SPC   ,  KC.M    ,  X        ,
    ]

layer1 = [
    KC.QUOT  ,  KC.DQT    ,  KC.LPRN  ,  KC.LABK  ,  KC.RABK  ,  KC.RPRN  ,  KC.SCLN ,  KC.COLN  ,
    KC.N1    ,  KC.N2     ,  KC.N3    ,  KC.N4    ,  KC.N7    ,  KC.N8    ,  KC.N9   ,  KC.N0    ,
    KC.TILD  ,  KC.GRV    ,  KC.LCBR  ,  KC.LBRC  ,  KC.RBRC  ,  KC.RCBR  ,  KC.COMM ,  KC.DOT   ,
    X        ,  KC.N5     ,  L1_BSP   ,  L3_TAB   ,  L4_DEL   ,  L2_SPC   ,  KC.N6   ,  X        ,
    ]

layer2 = [
    KC.EXLM  ,  KC.AT     ,  KC.HASH  ,  KC.DLR   ,  KC.PERC  ,  KC.CIRC  ,  KC.AMPR ,  KC.ASTR  ,
    HOME_LCTL,  PGDN_LSFT ,  PGUP_LGUI,  END_LALT ,  KC.LEFT  ,  KC.DOWN  ,  KC.UP   ,  KC.RIGHT ,
    KC.QUES  ,  KC.PIPE   ,  KC.BSLS  ,  KC.SLSH  ,  KC.UNDS  ,  KC.MINS  ,  KC.PLUS ,  KC.EQL   ,
    X        ,  KC.ESC    ,  L1_BSP   ,  L3_TAB   ,  L4_DEL   ,  L2_SPC   ,  KC.ENT  ,  X        ,
    ]

layer3 = [
    KC.ESC   ,  KC.F2     ,  KC.F3    ,  KC.ENT   ,  KC.MW_UP ,  X        ,  X       ,  X        , 
    CNTRL_A  ,  CNTRL_X   ,  KC.MB_LMB,  KC.MB_RMB,  KC.MS_LT ,  KC.MS_DN ,  KC.MS_UP,  KC.MS_RT , 
    CNTRL_Z  ,  CNTRL_C   ,  CNTRL_V  ,  CNTRL_Y  ,  KC.MW_DN ,  X        ,  X       ,  X        ,
    X        ,  X         ,  L1_BSP   ,  L3_TAB   ,  L4_DEL   ,  L2_SPC   ,  KC.PSCR ,  X        ,
    ]

layer4 = [
    X        ,  X         ,  X        ,  X        ,  X        ,  X        ,  X       ,  X        ,
    X        ,  KC.BRIU   ,  KC.BRID  ,  X        ,  KC.MPLY  ,  KC.VOLD  ,  KC.VOLU ,  X        ,  
    X        ,  X         ,  X        ,  X        ,  X        ,  X        ,  X       ,  X        ,
    X        ,  X         ,  L1_BSP   ,  L3_TAB   ,  L4_DEL   ,  L2_SPC   ,  KC.MUTE ,  X        ,
    ]    

layer5 = [
    KC.ESC   ,  X        ,  X        ,  KC.ENT   ,  KC.N7    ,  KC.N8    ,  KC.N9    ,  X        ,
    X        ,  X        ,  X        ,  X        ,  KC.N4    ,  KC.N5    ,  KC.N6    ,  KC.N0    ,
    X        ,  X        ,  X        ,  X        ,  KC.N1    ,  KC.N2    ,  KC.N3    ,  KC.DOT   ,
    X        ,  X        ,  L1_BSP   ,  L3_TAB   ,  L4_DEL   ,  L2_SPC   ,  X        ,  X        ,
    ]

keyboard.keymap = [
    layer0, layer1, layer2, layer3, layer4, layer5
    ]
if __name__ == '__main__':
    keyboard.go()
