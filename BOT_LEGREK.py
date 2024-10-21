from rubpy import Client, handlers, Message
from asyncio import run 
import json , requests , os
from re import search
print("𝐓𝐬 • 𝐋𝐄𝐆𝐑𝐊𝐄࿐                                          𝗕𝗼𝘁 𝗹𝘀 𝗥𝗨𝗡")
async def main():
    async with Client(session='bot') as client:
        @client.on(handlers.MessageUpdates())
        async def updates(message: Message):
            object_guid = message.object_guid
            msg = message.message_id
            print(object_guid)
            admin = await client.get_group_admin_members(object_guid)
            admin = [i.member_guid for i in admin.in_chat_members]
##################################
            if message.raw_text is not None and message.raw_text.startswith("راهنما"):
                try:
                    eg = await message.reply(f"""• سازنده
• قوانین
• لیست آموزش
• لیست فیلتر""")
                    jd = eg['message_update']['message_id']
                    await client.messages(object_guid=object_guid,message_ids=jd)
                except Exception as e:
                    print(f"T.me/PASHA_FILTERING")
##################################
            elif message.raw_text is not None and message.raw_text.startswith("سازنده"):
                eggggg = await message.reply(f"T.me/PASHA_FILTERING")
                await client.messages(object_guid=object_guid,message_ids=jd)
##################################
            elif message.raw_text is not None and message.raw_text.startswith("قوانین"):
                eggggg = await message.reply(f"""• فحش و لینک ممنوع
• تبلیغات ممنوع
• توهین به کاربران و ادمین ها ممنوع
• بحث سیاسی ممنوع
• دستورات مستهجن به ربات ممنوع

● در صورت مشاهده و زیر پا گذاشتن قوانین فورا شما از گروه حذف میشوید!""")
                await client.messages(object_guid=object_guid,message_ids=jd)
##################################
            elif message.raw_text is not None and message.raw_text.startswith("لیست آموزش"):
                eggggg = await message.reply(f"""• آموزش ترموکس ~~هک~~
• آموزش ~~فیلتری~~ روبیکا
• آموزش ~~فیلتری~~ شاد
• آموزش ~~فیلتری~~ سروش""")
                await client.delete_messages(object_guid=object_guid,message_ids=jd)
##################################
            elif message.raw_text is not None and message.raw_text.startswith("لیست فیلتر"):
                eggggg = await message.reply(f"""• ک/و/ص
• ک/و/ن 
• ج/ن/د/ه 
• ک/س 
• ک/ی/ر 
• ک/و/ن/ی 
• پ/ر/ی/و/د
• ت/ع/ل/ی/ق
• ف/ی/ل/ت/ر
• ک/ی/ر 
• م/ا/د/ر ج/ن/د/ه 
• م/ا/د/ر/ت/و گ/ا/ی/د/م 
• ن/ن/ت
• س/ا/ک""")
                await client.delete_messages(object_guid=object_guid,message_ids=jd)
##################################
            elif message.raw_text is not None and message.raw_text.startswith("آموزش ترموکس هک"):
                eggggg = await message.reply(f"وجود ندارد")
                await client.messages(object_guid=object_guid,message_ids=jd)
##################################
            elif message.raw_text is not None and message.raw_text.startswith("آموزش فیلتری روبیکا"):
                eggggg = await message.reply(f"وجود ندارد")
                await client.messages(object_guid=object_guid,message_ids=jd)
##################################
            elif message.raw_text is not None and message.raw_text.startswith("آموزش فیلتری شاد"):
                eggggg = await message.reply(f"وجود ندارد")
                await client.messages(object_guid=object_guid,message_ids=jd)
##################################
            elif message.raw_text is not None and message.raw_text.startswith("آموزش فیلتری سروش"):
                eggggg = await message.reply(f"وجود ندارد")
                await client.messages(object_guid=object_guid,message_ids=jd)
