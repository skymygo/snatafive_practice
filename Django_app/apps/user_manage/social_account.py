from django.http import JsonResponse



def social_naver_callback(request, *args, **kwargs):
    print(request)
    return JsonResponse({"msg": f" updated using "}, status=200)