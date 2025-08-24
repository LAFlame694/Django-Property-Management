from django.shortcuts import render
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from finance.models import TenantAccount, Invoice, Payment
from main.models import Profile

@csrf_exempt
def mpesa_confirmation(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)

            # Extract details from JSON
            trans_id = data.get('TransID')
            amount = float(data.get('TransAmount', 0))
            bill_ref = data.get('BillRefNumber')  # Bedsitter number
            phone = data.get('MSISDN')

            # 1) Find the Profile using bedsitter number
            profile = Profile.objects.filter(bedsitter__number=bill_ref).first()

            if profile:
                # 2) Find the unpaid invoice for this tenant
                invoice = Invoice.objects.filter(tenant=profile.user, status="unpaid").first()

                if invoice:
                    # 3) Create the payment
                    Payment.objects.create(
                        tenant=profile.user,
                        invoice=invoice,
                        amount=amount,
                        method="mpesa"
                    )

                    # Signals will update tenant account + invoice status
                    return JsonResponse({"ResultCode": 0, "ResultDesc": "Accepted"})
                
                return JsonResponse({"ResultCode": 1, "ResultDesc": "No unpaid invoice found for this tenant"})
            
            return JsonResponse({"ResultCode": 1, "ResultDesc": "No matching tenant found"})

        except Exception as e:
            return JsonResponse({"ResultCode": 1, "ResultDesc": f"Error: {str(e)}"})

    return JsonResponse({"ResultCode": 1, "ResultDesc": "Invalid request"})
