import re


def extract_course_times():
    '''Use re.findall to capture all mm:ss timestamps in a list'''
    flask_course = ('Introduction 1 Lecture 01:47'
                    'The Basics 4 Lectures 32:03'
                    'Getting Technical!  4 Lectures 41:51'
                    'Challenge 2 Lectures 27:48'
                    'Afterword 1 Lecture 05:02')
    return re.findall(r"\d+:\d+", flask_course)


def split_on_multiple_chars():
    '''Use re.split to split log line by ; , .
       but not on the last ... so list should have len of 4
       (hint check re.split docs for extra switches)'''
    logline = ('2017-11-03T01:00:02;challenge time,regex!.'
               'hope you join ... soon')
    return re.split(r";|,|[.]{1}\b", logline)


def get_all_hashtags_and_links():
    '''Use re.findall to extract the URL and 2 hashtags of this tweet'''
    tweet = ('New PyBites article: Module of the Week - Requests-cache '
             'for Repeated API Calls - http://pybit.es/requests-cache.html '
             '#python #APIs')
    return re.findall(r"http:.+|^#", tweet)[0].split()


def match_first_paragraph():
    '''Use re.sub to extract the content of the first paragraph (excl tags)'''
    html = ('<p>pybites != greedy</p>'
            '<p>not the same can be said REgarding ...</p>')
    return re.sub(r"<p>|</p>", r"", html)[:17]


def find_double_words():
    '''Use re.search(regex, text).group() to find the double words'''
    text = 'Spain is so nice in the the spring'
    return re.search(r"(\w+)\s\1\b", text).group()


def match_ip_v4_address(ip):
    '''Use re.match to match an ip v4 address (no need for exact IP ranges)'''
    return re.match(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", ip)


if __name__ == "__main__":
    # print(extract_course_times())
    # print(split_on_multiple_chars())
    # print(get_all_hashtags_and_links())
    # print(match_first_paragraph())
    # print(find_double_words())
    # print(match_ip_v4_address('255.255.255.255'))

