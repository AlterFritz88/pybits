import requests
from bs4 import BeautifulSoup

cached_so_url = 'https://bit.ly/2IMrXdp'




def top_python_questions(url=cached_so_url):
    """Use requests to retrieve the url / html,
       parse the questions out of the html with BeautifulSoup,
       filter them by >= 1m views ("..m views").
       Return a list of (question, num_votes) tuples ordered
       by num_votes descending (see tests for expected output).
    """
    page = requests.get(cached_so_url).text
    soup = BeautifulSoup(page)
    questions = soup.findAll(class_="question-hyperlink")
    questions = [x for x in questions if len(x['class']) == 1]

    votes = soup.findAll(class_ ="vote-count-post")

    viers = soup.findAll(class_= "views")


    ans_tupples = []
    for question, vote, vier in zip(questions, votes, viers):
        if vier.text.split()[0][-1] == 'm':
            ans_tupples.append((question.text, int(vote.text)))

    return  sorted(ans_tupples, key=lambda x: x[1], reverse=True)


print(top_python_questions())

