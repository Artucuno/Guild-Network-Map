from pyvis.network import Network
from discord.ext import commands

token = ""  # Put your token here


class Map:
    def __init__(self):
        self.net = Network(select_menu=True)
        self.net.show_buttons(filter_=["physics"])
        self.net.toggle_physics(False)

        self.bot = commands.Bot(command_prefix="!(UR#UR(#Y@)R_)#U@)(*)-", self_bot=True)
        self.botS()

        self.members = {}
        self.friends = []

    def botS(self):
        """
        Hacky way to pass self
        """

        @self.bot.event
        async def on_ready():
            print("Bot is ready!")
            self.friends = self.bot.relationships
            _fids = [x.id for x in self.friends]
            input("Press enter to continue")
            await self.bot.fetch_guilds(with_counts=True)
            for f in self.bot.guilds:
                print('[GUILD] ', f.name, f.id)
                self.net.add_node(str(f.id), label=f.name, color='#7FFFD4', value=1000)  # Add the guild to the network
                for m in f.members:  # Go through all members in the guild
                    print(f'[MEMBER] ({f.id})', m.name, m.id)
                    if str(m.id) not in self.members:  # If the member is not in the network, add them
                        if m.id in _fids:  # If the member is a friend, color them red
                            print('FRIEND')
                            self.net.add_node(str(m.id), label=m.name, color='#880808')
                        else:
                            if m.bot:  # If the member is a bot, color them orange
                                self.net.add_node(str(m.id), label=m.name, color='#FFA500')
                            else:  # If the member is a normal member, keep them default
                                self.net.add_node(str(m.id), label=m.name)
                        self.net.add_edge(str(m.id), str(f.id))  # Add an edge between the member and the guild
                    else:
                        self.net.add_edge(str(m.id), str(f.id))
            self.net.show("map.html", notebook=False)  # Show the network

    def run(self):
        self.bot.run(token)


p = Map()
p.run()
