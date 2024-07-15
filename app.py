from flask import Flask, render_template, request
import datetime
from fatoora import Fatoora

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # استقبال البيانات من النموذج HTML
        seller_name = request.form['seller_name']
        tax_number = int(request.form['tax_number'])
        total_amount = float(request.form['total_amount'])
        tax_amount = float(request.form['tax_amount'])

        # الحصول على الوقت الحالي وتنسيقه
        current_time = datetime.datetime.now()
        formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")

        # إنشاء كائن Fatoora مع البيانات المدخلة من المستخدم
        fatoora_obj = Fatoora(
            seller_name=seller_name,
            tax_number=tax_number,
            invoice_date=formatted_time,
            total_amount=total_amount,
            tax_amount=tax_amount,
        )

        # استخدام دالة qrcode() لإنشاء رمز الاستجابة السريعة
        fatoora_obj.qrcode("static/qr_code.png")

        return render_template('index.html', created=True)

    # عرض الصفحة الأولية أو النموذج
    return render_template('index.html', created=False)

if __name__ == '__main__':
    app.run(debug=True)
