from flask import Flask, render_template  # Импортируем Flask и функцию render_template

app = Flask(__name__)  # Создаём экземпляр приложения

# Определяем маршрут для главной страницы
@app.route('/')
def index():
    return render_template('index.html')  # Загружаем файл index.html из папки templates

# Определяем маршрут для страницы блога
@app.route('/blog')
def blog():
    return render_template('blog.html')  # Загружаем файл blog.html из папки templates

# Определяем маршрут для страницы контактов
@app.route('/contacts')
def contacts():
    return render_template('contacts.html')  # Загружаем файл contacts.html из папки templates

# Запускаем приложение
if __name__ == "__main__":
    app.run(debug=True)
