from django.shortcuts import render

def index(request):
    context = {
        'title': 'Store', 
        'is_promotion': True,
    }
    return render(request, 'products/index.html', context)

def products(request):
    context = {
        'title': 'Store - Каталог',
        'products': [
            {
                'image': '/static/vendor/img/products/Adidas-hoodie.webp',
                'name': 'Чёрный худи Adidas с монограммой',
                'price': 6000,
                'description': 'Мягкая ткань для свитшотов. Стиль и комфорт для повседневной носки.'
            },
            {
                'image': '/static/vendor/img/products/north_face.jpg',
                'name': 'Синяя куртка The North Face',
                'price': 23725,
                'description': 'Гладкая ткань. Водонепроницаемое покрытие. Лёгкий и тёплый пуховый наполнитель.'
            },{
                'image': '/static/vendor/img/products/asos_design.jpeg',
                'name': 'Коричневый оверсайз-топ Asos Design',
                'price': 3400,
                'description': 'Материал с плюшевой текстурой. Удобный и мягкий.'
            },
        ]
    }
    return render(request, 'products/products.html', context)