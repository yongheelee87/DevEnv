from flask import Flask, render_template, request, redirect, send_file
from werkzeug.utils import secure_filename
from waitress import serve
from flask_caching import Cache
from datetime import datetime
from src.dataProcess import *


config = {
    "DEBUG": False,          # some Flask specific configs
    "CACHE_TYPE": "simple",  # Flask-Caching related configs
    "CACHE_DEFAULT_TIMEOUT": 300,
    "JSON_AS_ASCII": False,
    "UPLOAD_FOLDER": "./data"
}

app = Flask(__name__)

# tell Flask to use the above defined config
app.config.from_mapping(config)
cache = Cache(app)


class Global:
    period = 'M'


class WorkLog:
    # filepath = r'C:\Users\이영희\Desktop\컴인워시작업일지'
    filepath = r'C:\Users\yongh\PycharmProjects\webApp\data'
    backup_filepath = r'C:\컴인워시_백업\컴인워시_작업일지.csv'


@app.route('/')
@cache.cached(timeout=50)
def home():
    logging_print(BRIGHT_YELLOW + "알림: 홈 페이지 접속\n" + BRIGHT_END)
    end_date = datetime.now().strftime('%Y-%m-%d')
    return render_template('home.html', current_date=end_date)


@app.route('/input')
@cache.cached(timeout=50)
def write_csv():
    logging_print(BRIGHT_YELLOW + "알림: 입력 페이지 접속\n" + BRIGHT_END)
    return render_template('input.html', file_close=is_file_close('컴인워시_작업일지'))


@app.route('/input_data', methods=['POST', 'GET'])
def save_data():
    if request.method == 'POST':
        car_number = request.form['car_number']
        car_name = request.form['car_name']
        wash_option = request.form.getlist('wash_option')
        pay_option = request.form.getlist('pay_in_option')
        cost = request.form['cost']
        remark_word = request.form['remark_word']
        logging_print("입력 데이터\n"
                      "차량 번호: {number}, 차량 종류: {name}, 세자 종류: {wash}\n"
                      "결제 방식: {option}, 금액: {cost}, 비고: {remark}\n"
                      .format(number=car_number, name=car_name, wash=wash_option, option=pay_option, cost=cost, remark=remark_word))

        input_df = save_input_data(WorkLog.backup_filepath, car_number, car_name, wash_option, cost, pay_option, remark_word)
        return redirect('/input')


@app.route('/data', methods=['POST', 'GET'])
def display_filtered_data():
    if request.method == 'POST':
        car_number = request.form['car_number']
        car_type = request.form['car_type']
        remark_word = request.form['remark_word']
        start_date = request.form['start_date']
        end_date = request.form['end_date']
        pay_option = request.form.getlist('pay_option')
        logging_print("검색 데이터\n"
                      "차량 번호: {number}\n"
                      "차량 종류: {car_type}, 비고: {remark}\n"
                      "시작 날짜: {start}, 끝 날짜: {end}\n"
                      "결제 방식: {option}\n"
                      .format(number=car_number, car_type=car_type, remark=remark_word, start=start_date, end=end_date, option=pay_option))
        data_list, name_list = load_filtered_data(WorkLog.backup_filepath, car_number, car_type, remark_word, start_date, end_date, pay_option)
        tables = [data.to_html(classes='blue_data') for data in data_list]
        logging_print("검색 번호 리스트\n{}\n".format(name_list))
        return render_template('table.html', tables=tables, titles=name_list)


@app.route('/recent_data')
def display_recent_data():
    logging_print(BRIGHT_YELLOW + "알림: 최근 데이터 조회 접속\n" + BRIGHT_END)
    data_list, name_list = load_recent_data(WorkLog.backup_filepath)
    tables = [data.to_html(classes='blue_data') for data in data_list]
    return render_template('table.html', tables=tables, titles=name_list)


@app.route('/delete_data')
def delete_previous_data():
    if is_file_close('컴인워시_작업일지') != 'Open':
        data_last = remove_previous_data(WorkLog.backup_filepath)
        logging_print(BRIGHT_GREEN + "성공: 직전 데이터 삭제\n{}\n".format(data_last) + BRIGHT_END)
    return redirect('/recent_data')


@app.route("/revenue", methods=['POST', 'GET'])
def display_revenue():
    if request.method == 'POST':

        # Generate the figure **without using pyplot**.
        data = pd.read_csv(WorkLog.backup_filepath, dtype=object, encoding='cp949')
        Global.period = request.form['period']
        end_date = datetime.now().strftime('%Y-%m-%d')

        if Global.period == 'Ratio':
            logging_print(BRIGHT_YELLOW + "알림: 매출 비율 보기 접속\n" + BRIGHT_END)
            revenue_cnt = calculate_revenue_ratio(data)
            background_color = ['rgba(75, 192, 192, 0.2)', 'rgba(204, 51, 51, 0.2)', 'rgba(0, 51, 153, 0.2)',
                                'rgba(204, 255, 0, 0.2)',
                                'rgba(255, 153, 0, 0.2)', 'rgba(153, 0, 204, 0.2)', 'rgba(0, 102, 153, 0.2)',
                                'rgba(153, 204, 153, 0.2)',
                                'rgba(102, 0, 0, 0.2)', 'rgba(0, 0, 0, 0.2)']

            return render_template('chart.html', x_data=revenue_cnt['종류'].values.tolist(),
                                   y_data=revenue_cnt['횟수'].values.tolist(), background=background_color,
                                   title_str='매출 비율', ylabel_str='횟수', current_date=end_date)
        else:
            if Global.period == 'M':
                title = '월별 매출 그래프'
                logging_print(BRIGHT_YELLOW + "알림: 월별 매출 보기 접속\n" + BRIGHT_END)
            elif Global.period == 'W-MON':
                title = '주별 매출 그래프'
                logging_print(BRIGHT_YELLOW + "알림: 주별 매출 보기 접속\n" + BRIGHT_END)
            else:
                title = '일별 매출 그래프'
                logging_print(BRIGHT_YELLOW + "알림: 일별 매출 보기 접속\n" + BRIGHT_END)
            data_period, cost_sum = calculate_revenue(data, Global.period)
            total_revenue = ' [총 매출액: {0:,}(천원)]'.format(int(cost_sum))
            background_color = ['rgba(75, 192, 192, 0.2)' for _ in range(len(data_period))]
            return render_template('chart.html', x_data=data_period['날짜'].values.tolist(),
                                   y_data=data_period['금액'].values.tolist(), background=background_color, total_revenue=total_revenue,
                                   title_str=title, ylabel_str='매출액(천원)', current_date=end_date)


