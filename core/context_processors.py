from .models import Order

def cart_item_count(request):
    if request.user.is_authenticated:
        try:
            order = Order.objects.get(user=request.user, ordered=False)
            count = sum([item.quantity for item in order.items.all()])
            return {'cart_item_count': count}
        except Order.DoesNotExist:
            return {'cart_item_count': 0}
    return {'cart_item_count': 0}