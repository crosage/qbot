from nonebot import on_notice, NoticeSession
from .ingroup import isin

# 将函数注册为群成员增加通知处理器
@on_notice('group_increase')
async def _(session: NoticeSession):
    if isin(session.event.group_id,'newfriend')==0 :
        return
    if session.event.group_id==816950992:
    # 发送欢迎消息
        await session.send('欢迎新叔叔～')
    if session.event.group_id==816950992:
    # 发送欢迎消息
        await session.send('欢迎新叔叔～')
    if session.event.group_id==882814796:
        message=[
            {
                "type":"text",
                "data":{
                  "text":"女留id，男自强"
                }
            },
            {
                "type":"image",
                "data":{
                    "file":'file:///C:/all_for_qqbot/awesome-bot/awesome/plugins/image/heartstonehello.jpg'
                }
            }
        ]
        await session.send(message)