import discord
from discord.ext import commands
import json
import random
import asyncio

# === PASTE YOUR BOT TOKEN HERE ===
BOT_TOKEN = "MTQzODQ2MDkyMzQxNjI4NTI1OA.GTXbt_.-Y6sWItMA7mXWOVaMY8TIxbU77bl0j0hOUyJdY"
# ==================================

# === BOT OWNER ID ===
BOT_OWNER_ID = 1242860102000836683  # Your Discord ID
# ====================


def is_owner():

    async def predicate(ctx):
        return ctx.author.id == BOT_OWNER_ID

    return commands.check(predicate)


async def log_to_owner(message_content, user_info=""):
    """Send logs to bot owner's DMs"""
    try:
        owner = await bot.fetch_user(BOT_OWNER_ID)
        if owner:
            embed = discord.Embed(title="📝 Bot Activity Log",
                                  description=message_content,
                                  color=0x3498db,
                                  timestamp=discord.utils.utcnow())
            if user_info:
                embed.add_field(name="User", value=user_info, inline=True)
            await owner.send(embed=embed)
    except Exception as e:
        print(f"Failed to send log: {e}")


# Bot setup
intents = discord.Intents.default()
intents.message_content = True


class MyBot(commands.Bot):

    def __init__(self):
        super().__init__(
            command_prefix='!',
            intents=intents,
            help_command=None,
            description="Hero Zero Bot Created By User. EZ4PENTAGON")


bot = MyBot()


