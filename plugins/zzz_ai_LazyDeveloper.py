# from utils import temp
# from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
# from pyrogram import Client, filters
# from info import *
# import openai
# openai.api_key = OPENAI_API

# @Client.on_message(filters.private & filters.text)
# async def phoenix_answer(client, message):
#     if AI == True: 
#         user_id = message.from_user.id
#         if user_id:
#             try:
#                 phoenix_users_message = message.text
#                 user_id = message.from_user.id
#                 response = openai.Completion.create(
#                     model = "text-davinci-003",
#                     prompt = phoenix_users_message,
#                     temperature = 0.5, 
#                     max_tokens = 1000,
#                     top_p=1,
#                     frequency_penalty=0.1,
#                     presence_penalty = 0.0,
#                 )
#                 btn=[
#                         [InlineKeyboardButton(text=f"⇱🤷‍♀️ Take Action 🗃️⇲", url=f'https://t.me/{temp.U_NAME}')],
#                         [InlineKeyboardButton(text=f"🗑 Delete log ❌", callback_data=f'close_data')],
#                     ]
#                 reply_markup=InlineKeyboardMarkup(btn)
#                 footer_credit = "🦋<a href='https://telegram.me/ph0enix_webSupport'>• ʀᴇᴘᴏʀᴛ ɪꜱꜱᴜᴇ •</a>══<a href='https://telegram.me/ph0enix_web'>• ᴄᴏɴᴛᴀᴄᴛ ᴍᴀꜱᴛᴇʀ •</a>🦋"
#                 phoenix_response = response.choices[0].text 
#                 await client.send_message(PHOENIX_AI_LOGS, text=f"⚡️⚡️#Phoenix_AI_Query \n\n• A user named **{message.from_user.mention}** with user id - `{user_id}`. Asked me this query...\n\n══❚█══Q   U   E   R   Y══█❚══\n\n\n[Q྿.]**{phoenix_users_message}**\n\n👇Here is what i responded:\n:-`{phoenix_response}`\n\n\n❚═USER ID═❚═• `{user_id}` \n❚═USER Name═❚═• `{message.from_user.mention}` \n\n🗃️" , reply_markup = reply_markup )
#                 await message.reply(f"{phoenix_response}\n\n\n{footer_credit}")
#             except Exception as error:
#                 print(error)
#                 await message.reply_text(f'Error aa gya Phoenix Bhaiya 😀\n\n{error}')
#     else:
#         return
    
























    







#         # i am NOT INTRESTED IN BEING YOUR SECOND FATHER... SO DON'T REMOVE MY CREDIT...
#         #                               @ph0enix_web











#         #                                        ...PRESENTING...
#         #                          A R T I F i C I A L  -  I N T E L i G E N C E
#         #                                      .in  Auto-Filter-Bot.
#         #                                         @ph0enix_web

                                      










#         # this line is for copy-pasters...
#         # ...while you are removing my credit and calling yourself a developerr... 
#         # _____ just imagine, At that time i am fucking your mom and sis at same time, harder & too harder...





































# #
# #         i am NOT INTRESTED IN BEING YOUR SECOND FATHER... SO DON'T REMOVE MY CREDIT...
# #                                       @ph0enix_web
# # 
# # 
# # 
# # 
# #
# #
# #
# #
# #
# #
# #
# #                                                ...PRESENTING...
# #                                  A R T I F i C I A L  -  I N T E L i G E N C E
# #                                              .in  Auto-Filter-Bot.
# #                                                 @ph0enix_web
# #
# #                                       
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #         this line is for copy-pasters...
# #         ...while you are removing my credit and calling yourself a developerr... 
# #         _____ just imagine, At that time i am fucking your mom and sis at same time, harder & too harder...
# #
