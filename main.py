from flask import Flask, flash, render_template, request, redirect, url_for

app = Flask(__name__)
app.config['SECRET_KEY'] = b'hgkjfytdfguilikoiu'

cars = [
  {'id':1, 'brand': 'Toyota', 'model':'Yaris Ativ', 'year': 2024, 'price': 570000},
  {'id':2, 'brand':'Honda', 'model':'City Hatchback', 'year': 2024, 'price': 650000},
  {'id':3, 'brand': 'Nissan', 'model':'Amera', 'year': 2025, 'price': 550000}
]

@app.route('/')
def index():
  return render_template('index.html', title='Home Page')

@app.route('/cars', methods=['GET', 'POST'])
def all_cars():
  if request.method == 'POST':
    brand = request.form['brand']
    tmp_cars = []
    for car in cars:
      if brand.lower() in car['brand'].lower():
        tmp_cars.append(car)
    # cars = tmp_cars
    return render_template('cars/cars.html', 
                         title='Search Cars Page',
                         cars=tmp_cars)
  
  return render_template('cars/cars.html', 
                         title='Show All Cars Page',
                         cars=cars)

@app.route('/cars/new')
def new_car():
  # if request.method == 'POST':
  #   brand = request.form['brand']
  #   model = request.form['model']
  #   year = int(request.form['year'])
  #   price = int(request.form['price'])

  #   length = len(cars)
  #   id = cars[length-1]['id'] + 1

  #   car = {'id':id, 'brand': brand, 'model':model, 'year': year, 'price': price}

  #   cars.append(car)
  #   flash('Add new Car Successfull.', 'success')
  #   return redirect(url_for('all_cars'))

  return render_template('cars/new_car.html',
                          title='New Car Page')

@app.route('/cars/<int:id>/delete')
def delete_car(id):
  for car in cars:
    if id == car['id']:
      cars.remove(car)
      break
  flash('Delete car successfull', 'success')
  return redirect(url_for('all_cars'))

@app.route('/cars/<int:id>/edit', methods=['GET', 'POST'])
def edit_car(id):
  for c in cars:
    if id == c['id']:
      car = c
      break
  if request.method == 'POST':
    brand = request.form['brand']
    model = request.form['model']
    year = int(request.form['year'])
    price = int(request.form['price'])

    for c in cars:
      if id == c['id']:
        c['brand'] = brand
        c['model'] = model
        c['year'] = year
        c['price'] = price
        break
    
    flash('Update Car Successfull.', 'success')
    return redirect(url_for('all_cars'))
  
  return render_template('cars/edit_car.html',
                         title='Edit Car Page',
                         car=car)

@app.route('/cars/search')
def search_car():
  brand = request.args.get('brand')
  print(brand)
  tmp_cars = []
  for car in cars:
    if brand.lower() in car['brand'].lower():
      tmp_cars.append(car)
  # cars = tmp_cars
  return render_template('cars/search_car.html', 
                        title='Search Cars Page',
                        cars=tmp_cars)