@app.route('/period_revenue', methods=['POST', 'GET'])
def display_revenue_period():
    if request.method == 'POST':
        logging_print(BRIGHT_YELLOW + "알림: 매출액(기간 포함) 보기 접속\n" + BRIGHT_END)

        data_origin = pd.read_csv(WorkLog.backup_filepath, dtype=object, encoding='cp949')
        start_date = request.form['start_period']
        end_date = request.form['end_period']
        data = search_by_date(data_origin, start_date, end_date)

        if Global.period == 'Ratio':
            revenue_cnt = calculate_revenue_ratio(data)
            background_color = ['rgba(75, 192, 192, 0.2)', 'rgba(204, 51, 51, 0.2)', 'rgba(0, 51, 153, 0.2)',
                                'rgba(204, 255, 0, 0.2)',
                                'rgba(255, 153, 0, 0.2)', 'rgba(153, 0, 204, 0.2)', 'rgba(0, 102, 153, 0.2)',
                                'rgba(153, 204, 153, 0.2)',
                                'rgba(102, 0, 0, 0.2)', 'rgba(0, 0, 0, 0.2)']
            return render_template('chart.html', x_data=revenue_cnt['종류'].values.tolist(),
                                   y_data=revenue_cnt['횟수'].values.tolist(), background=background_color,
                                   title_str='매출 비율', ylabel_str='횟수', start_date=start_date, current_date=end_date)
        else:
            if Global.period == 'M':
                title = '월별 총 매출액'
            elif Global.period == 'W-MON':
                title = '주별 총 매출액'
            else:
                title = '일별 총 매출액'
            data_period, cost_sum = calculate_revenue(data, Global.period)
            total_revenue = ' [총 매출액: {0:,}(천원)]'.format(int(cost_sum))
            background_color = ['rgba(75, 192, 192, 0.2)' for _ in range(len(data_period))]
            return render_template('chart.html', x_data=data_period['날짜'].values.tolist(),
                                   y_data=data_period['금액'].values.tolist(), background=background_color, total_revenue=total_revenue,
                                   title_str=title, ylabel_str='매출액(천원)',
                                   start_date=start_date, current_date=end_date)

@app.route('/work_log')
@cache.cached(timeout=50)
def work_log():
    logging_print(BRIGHT_YELLOW + "알림: 작업 일지 페이지 접속\n" + BRIGHT_END)
    return render_template('work.html', file_exist=is_file_exist(WorkLog.backup_filepath))

@app.route('/download')
def download_file():
    r_csv = pd.read_csv(WorkLog.backup_filepath, dtype=object, encoding='cp949')
    save_xlsx = pd.ExcelWriter("./data/컴인워시_작업일지.xlsx")
    r_csv.to_excel(save_xlsx, index=False)  # xlsx 파일로 변환
    save_xlsx.close()  # xlsx 파일로 저장
    return send_file("./data/컴인워시_작업일지.xlsx", mimetype='application/x-xlsx', as_attachment=True)


@app.route('/upload', methods=['POST', 'GET'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(f.filename)))
        update_file('./data', WorkLog.backup_filepath)
        return render_template('work.html', file_exist='Success')

if __name__ == '__main__':
    import socket
    ipv4 = socket.gethostbyname(socket.gethostname())

    print(BRIGHT_GREEN + '***********************************************************' + BRIGHT_END)
    print(BRIGHT_GREEN + '*                 ' + BRIGHT_CYAN + '컴인워시 프로그램 시작' + BRIGHT_GREEN + '                  *' + BRIGHT_END)
    print(BRIGHT_GREEN + '*                                                         *' + BRIGHT_END)
    print(BRIGHT_GREEN + '*                   ' + BRIGHT_CYAN + '모바일 폰 접속 가능' + BRIGHT_GREEN + '                   *' + BRIGHT_END)
    print(BRIGHT_GREEN + '***********************************************************\n' + BRIGHT_END)

    print(BRIGHT_RED + '***********************************************************' + BRIGHT_END)
    print(BRIGHT_RED + ' 해당 주소 ' + BRIGHT_BLUE + 'http://{}:5000'.format(ipv4) + BRIGHT_RED + ' 를 통해 접속 하세요' + BRIGHT_END)
    print(BRIGHT_RED + '***********************************************************\n' + BRIGHT_END)

    logging_initialize()

    # app.run(host='0.0.0.0', port=5000, threaded=True)
    serve(app, host="0.0.0.0", port=5000)
