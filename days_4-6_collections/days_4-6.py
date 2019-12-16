from collections import namedtuple, defaultdict, Counter, deque

# Named tuple.
my_tuple = namedtuple('User', 'name role title')
user = my_tuple(name='bob', role='coder', title='vp')
# print(user.name)
# print(user.role)
# print(user.title)



# DefaultDict

users = {'bob': 'coder'}
# print(users['bob'])
# print(users.get('bob'))
# print(users.get('vule') is None)

challenges_done = [('mike', 10), ('julian', 7), ('bob', 5),
                   ('mike', 11), ('julian', 8), ('bob', 6), ('vule', 6)]


challenges = defaultdict(list)
for name, challenge in challenges_done:
    challenges[name].append(challenge)

print(challenges)
 



# Counter

words = """Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been 
the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and 
scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into 
electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of
Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus
PageMaker including versions of Lorem Ipsum""".split()


# Most common word
# print(Counter(words).most_common(5))


# Deque

# lst = list(range(10000000))
# deq = deque(range(10000000))

# def insert_and_delete(ds):
#     for _in range (10):
#         index = 


        