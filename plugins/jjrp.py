from nonebot import IntentCommand, on_command,CommandSession
#on_command将函数声明为命令处理器
import datetime 
import random
from nonebot import on_natural_language,NLPSession
from .ingroup import isin

@on_command('jjrp',only_to_me=False)
async def jrrp(session:CommandSession):
    if isin(session.event.group_id,'jjrp')==0 :
        return 
    answer=getit(session.event.user_id)
    message=[
        {
            "type":"at",
            "data":{
                "qq":f'{session.event.user_id}'
            }
        },
        {
            "type":"text",
            "data":{
                "text":answer
            }
        }
    ]
    await session.send(message)
def getit(user_id):
    return f'日日我的'