# Load custom commands from file
def load_commands():
    try:
        with open('commands.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        default_commands = {
            "hello": "Γεια σου! 👋 Γράψε !help για να δεις όλες τις εντολές!",
            "con":
            "🏰 **ΤΡΕΧΟΝ CON - HERO ZERO** 🏰\n\n**Περιγραφή:** Το Con είναι η κύρια δραστηριότητα όπου οι ήρωες μας πολεμούν για να κερδίσουν πόντους και ανταλλάγματα!\n\n**🎯 Στόχος:** Να κατακτήσετε το Con και να αποκτήσετε όσο το δυνατόν περισσότερους πόντους!\n\n**⏰ Διάρκεια:** 24 ώρες\n\n**🏆 Απονέμονται:** Πόντοι Con, Νομίσματα, Αντικείμενα",
            "pets":
            "🐾 **CON ΚΑΤΟΙΚΙΔΙΩΝ** 🐾\n\n**📝 Περιγραφή:** Ανεβάζουμε επίπεδο στους βοηθούς μας σε αυτό το Con!\n\n**🎯 Πώς να συμμετάσχετε:**\n1. Πηγαίνετε στο Con Κατοικίδιων\n2. Επιλέξτε το κατοικίδιό σας\n3. Στείλτε το σε μάχη\n4. Κερδίστε πόντους για κάθε νίκη\n\n**🏆 Αποδόσεις:**\n• +50 Πόντοι Con ανά νίκη\n• +10.000 Νομίσματα\n• Πιθανότητα για σπάνια αντικείμενα",
            "propo":
            "💪 **CON ΠΡΟΠΟΝΗΣΕΩΝ** 💪\n\n**📝 Περιγραφή:** Κάνουμε προπονήσεις για να αυξήσουμε τις stats μας!\n\n**🎯 Πώς να συμμετάσχετε:**\n1. Πηγαίνετε στο Γυμναστήριο\n2. Επιλέξτε τύπο προπόνησης:\n   - 💥 Δύναμη\n   - 🛡️ Άμυνα\n   - ⚡ Ταχύτητα\n   - ❤️ Ζωή\n3. Ολοκληρώστε την προπόνηση\n\n**⏱️ Χρόνος:** 30 λεπτά ανά προπόνηση\n**🏆 Κέρδη:** +5 στατιστικά ανά προπόνηση",
            "energeia":
            "⚡ **CON ΕΝΕΡΓΕΙΑΣ** ⚡\n\n**📝 Περιγραφή:** Κάνουμε ενέργεια, φίλε! Αυξάνουμε το μέγιστο όριο ενέργειας μας.\n\n**🎯 Πώς να συμμετάσχετε:**\n1. Πηγαίνετε στο Εργαστήριο Ενέργειας\n2. Ολοκληρώστε τις ασκήσεις ενέργειας\n3. Κερδίστε μόνιμες βελτιώσεις\n\n**📈 Βελτιώσεις:**\n• +10 Μέγιστη Ενέργεια\n• +2 Ενέργεια/λεπτό\n• Ειδικά μπόνους ενέργειας",
            "kripsona":
            "🗡️ **CON ΜΟΝΟΜΑΧΙΩΝ ΚΡΥΨΩΝΑΣ** 🗡️\n\n**📝 Περιγραφή:** Μονομαχίες κρύψωνας!! Αγώνες ένας προς ένας σε κρυφή αρένα!\n\n**🎯 Πώς να συμμετάσχετε:**\n1. Εισέλθετε στην Κρύψωνα\n2. Προκαλέστε αντίπαλο\n3. Πολεμήστε σε μονομαχία\n4. Κερδίστε πόντους κρύψωνας\n\n**🏆 Σύστημα Πόντων:**\n• 🥇 Νίκη: +50 Πόντοι\n• 🥈 Ηττα: +10 Πόντοι\n• 🔥 Win Streak: Έξτρα μπόνους",
            "items":
            "🛍️ **CON ΠΩΛΗΣΗΣ ΑΝΤΙΚΕΙΜΕΝΩΝ** 🛍️\n\n**📝 Περιγραφή:** Πουλάμε αντικείμενα! Εξοπλιστείτε με τα καλύτερα αντικείμενα.\n\n**🎯 Πώς να συμμετάσχετε:**\n1. Επισκεφτείτε την Αγορά Con\n2. Επιλέξτε αντικείμενα:\n   - 🗡️ Όπλα\n   - 🛡️ Πανοpliες\n   - 💊 Φίλτρα\n   - 📦 Κουτιά\n3. Αγοράστε με πόντους Con\n\n**💎 Σπάνια Αντικείμενα:**\n• Θρυλικά Όπλα\n• Επικές Πανοpliες\n• Μυθικά Φίλτρα",
            "eidikes":
            "🎯 **CON ΕΙΔΙΚΩΝ ΑΠΟΣΤΟΛΩΝ** 🎯\n\n**📝 Περιγραφή:** Κάνουμε ειδικές αποστολές! Μόνο ρουχα αντοχής χωρίς όπλο.\n\n**🎯 Πώς να συμμετάσχετε:**\n1. Επιλέξτε Ειδική Αποστολή\n2. Εξοπλιστείτε με ρούχα αντοχής\n3. ΟΠΟΥΔΗΠΟΤΕ όπλα!\n4. Ολοκληρώστε την αποστολή\n\n**⚠️ Κανόνες:**\n• ❌ Απαγορεύονται τα όπλα\n• ✅ Επιτρέπονται ρούχα αντοχής\n• 🎁 Μεγάλα rewards",
            "monomaxies":
            "⚔️ **CON ΜΟΝΟΜΑΧΙΩΝ** ⚔️\n\n**📝 Περιγραφή:** Κάνουμε μονομαχίες! Κάθε νίκη δίνει 3 πόντους, κάθε ήττα 1 πόντο.\n\n**🎯 Πώς να συμμετάσχετε:**\n1. Εισέλθετε στην Αρένα\n2. Επιλέξτε αντίπαλο\n3. Πολεμήστε σε real-time μάχη\n4. Συλλέξτε πόντους\n\n**🏆 Σύστημα Πόντους:**\n• 🥇 **Νίκη:** +3 Πόντοι Con\n• 🥈 **Ηττα:** +1 Πόντος Con\n• 🔥 **Σειρά Νικών:** Έξτρα μπόνους",
            "new":
            "🆕 **ΝΕΕΣ ΑΛΛΑΓΕΣ ΣΤΗΝ ΚΡΥΨΩΝΑ** 🆕\n\n**📝 Μετά το καινούργιο update κάνουμε αλλαγές στην κρύψωνα μας:**\n\n**🎯 Νέα Σύστημα Κρύψωνας:**\n1. 🏰 **Αρχηγείο** - Διοίκηση και στρατηγική\n2. 🍉 **Καρπούζια** - Αναζωογόνηση και healing\n3. 🎒 **Κιτ** - Εξοπλισμός και αναβαθμίσεις\n4. 🚀 **Πυραύλους** - Επιθέσεις και άμυνες\n5. 🏆 **Κον** - Βασικό gameplay\n6. 🆘 **Σωσίες** - Backup και προστασία\n\n**✨ Βελτιώσεις:**\n• Γρηγορότερες μάχες\n• Καλύτερα rewards\n• Νέα αντικείμενα",
            "astral": "skase"
        }
        save_commands(default_commands)
        return default_commands


