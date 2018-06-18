from .basic import *
from .intermediate import *
from .self import *
from .self_symmetrical_false import *
# models를 불러오기위해서 import시켜줘야 함
# 원래는 models.py에서 migrate할 때 알아서 해주지만
# models를 패키지로 만들었기 때문에 init파일에
# 따로 DB에 올릴 models를 지정해줘야함