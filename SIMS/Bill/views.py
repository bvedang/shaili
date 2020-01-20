from flask import render_template,redirect,url_for,request,make_response,Blueprint,send_file
from flask_login import login_required
import pdfkit
import datetime
from io import BytesIO
from SIMS.models import BillsPDF
from SIMS import db
from SIMS.Bill.table import PDF_table

bills = Blueprint('bills',__name__,template_folder='templates/Bill')

#config = pdfkit.configuration(wkhtmltopdf='/opt/bin/wkhtmltopdf')
#while uploading to server remove config from comment

# Bill Home
@bills.route('/home')
@login_required
def home():
    entries = BillsPDF.query.filter(BillsPDF.date).limit(10).all()
    table = PDF_table(entries,classes=['table','table-hover'])
    return render_template('bill_home.html',table=table)

# Bill Challan Form

@bills.route('/generate_challan',methods=['GET','POST'])
@login_required
def generate_challan():
    return render_template('generate_challan_form.html')

# Bill Generator Form

@bills.route('/generate_bill',methods=['GET','POST'])
@login_required
def generate_bill():
    invoice_number = request.args.get('invoice_number')
    order_number = request.args.get('order_number')
    invoice_date = datetime.datetime.strptime(request.args.get('invoice_date'),'%Y-%m-%d')
    challan_no = request.args.get('challan_no')
    state = request.args.get('state')
    state_code = request.args.get('state_code')
    lr_date = request.args.get('lr_date')
    buyer_name = request.args.get('buyer_name')
    buyer_add1 = request.args.get('buyer_add1')
    buyer_add2 = request.args.get('buyer_add2')
    consignee_name = request.args.get('consignee_name')
    consignee_add1 = request.args.get('consignee_add1')
    consignee_add2 = request.args.get('consignee_add2')
    gstin = request.args.get('gstin')
    buyer_state = request.args.get('buyer_state')
    buyer_state_code = request.args.get('buyer_state_code')
    goods_name = request.args.get('goods_name')
    goods_batch = request.args.get('goods_batch')
    goods_mfg_date = request.args.get('goods_mfg_date')
    goods_retest = request.args.get('goods_retest')
    packing_detail = request.args.get('packing_detail')
    hsn = request.args.get('hsn')
    qty_code = request.args.get('qty_code')
    remarks = request.args.get('Remarks')
    reminder_day = float(request.args.get('reminder'))
    reminder_date = invoice_date + datetime.timedelta(days=reminder_day)
    if invoice_number is not None:
        invoice_date = datetime.datetime.strptime(request.args.get('invoice_date'),'%Y-%m-%d').strftime('%d-%m-%Y')
        challan_date = datetime.datetime.strptime(request.args.get('challan_date'),'%Y-%m-%d').strftime('%d-%m-%Y')
        qty = float(request.args.get('qty'))
        rate = float(request.args.get('rate'))
        cgst = float(request.args.get('cgst'))
        sgst = float(request.args.get('sgst'))
        value = round(qty*rate,2)
        cgst_value = round((cgst/100)*value,2)
        sgst_value = round((sgst/100)*value,2)
        tax_amount = cgst_value + sgst_value #+ ((igst/100)*value)
        grand_total = tax_amount+value
        bill = render_template('bill_generator_pdf.html',invoice_number=invoice_number,invoice_date=invoice_date,order_number=order_number,
        state=state,state_code=state_code,lr_date=lr_date,buyer_name=buyer_name,buyer_add1=buyer_add1,buyer_add2=buyer_add2,
        consignee_name=consignee_name,consignee_add1=consignee_add1,consignee_add2=consignee_add2,gstin=gstin,buyer_state=buyer_state,
        buyer_state_code=buyer_state_code,goods_name=goods_name,goods_batch=goods_batch,goods_mfg_date=goods_mfg_date,goods_retest=goods_retest,
        packing_detail=packing_detail,hsn=hsn,qty=qty,qty_code=qty_code,rate=rate,cgst=cgst,sgst=sgst,value=value,
        tax_amount=tax_amount,grand_total=grand_total,remarks=remarks,cgst_value=cgst_value,sgst_value=sgst_value,challan_no=challan_no,challan_date=challan_date)
        option = {
            'page-size':'A4',
            'margin-top':'2in',
            'margin-bottom':'0.15in',
            'margin-right':'0.15in',
            'margin-left':'0.15in'
        }
        pdf = pdfkit.from_string(bill,False,options=option)
        billspdf = BillsPDF(name=invoice_number+'.pdf',bill_pdf=pdf,grand_total=grand_total,reminder_date=reminder_date)
        db.session.add(billspdf)
        db.session.commit()
        file_data = BillsPDF.query.filter_by(name=invoice_number+'.pdf').first()
        return send_file(BytesIO(file_data.bill_pdf),attachment_filename=invoice_number+'.pdf',as_attachment=True)
    return render_template('bill_generator_form.html')

#@bills.route('/')
#def index():
    #render = render_template('perfect.html')
    #option = {
        #'page-size':'A4',
        #'margin-top':'2in',
        #'margin-bottom':'0.15in',
        #'margin-right':'0.15in',
        #'margin-left':'0.15in'
    #}
    #pdf = pdfkit.from_string(render,False,options=option)

    #response = make_response(pdf)
    #response.headers['Content-Type'] = 'application/pdf'
    #response.headers['Content-Disposition'] = 'attachment; filename=output.pdf'
    #eturn response



