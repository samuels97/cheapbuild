from.models import *

def get_contact_info():
    try:
        locate = Location.objects.all()
        email = Email.objects.all()
        phone = OfficePhone.objects.all().order_by('-created')
        serviceh = Services.objects.all().order_by('-created')[:3]
        service = Services.objects.all().order_by('-created')
        servcapt = ServeCaptin.objects.all().order_by('-created')[:1]
        choose = ChoozeUs.objects.all().order_by('-created')[:1]

        msn = Mission.objects.all().order_by('-created')[:1]
        vsn = Vision.objects.all().order_by('-created')[:1]
        objz = Objective.objects.all().order_by('-created')[:1]

        banas = Banners.objects.all().order_by("created")
        bg    = background.objects.filter(is_published=True).order_by('-created')
        bgimg    = backgroudImages.objects.filter().order_by('-created')
        project    = Projects.objects.filter(status='finshed').order_by('-created')
        pends    = Projects.objects.filter(status='pending').order_by('-created')
        team    = Staff.objects.filter().order_by('department')[:3]
        testify    = Testimony.objects.filter().order_by('-created')

    except Exception as e:
        # Handle the exception here, log the error, or return default values if needed.
        print(f"Error: {e}")
        locate, email, phone,banas,bg,serviceh, service, servcapt, choose,msn,vsn,objz,project,pends,team,testify = (None,) * 16

    return {
    'locate': locate, 'email': email, 'phone': phone, 'banas':banas, 'bg':bg, 'serviceh':serviceh,
    'bgimg':bgimg,'service':service, 'servcapt':servcapt,'choose':choose,'msn':msn,'vsn':vsn,'objz':objz,
    'project':project,'pends':pends,'team':team,'testify':testify
    }
