from nonebot import IntentCommand, on_command,CommandSession
#on_command将函数声明为命令处理器
from nonebot import on_natural_language,NLPSession
from .ingroup import isin
import random 
@on_command('嘻嘻喵')
async def morning(session:CommandSession):
    if isin(session.event.group_id,'xiximeow')==0 :
        return 
    a=random.random()
    if a<0.5 :
        message=[
            {
                "type":"image",
                "data":{
                    "file":'file:///C:/all_for_qqbot/awesome-bot/awesome/plugins/image/xiximeow.jpg'
                    #必须///
                }
            }
        ]
    else :
        message=[
            {
                "type":"image",
                "data":{
                    "file":'file:///C:/all_for_qqbot/awesome-bot/awesome/plugins/image/xiximeow.gif'
                    #必须///
                }
            }
        ]
    await session.send(message)

@on_natural_language(keywords='嘻嘻喵',only_to_me=False)
async def _(session:NLPSession):
    return IntentCommand(90,'嘻嘻喵')