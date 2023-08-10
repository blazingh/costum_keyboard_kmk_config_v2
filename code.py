import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.layers import Layers
from kmk.modules.tapdance import TapDance

from kmk.modules.holdtap import HoldTap

keyboard = KMKKeyboard()
holdtap = HoldTap()
tapdance = TapDance()

holdtap.tap_time = 200

tapdance.tap_time = 750

combo_layers = {(1, 2): 3}

keyboard.modules.append(Layers(combo_layers))
keyboard.modules.append(holdtap)
keyboard.modules.append(tapdance)

keyboard.col_pins = (board.GP14,board.GP9,board.GP3,board.GP4, board.GP18,board.GP19,board.GP20,board.GP21)
keyboard.row_pins = (board.GP0,board.GP5,board.GP10,board.GP15)
keyboard.diode_orientation = DiodeOrientation.COL2ROW


HOME_LCTL = KC.HT(KC.HOME    , KC.LCTRL, prefer_hold=False, tap_interrupted=False) # home and control
PGDN_LSFT = KC.HT(KC.PAGEDOWN, KC.LSFT , prefer_hold=False, tap_interrupted=False) # page down and shift
PGUP_LGUI = KC.HT(KC.PAGEUP  , KC.LGUI , prefer_hold=False, tap_interrupted=False) # page up and gui
END_LALT  = KC.HT(KC.END     , KC.LALT , prefer_hold=False, tap_interrupted=False) # end and alt

L1_BSP = KC.HT(KC.BSPC, KC.MO(1)) # backspace and layer 1
L2_SPC = KC.HT(KC.SPC , KC.MO(2)) # space and layer 2

TAB_CTRL = KC.HT(KC.TAB, KC.LCTL) # tab and control
DEL_SHFT = KC.HT(KC.DEL, KC.LSFT) # delete and shift

    
L_R_PRN   = KC.TD(  KC.LPRN,  KC.RPRN,  tap_time=200) # open and close parenthesis
L_R_ABK   = KC.TD(  KC.LABK,  KC.RABK,  tap_time=200) # open and close angle brackets
L_R_BKT   = KC.TD(  KC.LBRC,  KC.RBRC,  tap_time=200) # open and close square brackets
L_R_BRC   = KC.TD(  KC.LCBR,  KC.RCBR,  tap_time=200) # open and close curly brackets
QUOT_DQT  = KC.TD(  KC.QUOT,  KC.DQT ,  tap_time=200) # single and double quotes
COLN_SCLN = KC.TD(  KC.COLN,  KC.SCLN,  tap_time=200) # colon and semicolon
DOT_COM   = KC.TD(  KC.DOT ,  KC.COMM,  tap_time=200) # dot and comma
EXLM_QUES = KC.TD(  KC.EXLM,  KC.QUES,  tap_time=200) # exclamation and question mark
MINS_PLUS = KC.TD(  KC.MINS,  KC.PLUS,  tap_time=200) # minus and plus
UNDS_EQL  = KC.TD(  KC.UNDS,  KC.EQL ,  tap_time=200) # underscore and equal
TILD_GRV  = KC.TD(  KC.TILD,  KC.GRV ,  tap_time=200) # tilde and grave
SLSH_BSLS = KC.TD(  KC.SLSH,  KC.BSLS,  KC.PIPE,  tap_time=200) # slash, backslash, and pipe


X = KC.NO

'''
layer0 = [
    X        ,  X        ,  X        ,  X        ,  X        ,  X        ,  X        ,  X        ,
    X        ,  X        ,  X        ,  X        ,  X        ,  X        ,  X        ,  X        ,
    X        ,  X        ,  X        ,  X        ,  X        ,  X        ,  X        ,  X        ,
    X        ,  L3_BSP   ,  L1_TAB   ,  X        ,  X        ,  L2_SPC   ,  L4_DEL   ,  X        ,
    ]
'''
# Base layer
layer0 = [
    KC.Q     ,  KC.W      ,  KC.F     ,  KC.P     ,  KC.L     ,  KC.U     ,  KC.Y    ,  KC.J     ,
    KC.A     ,  KC.R      ,  KC.S     ,  KC.T     ,  KC.N     ,  KC.E     ,  KC.I    ,  KC.O     ,
    KC.X     ,  KC.C      ,  KC.D     ,  KC.V     ,  KC.H     ,  KC.B     ,  KC.K    ,  KC.Z     ,
    X        ,  KC.G      ,  L1_BSP   ,  TAB_CTRL ,  DEL_SHFT ,  L2_SPC   ,  KC.M    ,  X        ,
    ]

# left hand layer 1
layer1 = [
    EXLM_QUES,  KC.AT     ,  KC.HASH  ,  KC.DLR   ,  KC.PERC  ,  KC.CIRC  ,  KC.AMPR ,  KC.ASTR  ,
    SLSH_BSLS,  QUOT_DQT  ,  L_R_PRN  ,  L_R_ABK  ,  X        ,  X        ,  X       ,  X        ,
    X        ,  TILD_GRV  ,  L_R_BRC  ,  L_R_BKT  ,  UNDS_EQL ,  MINS_PLUS, COLN_SCLN,  DOT_COM  ,
    X        ,  X         ,  L1_BSP   ,  TAB_CTRL ,  DEL_SHFT ,  L2_SPC   ,  X       ,  X        ,
    ]

# right hand layer 2
layer2 = [
    KC.ESC   ,   X        ,  X        ,  X        ,  KC.BSPC  ,  X        ,  X       ,  KC.ENT   ,
    HOME_LCTL,  PGDN_LSFT ,  PGUP_LGUI,  END_LALT ,  KC.LEFT  ,  KC.DOWN  ,  KC.UP   ,  KC.RIGHT ,
    X        ,  X         ,  X        ,  X        ,  X        ,  X        ,  X       ,  X        ,
    X        ,  X         ,  L1_BSP   ,  TAB_CTRL ,  DEL_SHFT ,  L2_SPC   ,  X       ,  X        ,
    ]

# two handed layer 3
layer3 = [
    X        ,  X         ,  X        ,  X        ,  KC.N7    ,  KC.N8    ,  KC.N9   ,  X        , 
    X        ,  X         ,  X        ,  X        ,  KC.N4    ,  KC.N5    ,  KC.N6   ,  KC.N0    , 
    X        ,  X         ,  X        ,  X        ,  KC.N1    ,  KC.N2    ,  KC.N3   ,  KC.DOT   ,
    X        ,  X         ,  L1_BSP   ,  TAB_CTRL ,  DEL_SHFT ,  L2_SPC   ,  KC.PSCR ,  X        ,
    ]
  

keyboard.keymap = [
    layer0, layer1, layer2, layer3
    ]


if __name__ == '__main__':
    keyboard.go()
