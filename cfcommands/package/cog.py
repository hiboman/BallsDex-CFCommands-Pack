from typing import TYPE_CHECKING

import discord
from discord import app_commands
from discord.ext import commands
from ballsdex.core.utils.transformers import BallEnabledTransform
from bd_models.models import Ball

if TYPE_CHECKING:
    from ballsdex.core.bot import BallsDexBot

class CFCommands(commands.Cog):
    def __init__(self, bot: "BallsDexBot"):
        self.bot = bot

    @app_commands.command()
    @app_commands.checks.cooldown(1, 5, key=lambda i: i.user.id)
    async def inspect(self, interaction: discord.Interaction["BallsDexBot"], countryball: BallEnabledTransform):
        """
        Display info from a countryball without having the countryball.

        Parameters
        ----------
        countryball: Ball
            The countryball you want to inspect.
        """
        await interaction.response.defer(thinking=True)

        ball = await Ball.objects.select_related("regime", "economy").aget(pk=countryball.pk)

        emoji = self.bot.get_emoji(ball.emoji_id) or ""

        regime_name = ball.regime.name if ball.regime else "N/A"
        economy_name = ball.economy.name if ball.economy else "N/A"
        
        embed = discord.Embed(
            title=f"{emoji} {ball.country} Information:",
            description=(
                f"⋄ **Short Name:** {ball.short_name or 'N/A'}\n"
                f"⋄ **Catch Names:** {ball.catch_names or 'N/A'}\n"
                f"⋄ **Regime:** {regime_name}\n"
                f"⋄ **Economy:** {economy_name}\n"
                f"⋄ **Health:** {ball.health}\n"
                f"⋄ **Attack:** {ball.attack}\n"
                f"⋄ **Rarity:** {ball.rarity}\n"
                f"⋄ **Ability Name:** {ball.capacity_name}\n"
                f"⋄ **Ability Description:** {ball.capacity_description}\n"
                f"⋄ **Artwork Author:** {ball.credits}\n"
            ),
            color=discord.Color.blurple(),
        )

        await interaction.followup.send(embed=embed)
