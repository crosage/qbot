from nonebot import IntentCommand, on_command,CommandSession
#on_command将函数声明为命令处理器
from .ingroup import isin
import datetime 
from nonebot import on_natural_language,NLPSession

@on_command('晚安')
async def night(session:CommandSession):
    if isin(session.event.group_id,'night')==0 :
        return 
    answer=await getit(session.event.group_id,session.event.user_id)
    await session.send(answer)
async def getit(group_id,user_id):
    i =datetime.datetime.now()
    msg='0'
    if (i.hour >=20 and i.hour<=24 )or(i.hour>=0 and i.hour<=4) :
        data=open('C:\\all_for_qqbot\\awesome-bot\\awesome\\plugins\\data\\night.txt','r+')
        yesterday=0
        if i.hour>=0 and i.hour<=4 :
            yesterday=1
        tot=1
        for line in data :
            list=[int(i) for i in line.split()]
            if group_id==list[2] :
                if yesterday==1:
                    if (list[0]==(i.day-1) and list[1]>=20 and list[1]<=24) or (list[0]==i.day and list[1]>=0 and list[1]<=4):
                        tot=tot+1 
                else :
                    if (list[0]==i.day and list[1]>=20 and list[1]<=24):
                        tot=tot+1
        s=f'{i.day} {i.hour} {group_id}\n'
        data.write(s)
        if i.minute<10 :
            msg=f'晚安，现在是{i.hour}:0{i.minute}，你是群里第{tot}个睡觉的人哦'
        else :
            msg=f'晚安，现在是{i.hour}:{i.minute}，你是群里第{tot}个睡觉的人哦'
        message=[
            {
                "type":"text",
                "data":{
                    "text":msg
                }
            },
            {
                "type":"image",
                "data":{
                    "file":'file:///C:/all_for_qqbot/awesome-bot/awesome/plugins/image/huhumeow.png',
                }
            }
        ]
        return message
    else :
        msg='现在才睡吗，不过快点睡吧'
        message=[
            {
                "type":"text",
                "data":{
                    "text":msg
                }
            }
        ]
        return message
@on_natural_language(keywords={'晚安'},only_to_me=False)
async def _(session:NLPSession):
    return IntentCommand(90,'晚安')
@on_natural_language(keywords={'呼呼'},only_to_me=False)
async def _(session:NLPSession):
    return IntentCommand(90,'晚安')