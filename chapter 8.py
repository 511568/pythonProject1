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
    album = {'singer':singer,
                 'albumname':albumname,
             }
    print(album)
make_album('singer1','album1')
make_album('singer2','album2')
make_album('singer3','album3')
