#!/usr/bin/env python3
import main_test
import web
import os 


urls = (
    '/', 'Home'
)

app = web.application(urls, globals())
render = web.template.render('')


class Home:
    def GET(self):
        return render.html_diabetes()

    def POST(self):
        data = web.input()
        seq_data = (data.preg, data.plas, data.pres, data.skin, data.test, data.mass, data.pedi, data.age)
        result = main_test.main_test().result(seq_data)
        if result:
            return "you have diabetes"
        else:
            return "no you do not have diabetes"


if __name__ == "__main__":
	app.run()















