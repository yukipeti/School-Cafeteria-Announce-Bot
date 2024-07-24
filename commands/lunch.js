const { SlashCommandBuilder, EmbedBuilder } = require("discord.js");
const lunch = require("../data/lunch.json");

const days = ["Mon", "Tue", "Wed", "Thu", "Fri"];
const today = new Date().getDay();
const dispMenu = ["Aセット", "Bセット", "カレー", "日替わりうどん・そば", "うどん・そば", "日替わりラーメン・パスタ", "ラーメン"];
const menu = ["Aset", "Bset", "curry", "dailySpecialUdonSoba", "UdonSoba", "dailySpecialRamenPasta", "ramen"];


module.exports = {
	data: new SlashCommandBuilder()
		.setName("today")
		.setDescription("今日の学食を表示します"),
        async execute(interaction) {
            if (today === 0 || today === 6) {
                await interaction.reply("今日は土日です。学食はありません");
                return;
            }

            const embed = new EmbedBuilder()
                .setTitle("今日の学食")
                .setDescription("今日の学食は以下の通りです")
                .setFooter({text: "※内容は変更される可能性があります"})
                .setTimestamp();
                dispMenu.forEach((item, index) => {
                    embed.addFields({
                        name: item,
                        value: lunch[menu[index]][days[today]],
                        inline: false
                    });
                });
            await interaction.reply({ embeds: [embed]});
        }
};