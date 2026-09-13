from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q  # Arama işlemi için Q nesnesi eklendi
from .models import Perfume, Category

def perfume_list(request):
    category_slug = request.GET.get('category')
    query = request.GET.get('q')  # Kullanıcının arama kutusuna yazdığı metni al
    
    # Sayfalama yapabilmek için sıralama şarttır. -id ile en son eklenenleri başa alıyoruz.
    perfumes = Perfume.objects.filter(is_active=True).order_by('-id')
    categories = Category.objects.all()

    # Eğer kategori seçildiyse ona göre filtrele
    if category_slug:
        perfumes = perfumes.filter(category__slug=category_slug)

    # EĞER ARAMA YAPILDIYSA isme VEYA açıklamaya göre filtrele
    if query:
        perfumes = perfumes.filter(
            Q(name__icontains=query) | 
            Q(description__icontains=query)
        )

    # Sayfalama ayarları (Her sayfada 12 ürün gösterilecek)
    paginator = Paginator(perfumes, 12)
    page = request.GET.get('page')

    try:
        perfumes_page = paginator.page(page)
    except PageNotAnInteger:
        # Eğer page bir tam sayı değilse ilk sayfayı ver
        perfumes_page = paginator.page(1)
    except EmptyPage:
        # Eğer page sayfa sınırını aştıysa en son sayfayı ver
        perfumes_page = paginator.page(paginator.num_pages)

    context = {
        'perfumes': perfumes_page,
        'categories': categories,
        'active_category': category_slug,
        'query': query,  # Arama metnini template'te kullanabilmek için context'e ekledik
    }
    return render(request, 'catalog/index.html', context)