##################################
                await message.reply(resultg)
            if message.raw_text is not None and not message.author_guid in admin and (search("کوص", message.raw_text) or search("کون", message.raw_text) or
search("جنده", message.raw_text) or
search("کس", message.raw_text) or
search("کیر", message.raw_text) or
search("کونی", message.raw_text) or
search("پریود", message.raw_text) or
search("تعلیق", message.raw_text) or
search("فیلتر", message.raw_text) or
search("کیر", message.raw_text) or
search("مادر جنده", message.raw_text) or
search("مادرتو گایدم", message.raw_text) or
search("ننت", message.raw_text) or
search("ساک", message.raw_text)):
                    reg = await message.delete_messages()
                    #reg = await client.send_message(object_guid,"")
                    await client.messages(object_guid,message_ids=dell)
            if not message.author_guid in admin and 'forwarded_from' in message.to_dict().get('message').keys():
##################################
                await message.reply(resultg)
            if message.raw_text is not None and not message.author_guid in admin and (search("https:", message.raw_text) or search("@", message.raw_text)):
                    reg = await message.delete_messages()
                    await client.messages(object_guid,message_ids=dell)
            if not message.author_guid in admin and 'forwarded_from' in message.to_dict().get('message').keys():
                await client.messages(object_guid,message_ids=dell)
##################################
#مهم
##################################
            elif message.raw_text is not None and message.raw_text.startswith("ربات"):
                eggggg = await message.reply(f"𝐏𝐬 • 𝐋𝐄𝐆𝐑𝐊𝐄࿐")
                await client.messages(object_guid=object_guid,message_ids=jd)
##################################
#سخن سخن سخن سخن سخن سخن سخن سخن 
##################################
            elif message.raw_text is not None and message.raw_text.startswith("هعی"):
                eggggg = await message.reply(f"کیر خر ماده")
                await client.messages(object_guid=object_guid,message_ids=jd)
##################################
            elif message.raw_text is not None and message.raw_text.startswith("افکار حرام"):
                eggggg = await message.reply(f"مایل به افکار حرام")
                await client.messages(object_guid=object_guid,message_ids=jd)
##################################
            elif message.raw_text is not None and message.raw_text.startswith("چخبر"):
                eggggg = await message.reply(f"بزن شبکه خبر")
                await client.messages(object_guid=object_guid,message_ids=jd)
##################################
            elif message.raw_text is not None and message.raw_text.startswith("بکیرم"):
                eggggg = await message.reply(f"اینم کیر داره:")
                await client.messages(object_guid=object_guid,message_ids=jd)
##################################
            elif message.raw_text is not None and message.raw_text.startswith("رو ربات کراشم"):
                eggggg = await message.reply(f"پا نمیدم")
                await client.messages(object_guid=object_guid,message_ids=jd)
##################################
            elif message.raw_text is not None and message.raw_text.startswith("سکوت"):
                eggggg = await message.reply(f"سکوت کردم که جواب کسکشان ابلهیست")
                await client.messages(object_guid=object_guid,message_ids=jd)
##################################
            elif message.raw_text is not None and message.raw_text.startswith("ببخشید"):
                eggggg = await message.reply(f"باشه")
                await client.messages(object_guid=object_guid,message_ids=jd)
##################################
            elif message.raw_text is not None and message.raw_text.startswith("تریاک فروش صدام کرد"):
                eggggg = await message.reply(f"یواشکی صدام کرد میدونست که محتاد هستم شیره چرا داد به دستم")
                await client.messages(object_guid=object_guid,message_ids=jd)
##################################
            elif message.raw_text is not None and message.raw_text.startswith("چرا نمیخوریش"):
                eggggg = await message.reply(f"چون کیرم کلفته")
                await client.messages(object_guid=object_guid,message_ids=jd)
##################################
            elif message.raw_text is not None and message.raw_text.startswith("گشنمه"):
                eggggg = await message.reply(f"بیا موزمو بخور")
                await client.messages(object_guid=object_guid,message_ids=jd)
