character={
    'name':'기사',
    'level':12,
    'items':{
        'sword':'불꽃의 검',
        'armor':'풀플레이트'
    },
    'skill':['베기','세게 베기','아주 세개 베기']
}

for key, value in character.items():
    print(type(value))

# for key, value in character.items():
#     if type(value) is str:
#         print(f"{key} : {character[key]}")
#     elif type(value) is int:
#         print(f"{key} : {character[key]}")
#     elif type(value) is dict:
#         for k,v in value.items():
#             print(f"{k} : {v}")
#     elif type(value) is list:
#         for i in value:
#             print(f"{key} : {i}")