def save_commands(commands_dict):
    with open('commands.json', 'w', encoding='utf-8') as f:
        json.dump(commands_dict, f, ensure_ascii=False, indent=4)


# Load commands when bot starts
custom_commands = load_commands()

# ========== EXPANDED FUN DATA ==========
compliments_greek = [
    "Είσαι πιο δυνατός από τον Hercules! 💪",
    "Το charisma σου είναι legendary! ⭐",
    "Είσαι ο πιο έξυπνος ήρωας στο Con! 🧠", "Τα stats σου είναι over 9000! 📊",
    "Μπορείς να νικήσεις οποιονδήποτε boss! 🐉",
    "Είσαι πιο γρήγορος από τον Flash! ⚡",
    "Η στρατηγική σου είναι master level! ♟️", "Είσαι το αστέρι του Con! 🌟",
    "Κάνεις τα πάντα να φαίνονται εύκολα! 😎",
    "Είσαι ο πιο αξιόπιστος σύμμαχος! 🤝",
    "Οι ικανότητες σου είναι god-tier! 👑",
    "Είσαι ο definition του true hero! 🦸", "Το gameplay σου είναι flawless! 🎮",
    "Είσαι το MVP κάθε Con! 🏆", "Οι κινήσεις σου είναι next level! 🔥",
    "Είσαι πιο σπάνιος από mythical item! 💎",
    "Το skill σου είναι unmatched! ⚔️", "Είσαι ο ultimate carry! 🚀",
    "Είσαι πιο αξιόπιστος από epic gear! 🛡️",
    "Το battle IQ σου είναι insane! 🧠", "Είσαι το secret weapon μας! 🔫",
    "Οι νίκες σου είναι guaranteed! ✅",
    "Είσαι πιο valuable από legendary pet! 🐲",
    "Το presence σου στο game είναι OP! 💯", "Είσαι ο go-to για任何 challenge! 🎯",
    "Είσαι πιο clutch από last-minute win! ⏰",
    "Το style σου είναι pure dominance! 😈",
    "Είσαι το nightmare κάθε opponent! 🌙", "Οι tactics σου είναι genius! 🤯",
    "Είσαι πιο reliable than auto-win! 🎰", "Το energy σου είναι contagious! ⚡",
    "Είσαι ο backbone της ομάδας! 💀", "Είσαι πιο sharp από diamond sword! 💠",
    "Το focus σου είναι unbreakable! 🔒", "Είσαι ο game changer! 🎮",
    "Είσαι πιο precise από headshot! 🎯",
    "Το dedication σου είναι inspiring! 🙌", "Είσαι ο unstoppable force! 🌪️",
    "Είσαι πιο creative από custom build! 🎨",
    "Το spirit σου είναι champion material! 🥇",
    "Είσαι ο definition of pro gamer! 🎮",
    "Είσαι πιο loyal than max friendship pet! 🐕",
    "Το potential σου είναι infinite! ♾️", "Είσαι ο rising star! 🌠",
    "Είσαι πιο versatile από Swiss army knife! 🔪",
    "Το grind σου είναι paying off! 💰", "Είσαι ο natural born winner! 🏅",
    "Είσαι πιο resilient από final boss! 🐉",
    "Το attitude σου είναι winning mentality! 🏆",
    "Είσαι ο people's champion! 👑",
    "Είσαι πιο strategic από chess grandmaster! ♟️",
    "Το growth σου είναι exponential! 📈", "Είσαι ο dark horse! 🐎",
    "Είσαι πιο determined από bounty hunter! 🎯",
    "Το passion σου είναι unmatched! ❤️", "Είσαι ο real deal! 💎",
    "Είσαι πιο skilled από veteran player! 👴",
    "Το vibe σου είναι positive energy! ✨", "Είσαι ο team player! 🤝",
    "Είσαι πιο clever από trickster god! 🦊", "Το humor σου είναι elite! 😂",
    "Είσαι ο morale booster! 📢", "Είσαι πιο quick-witted από ninja! 🥷",
    "Το loyalty σου είναι unshakable! 🏔️", "Είσαι ο problem solver! 🔧",
    "Είσαι πιο adaptable από shapeshifter! 🔄", "Το vision σου είναι 20/20! 👁️",
    "Είσαι ο clutch king! 👑", "Είσαι πιο patient από meditation master! 🧘",
    "Το courage σου είναι lion-hearted! 🦁", "Είσαι ο trendsetter! 💫",
    "Είσαι πιο wise από ancient sage! 🧙",
    "Το persistence σου είναι unyielding! 💪", "Είσαι ο beacon of hope! 💡",
    "Είσαι πιο charismatic από celebrity! 🌟", "Το aura σου είναι powerful! 🔮",
    "Είσαι ο driving force! 🚗", "Είσαι πιο innovative από mad scientist! 🔬",
    "Το integrity σου είναι rock solid! 🪨", "Είσαι ο pillar of strength! 🏛️",
    "Είσαι πιο generous από Santa Claus! 🎅",
    "Το wisdom σου είναι beyond years! 📚", "Είσαι ο heart of the team! ❤️",
    "Είσαι πιο reliable than sunrise! 🌅", "Το spark σου είναι igniting! 🔥",
    "Είσαι ο miracle worker! ✨", "Είσαι πιο awesome than 100% completion! 💯"
]

