import sqlite3
import matplotlib.pyplot as plt

def get_data(start_date, end_date):
    con = sqlite3.connect('data.db')
    cur = con.cursor()
    cur.execute("SELECT * FROM data WHERE date BETWEEN ? AND ? ORDER BY date ", (start_date, end_date))
    res = cur.fetchall()
    con.close()
    dates = [res[i][0] for i in range(len(res))]
    prices = [res[i][1] for i in range(len(res))]
    return dates, prices

def gen_graph(dates, prices, path="images/22"):
    plt.figure(figsize=(8, 6))
    plt.plot(dates[::100], prices[::100], marker='o', color='r', linestyle='--')
    # доделать
    plt.title('Курс долора')
    plt.xlabel('Год-месяц-день')
    plt.ylabel('Цена')
    plt.savefig(path)
    plt.close()

dates, prices = get_data('2001-09-14', '2022-04-14') # указываем даты
# применяете функцию gen_graph
gen_graph(dates,prices)