##################################
            elif message.raw_text is not None and message.raw_text.startswith("میقولی"):
                eggggg = await message.reply(f"بده عمت بخوره")
                await client.messages(object_guid=object_guid,message_ids=jd)
##################################
            elif message.raw_text is not None and message.raw_text.startswith("باش"):
                eggggg = await message.reply(f"حل چشات")
                await client.messages(object_guid=object_guid,message_ids=jd)
##################################
            elif message.raw_text is not None and message.raw_text.startswith("سوری"):
                eggggg = await message.reply(f"کسیروسعلی چیه مُرادوک من لَگِرَکعلیم")
                await client.messages(object_guid=object_guid,message_ids=jd)
##################################
            elif message.raw_text is not None and message.raw_text.startswith("دمت گرم"):
                eggggg = await message.reply(f"چاکرتیم")
                await client.messages(object_guid=object_guid,message_ids=jd)
##################################
            elif message.raw_text is not None and message.raw_text.startswith("وات"):
                eggggg = await message.reply(f"اینجا خارجکی مارجکی نتایپ تل نیست نوبیکاست")
                await client.messages(object_guid=object_guid,message_ids=jd)
##################################
            elif message.raw_text is not None and message.raw_text.startswith("کصلیس"):
                eggggg = await message.reply(f"ولی من سیگمام")
                await client.messages(object_guid=object_guid,message_ids=jd)
##################################
            elif message.raw_text is not None and message.raw_text.startswith("چی بلدی"):
                eggggg = await message.reply(f"~~کیر~~کردن")
                await client.messages(object_guid=object_guid,message_ids=jd)
##################################
            elif message.raw_text is not None and message.raw_text.startswith("نکص"):
                eggggg = await message.reply(f"نکیر")
                await client.messages(object_guid=object_guid,message_ids=jd)
##################################
            elif message.raw_text is not None and message.raw_text.startswith("هوش"):
                eggggg = await message.reply(f"حوش و ظکاوطح")
                await client.messages(object_guid=object_guid,message_ids=jd)
##################################
            elif message.raw_text is not None and message.raw_text.startswith("عجب"):
                eggggg = await message.reply(f"عجب عربیه بگو ~~کیر خر ماده~~")
                await client.messages(object_guid=object_guid,message_ids=jd)
##################################
            elif message.raw_text is not None and message.raw_text.startswith("من بای"):
                eggggg = await message.reply(f"بابا میموندی میخندوندی یکم")
                await client.messages(object_guid=object_guid,message_ids=jd)
##################################
            elif message.raw_text is not None and message.raw_text.startswith("شتر دیدی"):
                eggggg = await message.reply(f"بین خودمون باشه")
                await client.messages(object_guid=object_guid,message_ids=jd)
##################################
            elif message.raw_text is not None and message.raw_text.startswith("توکی"):
                eggggg = await message.reply(f"من رباتم")
                await client.messages(object_guid=object_guid,message_ids=jd)
##################################
            elif message.raw_text is not None and message.raw_text.startswith("سلام"):
                eggggg = await message.reply(f"سلام عربیه بگو درود")
                await client.messages(object_guid=object_guid,message_ids=jd)
##################################
            elif message.raw_text is not None and message.raw_text.startswith("درود"):
                eggggg = await message.reply(f"بدرود")
                await client.messages(object_guid=object_guid,message_ids=jd)
##################################
            elif message.raw_text is not None and message.raw_text.startswith("وای"):
                eggggg = await message.reply(f"وای؟")
                await client.messages(object_guid=object_guid,message_ids=jd)
##################################
            elif message.raw_text is not None and message.raw_text.startswith("سوپر بده"):
                eggggg = await message.reply(f"د")
                await client.messages(object_guid=object_guid,message_ids=jd)
##################################
            elif message.raw_text is not None and message.raw_text.startswith("میکنمت"):
                eggggg = await message.reply(f"نهایت میتونی ~~کیرمو~~ بمالی")
                await client.messages(object_guid=object_guid,message_ids=jd)
