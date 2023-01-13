import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from flask import Flask, render_template
from flask import request
import yfinance
def plot(key,pur,sale1,sale2,time):
    key.upper()
    st_key = yfinance.Ticker(key)
    hist = st_key.history(period=time)
    items= len(hist.index)
    purchase = [int(pur)]*items
    sale_val1= [int(sale1)]*items
    sale_val2 = [int(sale2)]*items
    plt.plot(hist.index, hist['Close'],label= "Orignal price")
    plt.plot(hist.index, purchase, label = "purchase price")
    plt.plot(hist.index, sale_val1, label = "Sale Price 1")
    plt.plot(hist.index, sale_val2, label = "Sale Price 2")
    plt.title(key+' '+time)
    name = 'static/'+time+'myplot.png'
    plt.savefig(name)
    return name

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/get_plot', methods=["GET","POST"])
def get_plot():
    if request.method == "POST":
        key=request.form['Stock_Key']
        pur = request.form['Purchase_price']
        sale1=request.form["Sale_price_1"]
        sale2=request.form["Sale_price_2"]
        p1 = plot(key,pur,sale1,sale2,"1d")
        p2 = plot(key,pur,sale1,sale2,"1w")
        p3 = plot(key,pur,sale1,sale2,"1mo")
        p4 = plot(key,pur,sale1,sale2,"1y")
        p5 = plot(key,pur,sale1,sale2,"max")
        '''key.upper()
        st_key = yfinance.Ticker(key)
        hist = st_key.history(period="1y")
        items= len(hist.index)
        purchase = [int(pur)]*items
        sale_val1= [int(sale1)]*items
        sale_val2 = [int(sale2)]*items
        plt.plot(hist.index, hist['Close'], label= "Original Price")
        plt.plot(hist.index, purchase, label= "Purchase Price")
        # plotting the line 2 points 
        plt.plot(hist.index, sale_val1,  label= "Sale Price 1")
        plt.plot(hist.index, sale_val2, label= "Sale Price 2")
        # giving a title to my graph
        plt.title("1y")
        # show a legend on the plot
        #plt.legend("Actual Price","Purchase Price", "Sale Price 1", "Sale Price 2")
        plt.savefig('static/myplot.png')'''
        return render_template('index.html',plot_url1=str(p1),plot_url2=str(p2),plot_url3=str(p3),plot_url4=str(p4),plot_url5=str(p5))
    else:
        return render_template('index.html')
app.secret_key = 'qwerty'

if __name__ == "__main__":
    app.run('127.0.0.1', 5000,debug=True)