import web

urls = (
  '/', 'index',
  '/index', 'index',
  '/foo', 'foo')

app = web.application(urls, globals())

render = web.template.render('templates/')

class index:
    def GET(self):
        greeting = "YOUR OK I GUESS"
        return render.index(greeting = greeting)

class foo:
    def GET(self):
        recrimination = "I have NEVER been fond of you. :("
        return render.foo(recrimination = recrimination)

if __name__ == "__main__":
    app.run()