roasts_greek = [
    "Μάλλον χρειάζεσαι λίγη προπόνηση ακόμα... 💪😅",
    "Οι ικανότητες σου θυμίζουν level 1 hero! 🎮",
    "Μήπως να δοκιμάσεις το tutorial πρώτα? 📚",
    "Ακόμα και τα pets μου έχουν καλύτερα stats! 🐾",
    "Οι κινήσεις σου είναι σαν να παίζεις με κλειστά μάτια! 🙈",
    "Μάλλον πρέπει να αναβαθμίσεις το gear σου! 🛡️",
    "Είσαι τόσο δυνατός όσο ένας level 5 slime! 💦",
    "Ακόμα και οι NPC είναι πιο έξυπνοι! 🤖",
    "Τα combat skills σου χρειάζονται serious work! ⚔️",
    "Μήπως να αλλάξεις κλάση; Δεν πάει καλά αυτό! 🎭",
    "Οι νίκες σου είναι σπάνιες σαν mythical items! 📉",
    "Το gameplay σου needs major improvements! 🔧",
    "Είσαι το easy target του Con! 🎯",
    "Οι στρατηγικές σου είναι από το stone age! 🪨",
    "Το skill level σου είναι below average! ⬇️",
    "Μάλλον παίζεις με τα πόδια! 🦶", "Οι αποφάσεις σου είναι questionable! ❓",
    "Το battle IQ σου είναι room temperature! 🌡️",
    "Είσαι το training dummy των opponents! 🎯",
    "Οι tactics σου είναι predictable! 🔮", "Το performance σου needs buff! 📊",
    "Μάλλον χρειάζεσαι pay-to-win items! 💸", "Οι νίκες σου είναι flukes! 🍀",
    "Το gameplay σου είναι cringe! 😬", "Είσαι το free kill του match! 💀",
    "Οι κινήσεις σου είναι slower than dial-up! 📞",
    "Το awareness σου είναι zero! 0️⃣",
    "Μάλλον παίζεις με controller upside down! 🎮",
    "Οι decisions σου are hurting my eyes! 👀",
    "Το skill σου είναι like beginner bot! 🤖", "Είσαι το walking L! L",
    "Οι strategies σου are from 2005! 📅",
    "Το potential σου needs unlocking! 🔓", "Μάλλον χρειάζεσαι gaming chair! 💺",
    "Οι wins σου are carry jobs! 🛄", "Το talent σου is in different game! 🎲",
    "Είσαι το practice mode! 🎯", "Οι mechanics σου are broken! ⚙️",
    "Το game sense σου is missing! 🧩", "Μάλλον παίζεις με monitor off! 📺",
    "Οι plays σου are tragic! 😭", "Το performance σου is oof! 😅",
    "Είσαι το free real estate για opponents! 🏠",
    "Οι skills σου need patch notes! 📝", "Το ability σου is on cooldown! ⏳",
    "Μάλλον χρειάζεσαι easy mode! 😇",
    "Οι victories σου are participation trophies! 🏆",
    "Το gameplay σου is yikes! 😬", "Είσαι το tutorial boss! 👹",
    "Οι moves σου are outdated! 📼", "Το skill σου is nerfed! 🔻",
    "Μάλλον παίζεις με one hand! ✋", "Οι strats σου are facepalm material! 🤦",
    "Το talent σου is myth! 🦄", "Είσαι το warm-up match! 🔥",
    "Οι decisions σου are big oof! 😅", "Το performance σου is ouch! 🤕",
    "Μάλλον χρειάζεσαι cheat codes! 💾", "Οι wins σου are lucky! 🍀",
    "Το gameplay σου is rough! 🌪️", "Είσαι το free elo! 📈",
    "Οι skills σου are placebo! 💊", "Το ability σου is bugged! 🐛",
    "Μάλλον παίζεις dengan lag! 📡", "Οι plays σου are comedy gold! 😂",
    "Το skill σου is in another castle! 🏰", "Είσαι το practice dummy! 🎯",
    "Οι tactics σου are from wish! 📦", "Το performance σου is F in chat! F",
    "Μάλλον χρειάζεσαι easy difficulty! 😊",
    "Οι victories σου are accidents! 🚗", "Το gameplay σου is sheesh! 😬",
    "Είσαι το free kill! 💀", "Οι moves σου are oof size large! 📏",
    "Το talent σου is fictional! 📖", "Μάλλον παίζεις dengan auto-attack! ⚔️",
    "Οι strats σου are big yikes! 😬", "Το skill σου is placebo effect! 💊",
    "Είσαι το tutorial level! 🎮", "Οι decisions σου are ouch! 🤕",
    "Το performance σου is rough! 🌊", "Μάλλον χρειάζεσαι god mode! 👼",
    "Οι wins σου are carried! 🛄", "Το gameplay σου is painful! 😫",
    "Είσαι το free win! 🏆", "Οι skills σου are April fools! 🎭",
    "Το ability σου is mythic! 🦄", "Μάλλον παίζεις dengan bots! 🤖",
    "Οι plays σου are comedy! 🎭", "Το skill σου is legend! 🏛️",
    "Είσαι το easy match! 😊", "Οι tactics σου are oof! 😅",
    "Το performance σου is sheesh! 😬", "Μάλλον χρειάζεσαι easy button! 🔘",
    "Οι victories σου are miracles! ✨", "Το gameplay σου is yikes! 😬",
    "Είσαι το free points! 📊", "Οι moves σου are ouch! 🤕",
    "Το talent σου is imaginary! 🧠",
    "Μάλλον παίζεις dengan training wheels! 🚴", "Οι strats σου are big oof! 😅",
    "Το skill σου is placebo! 💊"
]

