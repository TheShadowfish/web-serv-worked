from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs

# Для начала определим настройки запуска
hostName = "localhost"
serverPort = 8080


class MyServer(BaseHTTPRequestHandler):
    """ 
        Специальный класс, который отвечает за 
        обработку входящих запросов от клиентов
    """

    def get_html_content(self):
        return """
        <!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Bootstrap demo</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet"
          integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
</head>
<body>

<div class="container">
    <div class="row mt-5">
        <div class="col-6">
            <div class="card bg-primary">
                <div class="card-body text-white">
                    <h3 class="card-title">Контактная информация</h3>
                    <div class="row">
                        <div class="col-6">Москва</div>
                        <div class="col-6">+7 777 777 77 77</div>
                        <div class="col-6">Санкт-петербург</div>
                        <div class="col-6">+7 888 888 88 88</div>

                    </div>
                </div>
            </div>

        </div>
        <div class="col-6">
            <div class="card">
                <div class="card-body">
                    <h3 class="card-title">Оставьте заявку</h3>
                    <form>
                        <div class="mb-3">
                            <input name="name" type="text" class="form-control" id="exampleFormControlInput1"
                               placeholder="Имя">
                        </div>
                        <div class="mb-3">
                            <input name="email" type="email" class="form-control" id="exampleFormControlInput2"
                               placeholder="Email">
                        </div>
                        <div class="mb-3">
                            <textarea name="message" class="form-control" placeholder="Сообщение" id="exampleFormControlTextarea1" rows="3"></textarea>
                        </div>
                        <button type="submit" class="btn btn-primary form-control">Отправить</button>
                    </form>
                    
                    


                </div>
            </div>

        </div>
    </div>
</div>
</body>
</html>
        """

    def do_GET(self):
        query_components = parse_qs(urlparse(self.path).query)
        # print("print: ")
        print(query_components)

        page_content = self.get_html_content()
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes(page_content, "utf-8"))


if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        # Cтарт веб-сервера в бесконечном цикле прослушивания входящих запросов
        webServer.serve_forever()
    except KeyboardInterrupt:
        # Корректный способ остановить сервер в консоли через сочетание клавиш Ctrl + C
        pass

    # Корректная остановка веб-сервера, чтобы он освободил адрес и порт в сети, которые занимал
    webServer.server_close()
    print("Server stopped.")