##################################
            elif message.raw_text is not None and message.raw_text.startswith("خمینی"):
                eggggg = await message.reply(f""" ⣿⣿⣿⣿⣿⡿⠋⠁⠄⠄⠄⠈⠘⠩⢿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⠃⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠻⣿⣿⣿⣿
⣿⣿⣿⣿⠄⠄⣀⣤⣤⣤⣄⡀⠄⠄⠄⠄⠙⣿⣿⣿
⣿⣿⣿⣿⡀⢰⣿⣿⣿⣿⣿⢿⠄⠄⠄⠄⠄⠹⢿⣿
⣿⣿⣿⣿⣿⡞⠻⠿⠟⠋⠉⠁⣤⡀⠄⠄⠄⠄⠄⠄
⣿⣿⣿⣿⣿⣿⣶⢼⣷⡤⣦⣿⠛⡰⢃⠄⠐⠄⠄⢸
⣿⣿⣿⣿⣿⣿⣿⡯⢍⠿⢾⡿⣸⣿⠰⠄⢀⠄⠄⡬
⣿⣿⣿⣿⣿⣿⣿⣴⣴⣅⣾⣿⣿⡧⠦⡶⠃⠄⠠⢴
⣿⣿⣿⣿⠿⠍⣿⣿⣿⣿⣿⣿⣿⢇⠟⠁⠄⠄⠄⠄
⠟⠛⠉⠄⠄⠄⡽⣿⣿⣿⣿⣿⣯⠏⠄⠄⠄⠄⠄⠄
⠄⠄⠄⢀⣾⣾⣿⣤⣯⣿⣿⡿⠃⠄⠄⠄⠄⠄⠄⠄""")
                await client.messages(object_guid=object_guid,message_ids=jd)
##################################
            elif message.raw_text is not None and message.raw_text.startswith("ریات"):
                eggggg = await message.reply(f"کصدصت بگو ربات")
                await client.messages(object_guid=object_guid,message_ids=jd)
##################################
            elif message.raw_text is not None and message.raw_text.startswith("سلام دختری"):
                eggggg = await message.reply(f"Are you a Amir?")
                await client.messages(object_guid=object_guid,message_ids=jd)
##################################
            elif message.raw_text is not None and message.raw_text.startswith("نمیدونم"):
                eggggg = await message.reply(f"به ~~تخمم~~")
                await client.messages(object_guid=object_guid,message_ids=jd)
##################################
            elif message.raw_text is not None and message.raw_text.startswith("گونخور"):
                eggggg = await message.reply(f"تو بخوری جایزت یه کد فیلقوریه")
                await client.messages(object_guid=object_guid,message_ids=jd)
##################################
            elif message.raw_text is not None and message.raw_text.startswith("گوخوردم"):
                eggggg = await message.reply(f"نوش")
                await client.messages(object_guid=object_guid,message_ids=jd)
##################################
            elif message.raw_text is not None and message.raw_text.startswith("شب بخیر"):
                eggggg = await message.reply(f"نرو مریم میدونی عاشق چشماتم")
                await client.messages(object_guid=object_guid,message_ids=jd)
##################################
            elif message.raw_text is not None and message.raw_text.startswith("کصشعر"):
                eggggg = await message.reply(f"به نظر من که محتوایه خوبی بود")
                await client.messages(object_guid=object_guid,message_ids=jd)
##################################
            elif message.raw_text is not None and message.raw_text.startswith("سیگما"):
                eggggg = await message.reply(f"سیغمام")
                await client.messages(object_guid=object_guid,message_ids=jd)
##################################
            elif message.raw_text is not None and message.raw_text.startswith("عمتو"):
                eggggg = await message.reply(f"خالتو")
                await client.messages(object_guid=object_guid,message_ids=jd)