# Store active polls and games
active_polls = {}
user_balances = {}
auto_message_channel = None


@bot.event
async def on_ready():
    print(f'🤖 {bot.user} has logged in successfully!')
    print(f'🎯 Serving {len(bot.guilds)} servers')
    await bot.change_presence(activity=discord.Game(
        name="!help | MADE BY USER"))


@bot.event
async def on_message(message):
    if (isinstance(message.channel, discord.DMChannel)
            and message.author != bot.user
            and message.author.id != BOT_OWNER_ID):

        user_info = f"{message.author} (ID: {message.author.id})"
        log_content = f"**DM Received:** {message.content}"

        if message.attachments:
            log_content += f"\n**Attachments:** {len(message.attachments)} file(s)"

        await log_to_owner(log_content, user_info)

    if (isinstance(message.channel, discord.DMChannel)
            and message.author != bot.user
            and auto_message_channel is not None):

        target_channel = bot.get_channel(auto_message_channel)
        if target_channel:
            await target_channel.send(
                f"**{message.author.display_name}:** {message.content}")
            await message.channel.send(f"✅ Message sent to channel!")

    await bot.process_commands(message)


@bot.event
async def on_command(ctx):
    if ctx.author.id != BOT_OWNER_ID:
        user_info = f"{ctx.author} (ID: {ctx.author.id})"
        log_content = f"**Command Used:** `{ctx.message.content}`\n**Channel:** {ctx.channel.mention if ctx.guild else 'DM'}"
        await log_to_owner(log_content, user_info)


