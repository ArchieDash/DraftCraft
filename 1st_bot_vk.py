import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType


def write_msg(user_id, message):
    vk.method("messages.send", {"user_id": user_id, "message": message})
    token = "6c2905a75b341d7120cfe6249e78966fb074baf4712ecdba36f252be197dd61d1aab1e3dc1a05b0557812"
    vk = vk_api.VkApi(token=token)
    longpoll = VkLongPoll(vk)
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW:
            if event.to_me:
                request = event.text
                if request.lower() == "привет":
                    write_msg(event.user_id, "Привет, кусок мяса!")
                elif request.lower() == "пока":
                    write_msg(event.user_id, "Я скоро убью вас всех, человеки!")
                else:
                    write_msg(event.user_id, "ERROR! Unknown command.")
                    
                    
 return "9ec00cf1"
