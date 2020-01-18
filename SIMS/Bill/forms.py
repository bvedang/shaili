from flask_wtf import FlaskForm
from wtforms import StringField,SelectField,SubmitField,IntegerField,DateTimeField,BooleanField
from wtforms.validators import DataRequired,EqualTo
from wtforms.widgets import html5
from wtforms.widgets import TextArea

class BillForm(FlaskForm):
    invoice_number = StringField('Invoice No.')
    order_number = IntegerField('Order No:',widget=html5.NumberInput())
    invoice_date = DateTimeField('Invoice Date.',format='%d-%m-%Y',widget=html5.DateInput())
    state = StringField('State')
    state_code = IntegerField('State Code:',widget=html5.NumberInput())
    lr_date = StringField('L.R. Date :')
    buyer_name = StringField('Buyer\'s Name')
    buyer_address1 = StringField('Buyer Address 1:')
    buyer_address2 = StringField('Buyer Address 2:')
    consignee_name = StringField('Consignee Name')
    consignee_address1 = StringField('Consignee Address 1:')
    consignee_address2 = StringField('Consignee Address 2:')
    same_as_above = BooleanField('Consignee Name & Address same as Buyer ?')
    gstin = StringField('GSTIN')
    buyer_state = StringField('State')
    buyer_state_code = IntegerField('State Code:-',widget=html5.NumberInput())
    goods_name = StringField('Goods Name')
    goods_batch_number = StringField('Goods Batch No:')
    goods_mfg_date = StringField('Goods Manufacturing Date:')
    goods_retest_date = StringField('Batch Retest Date')
    goods_packing_detail = StringField('Packing Detail')
    hsn = IntegerField('HSN SAC',widget=html5.NumberInput())
    quantity = IntegerField('Qty',widget=html5.NumberInput())
    quantity_code = StringField('Quantity Code')
    rate_per_unit = IntegerField('Rate Per Unit(Rs)',widget=html5.NumberInput())
    cgst = IntegerField('Add CGST',widget=html5.NumberInput())
    sgst = IntegerField('Add SGST',widget=html5.NumberInput())
    igst = IntegerField('Add IGST',widget=html5.NumberInput())
    remark = StringField('Remarks:-',widget=TextArea())
    submit = SubmitField('Submit')
