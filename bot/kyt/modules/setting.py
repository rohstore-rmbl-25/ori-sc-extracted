from kyt import *

@bot.on(events.CallbackQuery(data=b'reboot'))
async def rebooot(event):
	async def rebooot_(event):
		cmd = f'shutdown -r now'
		await event.edit(f"""
**» REBOOT SERVER**
**» DONE**
""",buttons=[[Button.inline("‹ Main Menu ›","menu")]])
		subprocess.check_output(cmd, shell=True)
	sender = await event.get_sender()
	a = valid(str(sender.id))
	if a == "true":
		await rebooot_(event)
	else:
		await event.answer("Access Denied",alert=True)


@bot.on(events.CallbackQuery(data=b'resx'))
async def resx(event):
	async def resx_(event):
		cmd = f'systemctl restart xray | systemctl restart nginx | systemctl restart haproxy | systemctl restart server | systemctl restart client'
		subprocess.check_output(cmd, shell=True)
		await event.edit(f"""
**» Restarting Service Done**
**» 🤖@D_swara**
""",buttons=[[Button.inline("‹ Main Menu ›","menu")]])
	sender = await event.get_sender()
	a = valid(str(sender.id))
	if a == "true":
		await resx_(event)
	else:
		await event.answer("Access Denied",alert=True)
		
@bot.on(events.CallbackQuery(data=b'speedtest'))
async def speedtest(event):
	async def speedtest_(event):
		cmd = 'speedtest-cli --share'.strip()
		x = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT, universal_newlines=True)
		print(x)
		z = subprocess.check_output(cmd, shell=True).decode("utf-8")
		await event.edit(f"""
**
{z}
**
**» Succes**
""",buttons=[[Button.inline("‹ Main Menu ›","menu")]])
	sender = await event.get_sender()
	a = valid(str(sender.id))
	if a == "true":
		await speedtest_(event)
	else:
		await event.answer("Access Denied",alert=True)


@bot.on(events.CallbackQuery(data=b'backup'))
async def backup(event):
	async def backup_(event):
		cmd = f'printf "%s\n" "3" | m-backup | sleep 6 | exit'
		subprocess.check_output(cmd, shell=True).decode("utf-8")
		await event.edit(f"""
**» Succes**
""",buttons=[[Button.inline("‹ Main Menu ›","menu")]])
	sender = await event.get_sender()
	a = valid(str(sender.id))
	if a == "true":
		await backup_(event)
	else:
		await event.answer("Access Denied",alert=True)

@bot.on(events.CallbackQuery(data=b'restore'))
async def create_restore(event):
	async def create_restore_(event):
		async with bot.conversation(chat) as pw2:
			await event.respond("**» LINK BACKUP :**")
			pw2 = pw2.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
			pw2 = (await pw2).raw_text
		cmd = f'printf "%s\n" "1" "{pw2}" | m-backup | sleep 15 | exit'
		subprocess.check_output(cmd, shell=True)
		await event.respond(f"""
**» SUCCES RESTORE AKUN**
**» DONE**
""",buttons=[[Button.inline("‹ Main Menu ›","menu")]])
	chat = event.chat_id
	sender = await event.get_sender()
	a = valid(str(sender.id))
	if a == "true":
		await create_restore_(event)
	else:
		await event.answer("Akses Ditolak",alert=True)

@bot.on(events.CallbackQuery(data=b'backer'))
async def backers(event):
	async def backers_(event):
		inline = [
[Button.inline(" BACKUP","backup"),
Button.inline(" RESTORE","restore")],
[Button.inline("‹ Main Menu ›","menu")]]
		z = requests.get(f"http://ip-api.com/json/?fields=country,region,city,timezone,isp").json()
		msg = f"""
✧◇───────────────────◇✧
  🧿 PREMIUM PANEL MENU 🧿
✧◇───────────────────◇✧
`☉ Hostname:` `{DOMAIN}`
`☉ ISP     :` `{z["isp"]}`
`☉ Country :` `{z["country"]}`
 ☉@D_swara**
✧◇───────────────────◇✧
"""
		await event.edit(msg,buttons=inline)
	sender = await event.get_sender()
	a = valid(str(sender.id))
	if a == "true":
		await backers_(event)
	else:
		await event.answer("Access Denied",alert=True)


@bot.on(events.CallbackQuery(data=b'setting'))
async def settings(event):
	async def settings_(event):
		inline = [
[Button.inline(" SPEEDTEST","speedtest"),
Button.inline(" BACKUP & RESTORE","backer")],
[Button.inline(" REBOOT SERVER","reboot"),
Button.inline(" RESTART SERVICE","resx")],
[Button.inline("‹ Main Menu ›","menu")]]
		z = requests.get(f"http://ip-api.com/json/?fields=country,region,city,timezone,isp").json()
		msg = f"""
✧◇───────────────────◇✧
  🧿 PREMIUM PANEL MENU 🧿
✧◇───────────────────◇✧
`☉ Hostname:` `{DOMAIN}`
`☉ ISP     :` `{z["isp"]}`
`☉ Country :` `{z["country"]}`
 ☉@D_swara**
✧◇───────────────────◇✧
"""
		await event.edit(msg,buttons=inline)
	sender = await event.get_sender()
	a = valid(str(sender.id))
	if a == "true":
		await settings_(event)
	else:
		await event.answer("Access Denied",alert=True)