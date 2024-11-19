const { SlashCommandBuilder, EmbedBuilder } = require("discord.js");
const lunch = require("../data/lunch.json");

const days = ["Mon", "Tue", "Wed", "Thu", "Fri"];
const dispMenu = ["Aセット", "Bセット", "カレー", "日替わりうどん・そば", "うどん・そば", "日替わりラーメン・パスタ", "ラーメン"];
const menu = ["Aset", "Bset", "curry", "dailySpecialUdonSoba", "UdonSoba", "dailySpecialRamenPasta", "ramen"];

module.exports = {
	data: new SlashCommandBuilder()
		.setName("tomorrow")
		.setDescription("明日の学食を表示します")
        .setDMPermission(false),
        async execute(interaction) {
            const today = new Date().getDay();
            if ((today+1) === 0 || (today+1) === 6) {
                await interaction.reply("明日は休日です。学食はありません");
                return;
            }
            const embed = new EmbedBuilder()
                .setTitle("明日の学食")
                .setDescription("明日の学食は以下の通りです")
                .setFooter({text: "※内容は変更される可能性があります"})
                .setTimestamp()
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