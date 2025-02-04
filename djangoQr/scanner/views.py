# from django.shortcuts import render
# from .models import QRcode
# import qrcode
# from django.core.files.storage import FileSystemStorage
# from io import BytesIO
# from django.core.files.base import ContentFile
# from django.conf import settings
# from pathlib import Path
# from pyzbar.pyzbar import decode
# from PIL import Image

# # Create your views here.
# def generate_qr(request):
#     qr_image_url = None         
#     if request.method =='POST':
#         mobile_number = request.POST.get('mobile_number')
#         data = request.POST.get('qr_data')
        
#         # validate the mobile number
#         if not mobile_number or len(mobile_number) !=10 or not mobile_number.isdigit():
#             return render(request, 'scanner/generate.html', {'error':'Invalid Mobile number'})
        
#         # Generate the QR code image with data and mobile number
#         qr_content = f"{data}|{mobile_number}"
#         qr = qrcode.make(qr_content)
#         qr_image_io = BytesIO() #Create  a BytesIO stream
#         # save the qr code image to qr_image_io
#         qr.save(qr_image_io, format='PNG')
#         qr_image_io.seek(0)# RESET the position of the stream
          
#         #   Define the storage location for the qr code images
#         qr_storage_path = Path(settings.MEDIA_ROOT) /'qr_codes' 
#         fs = FileSystemStorage(location=qr_storage_path, base_url='/media/qr_codes/')
#         filename = f"{data}_{mobile_number}.png"
#         qr_image_content = ContentFile(qr_image_io.read(), name=filename)
#         file_path = fs.save(filename, qr_image_content)
#         qr_image_url = fs.url(filename)
        
#         # Save the Qr code data and mobile number in the database
#         QRcode.objects.create(data=data, mobile_number= mobile_number)  
#     return render(request, 'scanner/generate.html',{'error':'Invalid mobile number  '})

# def scan_qr(request):
#     result = None
#     if request.method == 'POST' and request.FILES.get('qr_image'):
#         mobile_number = request.POST.get('mobile_number')
#         qr_image = request.FILES['qr_image']
        
#         # validate the mobile number
#         if not mobile_number or len(mobile_number) !=10 or not mobile_number.isdigit():
#             return render(request, 'scanner/scanner.html', {'error':'Invalid Mobile number'})
        
#         # save the upload image
#         fs = FileSystemStorage()
#         filename = fs.save(qr_image.name, qr_image)
#         image_path = Path(fs.location) / filename
#         try:
#             # open and decode the image
#             image = Image.open(image_path)
#             decoded_objects = decode(image)
            
#             if decoded_objects:
#                 #Get the data from the first decoded object
#                 qr_content = decoded_objects[0].data.decode('utf-8').strip()
#                 qr_data, qr_mobile_number = qr_content.split('|')
                
#                 # Check if the data is exists in the QRcode model with the provided mobile number
#                 qr_entry =  QRcode.objects.filter(data=qr_data,mobile_number=qr_mobile_number).first()
#                 if qr_entry and qr_mobile_number == mobile_number:
#                     result = "Scan Success: Valid QR Code for the provided mobile number"
                    
#                 # delete the specific qr code entry form the database
#                     qr_entry.delete()
                
#                 #Delete the Qr code image from the 'media/qr_code' directory
#                     settings.MEDIA_ROOT / 'qr_codes'/ f"{qr_data}_{qr_mobile_number}.png"
#                     if image_path.exists():
#                         image_path.unlink() #deletes the Qr code image
                
#                 else:
#                     result = "Scan Failed: Invalid QR code or mobile number mismatch" 
#             else:
#                 result = "No QR code detected in the image."  
#         except Exception as e:
#             result = f"Error processing the image:{str(e)}"
#         finally:
#             if image_path.exists():
#                         image_path.unlink() #delete the qr image
            
#     return render(request, 'scanner/scan.html',{'result': result})

from django.shortcuts import render
from .models import QRcode
import qrcode
from django.core.files.storage import FileSystemStorage
from io import BytesIO
from django.core.files.base import ContentFile
from django.conf import settings
from pathlib import Path
from pyzbar.pyzbar import decode
from PIL import Image

# Create your views here.
def generate_qr(request):
    qr_image_url = None  # Initialize outside to avoid reference errors

    if request.method == 'POST':
        mobile_number = request.POST.get('mobile_number')
        data = request.POST.get('qr_data')

        # Validate the mobile number
        if not mobile_number or len(mobile_number) != 10 or not mobile_number.isdigit():
            return render(request, 'scanner/generate.html', {'error': 'Invalid Mobile number'})

        # Generate the QR code image with data and mobile number
        qr_content = f"{data}|{mobile_number}"
        qr = qrcode.make(qr_content)
        qr_image_io = BytesIO()  # Create a BytesIO stream
        qr.save(qr_image_io, format='PNG')  # Save the QR code image
        qr_image_io.seek(0)  # Reset the position of the stream

        # Define the storage location for the QR code images
        qr_storage_path = Path(settings.MEDIA_ROOT) / 'qr_codes'
        fs = FileSystemStorage(location=qr_storage_path, base_url='/media/qr_codes/')
        filename = f"{data}_{mobile_number}.png"
        qr_image_content = ContentFile(qr_image_io.read(), name=filename)
        file_path = fs.save(filename, qr_image_content)
        qr_image_url = fs.url(filename)  # Correctly retrieve the URL

        # Save the QR code data and mobile number in the database
        QRcode.objects.create(data=data, mobile_number=mobile_number)

        return render(request, 'scanner/generate.html', {'qr_image_url': qr_image_url})

    return render(request, 'scanner/generate.html')


def scan_qr(request):
    result = None

    if request.method == 'POST' and request.FILES.get('qr_image'):
        mobile_number = request.POST.get('mobile_number')
        qr_image = request.FILES['qr_image']

        # Validate the mobile number
        if not mobile_number or len(mobile_number) != 10 or not mobile_number.isdigit():
            return render(request, 'scanner/scan.html', {'error': 'Invalid Mobile number'})

        # Save the uploaded image
        fs = FileSystemStorage()
        filename = fs.save(qr_image.name, qr_image)
        image_path = Path(fs.location) / filename

        try:
            # Open and decode the image
            image = Image.open(image_path)
            decoded_objects = decode(image)

            if decoded_objects:
                # Get the data from the first decoded object
                qr_content = decoded_objects[0].data.decode('utf-8').strip()
                qr_data, qr_mobile_number = qr_content.split('|')

                # Check if the data exists in the QRcode model with the provided mobile number
                qr_entry = QRcode.objects.filter(data=qr_data, mobile_number=qr_mobile_number).first()

                if qr_entry and qr_mobile_number == mobile_number:
                    result = "Scan Success: Valid QR Code for the provided mobile number"

                    # Delete the specific QR code entry from the database
                    qr_entry.delete()

                    # Delete the QR code image from 'media/qr_codes' directory
                    qr_code_image_path = Path(settings.MEDIA_ROOT) / 'qr_codes' / f"{qr_data}_{qr_mobile_number}.png"
                    if qr_code_image_path.exists():
                        qr_code_image_path.unlink()  # Deletes the QR code image
                else:
                    result = "Scan Failed: Invalid QR code or mobile number mismatch"
            else:
                result = "No QR code detected in the image."
        except Exception as e:
            result = f"Error processing the image: {str(e)}"
        finally:
            if image_path.exists():
                image_path.unlink()  # Delete the uploaded QR image

    return render(request, 'scanner/scan.html', {'result': result})
