import sys
sys.path.append('.')
sys.path.append('../')
sys.path.append('../../')
sys.path.append('../configs')
sys.path.append('./configs')
sys.path.append('/home/runner/work/GeneralQBOT/GeneralQBOT')
sys.path.append('/home/runner/work/GeneralQBOT/GeneralQBOT/configs')
from handlers.tms import ai_moderation, tencent_moderation

def test_ai():
    # assert ai_moderation('你好')['bad'] == True
    assert ai_moderation('你看一下这个报错')['bad'] == True
    assert ai_moderation('我草你妈的')['bad'] == False
    assert ai_moderation('河北人就是这样的')['bad'] == False