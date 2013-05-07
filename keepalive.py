from errbot import BotPlugin, botcmd
from config import BOT_IDENTITY

class AgressiveKeepalive(BotPlugin):
	"""
	A plugin which sends additional keepalive messages every 30 seconds.

	Useful with some broken XMPP servers which timeout really quickly (like HipChat).
	"""

	def activate(self):
		super(AgressiveKeepalive, self).activate()
		self.start_poller(30, self.keepalive)
	
	def keepalive(self):
		self.send(BOT_IDENTITY['username'], "keepalive", message_type='chat')
