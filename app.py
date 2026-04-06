# Here
from flask import Flask, render_template, request, redirect, url_for, flash
app = Flask(__name__)
app.secret_key = 'secret123'

products = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form.get('name')
        price = request.form.get('price')
        category = request.form.get('category')

        for item in products:
            if item['name'] == name:
                flash('Такий товар вже є!')
                break
        else:
            products.append({
                'name': name,
                'price': price,
                'category': category
            })

        return redirect(url_for('index'))

    return render_template('index.html', products=products)


@app.route('/delete/<int:index>')
def delete(index):
    item_name = products[index]['name']
    products.pop(index)
    flash(f'Товар {item_name} видалено!')
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)