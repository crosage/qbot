from nonebot import IntentCommand, on_command,CommandSession
#on_command将函数声明为命令处理器
import datetime 
from nonebot import on_natural_language,NLPSession
from .seqcoms import seq
@on_command('set',only_to_me=False)
async def night(session:CommandSession):
    if session.event.user_id!=2051252420 :
        return 
    listcom=session.current_arg_text.strip()
    list=listcom.split()
    if list[0]=='all' :
        list[0]='hungry'
        list.append('jrrp')
        list.append('morning')
        list.append('night')
        list.append('xiximeow')
        list.append('newfriend')
    #初始光标在最前面，直接输入会覆盖相应个数的值
    data=open('C:\\all_for_qqbot\\awesome-bot\\awesome\\plugins\\data\\groupid.txt','a+')
    data.read()
    for i in list :
        msg=f'{session.event.group_id} {i}\n'
        data.write(msg)
    data.close()
    answer=await getit(session.event.group_id,session.event.user_id,list);
    await session.send(answer)
async def getit(group_id,user_id,thing) :
    ok=1
    for i in thing :
        print(i,seq(group_id), i not in seq(group_id))
        if i  not in seq(group_id) :
            ok=0
    if ok==1 :
        message=[
            {
                'type':'text',
                'data':{
                    "text":'Sussess!'
                }
            }
        ]
    else :
        message=[
            {
                'type':'text',
                'data':{
                    "text":'Fail'
                }
            }
        ]
    return message