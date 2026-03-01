from discord.ext import commands
from main import MyBot
from libs.gemini import run_gemini
import logging
from models.config import config

logger = logging.getLogger(__name__)

class Chat(commands.Cog):
    def __init__(self, bot: MyBot):
        self.bot = bot

    # command: !chat <message>
    @commands.command()
    async def chat(self, ctx: commands.Context[commands.Bot], *, message: str):
        # ensure the bot user is available
        if not self.bot.user:
            await ctx.send(config['ERROR_MESSAGE'])
            raise RuntimeError("Bot user is not available")

        content = message

        try:
            # response = run_openapi(content)
            async with ctx.typing():
                response = await run_gemini(content)
            await ctx.send(response)
        except Exception as e:
            logger.error(f"Lỗi khi gọi API Gemini: {e}")
            await ctx.send(config['ERROR_MESSAGE'])

    # error handler for !chat command
    @chat.error
    async def chat_error(self, ctx: commands.Context[commands.Bot], error: commands.CommandError):
        if isinstance(error, commands.MissingRequiredArgument):
            logger.error(f"Lỗi khi gọi API Gemini: {error}")
            await ctx.send("nhập gì đó đi chứ")

        elif isinstance(error, commands.BadArgument):
            logger.error(f"Lỗi khi gọi API Gemini: {error}")
            await ctx.send("nhập gì đó sai sai rồi đó :(((")

        else:
            logger.error(f"Lỗi khi gọi API Gemini: {error}")
            await ctx.send(config['ERROR_MESSAGE'])

async def setup(bot: MyBot):
    await bot.add_cog(Chat(bot))