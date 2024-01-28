import sqlite3
import time

from urllib.parse import urlparse
from flask import Flask, jsonify, request

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True


@app.errorhandler(Exception)
def http_error_handler(error):
    return jsonify(status=str(error))


@app.route("/visited_links", methods=['POST', 'GET'])
def visited_links():
    connection = sqlite3.connect('visitedLinks.db')
    cursor = connection.cursor()

    if request.method == 'GET':
        domains = []

        timeFrom = request.args['from']
        timeTo = request.args['to']

        cursor.execute('SELECT * FROM Links ')
        linksRaw = cursor.fetchall()
        connection.commit()
        connection.close()

        for link in linksRaw:
            for ll in str(link[1]).split(','):
                if (ll >= timeFrom) and (ll <= timeTo):
                    domains.append(link[0])
                    break

        return jsonify(domains=domains, status='ok'), 200, {'Content-Type': 'application/json; charset=UTF-8'}

    if request.method == 'POST':
        content = request.get_json()
        links = content['links']

        for link in links:
            cursor.execute('SELECT * FROM Links ')
            connection.commit()
            raw_time = cursor.fetchall()
            index = ''
            for a in range(0 if len(raw_time) == 0 else len(raw_time[0]) - 1):
                old_time = raw_time[0][a + 1]

                if raw_time[0][a] == link:
                    index = old_time

            is_this_unique = True
            for ind in index.split(','):
                if ind == str(int(time.time())):
                    is_this_unique = False

            time_to_write = ((str(int(time.time())) + ',') if is_this_unique else '') + index
            cursor.execute('INSERT OR REPLACE INTO Links (link, time) VALUES (?, ?)',
                           (urlparse(link).netloc, time_to_write))
            connection.commit()
        connection.close()

    return jsonify(status='ok')


def main():
    connection = sqlite3.connect('visitedLinks.db')
    cursor = connection.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Links (
        link TEXT PRIMARY KEY,
        time TEXT
        )
        ''')

    connection.commit()
    connection.close()

    app.run(debug=True)


if __name__ == "__main__":
    main()
