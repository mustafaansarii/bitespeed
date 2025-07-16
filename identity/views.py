from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Contact
import json
from django.db.models import Q

@csrf_exempt
def identify_contact(request):
    if request.method != "POST":
        return JsonResponse({"error": "Only POST requests allowed."}, status=405)

    data = json.loads(request.body)
    email = data.get("email")
    phone = data.get("phoneNumber")

    if not email and not phone:
        return JsonResponse({"error": "Email or PhoneNumber is required."}, status=400)

    related_contacts = Contact.objects.filter(
        Q(email=email) | Q(phoneNumber=phone)
    ).order_by('createdAt')

    if not related_contacts:
        new_contact = Contact.objects.create(
            email=email,
            phoneNumber=phone,
            linkPrecedence="primary"
        )
        response = {
            "contact": {
                "primaryContatctId": new_contact.id,
                "emails": [email] if email else [],
                "phoneNumbers": [phone] if phone else [],
                "secondaryContactIds": []
            }
        }
        return JsonResponse(response, status=200)

    all_contacts = list(related_contacts)

    visited = set(c.id for c in all_contacts)
    queue = list(all_contacts)

    while queue:
        current = queue.pop()
        connected = Contact.objects.filter(
            Q(email=current.email) | Q(phoneNumber=current.phoneNumber)
        ).exclude(id__in=visited)
        for c in connected:
            visited.add(c.id)
            all_contacts.append(c)
            queue.append(c)

    primary = sorted(
        [c for c in all_contacts if c.linkPrecedence == 'primary'],
        key=lambda x: x.createdAt
    )[0]
    for contact in all_contacts:
        if contact.id != primary.id:
            if contact.linkPrecedence != "secondary" or contact.linkedId_id != primary.id:
                contact.linkPrecedence = "secondary"
                contact.linkedId = primary
                contact.save()

    already_present = any(
        c.email == email and c.phoneNumber == phone for c in all_contacts
    )

    if not already_present:
        new_contact = Contact.objects.create(
            email=email,
            phoneNumber=phone,
            linkedId=primary,
            linkPrecedence="secondary"
        )
        all_contacts.append(new_contact)

    emails = list({c.email for c in all_contacts if c.email})
    phones = list({c.phoneNumber for c in all_contacts if c.phoneNumber})
    secondary_ids = [c.id for c in all_contacts if c.linkPrecedence == "secondary"]

    response = {
        "contact": {
            "primaryContatctId": primary.id,
            "emails": [primary.email] + [e for e in emails if e != primary.email],
            "phoneNumbers": [primary.phoneNumber] + [p for p in phones if p != primary.phoneNumber],
            "secondaryContactIds": secondary_ids
        }
    }
    return JsonResponse(response, status=200)
