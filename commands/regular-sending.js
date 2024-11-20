const { SlashCommandBuilder, EmbedBuilder } = require("discord.js");
const cron = require("node-cron");
const lunch = require("../data/lunch.json");

const days = ["Mon", "Tue", "Wed", "Thu", "Fri"];

const dispMenu = ["Aセット", "Bセット", "カレー", "日替わりうどん・そば", "うどん・そば", "日替わりラーメン・パスタ", "ラーメン"];
const menu = ["Aset", "Bset", "curry", "dailySpecialUdonSoba", "UdonSoba", "dailySpecialRamenPasta", "ramen"];

module.exports = {
    data: new SlashCommandBuilder()
		.setName("regular-sending")
		.setDescription("20:00に明日の学食のメニューを送信します")
        .setDefaultMemberPermissions(1<<3)
        .setDMPermission(false),
        async execute(interaction) {
            await interaction.deferReply({ephemeral: true});
            await interaction.editReply("20:00に明日の学食のメニューを送信します");
            cron.schedule("0 20 * * * ", async() => {
                const today = new Date().getDay();
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
                if ((today+1) === 0 || (today+1) === 6) {
                    await interaction.channel.send("明日は休日です。学食はありません");
                }
                else {
                    await interaction.channel.send({ embeds: [embed]});
                }    
            });
            
        }
}