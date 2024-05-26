import qrcode
import io
from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/api/generate', methods=['GET', 'POST'])
def generate_qr_code():
    url = request.args.get('url') or request.form.get('url')

    if not url:
        return "Missing 'url' parameter or form data", 400  # Bad Request

    output_buffer = io.BytesIO()

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    # Check for qrcode library version and use appropriate save method
    if hasattr(qr.make_image, 'format'):
        img = qr.make_image(fill_color="black", back_color="white", format='PNG')
    else:
        img = qr.make_image(fill_color="black", back_color="white")
        img.save(output_buffer)  # For older versions, format defaults to PNG

    response = make_response(output_buffer.getvalue())
    response.headers['Content-Type'] = 'image/png'
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