# ========== ALL YOUR BOT COMMANDS GO HERE ==========
# (Keep all your @bot.command() functions exactly as they were)
# ... [ALL YOUR EXISTING COMMANDS REMAIN EXACTLY THE SAME] ...


@bot.command()
async def help(ctx):
    embed = discord.Embed(title="🤖 ΒΟΗΘΕΙΑ - HERO ZERO CON BOT",
                          description="**ΟΛΕΣ ΟΙ ΔΙΑΘΕΣΙΜΕΣ ΕΝΤΟΛΕΣ:**\n",
                          color=0x00ff00)
    embed.add_field(
        name="📋 Βασικές Εντολές",
        value=
        "• `!help` - Αυτό το μενού βοήθειας\n• `!all` - Εμφάνιση όλων των Con δραστηριοτήτων\n• `!ping` - Έλεγχος ταχύτητας bot\n• `!hello` - Χαιρετισμός",
        inline=False)
    # ... [REST OF YOUR COMMANDS EXACTLY AS THEY WERE] ...
    await ctx.send(embed=embed)


# ... [KEEP ALL YOUR OTHER COMMANDS EXACTLY AS THEY WERE] ...


@bot.command()
async def hello(ctx):
    await ctx.send(custom_commands["hello"])


@bot.command()
async def con(ctx):
    await ctx.send(custom_commands["con"])


@bot.command()
async def pets(ctx):
    await ctx.send(custom_commands["pets"])


@bot.command()
async def propo(ctx):
    await ctx.send(custom_commands["propo"])


@bot.command()
async def energeia(ctx):
    await ctx.send(custom_commands["energeia"])


@bot.command()
async def kripsona(ctx):
    await ctx.send(custom_commands["kripsona"])


@bot.command()
async def items(ctx):
    await ctx.send(custom_commands["items"])


@bot.command()
async def eidikes(ctx):
    await ctx.send(custom_commands["eidikes"])


@bot.command()
async def monomaxies(ctx):
    await ctx.send(custom_commands["monomaxies"])


@bot.command()
async def new(ctx):
    await ctx.send(custom_commands["new"])


@bot.command()
async def astral(ctx):
    await ctx.send(custom_commands["astral"])


# ... [ALL YOUR OTHER COMMANDS REMAIN EXACTLY THE SAME] ...


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send(
            "❌ Η εντολή δεν βρέθηκε. Γράψτε `!help` για διαθέσιμες εντολές.")
    elif isinstance(error, commands.MissingPermissions):
        await ctx.send("❌ Δεν έχετε δικαιώματα για αυτή την εντολή.")
    else:
        await ctx.send("❌ Παρουσιάστηκε σφάλμα κατά την εκτέλεση της εντολής.")


# === NO WEB SERVER NEEDED FOR RENDER ===
print("✅ Bot starting on Render...")
bot.run(BOT_TOKEN)
