def image_gen(image_text, api_key):
    import openai
    openai.api_key = api_key
    response = openai.Image.create(
        prompt=image_text,
        n=1,
        size="1024x1024"
    )
    image_list = []
    for url in response['data']:
        image_list.append(url['url'])
    return image_list


def save_apis(user_id, api_key):
    import json
    with open("api.json", 'rb') as api_list:
        api_json = json.load(api_list)
        api_dict = dict(api_json)
    user_id = str(user_id)
    api_dict[user_id] = api_key
    json_object = json.dumps(api_dict, indent=4)
    with open('api.json', 'w') as outfile:
        outfile.write(json_object)

def search_api(user_id):
    import json
    user_id = str(user_id)
    with open("api.json", 'rb') as api_list:
        api_json = json.load(api_list)
        api_dict = dict(api_json)
    return api_dict[user_id]


def ai_chat(message, api_key):
    import openai
    openai.api_key = api_key

    response = openai.Completion.create(
        prompt=message,
        model="text-davinci-002",
        max_tokens=4000
    )

    reply = response["choices"][0]["text"]

    print(f"Bot : {reply}")
    reply = str(reply)
    # reply = reply.replace('\n',"")
    # reply = reply.replace('\t',"")

    return reply


from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes


async def art_gen(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    try:
        user_id = update.message.from_user.id
        user_api = search_api(user_id)
        # await update.message.reply_text(f'Hello {update.effective_user.first_name}')
        image_text = update.message.text[9:]
        image_urls = image_gen(image_text, user_api)
        for url in image_urls:
            await update.message.reply_photo(url)
    except:
        await update.message.reply_text("""You are not registered to use this bot.
Please follow the instructions.
ඔයාල පහල link එක ඔබලා register වෙලා ඒකෙ තියෙන api key එක කොපි කරගන්න ඕනි.

👇👇👇
https://beta.openai.com/account/api-keys

ඊට පස්සෙ,

/reg_api <ඔයාලගෙ api එක>

👆👆
ඔහොම මැසේජ් එකක් බොටාට inbox යවන්නයි තියෙම්නෙ.
ඊට පස්සෙ ඔයාට දිගටම අපේ bot use කරන්න පුලුවන්.

bot 👇
@HP_AI_BOT
""")


async def help_text(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("""Available commands
    
/reg_api <open ai api key> - register to use this bot

/art_gen <describe about art you want> - Draw ART using AI
/essay_gen <essay topic> - Write essay using AI
/song_gen <song topic> - Write song using AI
/grammar_check <your text> - Check all grammar problems 

/python_code_gen <describe code you want> - Write python code using AI
/go_code_gen - Write go code using AI
/java_script_code_gen - Write Java Script code using AI
/perl_code_gen - Write perl code using AI
/php_code_gen - Write php code using AI
/ruby_code_gen - Write ruby code using AI
/shell_code_gen - Write shell code using AI
/swift_code_gen - Write swift code using AI

/recipe_gen - Create recipe for cooking food
""")
    print(update.message.from_user.id)


async def essay_gen(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    try:
        user_id = update.message.from_user.id
        user_api = search_api(user_id)
        essay_topic = update.message.text[11:]
        response = ai_chat(f"Write a essay about {essay_topic}", user_api)
        await update.message.reply_text(response)
    except:
        await update.message.reply_text("""You are not registered to use this bot.
Please follow the instructions.
ඔයාල පහල link එක ඔබලා register වෙලා ඒකෙ තියෙන api key එක කොපි කරගන්න ඕනි.

👇👇👇
https://beta.openai.com/account/api-keys

ඊට පස්සෙ,

/reg_api <ඔයාලගෙ api එක>

👆👆
ඔහොම මැසේජ් එකක් බොටාට inbox යවන්නයි තියෙම්නෙ.
ඊට පස්සෙ ඔයාට දිගටම අපේ bot use කරන්න පුලුවන්.

bot 👇
@HP_AI_BOT
""")


async def grammar_check(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    try:
        user_id = update.message.from_user.id
        user_api = search_api(user_id)
        user_text = update.message.text[15:]
        response = ai_chat(f"""Check grammar problems in following text. 
{user_text}""", user_api)
        await update.message.reply_text(response)
    except:
        await update.message.reply_text("""You are not registered to use this bot.
Please follow the instructions.
ඔයාල පහල link එක ඔබලා register වෙලා ඒකෙ තියෙන api key එක කොපි කරගන්න ඕනි.

👇👇👇
https://beta.openai.com/account/api-keys

ඊට පස්සෙ,

/reg_api <ඔයාලගෙ api එක>

👆👆
ඔහොම මැසේජ් එකක් බොටාට inbox යවන්නයි තියෙම්නෙ.
ඊට පස්සෙ ඔයාට දිගටම අපේ bot use කරන්න පුලුවන්.

bot 👇
@HP_AI_BOT
""")


async def recipe_gen(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    try:
        user_id = update.message.from_user.id
        user_api = search_api(user_id)
        recipe_topic = update.message.text[12:]
        response = ai_chat(f"Write a recipe for {recipe_topic}", user_api)
        await update.message.reply_text(response)
    except:
        await update.message.reply_text("""You are not registered to use this bot.
Please follow the instructions.
ඔයාල පහල link එක ඔබලා register වෙලා ඒකෙ තියෙන api key එක කොපි කරගන්න ඕනි.

👇👇👇
https://beta.openai.com/account/api-keys

ඊට පස්සෙ,

/reg_api <ඔයාලගෙ api එක>

👆👆
ඔහොම මැසේජ් එකක් බොටාට inbox යවන්නයි තියෙම්නෙ.
ඊට පස්සෙ ඔයාට දිගටම අපේ bot use කරන්න පුලුවන්.

bot 👇
@HP_AI_BOT
""")


async def python_code_gen(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    try:
        user_id = update.message.from_user.id
        user_api = search_api(user_id)
        code_description = update.message.text[10:]
        response = ai_chat(f"Write a python code for {code_description}", user_api)
        await update.message.reply_text(response)
    except:
        await update.message.reply_text("""You are not registered to use this bot.
Please follow the instructions.
ඔයාල පහල link එක ඔබලා register වෙලා ඒකෙ තියෙන api key එක කොපි කරගන්න ඕනි.

👇👇👇
https://beta.openai.com/account/api-keys

ඊට පස්සෙ,

/reg_api <ඔයාලගෙ api එක>

👆👆
ඔහොම මැසේජ් එකක් බොටාට inbox යවන්නයි තියෙම්නෙ.
ඊට පස්සෙ ඔයාට දිගටම අපේ bot use කරන්න පුලුවන්.

bot 👇
@HP_AI_BOT
""")


async def song_gen(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    try:
        user_id = update.message.from_user.id
        user_api = search_api(user_id)
        song_topic = update.message.text[10:]
        response = ai_chat(f"Write a song about {song_topic}", user_api)
        print(response)
        await update.message.reply_text(response)
    except:
        await update.message.reply_text("""You are not registered to use this bot.
Please follow the instructions.
ඔයාල පහල link එක ඔබලා register වෙලා ඒකෙ තියෙන api key එක කොපි කරගන්න ඕනි.

👇👇👇
https://beta.openai.com/account/api-keys

ඊට පස්සෙ,

/reg_api <ඔයාලගෙ api එක>

👆👆
ඔහොම මැසේජ් එකක් බොටාට inbox යවන්නයි තියෙම්නෙ.
ඊට පස්සෙ ඔයාට දිගටම අපේ bot use කරන්න පුලුවන්.

bot 👇
@HP_AI_BOT
""")


async def c_code_gen(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    try:
        user_id = update.message.from_user.id
        user_api = search_api(user_id)
        code_topic = update.message.text[12:]
        response = ai_chat(f"Write a C code for {code_topic}", user_api)
        print(response)
        await update.message.reply_text(response)
    except:
        await update.message.reply_text("""You are not registered to use this bot.
Please follow the instructions.
ඔයාල පහල link එක ඔබලා register වෙලා ඒකෙ තියෙන api key එක කොපි කරගන්න ඕනි.

👇👇👇
https://beta.openai.com/account/api-keys

ඊට පස්සෙ,

/reg_api <ඔයාලගෙ api එක>

👆👆
ඔහොම මැසේජ් එකක් බොටාට inbox යවන්නයි තියෙම්නෙ.
ඊට පස්සෙ ඔයාට දිගටම අපේ bot use කරන්න පුලුවන්.

bot 👇
@HP_AI_BOT
""")


async def java_script_code_gen(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    try:
        user_id = update.message.from_user.id
        user_api = search_api(user_id)
        code_topic = update.message.text[22:]
        response = ai_chat(f"Write a Java Script code for {code_topic}", user_api)
        print(response)
        await update.message.reply_text(response)
    except:
        await update.message.reply_text("""You are not registered to use this bot.
Please follow the instructions.
ඔයාල පහල link එක ඔබලා register වෙලා ඒකෙ තියෙන api key එක කොපි කරගන්න ඕනි.

👇👇👇
https://beta.openai.com/account/api-keys

ඊට පස්සෙ,

/reg_api <ඔයාලගෙ api එක>

👆👆
ඔහොම මැසේජ් එකක් බොටාට inbox යවන්නයි තියෙම්නෙ.
ඊට පස්සෙ ඔයාට දිගටම අපේ bot use කරන්න පුලුවන්.

bot 👇
@HP_AI_BOT
""")


async def ruby_code_gen(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    try:
        user_id = update.message.from_user.id
        user_api = search_api(user_id)
        code_topic = update.message.text[15:]
        response = ai_chat(f"Write a Ruby code for {code_topic}", user_api)
        print(response)
        await update.message.reply_text(response)
    except:
        await update.message.reply_text("""You are not registered to use this bot.
Please follow the instructions.
ඔයාල පහල link එක ඔබලා register වෙලා ඒකෙ තියෙන api key එක කොපි කරගන්න ඕනි.

👇👇👇
https://beta.openai.com/account/api-keys

ඊට පස්සෙ,

/reg_api <ඔයාලගෙ api එක>

👆👆
ඔහොම මැසේජ් එකක් බොටාට inbox යවන්නයි තියෙම්නෙ.
ඊට පස්සෙ ඔයාට දිගටම අපේ bot use කරන්න පුලුවන්.

bot 👇
@HP_AI_BOT
""")


async def php_code_gen(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    try:
        user_id = update.message.from_user.id
        user_api = search_api(user_id)
        code_topic = update.message.text[14:]
        response = ai_chat(f"Write a PHP code for {code_topic}", user_api)
        print(response)
        await update.message.reply_text(response)
    except:
        await update.message.reply_text("""You are not registered to use this bot.
Please follow the instructions.
ඔයාල පහල link එක ඔබලා register වෙලා ඒකෙ තියෙන api key එක කොපි කරගන්න ඕනි.

👇👇👇
https://beta.openai.com/account/api-keys

ඊට පස්සෙ,

/reg_api <ඔයාලගෙ api එක>

👆👆
ඔහොම මැසේජ් එකක් බොටාට inbox යවන්නයි තියෙම්නෙ.
ඊට පස්සෙ ඔයාට දිගටම අපේ bot use කරන්න පුලුවන්.

bot 👇
@HP_AI_BOT
""")


async def go_code_gen(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    try:
        user_id = update.message.from_user.id
        user_api = search_api(user_id)
        code_topic = update.message.text[13:]
        response = ai_chat(f"Write a GO code for {code_topic}", user_api)
        print(response)
        await update.message.reply_text(response)
    except:
        await update.message.reply_text("""You are not registered to use this bot.
Please follow the instructions.
ඔයාල පහල link එක ඔබලා register වෙලා ඒකෙ තියෙන api key එක කොපි කරගන්න ඕනි.

👇👇👇
https://beta.openai.com/account/api-keys

ඊට පස්සෙ,

/reg_api <ඔයාලගෙ api එක>

👆👆
ඔහොම මැසේජ් එකක් බොටාට inbox යවන්නයි තියෙම්නෙ.
ඊට පස්සෙ ඔයාට දිගටම අපේ bot use කරන්න පුලුවන්.

bot 👇
@HP_AI_BOT
""")


async def perl_code_gen(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    try:
        user_id = update.message.from_user.id
        user_api = search_api(user_id)
        code_topic = update.message.text[15:]
        response = ai_chat(f"Write a Perl code for {code_topic}", user_api)
        print(response)
        await update.message.reply_text(response)
    except:
        await update.message.reply_text("""You are not registered to use this bot.
Please follow the instructions.
ඔයාල පහල link එක ඔබලා register වෙලා ඒකෙ තියෙන api key එක කොපි කරගන්න ඕනි.

👇👇👇
https://beta.openai.com/account/api-keys

ඊට පස්සෙ,

/reg_api <ඔයාලගෙ api එක>

👆👆
ඔහොම මැසේජ් එකක් බොටාට inbox යවන්නයි තියෙම්නෙ.
ඊට පස්සෙ ඔයාට දිගටම අපේ bot use කරන්න පුලුවන්.

bot 👇
@HP_AI_BOT
""")


async def shell_code_gen(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    try:
        user_id = update.message.from_user.id
        user_api = search_api(user_id)
        code_topic = update.message.text[16:]
        response = ai_chat(f"Write a Shell code for {code_topic}", user_api)
        print(response)
        await update.message.reply_text(response)
    except:
        await update.message.reply_text("""You are not registered to use this bot.
Please follow the instructions.
ඔයාල පහල link එක ඔබලා register වෙලා ඒකෙ තියෙන api key එක කොපි කරගන්න ඕනි.

👇👇👇
https://beta.openai.com/account/api-keys

ඊට පස්සෙ,

/reg_api <ඔයාලගෙ api එක>

👆👆
ඔහොම මැසේජ් එකක් බොටාට inbox යවන්නයි තියෙම්නෙ.
ඊට පස්සෙ ඔයාට දිගටම අපේ bot use කරන්න පුලුවන්.

bot 👇
@HP_AI_BOT
""")


async def swift_code_gen(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    try:
        user_id = update.message.from_user.id
        user_api = search_api(user_id)
        code_topic = update.message.text[16:]
        response = ai_chat(f"Write a Swift code for {code_topic}", user_api)
        print(response)
        await update.message.reply_text(response)
    except:
        await update.message.reply_text("""You are not registered to use this bot.
Please follow the instructions.
ඔයාල පහල link එක ඔබලා register වෙලා ඒකෙ තියෙන api key එක කොපි කරගන්න ඕනි.

👇👇👇
https://beta.openai.com/account/api-keys

ඊට පස්සෙ,

/reg_api <ඔයාලගෙ api එක>

👆👆
ඔහොම මැසේජ් එකක් බොටාට inbox යවන්නයි තියෙම්නෙ.
ඊට පස්සෙ ඔයාට දිගටම අපේ bot use කරන්න පුලුවන්.

bot 👇
@HP_AI_BOT
""")


async def reg_api(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    try:
        api_key = update.message.text[9:]
        user_id = update.message.from_user.id
        ai_chat("what is your name?", api_key)
        save_apis(user_id, api_key)
        await update.message.reply_text("success")
    except:
        await update.message.reply_text("invalid API key.")


app = ApplicationBuilder().token("BOT_TOKEN").build()

app.add_handler(CommandHandler("reg_api", reg_api))
app.add_handler(CommandHandler("art_gen", art_gen))
app.add_handler(CommandHandler("essay_gen", essay_gen))
app.add_handler(CommandHandler("song_gen", song_gen))
app.add_handler(CommandHandler("grammar_check", grammar_check))
app.add_handler(CommandHandler("python_code_gen", python_code_gen))
app.add_handler(CommandHandler("go_code_gen", go_code_gen))
app.add_handler(CommandHandler("java_script_code_gen", java_script_code_gen))
app.add_handler(CommandHandler("perl_code_gen", perl_code_gen))
app.add_handler(CommandHandler("php_code_gen", php_code_gen))
app.add_handler(CommandHandler("ruby_code_gen", ruby_code_gen))
app.add_handler(CommandHandler("shell_code_gen", shell_code_gen))
app.add_handler(CommandHandler("swift_code_gen", swift_code_gen))
app.add_handler(CommandHandler("recipe_gen", recipe_gen))
app.add_handler(CommandHandler("help", help_text))

app.run_polling()
