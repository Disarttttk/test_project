from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import MediaFile


@csrf_exempt
def upload_file(request):
    if request.method == 'POST':
        media_type = request.POST.get('media_type')
        file = request.FILES.get('file')

        if media_type not in ['photo', 'video']:
            return JsonResponse({'status': 'error', 'message': 'Invalid media type'}, status=400)

        media_file = MediaFile.objects.create(media_type=media_type, file=file)
        return JsonResponse({'status': 'success', 'media_file_id': media_file.id})
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=405)

