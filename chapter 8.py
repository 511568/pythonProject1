def favorite_book(title):
    """最新换的书"""
    print(f"One of my favorite books is {title.title()}")


favorite_book('Alice in wonderland')


# 练习8-3 T恤
def make_shirt(size, painting):
    """说明T恤的尺码和字样"""
    print(f"衣服尺寸为{size.title()},需要印的字样为'{painting}'")


make_shirt("l", "这是一件大号衣服")
make_shirt(size="l", painting="这是一件大号衣服")
make_shirt(painting="这是一件大号衣服", size="l")


#练习8-4
# 练习8-3 T恤
def make_shirt(size, painting="I Love Python"):
    """说明T恤的尺码和字样"""
    print(f"衣服尺寸为{size.title()},需要印的字样为'{painting}'")


make_shirt("l")
make_shirt(size="l", painting="这是一件大号衣服")
make_shirt(painting="这是一件大号衣服", size="l")


#练习4-5
def describe_city(city, country='PRC'):
    country = country.upper()
    """城市所属"""
    print(f"{city.title()} belongs to {country.title()}")


describe_city('Newyork',"USA")
describe_city('Beijing',"PRC")


#8-3 返回值
    #8.3.3 返回字典
def build_person(first_name,last_name):
    person = {'first':first_name,'last':last_name}
    return person

musician = build_person('jimi','hendrx')
print(musician)

#练习8-6
def city_country(city, country):
    """返回一个类似于'Santiago, Chile'的字符串。"""
    return f"{city.title()}, {country.title()}"

city = city_country('santiago', 'chile')
print(city)

#练习8-7
def make_album(singer,albumname):
    """创建歌手名和专辑名的字典"""
    album = {
        'singer':singer,
        'albumname':albumname,
    }
    print(album)
make_album('singer1','album1')
make_album('singer2','album2')
make_album('singer3','album3')


#！！！8-7 样本答案
def make_album(artist, title):
    """创建一个包含专辑信息的字典。"""
    album_dict = {
       'artist': artist.title(),        #1.设定字典键，并设定值为函数的值
       'title': title.title(),
       }
    return album_dict                   #3.通过返回字典键值，赋值给album，并打印album
    #return在这里充当了返回值的作用，当给出了函数实参后，album_dict里的键值被填充了，进一步album =使得填充的键值被赋值给了album


album = make_album('metallica', 'ride the lightning')       #2.函数实参填入后，实参被传递到字典内
print(album)
album = make_album('beethoven', 'ninth symphony')
print(album)
album = make_album('willie nelson', 'red-headed stranger')
print(album)

#8-7高级版
def make_album(artist, title):
    """创建一个包含专辑信息的字典。"""
    album_dict = {
       'artist': artist.title(),        #1.设定字典键，并设定值为函数的值
       'title': title.title(),
       }
    return album_dict                   #3.通过返回字典键值，赋值给album，并打印album
    #return在这里充当了返回值的作用，当给出了函数实参后，album_dict里的键值被填充了，进一步album =使得填充的键值被赋值给了album


album = make_album('metallica', 'ride the lightning')       #2.函数实参填入后，实参被传递到字典内
print(album)
album = make_album('beethoven', 'ninth symphony')
print(album)
album = make_album('willie nelson', 'red-headed stranger')
print(album)

#8-8
def make_album(artist, title):
    """创建一个包含专辑信息的字典。"""
    album_dict = {
       'artist': artist.title(),
       'title': title.title(),
       }
    return album_dict
active = True
while active:
    artist = input("\n请输入歌手名称(可随时输入q来退出)： ")
    if artist == 'q':
        active = False
    title = input("\n请输入专辑名称： ")
    if title == 'q':
        active = False
    else:
        print(make_album(artist,title))

#8-9
def show_message(messages):
    for message in messages:
        print(f"{message.title()}")


messages_list = ['message1','message2','message3']
show_message(messages_list)

#8-10
def show_message(messages):
    for message in messages:
        print(f"{message.title()}")

def send_messages(messages,sent_messages):
    while messages:
        current_message = messages.pop()
        print(f"已打印{current_message}")
        sent_messages.append(current_message)

messages_list = ['message1','message2','message3']
show_message(messages_list)

sent_messages = []
send_messages(messages,sent_messages)

print("\nFinal lists: ")
print(messages_list)
print(sent_messages)



