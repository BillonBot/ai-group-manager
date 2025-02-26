from nonebot import require, Bot

require("nonebot_plugin_marshoai")

from nonebot_plugin_marshoai.plugin import on_function_call, String, Integer


@on_function_call(description="禁言指定用户指定时长").params(
    user_id=String(description="用户ID"), time=Integer(description="时长秒数")
)
async def _(user_id: str, time: int, bot: Bot):
    return await bot.call_api("set_group_ban", user_id=user_id, duration=time)