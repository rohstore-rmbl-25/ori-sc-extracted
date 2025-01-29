from kyt import *

# // DELETE IP
@bot.on(events.CallbackQuery(data=b'deleteip'))
async def deleteipp(event):
	async def deleteipp_(event):
		async with bot.conversation(chat) as pw:
			await event.respond("**Input IP VPS:**")
			pw = pw.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
			pw = (await pw).raw_text
		cmd = f'printf "%s\n" "{pw}" | del-ip-bot'
		try:
			a = subprocess.check_output(cmd, shell=True).decode("utf-8")
		except:
			await event.respond("**Not Exist**")
		else:
			msg = f"""
**━━━━━━━━━━━━━━━━━━━**
 **⟨ SUCCESS DELETE IP ADDRESS ⟩**
**━━━━━━━━━━━━━━━━━━━**
 `IP VPS   :` `{pw}`
**━━━━━━━━━━━━━━━━━━━**
**» 🤖@D_swara**"""
			await event.respond(msg)
	chat = event.chat_id
	sender = await event.get_sender()
	a = valid(str(sender.id))
	if a == "true":
		await deleteipp_(event)
	else:
		await event.answer("Akses Ditolak",alert=True)

# // ADD IP
@bot.on(events.CallbackQuery(data=b'resgissc'))
async def registersc(event):
	async def registersc_(event):
		async with bot.conversation(chat) as user:
			await event.respond('**Username:**')
			user = user.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
			user = (await user).raw_text
		async with bot.conversation(chat) as pw:
			await event.respond("**IP VPS:**")
			pw = pw.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
			pw = (await pw).raw_text
		async with bot.conversation(chat) as exp:
			await event.respond("**Choose Expiry Day**",buttons=[
[Button.inline(" 30 Day ","30"),
Button.inline(" 60 Day ","60")],
[Button.inline(" 90 Day ","90"),
Button.inline(" Lifetime ","360")]])
			exp = exp.wait_event(events.CallbackQuery)
			exp = (await exp).data.decode("ascii")
		cmd = f'printf "%s\n" "{pw}" "{user}" "{exp}" | add-ip-bot'
		try:
			a = subprocess.check_output(cmd, shell=True).decode("utf-8")
		except:
			await event.respond("**User Already Exist**")
		else:
			msg = f"""
**━━━━━━━━━━━━━━━━━━━**
 **⟨ SUCCESS ADD IP ADDRESS ⟩**
**━━━━━━━━━━━━━━━━━━━**
 `Username :` `{user}`
 `IP VPS   :` `{pw}`
 `Expired  :` `{exp} Days`
**━━━━━━━━━━━━━━━━━━━**
**» 🤖@D_swara**"""
			await event.respond(msg)
	chat = event.chat_id
	sender = await event.get_sender()
	a = valid(str(sender.id))
	if a == "true":
		await registersc_(event)
	else:
		await event.answer("Akses Ditolak",alert=True)
		
@bot.on(events.CallbackQuery(data=b'regis'))
async def menu(event):
	inline = [
[Button.inline(" ADD IP ","resgissc"),
Button.inline(" DELETE IP ","deleteip")],
[Button.inline(" RENEW IP ","renewip")],
[Button.url(" CHANNEL ","https://t.me/D_swara")]]
	sender = await event.get_sender()
	val = valid(str(sender.id))
	if val == "false":
		try:
			await event.answer("Akses Ditolak", alert=True)
		except:
			await event.reply("Akses Ditolak")
	elif val == "true":
		sh = f' curl -sS https://raw.githubusercontent.com/okysmilee2/izin/main/ip | grep "###" | wc -l'
		usersc = subprocess.check_output(sh, shell=True).decode("ascii")
		sdss = f" cat /etc/os-release | grep -w PRETTY_NAME | head -n1 | sed 's/=//g' | sed 's/PRETTY_NAME//g'"
		namaos = subprocess.check_output(sdss, shell=True).decode("ascii")
		ipvps = f" curl -s ipv4.icanhazip.com"
		ipsaya = subprocess.check_output(ipvps, shell=True).decode("ascii")

		msg = f"""
━━━━━━━━━━━━━━━━━━━━━━━ 
  **⟨ REGISTRASI IP AUTO SCRIPT ⟩**
━━━━━━━━━━━━━━━━━━━━━━━ 
`➤ Hi** {sender.first_name}
`➤ Total User    :` `{usersc.strip()}`
`➤ Autoscript By :` @D_swara
━━━━━━━━━━━━━━━━━━━━━━━ 

"""
		x = await event.edit(msg,buttons=inline)
		if not x:
			await event.reply(msg,buttons=inline)

