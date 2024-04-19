import asyncio
from telegram import Bot
import time


bot_token = '7162513284:AAGUXwYIhA19hFyj8dGV26Qh-TnSJci6soI'

stock_lis_group_chat_id = '-1002131270840'
async def send_message_async(bot_token, group_chat_id, message):
    bot = Bot(token=bot_token)
    await bot.send_message(chat_id=group_chat_id, text=message,  parse_mode='html')


def main():
    while True:
        try:
            time.sleep(5)
            feed_url = 'https://www.upwork.com/ab/feed/jobs/rss?paging=0%3B50&verified_payment_only=1&q=python&sort=recency&api_params=1&securityToken=582f47ccdc3acc988372875406075b11e319f5825429ec5c2d463651dfa93f995186966226271363128756782e880e327c32161d405fd15360f7a57716b9a3fa&userUid=1752363490136178688&orgUid=1752363490136178689'
            feed = feedparser.parse(feed_url)
            if feed.bozo == 0: 
                for entry in feed.entries:
                    print("####################### ", "---- TR -----", " ######################")
                    if (entry.title).lower() not in job_list:
                        print(entry.title)
                        job_list.append((entry.title).lower())
                        summary = entry.summary
                        summary = (summary.replace('<br />', '\n'))
                        message = str(entry.published) + "\n\n" + str(entry.title)  +"\n\n" + summary
                        if len(message) > 3500:
                            message = entry.title
                        for i in trading_keyword_list:
                            if i in (entry.title).lower() or i in (entry.summary).lower():
                                print("------------------Triggered Trading-------------------")
                                asyncio.run(send_message_async(bot_token, trading_group_chat_id, message))
                                break           
                    break
                time.sleep(5)
        except Exception as e:
            print(e)
            error_handler_group_chat_id = '-1002016645426'
            asyncio.run(send_message_async(bot_token, error_handler_group_chat_id, "Trading  - " + str(e)))
            break
            
if __name__ == "__main__":
    main()
    