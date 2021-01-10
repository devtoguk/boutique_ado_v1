from django.shortcuts import render, redirect


# Create your views here.

def view_bag(request):
    """ A view that renders the bag contents page """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    size = None
    if 'product_size' in request.POST:
        size = request.POST.get('product_size')

    bag = request.session.get('bag', {})

    if size:
        if item_id in list(bag.keys()):  # is item in the bag
            if size in bag[item_id]['items_by_size'].keys():
                bag[item_id]['items_by_size'][size] += quantity  # item in bag with that size already
            else:
                bag[item_id]['items_by_size'][size] = quantity   # item in bag but not in that size
        else:
            bag[item_id] = {'items_by_size': {size: quantity}}   # item not in bag
    else:
        if item_id in list(bag.keys()):
            bag[item_id] += quantity
        else:
            bag[item_id] = quantity

    request.session['bag'] = bag
    return redirect(redirect_url)
