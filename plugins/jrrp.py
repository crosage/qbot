from nonebot import IntentCommand, on_command,CommandSession
#on_command将函数声明为命令处理器
import datetime 
import random
from nonebot import on_natural_language,NLPSession
from .ingroup import isin

@on_command('jrrp',aliases=('今日人品'),only_to_me=False)
async def jrrp(session:CommandSession):
    if isin(session.event.group_id,'jrrp')==0 :
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
    i=datetime.datetime.now()
    random.seed(user_id*i.day*i.month)
    x=random.random()
    if x<0.3 :
        y=random.randint(1,40)
        if y<15:
            return f'你今天的人品是{y}(寄)' 
        else :
            return f'你今天的人品是{y}(末吉)' 
    else :
        y=random.randint(40,100)
        if y>=40 and y<=60 :
            return f'你今天的人品是{y}(小吉)'
        elif y>60 and y<=80 :
            return  f'你今天的人品是{y}(吉)'
        else :
            return  f'你今天的人品是{y}(大吉)'
@on_natural_language(keywords={'昨日人品'},only_to_me=False)
async def _(session:NLPSession):
    return IntentCommand(90,'jrrp')
@on_natural_language(keywords={'明日人品'},only_to_me=False)
async def _(session:NLPSession):
    return IntentCommand(90,'jrrp')