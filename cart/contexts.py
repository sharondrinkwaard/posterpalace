from posters.models import Poster
from django.shortcuts import get_object_or_404
from django.conf import settings


def shopping_content(request):

    shopping_items = []
    total = 0
    poster_count = 0
    cart = request.session.get('cart', {})

    for article_id, item_data in cart.items():
        if isinstance(item_data, int):
            poster = get_object_or_404(Poster, pk=article_id)
            total += item_data * poster.price
            poster_count += item_data
            shopping_items.append({
                'article_id': article_id,
                'quantity': item_data,
                'poster': poster,
            })
        else:
            poster = get_object_or_404(Poster, pk=article_id)
            for color, quantity in item_data['items_by_color'].items():
                total += quantity * poster.price
                poster_count += quantity
                shopping_items.append({
                    'article_id': article_id,
                    'quantity': quantity,
                    'poster': poster,
                    'color': color,
                })
    

    context = {
        'shopping_items': shopping_items,
        'total': total,
        'poster_count': poster_count,
    }

    return context