##################################
            elif message.raw_text is not None and message.raw_text.startswith("میرم"):
                eggggg = await message.reply(f"بکیرم")
                await client.messages(object_guid=object_guid,message_ids=jd)
##################################
            elif message.raw_text is not None and message.raw_text.startswith("چی داش"):
                eggggg = await message.reply(f"اره داش")
                await client.messages(object_guid=object_guid,message_ids=jd)
##################################
            elif message.raw_text is not None and message.raw_text.startswith("ارضا چیست"):
                eggggg = await message.reply(f"دو نفر از کوچه رد میشن میگن عه اقا رضا")
                await client.messages(object_guid=object_guid,message_ids=jd)
##################################
            elif message.raw_text is not None and message.raw_text.startswith("جقی"):
                eggggg = await message.reply(f"برو ایه تلاوت نکن گلپسر")
                await client.messages(object_guid=object_guid,message_ids=jd)
##################################
            elif message.raw_text is not None and message.raw_text.startswith("کسی است"):
                eggggg = await message.reply(f"فقط من پلاسم")
                await client.messages(object_guid=object_guid,message_ids=jd)
##################################
            elif message.raw_text is not None and message.raw_text.startswith("ممه میخام"):
                eggggg = await message.reply(f"بیا پیوی با تمام وجود بزرگترین ~~کیر~~ رو جایزه بدمت")
                await client.messages(object_guid=object_guid,message_ids=jd)
##################################
            elif message.raw_text is not None and message.raw_text.startswith("این چیه"):
                eggggg = await message.reply(f"~~کیر~~ ادم نما")
                await client.messages(object_guid=object_guid,message_ids=jd)
##################################
            elif message.raw_text is not None and message.raw_text.startswith("بنظرم"):
                eggggg = await message.reply(f"نظرت خوـ[~~کیریه~~]ـبه")
                await client.messages(object_guid=object_guid,message_ids=jd)
##################################
            elif message.raw_text is not None and message.raw_text.startswith("کسکش"):
                eggggg = await message.reply(f"سرشو بگیر دستی بکش")
                await client.messages(object_guid=object_guid,message_ids=jd)
##################################
            elif message.raw_text is not None and message.raw_text.startswith("گی"):
                eggggg = await message.reply(f"نه داش اینجا گی ندارم")
                await client.messages(object_guid=object_guid,message_ids=jd)
##################################
            elif message.raw_text is not None and message.raw_text.startswith("بخورش"):
                eggggg = await message.reply(f"بمالش")
                await client.messages(object_guid=object_guid,message_ids=jd)
##################################
            elif message.raw_text is not None and message.raw_text.startswith("چجوری"):
                eggggg = await message.reply(f"ماس مالونشی؟")
                await client.messages(object_guid=object_guid,message_ids=jd)
##################################
            elif message.raw_text is not None and message.raw_text.startswith("سازنده"):
                eggggg = await message.reply(f"T.me/PASHA_FILTERING")
                await client.messages(object_guid=object_guid,message_ids=jd)
##################################
            elif message.raw_text is not None and message.raw_text.startswith("رل بزنیم"):
                eggggg = await message.reply(f"اگه ممه 85 داری اره")
                await client.messages(object_guid=object_guid,message_ids=jd)
##################################
            elif message.raw_text is not None and message.raw_text.startswith("بخورم"):
                eggggg = await message.reply(f"برا منو؟")
                await client.messages(object_guid=object_guid,message_ids=jd)
##################################
            elif message.raw_text is not None and message.raw_text.startswith("د"):
                eggggg = await message.reply(f"اخه/:")
                await client.messages(object_guid=object_guid,message_ids=jd)
##################################
            elif message.raw_text is not None and message.raw_text.startswith("س"):
                eggggg = await message.reply(f"""یاد بگیر بگو بلد نیستی سلام کنی؟🥺
مثل آدم بنویس سلام😐 س چیه؟""")
                await client.messages(object_guid=object_guid,message_ids=jd)
##################################
        await client.run_until_disconnected()
run(main())