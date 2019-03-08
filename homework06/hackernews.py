from bottle import (
    route, run, template, request, redirect, static_file
)

from scraputils import get_news
from db import News, session
from bayes import NaiveBayesClassifier
import string



s = session()
classifier = NaiveBayesClassifier()
mark_news = s.query(News).filter(News.label != None).all()
x_title = [row.title for row in mark_news]
y_lable = [row.label for row in mark_news]
classifier.fit(x_title, y_lable)


@route("/news")
def news_list():
    s = session()
    rows = s.query(News).filter(News.label == None).all()
    return template('news_template', rows=rows)


@route("/add_label/")
def add_label():
    news_id = request.query.id
    label = request.query.label
    c = session()
    qurent = c.query(News).filter(News.id == news_id).one()
    qurent.label = label
    c.commit()
    redirect("/news")


@route("/update")
def update_news():
    s = session()
    latest_news = get_news("https://news.ycombinator.com/newest", n_pages=5)
    authors = [news['author'] for news in latest_news]
    titles = s.query(News.title).filter(News.author.in_(authors)).subquery()
    existing_news = s.query(News).filter(News.title.in_(titles)).all()
    for item in latest_news:
        if not existing_news or item not in existing_news:
            s.add(News(**item))
    s.commit()
    redirect("/news")


@route("/classify")
def classify_news():
    s = session()
    labeled_news = s.query(News).filter(News.label != None).all()
    x_train = [clean(news.title) for news in labeled_news]
    y_train = [news.label for news in labeled_news]
    classifier.fit(x_train, y_train)

    rows = s.query(News).filter(News.label == None).all()
    good, maybe, never = [], [], []
    for row in rows:
        prediction = classifier.predict([clean(row.title)])
        if prediction == 'good':
            good.append(row)
        elif prediction == 'maybe':
            maybe.append(row)
        else:
            never.append(row)

    return template('news_recommendations', good=good, maybe=maybe, never=never)


def clean(s):
    translator = str.maketrans("", "", string.punctuation)
    return s.translate(translator).lower()


if __name__ == "__main__":
    run(host="localhost", port=8080)
